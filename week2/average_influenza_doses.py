import pandas as pd
import numpy as np


def average_influenza_doses():
    df = pd.read_csv('week2/NISPUF17.csv')
    breast_feed_cnt = df[df["CBF_01"] == 1]
    not_breast_feed_cnt = df[df["CBF_01"] == 2]
    breast_fed_average = np.mean(breast_feed_cnt["P_NUMFLU"])
    non_breast_fed_average = np.mean(not_breast_feed_cnt["P_NUMFLU"])
    result = (breast_fed_average, non_breast_fed_average)
    return result


if __name__ == '__main__':
    print(average_influenza_doses())
