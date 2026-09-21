import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

def ask_question(feature, questions):
    """question: dict of question dataset"""

    print(questions[feature])

    accepted_ans = ('Y', 'N', 'D')
 
    while True:
        ans = str(input())

        if ans.upper() not in accepted_ans:
            print("Please enter [Y]es or [N]o")
            continue

        return ans

def split_dataset(feature, ans, dataset):
    if ans == 'Y':
        return dataset[dataset[feature] == True]
    elif ans == 'N':
        return dataset[dataset[feature] == False]
    else: #if Don't know
        return dataset