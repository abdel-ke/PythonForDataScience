from load_csv import load
import matplotlib.pyplot as plt


def population_str_to_float(s_population: str) -> float:
    """Convert a population text like 10k or 2M into a float.
    """
    if s_population.endswith("k"):
        return float(s_population[:-1]) * 1000
    elif s_population.endswith("M"):
        return float(s_population[:-1]) * 1000000
    elif s_population.endswith("B"):
        return float(s_population[:-1]) * 1000000000
    else:
        return float(s_population)


def convert(data):
    """Convert a sequence of population strings into float values."""
    return [population_str_to_float(p) for p in data]


def population_data(data, country_name):
    """Return the population values for one country up to a given
    number of years.
    """
    assert country_name in data['country'].values, \
        f"The country '{country_name}' does not exist in the dataset"
    country_data = data[data['country'] == country_name].values[0][1:]
    country_data = country_data[:-50]
    return convert(country_data)


def population_total(data, first_country, second_country):
    """Plot the population projections for two countries on the same graph."""
    years = data.columns[1:-50]
    first_country_data = population_data(data, first_country)
    second_country_data = population_data(data, second_country)

    plt.plot(years, first_country_data, label=first_country, color="red")
    plt.plot(years, second_country_data, label=second_country, color="orange")
    plt.title("Population Projections")
    plt.xticks(years[::40])
    plt.xlabel("Year")
    plt.yticks([20000000, 40000000, 60000000], ["20M", "40M", "60M"])
    plt.ylabel("Population")
    plt.legend(loc="lower right")
    plt.show()


def main():
    """Load the population dataset and display the comparison plot."""
    try:
        data = load("population_total.csv")
        if data is None:
            return
        population_total(data, "Morocco", "Spain")
    except AssertionError as ae:
        print("AssertionError:", ae)
    except Exception as e:
        print("Exception:", e)


if __name__ == "__main__":
    main()
