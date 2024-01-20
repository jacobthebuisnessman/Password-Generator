import random
import time
list1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",]
list2 = ["1","2","3","4","5","6","7","8","9","0"]
list3 = ["!","£","$","%","^","&","*","(",")","@","~","#","=","-"]


a = 1
while a <= 10:
    b = (random.randint(0,3))
    if b == 2:
        print(random.choice(list2))
        a = a + 1
    elif b == 1:
        print(random.choice(list1))
        a = a + 1
    else:
        print(random.choice(list3))
        a = a + 1
