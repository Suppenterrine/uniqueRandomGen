# from msilib import init_database
import matplotlib.pyplot as plt
from random import randint
from random import seed


seed(1)

#history
history = {
    "indices": [],
    "vals": []
}

real_history = {
    "indices": [],
    "vals": []
}

double_counter = 0
random_max = 8
# seed random number generator


def genRandom():
    return randint(1, random_max)

def checkHistory(num):
    if len(history["vals"]) > 10:
        history["indices"].pop(0)
        history["vals"].pop(0)

    if num in history["vals"]:
        return False
    
    return True

# generate some integers
for index in range(1, random_max):

    value = genRandom()
    real_history["indices"].append(index)
    real_history["vals"].append(value)

    while True:
        if checkHistory(value) is False:
            double_counter = double_counter + 1
            print(value, "in list > gen new")
            value = genRandom()

        if checkHistory(value) is True:
            print("new value > ",value)
            break

    history["indices"].append(index)
    history["vals"].append(value)

print("\nMain loop finished\n------------------\n")



print("\nUnique history")
for h, i in enumerate(history["vals"]):
    print("index", history["indices"][h], "\tval", history["vals"][h])

print("\n> count: ",len(history["vals"]))
print("------------------\n")

print("\nReal history")
for h, i in enumerate(real_history["vals"]):
    print("index", real_history["indices"][h], "\tval", real_history["vals"][h])

print("\n> double_counter:",double_counter)
print("------------------\n")

plt.plot(history["indices"], history["vals"], label="unique history")
plt.plot(real_history["indices"], real_history["vals"], label="real history")

plt.xlabel('index')
plt.ylabel('value')
plt.legend()
plt.show()
