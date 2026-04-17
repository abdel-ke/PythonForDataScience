from load_csv import load


def main():
    print("TEST 1 (file exists)")
    dataset = load("life_expectancy_years.csv")
    print(dataset)

    print("TEST 2 (file does not exist)")
    baddataset = load("nani.wtf")
    print(baddataset)

    print("TEST 3 (print the load __doc__)")
    print(load.__doc__)


if __name__ == "__main__":
    main()
