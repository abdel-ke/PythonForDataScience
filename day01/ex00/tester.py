from give_bmi import give_bmi, apply_limit

height = [2.71, 1.15, 1.71, 1.15, 1.90]
weight = [165.3, 38.4, 165.3, 80, 90.5]

bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))
