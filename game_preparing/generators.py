import random


class GenerateValues:
    @staticmethod
    def generate_value():
        x = random.randint(1, 9)
        return x

    @staticmethod
    def generate_row_column_value(x):
        val = random.randint(x, x+2)
        return val

    @staticmethod
    def pick_final_number_completed():
        x = int(input("How many blocks you would like completed: 22 to 25? "))
        while 22 > x > 25:
            print("Pick one of the values from 22 to 25")
            x = int(input(""))
        return x
