from components import vars
from emoji import emojize

def total(value):

	if value <= 10:
		vars.character = vars.characters[0]

		print(fore.RED + "It's " + vars.characters)
		print(emoji.emojize('This character is :thumbs_up:'))