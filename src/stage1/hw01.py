class PiggyBank:
    def __init__(self, dollars=0, cents=0):
        self.dollars = 0
        self.cents = 0

        self.add_money(dollars, cents)

    def add_money(self, deposit_dollars, deposit_cents):
        self.dollars += deposit_dollars + (self.cents + deposit_cents) // 100
        self.cents = (self.cents + deposit_cents) % 100
