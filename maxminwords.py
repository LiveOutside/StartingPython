class MinMaxWordFinder:
    def __init__(self):
        self.min = 1000
        self.max = 0
        self.sentences = []
        self.short = []
        self.long = []

    def add_sentence(self, sentence):
        for i in sentence.split():
            self.sentences.append(i)

    def shortest_words(self):
        self.short = []
        for i in self.sentences:
            if len(i) < self.min:
                self.min = len(i)
        for j in self.sentences:
            if len(j) == self.min:
                self.short.append(j)
        return sorted(self.short)

    def longest_words(self):
        self.long = []
        for i in self.sentences:
            if len(i) > self.max:
                self.max = len(i)
        for j in self.sentences:
            if len(j) == self.max:
                if j not in self.long:
                    self.long.append(j)
        return sorted(self.long)



