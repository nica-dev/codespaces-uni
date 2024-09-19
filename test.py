from random import randint
class Number:
    value = 0
    lotteries = 1
    actual_cost = 5
    total_cost = 0
    total_revenue = 0
    def __init__(self, num):
        self.num = num
    def update(self, winner):
        if winner:
            total_revenue += self.actual_cost * 60
            total_cost += self.actual_cost
            self.actual_cost = 5
            self.lotteries = 1
        else:
            total_cost += self.actual_cost
            if self.lotteries >= 25:
                self.actual_cost *= 2
                self.lotteries = 1

numbers = [Number(x) for x in range(100)]
class Lotto:
    numbers = [Number(x) for x in range(100)]
    winners = []
    def draw(self):
        winner = randint(100)
        for number in self.numbers:
            if number.number == winner:
                