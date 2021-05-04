#Name: Alex Sarna
#Program: State Sorter
#Program Description: This file is meant to open the states file given to us, 
#and then sort it in alphabetical order whilst creating a new file

#This is the start of the new function
def newStates():
    #Start a placeholder for the new list of states
    listOfStates = []
    #This opens the flie
    file = open("states.txt", 'r')
    #This goes through the text file and appends them
    for word in file:
        listOfStates.append(word)
    #Close the text file
    file.close()
    #This reorders the text file by alphabetical order
    listOfStates.sort()
    #This creates the new text file
    f = open("alphabeticstates.txt", "w")
    for sortedWord in listOfStates:
        f.writelines(sortedWord + "\n")

#close the output file
    f.close()

#Run the Function
newStates()