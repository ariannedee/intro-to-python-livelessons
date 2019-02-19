# String formatting
num_problems = 99
print('I\'ve got %i problems' % num_problems)  # old-style
print('I\'ve got ' + str(num_problems) + ' problems')  # concatenation
print("I've got {} problems".format(num_problems))  # format
print("I've got {num_problems} problems".format(num_problems=num_problems))  # format with keywords
print(f"I've got {num_problems} problems")  # f-string

multi_line_string = '''
I have eaten
the plums
that were in
the icebox
'''

fruits = 'mangoes'
multi_line_fstring = f'''
I have eaten
the {fruits}
that were in
the icebox
'''

# String methods
string = 'Hello world'
print(string.upper())
print(string.lower())
print(string.title())
print(string.capitalize())

print(string[0:4])
print(string[5:])
print(string[::2])
print(string[::-1])

string_list = string.split()
print(string_list)
print('*'.join(string_list))
