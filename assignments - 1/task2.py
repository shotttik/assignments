from random import randint

word_list = []
for number in range(1, 13):
    word_list.append(input(f'{number}) Enter word or number: '))

# word_list = ['4', '5', 'me', 'her', '3', '8', 'see', '9', 'he', '7', '6', '2']

question = True

num = 0
while question:
    try:
        num = int(input('Please enter the number of delete items: '))
    except ValueError:
        print('You should enter int value')
        break

    if 2 < num < 6:
        print(f'{num} items were randomly deleted.')
        question = False
    else:
        print('The number should fall between 2 and 6')
original_list = list(word_list)


def function(lst: list, x: int):
    for i in range(x):
        lst.pop(randint(1, 4))
    return f'Result tuple: {tuple(lst)}'


print(function(word_list, num))
print(f'Original list: {original_list}')
