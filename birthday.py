#This program generates random birthdays until there is a match.
#A list with 366 indices (0 ignored) are used, each index represents a day
#When an index on the list hits 2, then a match has occured
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

    
#Prints function for counter
def printCounter(a):
    print "Amount of Total People:", a

#Print function for average
def printAverage(avg, iter):
    print "The average for", iter, "iterations is:", avg

#Checks birthdays for commonality
#If birthday has already occured once, return true.
def findMatch(list, day):
    if list[day] == 1:
        return True
    else:
        return False

#Extends a list so you can index up to 'size' amount
def arrayExtender(size, list):
    for i in range (0, size):
        list.append(0)
    
    return list

#Function used for each iteration of n.
#Returns amount of people until birthday match.
def iteration():
    birthdayList = []
    birthdayList = arrayExtender(366, birthdayList)
    counter = 1
    
    #Add random birthday
    randBirthday = addPerson()
    
    #If no match, increment day on birthdayList list and add another birthday
    while not(findMatch(birthdayList, randBirthday)):
        del birthdayList[randBirthday]
        birthdayList.insert(randBirthday, 1)
        randBirthday = addPerson()
        counter += 1
        
    return counter

#Gets input from only natural numbers
def getInput():
    n = raw_input ("How many times would you like to run this simulation? ")
    while (not n.isdigit()) or (int(n)< 1):
        n = raw_input ("Error. Please enter a whole number greater than 0: ")
    n = int(n)
    
    return n

def exitProgram():
    print "Exiting program."
    quit()

#Allows user to do more simulations after the first
def repeat():
    choice = raw_input ("Would you like to run this simulation again? ")
    choice = choice.lower()
    while not(choice == 'yes' or choice == 'no' or choice == 'y' or choice == 'n'):
        choice = raw_input ("Invalid input. Please input 'Yes' or 'No': ")
    
    if choice == 'yes' or choice == 'y':
        print "\n"
        return True
    else:
        print " "
        return False
    
    
def main():
    n = getInput()
    timerBegin = time.time()
    
    #Stores counters for each trial
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
    else:
        exitProgram()
    
    
main()