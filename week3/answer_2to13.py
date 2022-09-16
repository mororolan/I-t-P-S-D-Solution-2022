import pandas as pd
import numpy as np
# Filter all warnings. If you would like to see the warnings, please comment the two lines below.
import warnings

warnings.filterwarnings('ignore')


def answer_two():
    all_data = pd.merge(pd.merge(energy, gdp, how='outer', on='Country'), scim_en, how='outer', on='Country')
    center_data = pd.merge(pd.merge(energy, gdp, how='inner', on='Country'), scim_en, how='inner', on='Country')

    return len(all_data) - len(center_data)


def answer_three():
    a = answer_one()
    avgGDP = a[['2006', '2007', '2008', '2009',
                '2010', '2011', '2012', '2013', '2014',
                '2015']].mean(axis='columns').sort_values(ascending=False)

    return avgGDP


# dtype is not right, will fix this bug as soon.
# TODO
def answer_four():
    a = answer_one()
    avgGDP = a[['2006', '2007', '2008', '2009',
                '2010', '2011', '2012', '2013', '2014',
                '2015']].mean(axis='columns').sort_values(ascending=False)
    a.sort_values(avgGDP, ascending=False, inplace=True)

    return int(abs(combined.index[5]['2015'] - combined.index[5]['2006']))


def answer_five():
    a = answer_one()

    return a['Energy Supply per Capita'].mean()


def answer_six():
    a = answer_one()
    a.sort_values('% Renewable', ascending=False, inplace=True)
    return (a.index[0], a['% Renewable'][0])


def answer_seven():
    a = answer_one()
    a['Citation Ratio'] = a['Self-citations'] / a['Citations']
    a.sort_values('Citation Ratio', ascending=False, inplace=True)

    return (a.index[0], a['Citation Ratio'][0])


def answer_eight():
    a = answer_one()
    a['Est Pop'] = a['Energy Supply'] / a['Energy Supply per Capita']
    a.sort_values('Est Pop', ascending=False, inplace=True)

    return a.index[2]


def answer_nine():
    a = answer_one()
    a['Est Pop'] = a['Energy Supply'] / a['Energy Supply per Capita']
    a['Citable Doc per Capita'] = a['Citable documents'] / a['Est Pop']

    return a['Citable Doc per Capita'].astype('float64').corr(a['Energy Supply per Capita'].astype('float64'))


def answer_ten():
    a = answer_one()
    med = a['% Renewable'].median(axis="rows")

    a['HighRenew'] = a['% Renewable'].apply(lambda x: 1 if x >= med else 0)
    return a['HighRenew']


def answer_eleven():
    ContinentDict = {'China': 'Asia',
                     'United States': 'North America',
                     'Japan': 'Asia',
                     'United Kingdom': 'Europe',
                     'Russian Federation': 'Europe',
                     'Canada': 'North America',
                     'Germany': 'Europe',
                     'India': 'Asia',
                     'France': 'Europe',
                     'South Korea': 'Asia',
                     'Italy': 'Europe',
                     'Spain': 'Europe',
                     'Iran': 'Asia',
                     'Australia': 'Australia',
                     'Brazil': 'South America'}

    out = pd.DataFrame(columns=['size', 'sum', 'mean', 'std'])

    a = answer_one()
    a['Est Pop'] = a['Energy Supply'] / a['Energy Supply per Capita']

    for group, frame in a.groupby(ContinentDict):
        out.loc[group] = [len(frame), frame['Est Pop'].sum(), frame['Est Pop'].mean(), frame['Est Pop'].std()]

    return out


def answer_twelve():
    ContinentDict = {'China': 'Asia',
                     'United States': 'North America',
                     'Japan': 'Asia',
                     'United Kingdom': 'Europe',
                     'Russian Federation': 'Europe',
                     'Canada': 'North America',
                     'Germany': 'Europe',
                     'India': 'Asia',
                     'France': 'Europe',
                     'South Korea': 'Asia',
                     'Italy': 'Europe',
                     'Spain': 'Europe',
                     'Iran': 'Asia',
                     'Australia': 'Australia',
                     'Brazil': 'South America'}

    a = answer_one()
    a['Continent'] = a.index.map(lambda c: ContinentDict[c])
    a['% Renewable'] = pd.cut(a['% Renewable'], 5)

    return a.groupby(['Continent', '% Renewable']).size()


def answer_thirteen():
    a = answer_one()
    a['Est Pop'] = a['Energy Supply'] / a['Energy Supply per Capita']

    return a['Est Pop'].apply(lambda s: '{:,}'.format(s))
