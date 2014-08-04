from sys import argv
from random import randint
from string import punctuation, replace


def strip_punctuation(text, replace_with_and=False):
	new_text = text
	if replace_with_and:
		length = len(text)
		if text[length - 1] == '.':
			# Gets rid of trailing 'AND's
			new_text = text[: length - 1]
		new_text = new_text.replace('.', ' and')
	new_text = new_text.translate(None, punctuation)
	return new_text


def add_random_caps(text):
	# apparently "".join is the most efficient way to concat strings
	new_text = []
	length = len(text)
	start_all_caps = randint(int(length * 0.25), int(length * 0.75))
	for i, char in enumerate(text):
		if not char.isalpha():
			new_text.append(char)
		elif char.isupper() and i < start_all_caps:
			new_text.append(char.lower())
		elif char.islower() and i >= start_all_caps:
			new_text.append(char.upper())
		else:
			new_text.append(char)
	return "".join(new_text)


def tumblrify(text, replace_with_and=False):
	stripped_text = strip_punctuation(text, replace_with_and)
	capped_text   = add_random_caps(stripped_text)
	return capped_text	


if __name__ == '__main__':
	arguments = argv[1:]
	arguments_as_string = ' '.join(arguments)
	print tumblrify(arguments_as_string, True)
