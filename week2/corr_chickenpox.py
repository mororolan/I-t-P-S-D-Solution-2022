import pandas as pd
import scipy.stats as stats


def corr_chickenpox():
    df = pd.read_csv('NISPUF17.csv')
    df = df[df['P_NUMVRC'] >= 0]
    df = df[df['HAD_CPOX'] < 3]

    corr, pval = stats.pearsonr(df["HAD_CPOX"], df["P_NUMVRC"])
    return corr


if __name__ == '__main__':
    print(corr_chickenpox())
