
'''
2-1. Simple Message: Store a message in a variable, and then print that
message.

2-2. Simple Messages: Store a message in a variable, and print that message.
Then change the value of your variable to a new message, and print the new
message.
'''

# 1
hello = 'Hello github'
print(hello)

# 2
pyth = "Hi I'm Python"
print(pyth)
pyth = "I'm better than Java"
print(pyth)


'''
2-3. Personal Message: Store a person’s name in a variable, and print a message
to that person. Your message should be simple, such as, “Hello Eric,
would you like to learn some Python today?”

2-4. Name Cases: Store a person’s name in a variable, and then print that person’s
name in lowercase, uppercase, and titlecase.

2-5. Famous Quote: Find a quote from a famous person you admire. Print the
quote and the name of its author. Your output should look something like the
following, including the quotation marks:
Albert Einstein once said, “A person who never made a
mistake never tried anything new.”

2-6. Famous Quote 2: Repeat Exercise 2-5, but this time store the famous person’s
name in a variable called famous_person. Then compose your message
and store it in a new variable called message. Print your message.

2-7. Stripping Names: Store a person’s name, and include some whitespace
characters at the beginning and end of the name. Make sure you use each
character combination, "\t" and "\n", at least once.
Print the name once, so the whitespace around the name is displayed.
Then print the name using each of the three stripping functions, lstrip(),
rstrip(), and strip().
'''

# 3
Daniel = "Hello Daniel, what are you doing?"
print(Daniel)

# 4
ema = "Ema"
print(ema.lower())
print(ema.upper())
print(ema.title())

# 5
print('Steve Jobs once said, "Have the courage to follow your heart and intuition. They somehow know what you truly want to become."')

# 6
famous_person = "Albert Einstein"
message = "The difference between genius and stupidity is that genius has limits."
print(famous_person + ' once said, "' + message + '"')

# 7
name = "\tJohn Doe\n"

print("Unmodified:")
print(name)

print("\nUsing lstrip():")
print(name.lstrip())

print("\nUsing rstrip():")
print(name.rstrip())

print("\nUsing strip():")
print(name.strip())

'''
2-8. Number Eight: Write addition, subtraction, multiplication, and division
operations that each result in the number 8. Be sure to enclose your operations
in print statements to see the results. You should create four lines that look
like this:
print(5 + 3)
Your output should simply be four lines with the number 8 appearing once
on each line.

2-9. Favorite Number: Store your favorite number in a variable. Then, using
that variable, create a message that reveals your favorite number. Print that
message.
'''

# 8
print(2 + 4 * 3 / 2)

# 9
famous_number = 24
print("My favorite number is " + str(famous_number) + ".")

