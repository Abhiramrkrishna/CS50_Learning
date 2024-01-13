# import random

# class Hat:
#     def __init__(self):
#         self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Syltherin"]

#     def sort(self, name):
#         print(name, "is in", random.choice(self.houses))


# hat = Hat()
# hat.sort("Harry")

import random

class Hat:
    @classmethod
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Syltherin"]

    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))



Hat.sort("Harry")