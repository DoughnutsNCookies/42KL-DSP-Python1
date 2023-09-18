from give_bmi import give_bmi, apply_limit

height = [2.71, 1.15]
weight = [165.3, 38.4]

bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))

try:
    bmi = give_bmi([1, 2], [1, 2, 3])
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))
except ValueError as e:
    print(e)

try:
    bmi = give_bmi([1, 2], [1, "a"])
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))
except ValueError as e:
    print(e)

try:
    bmi = give_bmi([1, 2], [1, -2])
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))
except ValueError as e:
    print(e)

try:
    bmi = give_bmi([1, 2], [1, 2])
    print(bmi, type(bmi))
    print(apply_limit(bmi, "a"))
except ValueError as e:
    print(e)

try:
    bmi = give_bmi([1, 2], [1, 2])
    print("bmi", type(bmi))
    print(apply_limit([2, "a"], 26))
except ValueError as e:
    print(e)
