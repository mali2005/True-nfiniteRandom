import random
import sys

def true_random_number(len_seed,base):
    sayi = ""
    sayi += str(random.randrange(1,10))
    a = True
    while a:
        if random.randrange(1,len_seed) != base:
            sayi += str(random.randrange(0,10))
        else:
            a = False
    return int(sayi)

while True:
    lent = int(input("Seed Length: "))

    sayi = true_random_number(lent,3)
    print("----------------------------------------------------------")
    print("Your infinite random is ")
    print(str(sayi))
    print("----------------------------------------------------------")
    print("Your random number uses this amount of memory:")
    print(str(sys.getsizeof(sayi)/(10**6))+" mb")
    print("----------------------------------------------------------")