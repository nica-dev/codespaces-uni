from random import randint

class Number:
    value = 0
    lotteries = 1
    actual_cost = 5
    total_cost = 0
    total_revenue = 0
    def __init__(self, num):
        self.num = num
    def update(self, is_winner):
        if is_winner:
            total_revenue += self.actual_cost * 60
            total_cost += self.actual_cost
            self.actual_cost = 5
            self.lotteries = 1
        else:
            total_cost += self.actual_cost
            if self.lotteries >= 25:
                self.actual_cost *= 2
                self.lotteries = 1

class Lotto:
    numbers = [Number(x) for x in range(100)]
    winners = []
    def draw(self):
        winner = randint(100)
        for number in self.numbers:
            number.update(number.value == winner)
        return winner
    def get_result(self):
        total_cost = 0
        total_revenue = 0
        for number in self.numbers:
            total_cost += number.total_cost
            total_revenue += number.total_revenue
        return total_revenue - total_cost

def main():
    lotto = Lotto()
    for i in range(100):
        winner = lotto.draw()
        result = lotto.get_result()
        print(f"Sorteo: {i}, Ganador: {winner}, Resultado: {result}")

main()