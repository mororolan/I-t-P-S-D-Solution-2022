import pandas as pd


def chickenpox_by_sex():
    df = pd.read_csv('week2/NISPUF17.csv')
    males = df[df['SEX'] == 1]
    females = df[df['SEX'] == 2]
    vaccinated_male = males[males['P_NUMVRC'] > 0]
    vaccinated_female = females[females['P_NUMVRC'] > 0]

    vaccinated_male_ill = len(vaccinated_male[vaccinated_male['HAD_CPOX'] == 1])
    vaccinated_male_health = len(vaccinated_male[vaccinated_male['HAD_CPOX'] == 2])

    vaccinated_female_ill = len(vaccinated_female[vaccinated_female['HAD_CPOX'] == 1])
    vaccinated_female_health = len(vaccinated_female[vaccinated_female['HAD_CPOX'] == 2])

    result = {"male": vaccinated_male_ill / vaccinated_male_health,
              "female": vaccinated_female_ill / vaccinated_female_health}

    return result


if __name__ == '__main__':
    print(chickenpox_by_sex())
