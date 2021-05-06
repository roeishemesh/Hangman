import random
import json
file_path = r"C:\Users\Roei\OneDrive\שולחן העבודה\studies\python\self.py\unit 10\words.json"




def start_screen():
    """add letter to old_letter_guessed.
          :param: no param
          :return: the first game screen
          :rtype: str
          """
    print(""""  
    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \\ / _' | '_ ' _ \\ / _' | '_ \\
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                        __/ |
                       |___/)""")


def choose_word():
    """give us the secret word from json file.
      :return: a random word from file
      :rtype: str
      """
    global file_path
    with open(file_path, "r") as json_file:
        words_dict = json.load(json_file)
        words_list = words_dict["words"]
        return random.choice(words_list)

def print_hangman(number_of_tries):
    """give us a pic of hangman.
          :param number_of_tries: the number of worng guesses
          :type number_of_tries: int
          :return: picture of hangman
          :rtype: dict
          """
    hangman_dict = {
        1:
            "x-------x",

        2: """x-------x
|
|
|
|
|  """,

        3: '''x-------x
|       |
|       0
|
|
|''',

        4: '''x-------x
|       |
|       0
|       
|
|''',

        5: '''x-------x
|       |
|       0
|      /|\\
|
|''',

        6: '''x-------x
|       |
|       0
|      /|\\
|      /
|''',

        7: '''x-------x
|       |
|       0
|      /|\\
|      / \\
|'''}
    print(hangman_dict[number_of_tries] + "\n")


def show_hidden_word(secret_word, old_letter_guessed):
    """write "_" instead of letter in the secret word.
      :param secret_word: the secret word of the game
      :param old_letter_guessed: list of the letter that the player guess
      :type secret_word: str
      :type old_letter_guessed: list
      :return: our secret word with "_" instead of letter
      :rtype: str
      """
    new_str = ""
    for letter in secret_word:
        if letter in old_letter_guessed:
            new_str = new_str + " " + letter
        if letter not in old_letter_guessed:
            new_str = new_str + " _"
    return new_str


def check_valid_input(letter_guessed, old_letter_guessed):
    """check if the letter who geussed by the player are legal.
      :param letter_guessed: the letter that the player guess
      :param old_letter_guessed: the letter that the player already guess
      :type letter_guessed: str
      :type old_letter_guessed: list
      :return: if the letter is legal
      :rtype: bool
      """
    return len(letter_guessed) == 1 and letter_guessed.lower() not in old_letter_guessed


def try_update_letter_guessed(letter_guessed, old_letter_guessed):
    """add letter to old_letter_guessed.
      :param letter_guessed: the letter that the player guess
      :param old_letter_guessed: the letter that the player already guess
      :type letter_guessed: str
      :type old_letter_guessed: list
      :return: bool, list of the old_letter_guessed and message to player
      :rtype: list and str
      """
    if check_valid_input(letter_guessed, old_letter_guessed):
        old_letter_guessed.append(letter_guessed)
        return True
    else:
        print("Wrong !!!!")
        print("old letter guessed:" + "->".join(sorted(old_letter_guessed)))
        return False


def check_win(secret_word, old_letter_guessed):
    """check if the player guess all letters in secret word.
            :param secret_word: the secret word of the game
            :param old_letter_guessed: the letter that the player already guess
            :type secret_word: str
            :type old_letter_guessed: list
            :return: if the player guess all letter or not
            :rtype: bool
            """
    new_str = ""
    for letter in secret_word:
        if letter not in old_letter_guessed:
            new_str = new_str + letter
    if len(new_str) == 0:
        return True
    else:
        return False


def hangman_final_project(secret_word, old_letter_guessed):
    """combines all func together.
          :param secret_word: the secret word of the game
          :param old_letter_guessed: the letter that the player already guess
          :type secret_word: str
          :type old_letter_guessed: list
          :return: the result of the game
          :rtype: list and str
          """
    guess_number = 1
    print_hangman(guess_number)
    print(show_hidden_word(secret_word, old_letter_guessed))

    while True:
        letter_guessed = input("please guess a letter:")
        if letter_guessed in secret_word:
            try_update_letter_guessed(letter_guessed, old_letter_guessed)
            show_hidden_word(secret_word, old_letter_guessed)
            print_hangman(guess_number)
            print(show_hidden_word(secret_word, old_letter_guessed) + "\n")
            if check_win(secret_word, old_letter_guessed) is True:
                print("Good Job!!")
                break
        else:
            guess_number = guess_number + 1
            try_update_letter_guessed(letter_guessed, old_letter_guessed)
            try_update_letter_guessed(letter_guessed, old_letter_guessed)
            print_hangman(guess_number)
            print(show_hidden_word(secret_word, old_letter_guessed))
            if check_win(secret_word, old_letter_guessed) is True:
                print("Good Job!! \n Winner!!!!")
                break
        if guess_number == 7:
            print(f"You Lose!!!\nthe secret word is {secret_word}")
            break


def main():
    start_screen()
    choose_word()
    hangman_final_project(choose_word(), old_letter_guessed=[])


if __name__ == "__main__":
    main()
