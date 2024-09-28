import re

class WordsFinder:
    def __init__(self, *file_names: str):
        self.file_names = file_names
        
    def get_all_words(self):
        symbols_for_del = [',', '.', '=', '!', '?', ';', ':', ' - ']
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as f:
                string = f.read().lower().strip()

            for sub in symbols_for_del:
                string = string.replace(sub, ' ')
            
            all_words[file_name] = string.split()
        
        return all_words

    def find(self, word):
        all_words: dict[list] = self.get_all_words()

        res = {}
        for file in all_words:
            index = all_words[file].index(word)
            if index:
                res[file] = index + 1

        return res

    def count(self, word):
        all_words: dict[list] = self.get_all_words()

        res = {}
        for file in all_words:
            cnt = all_words[file].count(word)
            if cnt:
                res[file] = cnt

        return res


def main():
    finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                          'Rudyard Kipling - If.txt',
                          'Mother Goose - Monday’s Child.txt')
    print(finder1.get_all_words())
    print(finder1.find('the'))
    print(finder1.count('the'))


if __name__ == '__main__':
    main()
