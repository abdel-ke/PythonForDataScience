from load_csv import load
import matplotlib.pyplot as plt


def display_country_life_expectancy(country: str, data) -> None:
    """
    Display the life expectancy of a country over the years.

    Parameters
        country(str): The country to display the life expectancy for.
        data(pd.DataFrame): The data to display the life expectancy from.

    Returns
        None: If the country does not exist in the dataset.
    """
    if not len(data[data["country"] == country]):
        print(f"The country '{country}' does not exist in the dataset")
        return None

    country_data = data[data["country"] == country]

    years = data.columns[1:]
    life_expectancy = country_data.values[0][1:]

    plt.plot(years, life_expectancy)
    plt.title(country + " Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.xticks(years[::40])
    plt.show()


def main():
    """
    Main function to display the life expectancy of a country.

    Parameters
        None

    Returns
        None
    """

    try:

        data = load("life_expectancy_years.csv")

        display_country_life_expectancy("Morocco", data)

    except Exception as e:
        print("Exception:", e)


if __name__ == "__main__":
    main()
