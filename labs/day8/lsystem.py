class LSystem():

    def __init__(self, alphabet, starter, rules):
        self.alphabet = alphabet
        self.starter  = starter
        self.rules    = rules

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
        "A": {
            9/10 : funcA1,
            -1 : funcA2,
        }
        "B": {
            -1 : funcB
        }
    }

    """
    def __init__(self):
        self.dict = {}

    def __setitem__(self, key : str, value : dict):
        for key in value.keys():
            pass
        self.dict[key] = value

    def __getitem__(self, item):
        pass


if __name__ == "__main__":
    sys = LSystem("AB", "A", {"A":"AB","B":"A"})
    sys.revolveN(3)
    print(sys.getSequence())