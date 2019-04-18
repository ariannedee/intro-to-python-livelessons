"""
Ask the user to supply the words to the story in {}'s.
Tell them the story with the words they gave inserted in.
"""

# Write a story with some words missing
story = '''
Roses are {colour}
Violets are {colour2}
Sugar is {taste}
And so are you
'''

# Ask the user to provide the missing words
colour = input('Give me a colour: ')
colour2 = input('Give me another colour: ')
taste = input('Give me a flavour: ')

# Display the final story
print(story.format(colour=colour, colour2=colour2, taste=taste))
