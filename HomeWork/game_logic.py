import random


def get_dict(filename):
    words_dict = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            word, description = line.strip().split(':')
            words_dict[word] = description
    return words_dict


def read_file(result):
    filename = 'txt_files\\win.txt' if result == 'win' else 'txt_files\\fails3.txt'
    with open(filename, 'r', encoding='utf-8') as f:
        msg_result = f.read()
    return f'{msg_result}\n'


def get_word(words_list):
    words_dict = get_dict('txt_files\\wnd.txt')
    word = random.choice(words_list)
    word_description = words_dict.get(word)
    return word, word_description


def get_words_list(): return list(get_dict('txt_files\\wnd.txt').keys())


def get_lives(): return 3


def return_len(item): return len(item)


def word_list_is_not_empty(word_list): return len(word_list) - 1 != 0


def delete_word(current_word, word_list): word_list.remove(current_word)


def get_guessed(): return 0


def words_in_list(words_list): return len(words_list) != 0


def get_unique_letters(current_word): return set([letter for letter in current_word])


def get_guessed_letters(): return set('')


def create_table(current_word):
    table = ''
    for i in range(len(current_word)):
        table += '\u25A0 '
    return table


def check_new_game(continue_game): return 'да' in continue_game or 'нет' in continue_game


def continue_game(continue_game): return continue_game == 'да'


def add_guessed_letter(guessed_letters, answer): guessed_letters.add(answer)


def is_letter_guessed(guessed_letters, answer): return answer in guessed_letters


def word_guessed(guessed, unique_letters): return guessed == len(unique_letters)


def check_word(current_word, answer): return len(current_word) == len(answer)


def lose(): return 0


def lives_min(lives): return lives - 1


def guessed_plus(guessed): return guessed + 1


def is_alive(lives): return lives > 0


def prompt(msg): return input(msg).lower()


def show_message(*msg): print(*msg)


def letter_in_word(current_word, answer): return answer in current_word


def is_word_correct(current_word, answer): return answer == current_word


def check_input(answer, current_word):  return len(answer) == 1 or len(answer) == len(current_word)


def msg_lives(lives):
    hearts = f'|❤️x{lives} '
    filename = 'txt_files\\'
    if lives == 3:
        filename += 'fails0.txt'
    elif lives == 2:
        filename += 'fails1.txt'
    elif lives == 1:
        filename += 'fails2.txt'
    with open(filename, 'r', encoding='utf-8') as f:
        pic = f.read()
    return f'{pic}\n{hearts}'


def new_table(letter, current_word, oldtable):
    letter_list = [lt for lt in current_word]
    count = current_word.count(letter)
    oldtable = oldtable.split(' ')

    if count != 1:
        while count != 0:
            index = letter_list.index(letter)
            oldtable[index] = letter
            letter_list[index] = '-'
            count -= 1
    else:
        index = letter_list.index(letter)
        oldtable[index] = letter
    oldtable = ' '.join(oldtable)
    return oldtable