from give_bmi import give_bmi, apply_limit

height = [2.71, 1.15]
weight = [165.3, 38.4]

bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))

bmi = give_bmi([1, 2], [1, 2, 3])
print(bmi, type(bmi))
print(apply_limit(bmi, 26))

bmi = give_bmi([1, 2], [1, "a"])
print(bmi, type(bmi))
print(apply_limit(bmi, 26))

bmi = give_bmi([1, 2], [1, None])
print(bmi, type(bmi))
print(apply_limit(bmi, 26))

bmi = give_bmi([1, 'a'], [1, 2])
print(bmi, type(bmi))
print(apply_limit(bmi, 26))

bmi = give_bmi([1, None], [1, 2])
print(bmi, type(bmi))
print(apply_limit(bmi, 26))

bmi = give_bmi([1, 2], [1, -2])
print(bmi, type(bmi))
print(apply_limit(bmi, 26))

bmi = give_bmi([1, 2], [1, 2])
print(bmi, type(bmi))
print(apply_limit(bmi, "a"))

bmi = give_bmi([1, 2], [1, 2])
print("bmi", type(bmi))
print(apply_limit([2, "a"], 26))

bmi = give_bmi([1, 2], [1, 2])
print("bmi", type(bmi))
print(apply_limit([2, None], 26))

bmi = give_bmi([1, 2], None)
print("bmi", type(bmi))
print(apply_limit(bmi, 26))

bmi = give_bmi(None, [1, 2])
print("bmi", type(bmi))
print(apply_limit(bmi, 26))

bmi = give_bmi([1, 2], [1, 2])
print("bmi", type(bmi))
print(apply_limit(None, 26))

bmi = give_bmi([1, 2], [1, 2])
print("bmi", type(bmi))
print(apply_limit(bmi, None))

bmi = give_bmi(2, 1)
print("bmi", type(bmi))
print(apply_limit(bmi, 26))

bmi = give_bmi(2, 1)
print("bmi", type(bmi))
print(apply_limit(1, 26))