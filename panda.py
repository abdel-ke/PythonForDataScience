import pandas as pd
import matplotlib.pyplot as plt

mydataset = {
  'cars': ['BMW', 'BOLVO', 'FORD'],
  'passings': [320, 430, 240],
  'colors': ['RED', 'GREEN', 'YELLOW']
}

myvar = pd.DataFrame(mydataset)
data =  pd.read_csv('life_expectancy_years.csv')

def test(brand):
    try:
        # if not len(myvar[myvar['cars'] == brand]):
        #     print(f"The Brand '{brand}' does not exist in the dataset")
        #     return False
        print(brand, " exist")
        brands = myvar['cars'].values
        colors = myvar['colors'].values
        passings= myvar['passings'].values
        plt.plot(passings, colors)
        plt.xticks(brands)
        # plt.title("hello")
        plt.xlabel("Cars")
        plt.ylabel('colors')
        plt.show()
    except Exception as e:
        print ("eroor: ", e)

# test("BMW")

bmw = myvar[myvar['cars'] == 'BMW']
ok = bmw.values[0][1:]
print(bmw)
print(ok)
# print(myvar.columns[1:].values)
# print(myvar[myvar['colors'] == 'blue'])
# print(data.columns.values)
print('--------------------')
print(myvar.shape)
print(myvar)
