# the code below is modified from mapper.py provided during Lecture 17
import sys


def isValid(temperature, quality):
    if temperature == 9999 or quality not in [0,1,4,5,9]:
        return False
    return True

for line in sys.stdin:
    line = line.strip()

    # parse out needed param
    yearMonthDay = line[15:23] #string
    temperature = int(line[87:92]) #int
    quality = int(line[92]) #int

    # output if param isValid
    if isValid(temperature, quality):
        print('%s\t%d' % (yearMonthDay, temperature))