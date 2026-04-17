from load_csv import load
import matplotlib.pyplot as plt


def projection_life(income, life, year):
    assert year in income, \
        f"the year {year} not exist in data"
    assert year in life, \
        f"the year {year} not exist in data"

    income_data = income[year]
    life_data = life[year]
    plt.plot(income_data, life_data, 'o')
    plt.xscale('log')
    plt.xticks([300, 1000, 10000], [300, '1k', '10k'])
    plt.title('1900')
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life Expectancy')
    plt.show()


def main():
    try:
        income = \
            load('income_per_person_gdppercapita_ppp_inflation_adjusted.csv')
        life = load('life_expectancy_years.csv')
        if income is None:
            return None
        if life is None:
            return None
        projection_life(income, life, '1900')
    except AssertionError as a:
        print("AssertionError:", a)
    except Exception as e:
        print("Exception:", e)


if __name__ == "__main__":
    main()
