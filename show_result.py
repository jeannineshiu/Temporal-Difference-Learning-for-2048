import matplotlib.pyplot as plt
import pandas as pd

def main():
    df = pd.read_csv('mean_300k.csv')
    plt.plot(df.epoch, df.scores)
    plt.xlabel("epoch")
    plt.ylabel("scores")
    plt.show()


if __name__ == "__main__":
    main()
#%%