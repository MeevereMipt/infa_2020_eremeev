class Intervals:

    def __init__(self):
        self.list = dict()
        self.keys = []

    def find_greater(self, key):
        elem1, k = None, None
        for i, elem in enumerate(self.keys):
            print(elem)
            if elem >= key:
                elem1 = elem; k = i
                break
        return (elem1, k)

    def __setitem__(self, key, value):
        elem, k = self.find_greater(key)
        print(elem, k)
        if elem is None:
            self.keys.append(key)
        else:
            self.keys.insert(k, key)

        self.list[key] = value

    def __str__(self):
        return str(self.keys)+"|"+str(self.list)

if __name__ == "__main__":

    arr = Intervals()
    arr[50] = 10
    arr[40] = 30
    arr[60] = 30
    print(arr)


