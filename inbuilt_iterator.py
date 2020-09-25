class topten():


    def __init__(self):
        self.num = int(input())

    def __iter__(self):
        return self

    def __next__(self):

        if self.num <=10:
            vals = self.num
            self.num +=1

            return vals
        else:
            raise StopIteration


value = topten()
for i in value:
    print(i)
