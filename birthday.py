#This program generates random birthdays until there is a match.
#The amount of birthdays is recorded when the match occurs
#This amount is averaged if more than one simulation is done
#User can decide how many simulations to run

from random import randint
import time

#Generates random birthday
def addPerson():
    date = randint(1,365)
    return date

#Calendar translation for day number. 
#Argument would be a day from 1-365.
def dateCalendar(num):
    if num > 334:
        month = "December"
        day = num - 334
    
    elif num > 304:
        month = "November"
        day = num - 304
        
    elif num > 273:
        month = "October"
        day = num - 273
        
    elif num > 243:
        month = "September"
        day = num - 243
        
    elif num > 212:
        month = "August"
        day = num - 212
        
    elif num > 181:
        month = "July"
        day = num - 181
        
    elif num > 151:
        month = "June"
        day = num - 151
        
    elif num > 120:
        month = "May"
        day = num - 120
        
    elif num > 90:
        month = "April"
        day = num - 90
        
    elif num > 59:
        month = "March"
        day = num - 59
        
    elif num > 31:
        month = "February"
        day = num - 31

    else:
        month = "January"
        day = num
        
    #print "The Common Birthday:", month, day

#Checks all birthdays for commonality
def findMatch(list):
    length = len(list)
    if len(list) > 2:
        for i in range (0,length):
            for j in range (i+1, length):
                if list[i] == list[j]:
                    #print "All Birthdays:", list
                    #print "i:", i, "j:", j, "k:", k
                    #dateCalendar(list[i])
                    return True
    return False
    
#Prints function for counter
def printCounter(a):
    print "Amount of Total People:", a

#Print function for average
def printAverage(avg, iter):
    print "The average for", iter, "iterations is:", avg

#Function used for each iteration of n.
#Returns amount of people until birthday match.
def iteration():
    storage = []
    counter = 1

    #Add random birthday
    storage.append(addPerson())
    
    #While there is not a match, add birthdays
    while not(findMatch(storage)):
        storage.append(addPerson())
        counter += 1
        
    #printCounter(counter)
    return counter

#Gets input from only natural numbers
def getInput():
    n = raw_input ("How many times would you like to run this simulation? ")
    while (not n.isdigit()) or (int(n)< 1):
        n = raw_input ("Error. Please enter a whole number greater than 0: ")
    n = int(n)
    
    return n

#Allows user to do more simulations after the first
def repeat():
    n = raw_input ("Would you like to run this simulation again? ")
    n = str(n)
    
    if n.lower() == 'y' or n.lower() == 'yes':
        print "\n"
        return True
    elif n.lower() == 'n' or n.lower() == 'no':
        print "\n"
        return False
    else:
        print "Invalid input. Please input 'Yes' or 'No'"
        repeat()
        
        
def main():
    n = getInput()
    
    timerBegin = time.time()
    
    dataStorage = []
    
    #Runs iterations n times
    for i in range(0, n):
        numPeople = iteration()
        dataStorage.append(numPeople)
        
    #Averages all of the trials
    nAvg = sum(dataStorage) / float(len(dataStorage))
    
    printAverage(nAvg, n)
    timerEnd = time.time()
    print "Time to run", n, "simulation(s): ", timerEnd - timerBegin, "seconds."
    
    if repeat():
        main()
    
    
main()