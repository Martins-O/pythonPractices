import operator

number = eval(input("Enter a number=> "))
numbers = eval(input("Enter a number=> "))

print(operator.add(number, numbers))
print(operator.sub(number, numbers))
print(operator.mul(number, numbers))
print(operator.truediv(number, numbers))
print(operator.floordiv(number, numbers))
print(operator.mod(number, numbers))
print(operator.eq(number, numbers))
print(operator.ne(number, numbers))
print(operator.lt(number, numbers))
print(operator.le(number, numbers))
print(operator.ge(number, numbers))