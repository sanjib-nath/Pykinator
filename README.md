# Pykinator 🐍

## Project Idea

Build something similar to Akinator using Python.

The program will ask questions and try to guess the anime character the user is thinking of.

## Technologies Used

- Python
- NumPy
- Pandas

## Algorithm

A modified version of a Decision Tree.

## How It Works

Pykinator uses a modified version of a Decision Tree (at least that's what I call it) to decide the best feature to ask a question about using Information Gain.

The program then finds the question assigned to that specific feature and asks the player.

Depending on the player's answer (Yes or No), it splits the dataset and repeats the process.

It keeps doing this until there is only one character left or no useful feature is available to split the dataset.

## The Main Challenge

I did not know anything about Trees, Information Gain, Entropy or Gini Impurity before starting this project, so I had to learn them while working on the project.

I also faced quite a few challenges while writing the main algorithm and figuring out how to turn the theory into actual code.

## Future Plans

I am currently working on a way to make a larger database. I still don't know exactly how, maybe using some sort of anime database or API.

Eventually, I want to:

- Add more characters and datasets
- Add data beside anime characters
- Make it into a website
- Let my friends play it

## Bugs

I am still a beginner, so I am sure there are some bugs.

If you find one, feel free to mention it so we can fix it.

## Final Thoughts

Overall, this was a great learning experience.

I started this project without knowing anything about Decision Trees or Information Gain, and ended up building my own working version of the algorithm.

There is still a lot I want to improve, but for now, I am happy with how it turned out.