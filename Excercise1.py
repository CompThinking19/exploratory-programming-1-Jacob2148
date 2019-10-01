def double(sequence):
  result = []
  for element in sequence:
    result = result + [element * 2]
  return result
#defined the double function
double([3, 4, 5, 6])
#in comparison with jupyter notebook as to see results of function
x = [1, 2, 3]
y = [2, 4, 6]
double(x) + double(y)
