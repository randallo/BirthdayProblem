#This program generates random birthdays until there is a match.

from random import randint

#Generates random birthday
def addPerson():
    date = randint(1,365)
    return date

#Calendar translation for date number
def dateCalendar(a):
    if a > 334:
        month = "December"
        day = a - 334
    
    elif a > 304:
        month = "November"
        day = a - 304
        
    elif a > 273:
        month = "October"
        day = a - 273
        
    elif a > 243:
        month = "September"
        day = a - 243
        
    elif a > 212:
        month = "August"
        day = a - 212
        
    elif a > 181:
        month = "July"
        day = a - 181
        
    elif a > 151:
        month = "June"
        day = a - 151
        
    elif a > 120:
        month = "May"
        day = a - 120
        
    elif a > 90:
        month = "April"
        day = a - 90
        
    elif a > 59:
        month = "March"
        day = a - 59
        
    elif a > 31:
        month = "February"
        day = a - 31

    else:
        month = "January"
        day = a
        
    print "The Common Birthday:", month, day

#Checks all birthdays for commonality
def findMatch(list):
    length = len(list)
    if len(list) > 2:
        for i in range (0,length):
            for j in range (i+1, length):
                if list[i] == list[j]:
                    print "All Birthdays:", list
                    dateCalendar(list[i])
                    return True
    return False 
    
#Prints population
def printCounter(a):
    print "Amount of Total People:", a

def main():
    storage = []
    counter = 1

    #Add random birthday
    storage.append(addPerson())
    
    #While there is not a match, add birthdays
    while not(findMatch(storage)):
        storage.append(addPerson())
        counter += 1
        
    #Print population results
    printCounter(counter)
        
main()