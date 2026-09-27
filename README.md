# PoopleSolver
Basic script solver for the hit game "poople". This is a quick-and-dirty hacky solution I did for fun
but it seems to not only work but also to provide the optimal solution, might come back to this and workshop it to atleast make it more palatable

### How to run
Clone the repo, cd to the cloned directory and run

```pb
python -m poople_solver
```
The interaction should look something like this:

<img width="320" height="69" alt="image" src="https://github.com/user-attachments/assets/3123031b-63ef-4aaf-9c7f-f16637862965" />


### Possible issues
The valid 4-letter word list was compiled using the word-list repo: https://github.com/en-wl/wordlist 

As such, some of the words might not be recognized by Poople. I've removed most of those but if you run into such a word, just remove the word from the `four_letter_english_words.txt` file locally and re-run (and if you're feeling extra charitable you can open a PR with the removal)
