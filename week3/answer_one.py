from typing import Dict, Any

import pandas as pd
import numpy as np
from pandas import DataFrame


def answer_one():
    # read file
    energy = pd.read_excel('Energy Indicators.xls')
    # get rid of the first two columns
    energy.drop(energy.columns[[0, 1]], inplace=True, axis='columns')
    #  change the column labels
    energy.rename(columns={'Unnamed: 2': 'Country', 'Unnamed: 3': 'Energy Supply',
                           'Unnamed: 4': 'Energy Supply per Capita', 'Unnamed: 5': '% Renewable'},
                  inplace=True)
    # replace the missing data
    energy['Energy Supply'].replace('...', np.NaN, inplace=True)

    # Convert Energy Supply to gigajoules
    for k, v in energy['Energy Supply'].iteritems():
        energy['Energy Supply'].set_value(k, v * 1000000)

    # Rename countries
    replace_values = {"Republic of Korea": "South Korea",
                      "United States of America": "United States",
                      "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
                      "China, Hong Kong Special Administrative Region": "Hong Kong"}
    energy['Country'].rename(replace_values, inplace=True)
    # change nums
    energy['Country'].replace(r' \(.*\)', '', regex=True, inplace=True)
    energy['Country'].replace(r'[0-9]*', '', regex=True, inplace=True)
    pd.write_csv()
    result = 0
    return result


if __name__ == '__main__':
    answer_one()
