def lose_speech() :
    print("Вы проиграли!")
def win_speech() :
    print("Вы выиграли!")
def get_word(w) :
    """
    :param w:
    :return:
    """
    return w[0]
def welcome_speech(t) :
    """
    :param t:
    :return:
    """
    print(f'''
    Добро пожаловать в игру - Hangman Console Edition (1.0)
    Ваша задача угадать слово за 3 попытки!
    Загаданное слово состоит из {len(t)} букв {t}
    ''')

def start_template(w) :
    """
    :param w:
    :return:
    """
    msw = []
    for c in w :
        msw.append('_')
    return msw

def list_to_string_convert(t) :
    """
    :param t:
    :return:
    """
    s = ''
    return s.join(t)
def user_input() :
    """
    :return:
    """
    return input('Введите букву: ')

def build_template(t, w, g='') :
    """
    :param t:
    :param w:
    :param g:
    :return:
    """
    for i in range(len(w)) :
        if t[i] == '_' :
            if w[i] == g :
                t[i] = w[i]
            else:
                t[i] = '_'
    return t

def print_result(g) :
    """
    :param g:
    :return:
    """
    print(f"Результат {g}")

def check_win(g) :
    """
    :param g:
    :return:
    """
    wspm = 0
    for l in g :
        if l == '_' :
            return True
    return False

def check_mistake(w, g) :
    """
    :param w:
    :param g:
    :return:
    """
    flag = False
    for i in w :
        if i == g:
            flag = True
    return flag

def check_attempt(l) :
    """
    :param l:
    :return:
    """
    return l - 1

def game() :
    progress = True
    word = ['apple']
    life = 3
    user_guess = 'string'
    guessed = ''

    word_in_play = get_word(word)
    template = start_template(word_in_play)
    welcome_speech(list_to_string_convert(template))

    while progress :
        user_guess = user_input()
        template = build_template(template, word_in_play, user_guess)
        guessed = list_to_string_convert(template)
        print_result(guessed)
        progress = check_win(guessed)

        if not check_mistake(word_in_play, user_guess):
            print(f'Осталось {life} попытки(ок)')
            life = check_attempt(life)

        if life == 0 :
            lose_speech()
            break
        if not progress :
            win_speech()


game()