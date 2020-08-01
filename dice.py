import random


class MSdie:
    def __init__(self, n_sides):
        self.n_sides = n_sides
        self.current_Value = self.roll()

    def roll(self):
        self.current_Value = random.randrange(1, self.n_sides)
        return self.current_Value

    def __str__(self):
        return str(self. current_Value)

    def __repr__(self):
        return "MSD({})->{}".format(self.n_sides, self.current_Value)


# we have a class named MSDI
print(MSdie(5))


print("IM {}one IM {}two im {}three".format(1, 2, 3))
