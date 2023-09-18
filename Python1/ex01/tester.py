from array2D import slice_me

family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]

print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))

try:
    print(slice_me([[1, 2], [1, 2, 3]], 1, 5))
except ValueError as e:
    print(e)

try:
    print(slice_me([[1, 2], [1, 3]], "a", 5))
except TypeError as e:
    print(e)

try:
    print(slice_me([[1, 2], [1, 3]], 1, "a"))
except TypeError as e:
    print(e)
