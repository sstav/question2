# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class BankAccount:
    def __init__(self, name, amt):
        self.name = name
        self.amt = amt

    def __str__(self):
        return "Your account, " + self.name + ", has " + str(self.amt) + " dollars."


# OpenU - Maman 13 - Question 2.B
if __name__ == '__main__':
    t1 = BankAccount("Bob", 100)
    print(t1)

