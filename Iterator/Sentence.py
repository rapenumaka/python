class Sentence:
    def  __init__(self,sentence):
        self.sentence = sentence
        self.index =0
        self.word = self.sentence.split()

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.word):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.word[index]


my_send = Sentence("This is sentence")

for m in my_send:
    print(m)

my_lf = lambda x,y : x+y+1

def factorial(x):
    if x == 0:
        return 1
    else:
        return x*factorial(x-1)

print(my_lf(2,3))
print(factorial(8))

lam_fact = lambda x : factorial(x)

print(lam_fact(6))