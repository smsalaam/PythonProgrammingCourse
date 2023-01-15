# Name: Sierra Salaam
# Date: January 16, 2023
# Assignment: 0202 - Stem and Leaf Implementation
# Video Links:  https://youtu.be/PL_Ra4q5hgQ
# Honor Statement: "I have not given or receive any unauthorized 
# assistance on this assignment."


def main(): # function that execute all the other functions
    '''This is a function that calls out all the additional functions''' # docstring
    
    greetUser() # calling function to greet the user
    continueOrExitProgram() # calling function to continue or exit program

    
def greetUser(): # create a function that will greet the user 
    ''' This function is to greet the user before the Stem and Leaf Plot is generated ''' # docstring
    print("Hello! We are here to create a Stem and Leaf Plot for you! :)\n") # print greet statment


def chooseFile(): # this fucntion ask the user which file to read and read the file
    '''This function will read the file and place all the elements in the file in a list'''
    global datasetList # declare a global variable 
    
    filename = "" # declare a string to insert file name

    filetype = input("Please enter the number 1, 2 or 3 >  ") # prompt the user to select a number 1-3

    if filetype == "1": # if the user select number 1
        filename = "C:/Users/smos0/CodingPlayground/PythonPark/PythonClass/StemAndLeaf1.txt" # point to text file 1 
        
    elif filetype == "2": # if the user select number 2
        filename = "C:/Users/smos0/CodingPlayground/PythonPark/PythonClass/StemAndLeaf2.txt" # point to text file 2
        
    elif filetype == "3": # if the user select number 3
        filename = "C:/Users/smos0/CodingPlayground/PythonPark/PythonClass/StemAndLeaf3.txt" # point to text file 3
        
    else: # if conditions above is not met
        print("Invaild Entry! Please try again!") # print statment
        chooseFile() # loop the user back to beginning to choose the correct number

    
    StemandLeaf = open(filename, "r") # open the file and assign it to a variable 
    datasetList = StemandLeaf.readlines() # read each line and place the elements in a list
    StemandLeaf.close() # close the file
        

def createPlot(): # create a function that will calculate the Stem and Leaf Plot
    ''' The function is to calculate the Stem and Leaf Plot ''' # docstring
 
    global stemandleaf # declare a global variable 
    
    stemandleaf = { } # create a dictionary
    
    stem, leaf = 0, 0 # create stem and leaf variable 

    for n in range(0, len(datasetList)): # create loop that will go through all the numbers on the list
        number = int(datasetList[n].strip()) # assign each number in list and remove all the spaces
        stem = number // 10 # Calculate number to get the stem
        leaf = number % 10 # Calculate number to get the leaf
        stemandleaf.setdefault(stem, []).append(leaf) # add the stem as the key and add the leaf as the values 

def printPlot(): # this function will print out the Stem and Leaf Plot
    ''' This function will print out the Stem and Leaf Plot''' # docstring

    pipe = "|" # create a pipe string to seperate the stem and leaf

    print("\nHere is the Stem and Leaf Plot\n") # Print intro statement 
    print("Stem " + pipe + " Leaves") # Print Stem and Leaf header
    

    for i, x in sorted(stemandleaf.items()): # create a loop that will take all the keys and values from the sorted dictionary
        for y in sorted(x): # create a loop that will display all the elements in the list of values
            pipe = pipe + " " + str(y) # add the leaf values after the pipe value
        print(f"{i : >4}" + " " + pipe) # print the stem number, make sure the number has certain amound of spaces, and add pipe string
        pipe = "|" # reset the variable to only include the line seperating the stem and leaf
 
    print("\nThe Stem and Leaf Plot has been created.\n") # print statement 

 
def continueOrExitProgram(): # function that will execute program and give user option to continue or exit the program
    '''This function execute the program until the user chooses to exit out the program''' #docstring
    
    while True:
        chooseFile() # calling function to choose file and read file
        createPlot() # calling function to generate Stem and Leaf Plot
        printPlot() # calling function to print out the Stem adn Leaf Plot

        continueOption = input('''Would you like to generate another Stem and Leaf Plot?\n Type to create another plot. Type any key to exit out! > ''') # prompt the user to generate the plot or not

        if continueOption.capitalize() != "Yes": # if user does not Yes in previous input prompt
            print("\nThank you for creating Stem and Leaf Plot!\nHave a great day!\n") # print out statement
            break # exit out the loop
        else: # if condition is not met above
            continue # restart the loop and repeat functions above

    
main() # calling main function to execute the program