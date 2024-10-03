import string


class WordsFinder:
    def __init__(self, *file_name):
        self.file_names = file_name

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding="utf-8") as file:
                line = file.read().lower()
                for p in string.punctuation:
                    if p in line:
                        line = line.replace(p, "")
                all_words[file_name] = line.split()
        return all_words

    def find(self, word):
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                position = words.index(word.lower()) + 1
                return {name: position}

    def count(self, word):
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                count_ = words.count(word.lower())
                return {name: count_}


finder2 = WordsFinder("test_file.txt")
print(finder2.get_all_words())  # Все слова
print(finder2.find("TEXT"))  # 3 слово по счёту
print(finder2.count("teXT"))  # 4 слова teXT в тексте всего
