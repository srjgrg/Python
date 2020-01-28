#print("Giraffe\nAcadmey") #prints seperately

#print("Giraffe\"Acadmey") #prints in quatation

print("\n")

phrase = "Giraffe Acadmey"
print(phrase + " is cool") #concatination

print("\n")

#***string lower and upper case***
print(phrase.lower()) #prints all in lower case
print(phrase.upper()) #prints all in upper case
print(phrase.isupper()) #checks is all string is in upper case
print(phrase.upper().isupper()) #converts strings in upper case and checks if string is in upper case

#***stringslength***
print(len(phrase)) #len = counts the strngs lenght
print(phrase[0]) #return G
print(phrase.index("G")) #returns G index
print(phrase.index("a")) #retuns length from G to a

print(phrase.replace("Giraffe", " Elephant")) #replaces giraffe with Elephant
 

