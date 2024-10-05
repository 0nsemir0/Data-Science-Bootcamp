#1 count words
def count_vowels(word):
    count = 0
    vowels='aeiouAEIOU'
    for char in word: 
        if char in vowels:
            count += 1
    return count

#2
animals=['tiger', 'elephant', 'monkey', 'zebra', 'panther']
for i in range(len(animals)):
    animals[i] = animals[i].upper()
print(animals)
#3 
for i in range(20): 
    if i % 2 == 0: 
        print(i,"Even")
    else:
        print(i,"Odd")
#4
def sum_of_integers(a, b): 
    a = int(input("Enter the first integer"))
    b = int(input("Enter the second integer"))

    return a+b
print (sum_of_integers)