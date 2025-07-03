from collections import Counter

def colorize_guess(target_word: str, guess: str) -> str:
    correct_letters = ''
    word_colors = ''

    guess_letter_counts = Counter(guess)
    # print('guess letter counts: ' + str(guess_letter_counts))
    target_letter_counts = Counter(target_word)
    # print('target letter counts: ' + str(target_letter_counts))

    for target_letter, guess_letter in zip(target_word, guess):
        if guess_letter == target_letter:
            correct_letters += guess_letter

    correct_letters_counts = Counter(correct_letters)
    print('corrects letter counts: ' + str(correct_letters_counts))
    print('')

    for index, letter in enumerate(guess):
        letter_color = 'n'
        if letter == target_word[index]:
            letter_color = 'g'
            correct_letters_counts[letter] -= 1
        elif letter in target_word:
            num_remaining_target_letters = target_letter_counts[letter] - correct_letters_counts[letter]
            more_remain = num_remaining_target_letters > 0
            if letter in correct_letters and more_remain and correct_letters_counts[letter] > 0:
                letter_color = 'y'
            elif letter not in correct_letters and target_letter_counts[letter] > 0:
                letter_color = 'y'
            else:
                letter_color = 'e'

        guess_letter_counts[letter] -= 1
        target_letter_counts[letter] -= 1

        word_colors += letter_color

    return word_colors

if __name__ == '__main__':
    print(colorize_guess('cedar', 'seedy')) # ngxy