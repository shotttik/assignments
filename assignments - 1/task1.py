# word_list = ['farshad', 'ghassemi?d', 'madam', '?radar?', 'duration', 'con?tained']

word_list = []
ask = 0
question = True
while question:
	word_list.append(input('Please Enter word: '))
	ask = input('Do you want to stop asking? y or Y: ')
	if ask == 'y' or ask == 'Y':
		print(f'Your list - {word_list}')
		question = False


def check_question_marks(lst: list):
	print('Question Marks Check: ')
	for word in lst:
		if '?' in word:
			print(word, ' contains question mark')


check_question_marks(word_list)


def common_character_check(lst: list):
	print('\nCharacter a appears in all items')
	for word in lst:
		if 'a' in word:
			print(word, f'contains {word.count("a")} a')

	print('\nCharacter d appears in all items')
	for word in lst:
		if 'd' in word:
			print(word, f'contains {word.count("d")} d')


common_character_check(word_list)
