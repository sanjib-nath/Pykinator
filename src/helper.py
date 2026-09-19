import pandas as pd

def load_data(path, as_int=True):
    df = pd.read_csv(path)

    if as_int:
        #getting the col header exculding the name
        col_headers = df.columns.tolist()[1:]

        #convert all the true flase into 1 and 0
        for header in col_headers:
            df[header] = df[header].astype(int)

    return df.to_dict(orient='records')
