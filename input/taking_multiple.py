name, age = input("Enter your Name and age=> ").split()
print("your name is ", name)
print("you are ", age, " years old")
print()

firstName, lastName, age = input("Enter your first name, last name and age=> ").split()
print("your names are ", firstName, lastName)
print("you are ", age, " years old")
print()

firstname, lastname = input("Enter your first name and last name => ").split()
print("your first name is {} and your last name is {}".format(firstname, lastname))
print()

numbers = list(map(int, input("Enter multiple numbers => ").split()))
print("These are the number you input=> ", numbers)
print("The sum of the number you input=> ", sum(numbers))
print("This the largest number from the number you input => ", max(numbers))
print("This the smallest number from the number you input => ", min(numbers))
