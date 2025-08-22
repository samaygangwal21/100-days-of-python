import random
numbers = [1, 2, 3]
new_list = [n*n for n in numbers if n < 3]
print(new_list)

range_list = [n*n for n in range(1,4)]
print(range_list)

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
short_names = [name for name in names if len(name) < 5 ]
print(short_names)
capital_names = [name.upper() for name in names if len(name) > 5]
print(capital_names)

# Dictionary Comprehension
students_score = {student:random.randint(60,100) for student in names}
print(students_score)