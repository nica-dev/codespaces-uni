class Number:
    number = 0
    lotteries = 0
    actual_cost = 0
    total_cost = 0
    total_revenue = 0
    def __init__(self, num):
        self.num = num
    def update_cost(self, winner):
        if winner:
            total_revenue += self.actual_cost * 60