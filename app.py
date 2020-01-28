def animal_crackers(string):
    x, y = string.split(' ')
    return x[0].upper() == y[0].upper()

print(animal_crackers ("Crazy Kangaroo"))