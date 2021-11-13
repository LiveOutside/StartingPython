from pprint import pprint

p
class Cinema:
    def __init__(self, cinema_halls, time):
        self.halls = cinema_halls
        self.bank = 0
        self.time = time

    def append(self, new_halls):
        self.halls.append(new_halls)


class CinemaHall:
    def __init__(self, number, height, seats):
        self.number = number
        self.height = height
        self.seats = seats
        self.available_seats = [['0' for _ in range(height)] for _ in range(seats)]
        self.bank = 0
        self.films = []

    def append(self, new_film):
        self.films.append(new_film)


class Session:
    def __init__(self, cinema_hall, name, start_time, duration, cost):
        self.hall = cinema_hall
        self.name = name
        self.start_time = start_time
        self.duration = duration
        self.cost = cost

    def buy_ticket(self, row, place):
        if self.hall.available_seats[place - 1][row - 1] == '0':
            self.hall.available_seats[place - 1][row - 1] = 'X'
            self.hall.bank += self.cost
        else:
            print('Место занято')


hall1 = CinemaHall(1, 10, 20)
hall2 = CinemaHall(2, 10, 10)
hawaii = Cinema([hall1, hall2], 'С 10 до 7')
session1 = Session(hall1, '123', '12:00', '3:45', 5)
session2 = Session(hall1, '321', '16:00', '0:05', 5000)
session1.buy_ticket(3, 10)
session1.buy_ticket(5, 9)
session1.buy_ticket(3, 10)
pprint(hall1.available_seats)
print('Название:', session1.name, 'Начало:', session1.start_time, 'Длительность:', session1.duration, 'Заработок:', hall1.bank)