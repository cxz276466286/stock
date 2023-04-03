import pandas as pd



def simulate():
    df = pd.read_csv(r'trading.csv')
    # print(df)
    for i, line in df.iterrows():
        print(line['operation'], line['price'])

if __name__ == "__main__":
    simulate()