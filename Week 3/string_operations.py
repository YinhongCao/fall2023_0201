first_name = "Harry"
n = len(first_name)

first_name = 'Bruce'
last_name = 'Wayne'

full_name = first_name + ' ' + last_name
print(full_name)

full_name = 'Bruce '
full_name += 'Wayne'

print(full_name)

text = 'Apple'
print(text * 3)

age = 35
age_text = "My age is "
print(age_text + str(age))

first_name = "Harry"
start_character = first_name[0] # H
last_character = first_name[4] 	# y
char_sequence = first_name[1:2] # “ar”

text = 'Don Quijote'
text[4] # Gets the 5th character 'Q'
text[-1] # Gets the last character 'e'

text = 'Don Quijote'
text[4:8] # Slices the text 'Quij'
text[4:] # Slices the text from index 4 to the end of the string 'Quijote'
text[:4] # Slices the text up to index 4 (not included) 'Don'
text[:] # Whole text, no slicing