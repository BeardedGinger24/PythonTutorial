
# we might want to add a number into a string, but it will throw errors (giving a type error):
age = 23
message = "Happy " + age + "rd Birthday!"
print(message)

# instead convert the number value to a stirng:
age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)