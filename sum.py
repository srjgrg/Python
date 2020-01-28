def master_yoda(word):
    x = word.split(" ")
    return [x[len(x) -i -1] for i in range(len(x))]

master_yoda("here i am")