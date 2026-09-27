from __future__ import annotations
from typing import Final
from dataclasses import dataclass, field
from copy import deepcopy

ORDER_A: Final[int] = 97
ORDER_Z: Final[int] = ORDER_A + 25
ALL_LETTERS: Final[range] = range(ORDER_A, ORDER_Z + 1)
POOP: Final[list[str]] = ["p", "o", "o", "p"]
POOP_WORD:Final[str] = 'poop'


def generate_set_from_file() -> set[str]:
    with open(
        "four_letter_english_words.txt", "r"
    ) as word_file:
        return set([word.strip("\n") for word in word_file.readlines()])


WORD_SET: Final[set[str]] = generate_set_from_file()


@dataclass(kw_only=True, slots=True, repr=True)
class Vertex:
    id: list[str] | None = field(default=None)
    neighbours: dict[str, Vertex] = field(default_factory=dict)
    
    @property
    def readable_name(self)-> str:
        return ''.join(self.id) if self.id else ""

    def generate_neighbours(self):
        created: dict[str,Vertex] = {self.readable_name:self}
        self.generate_neighbours_rec(created=created, depth=1)

    def generate_neighbours_rec(
        self, *, created: set[str], depth: int, max_depth: int = 100
    ):
        if "".join(POOP) in created or depth >= max_depth:
            return

        for i in range(len(self.id)):
            for ch in ALL_LETTERS:
                current_word: list[str] = deepcopy(self.id)
                current_word[i] = chr(ch)
                current_word_whole: str = "".join(current_word)
                
                if current_word_whole in created:
                    self.neighbours[current_word_whole] = created[current_word_whole]
                    continue

                if current_word_whole in WORD_SET:
                    vertex_to_add:Vertex = Vertex(id=current_word)
                    self.neighbours[current_word_whole] = vertex_to_add
                    created[current_word_whole] = vertex_to_add

        for neighbour in self.neighbours.values():
            neighbour.generate_neighbours_rec(created=created, depth=depth + 1)


@dataclass(kw_only=True, slots=True, repr=True)
class Graph:
    head_vertex: Vertex | None = field(default=None)

    @property
    def all_words(self) -> list[str]:
        return self.head_vertex.all_words

    @staticmethod
    def generate_from_original_word(*, original_word: str) -> Graph:
        word_as_char_list: list[str] = [ch for ch in original_word]
        graph: Graph = Graph(head_vertex=Vertex(id=word_as_char_list))
        graph.head_vertex.generate_neighbours()

        return graph
    
    def BFS(self)->list[str]:
        visited:set[str] = set([''.join(self.head_vertex.id)])
        path = {self.head_vertex.readable_name:None}
        current_node:Vertex = self.head_vertex
        nodes_to_visit:list[tuple[str,Vertex]] = [(current_node.readable_name,neighbour) for neighbour in list(current_node.neighbours.values())]
        index:int = 0
        
        while index < len(nodes_to_visit):
            neighbour = nodes_to_visit[index][1]
            parent = nodes_to_visit[index][0]
            if neighbour.readable_name == POOP_WORD:
                visited.add(POOP_WORD)
                path[POOP_WORD] = parent
                k,v = POOP_WORD, parent
                complete_path:list[str] = []
                while v:
                    complete_path.append(k)
                    k,v = v,path[v]
                
                return complete_path[::-1]
            
            index+=1
            if neighbour.readable_name in visited:
                continue
            
            path[neighbour.readable_name] = parent
            visited.add(neighbour.readable_name)
            nodes_to_visit.extend([(neighbour.readable_name,next_neighbour) for next_neighbour in list(neighbour.neighbours.values())])
            
            
            

original_word:str = input("enter the word you wish to poople:\n")
g = Graph.generate_from_original_word(original_word=original_word)
result = [original_word]+g.BFS()
print(" -> ".join(result))