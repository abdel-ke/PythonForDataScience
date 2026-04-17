import pandas as pd
import matplotlib.pyplot as plt

# 1. Create a DataFrame with two columns
# df = pd.DataFrame({
#     'Coutry': [2019, 2020, 2021, 2022, 2023, 2024],
#     'Khouriba': [300, 0, 400, 200, 250, 300],
#     'BenGurir': [150, 0, 300, 200, 300, 250],
#     'Tetouan': [0, 0, 0, 100, 80, 120]
# })

df = pd.DataFrame({
    'Country': ['Khouribga', 'BenGurir', 'Tetouan'],
    2019: [300, 150, 0],
    2020: [0, 0, 0],
    2021: [400, 300, 0],
    2022: [200, 200, 100],
    2023: [250, 300, 80],
    2024: [300, 250, 120],

})

try:
    years = df.columns[1:]
    total_kh = df[df['Country'] == 'Khouribga'].values[0][1:]
    total_bg = df[df['Country'] == 'BenGurir'].values[0][1:]
    total_ttn = df[df['Country'] == 'Tetouan'].values[0][1:]

    print(df)
    # print(years)
    print('-----------------------------')
    # print(years.values)
    plt.plot(years, total_kh)
    plt.plot(years, total_bg)
    plt.plot(years, total_ttn)
    plt.xlabel('Years')
    plt.ylabel('total students')
    plt.grid()
    plt.show()
except Exception as e:
    print('error: ', e)
