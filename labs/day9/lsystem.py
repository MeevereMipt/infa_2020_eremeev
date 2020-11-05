from random import random

class LSystem():

    def __init__(self, alphabet, starter, rules):
        self.alphabet = alphabet
        self.starter = starter
        self.rules = rules

        self.sequence = self.starter

    def revolve(self):
        new_sequence = ""
        for sym in self.sequence:
            if sym in self.rules:
                new_sequence += self.rules[sym]
            else:
                new_sequence += sym
        self.sequence = new_sequence

    def revolveN(self, n):
        for i in range(n):
            self.revolve()

    def getSequence(self):
        return self.sequence


class Rule():
    """
    example
    {
        "A": [
            { funcA1, 0.5 }
            { funcA1, -1  } # "else"
        ],
        "B": [
            -1 : funcB
        ]
    }

    """

    PROBABILITY = 1
    FUNCTION = 0

    def __init__(self, dict=None):

        self.dict = {}

        if dict is not None:
            for key in dict.keys():
                self.__setitem__(key, dict[key])


    @staticmethod
    def reformat(array: list):
        arr = []
        start = 0
        default_func = None
        for elem in array:
            if elem[Rule.PROBABILITY] > 0:
                arr.append([elem[Rule.FUNCTION], elem[Rule.PROBABILITY] + start])
                start += elem[Rule.PROBABILITY]
            elif default_func is None:
                default_func = elem[Rule.FUNCTION]

        return arr, default_func

    def __setitem__(self, key: str, value):

        funcs = None
        default_func = None

        if isinstance(value, list):
            # if it's a list of functions
            funcs, default_func = Rule.reformat(value)  # make func array with proper format

        else:
            # if it's just some function
            funcs, default_func = None, value

        self.dict[key] = (funcs, default_func)

    def __getitem__(self, key):

        rand = random()

        funcs, default_func = self.dict[key]
        if funcs is not None:
            for elem in funcs:
                if rand < elem[Rule.PROBABILITY]:
                    return elem[Rule.FUNCTION]
        return default_func

    def __contains__(self, item):
        return item in self.dict.keys()


if __name__ == "__main__":
    sys = LSystem("AB", "A", {"A": "AB", "B": "A"})
    sys.revolveN(3)
    print(sys.getSequence())

    array = [
        ["test1", 0.5],
        ["test2", 0.2],
        ["wind1", -1],
        ["wind2", -1]
    ]
    print(array)
    print(Rule.reformat(array))
    print(array)

    rules = Rule({
        "A": [
            ["test",0.5],
            ["heh",-1]
        ],
        "B": "bruh"
    })

    print(rules["A"], rules["B"])



