import game_logic

words_list = game_logic.get_words_list()

while game_logic.words_in_list(words_list):
    current_word, word_description = game_logic.get_word(words_list)
    lives = game_logic.get_lives()
    guessed = game_logic.get_guessed()
    table = game_logic.create_table(current_word)
    unique_letters = game_logic.get_unique_letters(current_word)
    guessed_letters = game_logic.get_guessed_letters()
    count_of_words = game_logic.return_len(words_list)
    msg_letter_or_word = 'Введите букву или слово целиком: '
    msg_wrong = '\nНеправильно. Вы теряете жизнь :( \n'
    msg_viselica_win = game_logic.read_file('win')
    msg_win = '\nВы угадали слово ' + current_word + '! Приз в студию!'
    msg_viselica_lose = game_logic.read_file('lose')
    msg_lose = 'Вы проиграли'
    msg_letter_guessed = 'Эта буква уже была угадана\n'
    msg_continue_game = '\nХотите поиграть еще? Да | Нет \n'
    msg_start_new_game = f'\nПоехали! Осталось угадать {count_of_words - 1} слов'
    msg_no_words = 'Вы угадали все слова'
    msg_exit = 'До встречи!'
    msg_ = ''

    while game_logic.is_alive(lives):
        if game_logic.word_guessed(guessed, unique_letters):
            break
        game_logic.show_message(game_logic.msg_lives(lives) + table + '\n' + word_description)
        answer = game_logic.prompt(msg_letter_or_word)
        while True:
            if game_logic.check_input(answer, current_word):
                break
            else:
                answer = game_logic.prompt(msg_letter_or_word)
        if game_logic.check_word(current_word, answer):
            if game_logic.is_word_correct(current_word, answer):
                break
            else:
                lives = game_logic.lose()
        elif game_logic.letter_in_word(current_word, answer):
            if game_logic.is_letter_guessed(guessed_letters, answer):
                game_logic.show_message(msg_letter_guessed)
            else:
                game_logic.add_guessed_letter(guessed_letters, answer)
                table = game_logic.new_table(answer, current_word, table)
                guessed = game_logic.guessed_plus(guessed)
                game_logic.show_message(msg_)
        else:
            lives = game_logic.lives_min(lives)
            game_logic.show_message(msg_wrong, msg_)

    if game_logic.is_alive(lives):
        game_logic.show_message(msg_viselica_win, msg_win)
        while True:
            continue_game = game_logic.prompt(msg_continue_game)
            if game_logic.check_new_game(continue_game):
                break
            else:
                continue_game = game_logic.prompt(msg_continue_game)
        if game_logic.continue_game(continue_game):
            if game_logic.word_list_is_not_empty(words_list):
                game_logic.delete_word(current_word, words_list)
                game_logic.show_message(msg_start_new_game)
                continue
            else:
                game_logic.show_message(msg_no_words)
                break
        else:
            game_logic.show_message(msg_exit)
            break
    else:
        game_logic.show_message(msg_viselica_lose, msg_lose)
        break
else:
    game_logic.show_message(msg_no_words)