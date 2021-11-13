class Selector:
    def __init__(self, values):
        self.list = values
        self.ODDS = []
        self.EVENS = []
        for i in self.list:
            if i % 2 != 0:
                self.ODDS.append(i)
            else:
                self.EVENS.append(i)

    def get_odds(self):
        return self.ODDS

    def get_evens(self):
        return self.EVENS


values = [11, 12, 13, 14, 15, 16, 22, 44, 66]
selector = Selector(values)
values.clear()
odds = selector.get_odds()
evens = selector.get_evens()
print(' '.join(map(str, evens)))
print(' '.join(map(str, odds)))

selector = Selector([])
odds = selector.get_odds()
evens = selector.get_evens()
print(' '.join(map(str, evens)))
print(' '.join(map(str, odds)))

selector = Selector([0])
odds = selector.get_odds()
evens = selector.get_evens()
print(' '.join(map(str, evens)))
print(' '.join(map(str, odds)))


