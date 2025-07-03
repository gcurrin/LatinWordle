from random import choice

print('word_list.py console test')

class WordList:
    def __init__(self):
        with open('static/words.txt', 'r') as file:
            lines = file.readlines()

        trimmed_lines = [line.strip() for line in lines]
        self.words = set(trimmed_lines)

    def __contains__(self, item):
        return item in self.words

    def choose_random(self):
        return choice(list(self.words))

if __name__ == '__main__':
    words = WordList()
    # print('medea' in words)
    # print('spies' in words)