name = 'John'
print('Hello, {}!' .format(name))

age = 25
print('Hello, {}. You are {} years old.' .format(name, age))

print('Hello, {name}. You are {age} years old.' .format(name='Jane', age=30))

print('Hello, {1}. You are {0} years old.' .format(age, name))



s = "Hello, wprld!"
first_five = s[:6]
print(first_five)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = numbers[0:10:2]
print(odd_numbers)

odd_numbers = numbers[::2]
print(odd_numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = numbers [1:10:2]
print(even_numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
three_numbers = numbers[2:10:3]
print(three_numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reverse_numbers = numbers[:-2]
print(reverse_numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
copy_numbers = numbers[:]
print(copy_numbers)