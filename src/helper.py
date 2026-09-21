import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

def ask_question(feature, dataset):
    questions = dict(zip(dataset['feature'], dataset['question']))
    print(questions[feature])

    accepted_ans = ('Y', 'N')
 
    while True:
        ans = str(input())

        if ans.upper() not in accepted_ans:
            print("Please enter [Y]es or [N]o")
            continue

        return ans