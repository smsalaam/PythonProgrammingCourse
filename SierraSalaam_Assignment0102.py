# Name: Sierra Salaam
# Date: January 09, 2023
# Assignment: 0102 - Coprime
# Video Link: https://youtu.be/Rt8jJMvKZYU
# Honor Statement: "I have not given or receive any unauthorized 
# assistance on this assignment."

import sys # import sys library to exit out of program

num1, num2 = 0.0, 0.0 # declare two variable for number input

list_a_factors = [ ] # create a list of all factor numbers for num1 
list_b_factors = [ ] # create a list of all factor numbers for num2
common_factors_list = [ ] # create a list of all common factors num1 and num2 had


def findCoprimeQuestion(): # a helper function
    ''' This helper function will prompt the user to answer the question about finding the coprime number''' # docstring

    global find_coprime # create global variable 
    print("Instructions:\nType Yes or Y to continue. (make sure to not include spaces  response) Press any charater to exit .\n") # print instructions
    find_coprime = input("Would you like to find the coprime of two numbers > ") # prompt user to continue finding coprime or not
    return find_coprime # return user answer

def printList(value, list): # a helper function
    ''' This function will print out a statment that will display the list of factor numbers'''

    string_list = ', '.join(str(i) for i in list) # create a list as a string to print
    if list == common_factors_list: # if the list parameter is the common_factor List, print statment 
        return print("Here are the common factors " + ":\n" + string_list) # print statement of common factor list
    else: # if statement is not true above
        return print("Here are the factor numbers of " + str(value) + ":\n" + string_list) # print statement of factor numbers 

def coprime_test_loop(): # a function
    '''  This function will ask for the input numbers, find the coprime and continue finding coprime until user wish to exit the program ''' #docstring

    findCoprimeQuestion() # call the function to prompt user to answer a question

    if find_coprime.capitalize() == "Yes" or find_coprime.capitalize() == "Y": # if queston is yes or y then execute program
        while True: # ongoing loop to execute code
            print("\nPlease enter two numbers to see if they are Coprime?\n(Please Note: All number entered will be round up to the nearest whole number.)\n ") # print instructions to prompt user to enter numbers
            num1, num2 = float(input( "First Number > ")), float(input( "Second Number > ")) # ask user to enter two coprime number
            num1 = round(num1) # round up num1 variable 
            num2 = round(num2) # round up num2 variable
            print(" ") # print a blank space
            print("Now, we will determine if " + str(num1) + " and " + str(num2) + " are coprime!\n") # print statement to let user know the next action

            if coprime(num1, num2) == True: # run function and see if function results are true
                print("\nYes! " + str(num1) + " and " + str(num2) + " are coprime!\n") # print statement numbers are coprime
            else: # if statement is not true above
                print("\nNo! " + str(num1) + " and " + str(num2) + " have other common factors. \nThese numbers are not coprime!\n") # print statement number are not coprime
            
            findCoprimeQuestion() # call function to ask to continue program

            if find_coprime == "Yes"or find_coprime == "Y": # if variable result is true, do nothing and continue program
                pass
            else: # if state is not true above 
                sys.exit(" You are finished. Have a great day") # exit out the program and print a statment 
                
            
    else: # if statement above  is not true 
        sys.exit(" You are finished. Have a great day") #exit out the program and print a statment 



def coprime(a,b): # a function that calculates and produce answer if number is coprime
    ''' This function will caculate each number, check both factor numbers list to see if two numbers are coprime and produce results  ''' # docstring

    for factor_a in range(1,a+1): # run a for loop takes input number and check to see if number is consider as factor for num1
        num_a = a % factor_a # calculate module 
        if num_a == 0: # if results are 0, it is considered as a factor 
            list_a_factors.append(factor_a) # add factor number to list
        factor_a += 1 # count up until variable is out of range

    for factor_b in range(1,b+1): # run a for loop takes input number and check to see if number is consider as factor for num2
        num_b = b % factor_b # calculate module 
        if num_b == 0: # if results are 0, it is considered as a factor 
            list_b_factors.append(factor_b) # add factor number to list
        factor_b += 1 # count up until variable is out of range

    printList(a, list_a_factors) # call function to print num1 factor numbers list
    printList(b, list_b_factors) # call function to print num2 factor numbers list

    for i in list_a_factors: # run a for loop that reviews each number in the num1 factor number list
        for j in list_b_factors:  # run a nested for loop that reviews each number in the num2 factor number list
            if i == j: # if number from num1 factor list is equal to number from num2 factor list
                common_factors_list.append(i) # add number to the common factor list

    printList(0, common_factors_list) # call function to print common number factor list


    if len(common_factors_list) == 1 and common_factors_list[0] == 1: # if the common factor list has only one number and the numbeer is 1
        return True # results of functions is true
    else: # if the statement above is not true
        return False # results of function is false

        

coprime_test_loop() # execute function

# test out the calculation function
#coprime(3,9)
#coprime(2,5)
#coprime(25.50)
#coprime(3.27)