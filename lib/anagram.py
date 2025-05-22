class Anagram:
    def __init__(self, word):
        self.word = word
        self.sorted_word = sorted(self.word)

    def match(self, words):
        matches = []

        for possible in words:
            possible_lower = possible.lower()
            if possible_lower != self.word and sorted(possible_lower) == self.sorted_word:
                matches.append(possible)
        return matches
    
listen = Anagram("listen")
print(listen.match(['enlists', 'google', 'icelets', 'banana']))
