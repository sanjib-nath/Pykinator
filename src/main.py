from decision_tree import DecisionTree
from helper import *

#load the data
char_data = load_data('data/characters.csv')
ques_data = load_data('data/questions.csv')

#main game
def game():
    characters = char_data
    questions = dict(zip(ques_data['feature'], ques_data['question']))

    print("\n-------------------------------------------------------------")
    print("---PYAKINATOR---\n")
    print("Think of an anime character. I'll try to figure out who it is.\n")

    print("Alright, let's begin.")
    print("I've got a few questions for you...\n")
        

    while True:
        if len(characters) == 0: #type: ignore
            print("You got me. I am unable to guess your character.")
            break

        if len(characters) == 1: #type: ignore
            character = characters.iloc[0]['name'] #type: ignore
            print(f"\nGot you! It's {character}, right?")

            answer = input()
            if answer.upper() == 'Y':
                print("YES! I knew it.")
            else:
                print("You got me. My knowledge needs an update.")

            print("\n-------------------------------------------------------------")
            break

        #get the best feature to ask question
        decision_tree = DecisionTree()
        feature = decision_tree.best_feature(characters)

        if feature is None:
            print("\nI am sorry. My current database does not have your character")
            break

        ans = ask_question(feature, questions)

        #split the dataset
        characters = split_dataset(feature, ans, characters)

game()