import pandas as pd


def proportion_of_education():
    df = pd.read_csv('week2/NISPUF17.csv')
    all_cnt = len(df)
    ls_high = len(df[df['EDUC1'] == 1])
    high = len(df[df['EDUC1'] == 2])
    not_clg = len(df[df['EDUC1'] == 3])
    clg = len(df[df['EDUC1'] == 4])
    result = {"less than high school": ls_high / all_cnt,
              "high school": high / all_cnt,
              "more than high school but not college": not_clg / all_cnt,
              "college": clg / all_cnt}
    return result


if __name__ == '__main__':
    print(proportion_of_education())

