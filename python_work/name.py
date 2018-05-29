name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

#concatenation
first_name = "Ada"
last_name = "Lovelace"
full_name = first_name + " " + last_name
print(full_name)

print("Hello, " + full_name.title() + "!")

#tabs
print("\tPython")
#new line
print("\nThis\nis\na\nnew\nline")

#stripping whitespace
	#strip white space on right end
favorite_language = "python "
favorite_language.rstrip()

	# ** this is only removed temporarily
	# need to write over old variable

	favorite_language = favorite_language.rstrip()

	# left strip
	favorite_language = " python"
	favorite_language.rstrip()

	# strip both sides
	favorite_language = " python "
	favorite_language.strip()