# Name: Sierra Salaam
# Date: January 09, 2023
# Assignment: 0101 Grading Logic
# Video Link: https://youtu.be/gs-8ofc_pMg
# Honor Statement: "I have 
# not given or receive any unauthorized 
# assistance on this assignment."

import sys #importing sys library to exit out of program

total_grade = 0.0 # declaring global variable to calculate total score

def automaticZero(userEntry): # a helper function 
    ''' This function will exit out the program with a total grade of 0 for assignment when assignment does not meet the conditions ''' #docstring of function
    if userEntry == False: # if the value is false, exit out the program and print total grade
        return  sys.exit(f"Student total grade is {total_grade} \nTry again next time!\n")

def turnInLateAssignment(userEntry): # a helper function 
    ''' This function returns the total percentage loss when the student turns in the assignment late''' #docstring of function
    global late_hours # create variable as global to use in another function
    late_hours = 0 # set variable to 0
    
    if userEntry == True: # if the value is true then proceed calculating the total percentage loss 
        print('''Instructions: 
        For the following question, please answer an vaild number (The number entered will be rounded up to the nearest whole number).
        ''') #print out instructions for user to follow
        
        late_hours = float(input("How many hours did was the student late on turning in the assignment > ")) # Prompt user to input total hours late
        late_hours = round(late_hours)/100 # round answer to the nearest whole number and calculate decimal
    return late_hours # the result of calculation

def ratePerformance(rateQuestion): # a helper function
    ''' This function continues to ask the question until user rates question with the correct number ''' #docstring
    while True: # loop rated questions until user enters the correct range of numbers
        answer = float(input("Out of ten points, " + rateQuestion)) # prompt the user to enter numbers
        if answer <= 10 and answer >= 0: #if answer fits within the range
            return answer # results of answer
            break # end the loop
        else: #if the condition above is not met
            print("Invaild Entry! Please rate student's performance 1 - 10 ") # print message to instruct user to enter correct value
            print(" ") #extra space
    
    
  

def grader(): # function that will grade assignment
    ''' This function provides instructions and prompts the user to answer multiple of questions to produce a total grade for an assignment ''' #docstring
    

    print('''Instructions: 
    For the following questions, please answer True for Yes or False for No.
    ''') # instuctions on how to answer the following conditions listed below

    submission_file_format = eval(input("Did the student submit a single uncompressed .py file? > ")) # prompt user to answer a conditon and assign to boolan variable 
    print(" ") # extra space
    automaticZero(submission_file_format) # call helper function to check if user answered False
    
    name_and_date_submission = eval(input("Did the student include his/her name and date in the assignment? > ")) # prompt user to answer a conditon and assign to boolan variable
    print(" ") # extra space
    automaticZero(name_and_date_submission) # call helper function to check if user answered False

    honor_statement = eval(input("Did the student include the honor statement? > ")) # prompt user to answer a conditon and assign to boolan variable
    print(" ") # extra space
    automaticZero(honor_statement) # call helper function to check if user answered False

    link_to_video = eval(input("Did the student include the Youtube link to the video presentation? > ")) # prompt user to answer a conditon and assign to boolan variable
    print(" ") # extra space
    automaticZero(link_to_video) # call helper function to check if user answered False


    late_assignment = eval(input("Did the student turn in the assignment late? > ")) # prompt user to answer a conditon and assign to boolan variable
    turnInLateAssignment(late_assignment) # call helper function to check if user answered True
    
  
    print('''Instructions: 
    For the following questions, please rate student's performance 1 - 10.
    With 10 being the highest score and 1 being the lowest score.
    ''') # instuctions on how to answer the following conditions listed below
    print(" ") # extra space

    question_code_correctness = "how would you evaluate the correctness of the code? > " # delcare string variable for condition
    code_correctness = ratePerformance(question_code_correctness) # call helper function to prompt user to answer condition correctly
    print("") # extra space

    question_elegant_code = "how would you evaluate the elegant of the code? > " # delcare string variable for condition
    elegant_code = ratePerformance(question_elegant_code) # call helper function to prompt user to answer condition correctly
    print(" ") # extra space

    question_code_hygiene = "how would you evaluate the code hygiene? >  " # delcare string variable for condition
    code_hygiene = ratePerformance(question_code_hygiene) # call helper function to prompt user to answer condition correctly
    print(" ")

    question_discussion_quality = "how would you evaluate the quality of the discussion in the Youtube video? > " # delcare string variable for condition
    discussion_quality = ratePerformance(question_discussion_quality) # call helper function to prompt user to answer condition correctly
    print(" ") # extra space

    total_grade = ((code_correctness + elegant_code + code_hygiene + discussion_quality)/ 40) - late_hours # calculating the total grade of assignment
    total_grade = total_grade * 100 # converting total into percentage

    return sys.exit(f"You have completed the grading process. \nThe student's total grade is {total_grade} %. \nHave a great day!") # produce results with statment and exit program


grader() # call function to run program
