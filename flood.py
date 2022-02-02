import threading
import random


def makefile():
    thing = random.randint(1, 100000)
    number = thing
    f = open('file.txt' + str(number), "w")
    f.write(':))))))')
    f.close()


threads = 512
while threads >= 0:
    print('making file')
    thread = threading.Thread(target=makefile())
    thread.start()
    threads -= 1
