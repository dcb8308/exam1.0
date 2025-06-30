''' 
*   Professor B would like to know which of his student have a GPA below 3.0.
    To accomplish this, read the file - students.csv into the program. The program
    should evaluate the GPA to see if it is higher or lower than 3.0. If it is,
    then it should be written out to the file - processedStudents.csv. (This file
    already contains headers and the headers should NOT be overwritten.)

*   Create a VE and name it quiz_ve. Install the 3rd party libraries- wordcloud and imageio.
    Make sure your VE is NOT part of your repository. Make sure your .gitignore
    IS part of your repo. The code will produce a heart-shaped wordcloud of the most
    frequently appearing words in the text of Romeo and Juliet.

*   Create a dictionary of each student where the student FULL NAME (proper casing) is the key
    and the GPA is the value. 

*   print out the dictionary

*   print out the corresponding GPA for student - Luke Brazzi

*   push your repo to GitHub. Only your VE should not be in your repo. Everything else should be
    pushed. Submit your Github repo URL in the response field of the quiz.

I have outlined comments for each step of the program. You are
not required to use them but it is provided to help you work
through the logic of the problem.


'''


import csv

studict = {}


# create a file object to open the file in read mode
with open("students.csv", "r") as infile:
    next(infile)
    for line in infile:
        categories = line.strip().split(",")
        student_id = categories[0]
        gpa = float(categories[8])
        fname = categories[2]
        lname = categories[3]
        major = categories[6]
        calssification = categories[7]
        

        fullname = f"{fname} {lname}"

        studict[fullname] = gpa

        if gpa > 3.0:
            with open("processedStudents.csv", "a") as outfile:
                outfile.write(f"{student_id},{fname},{lname},{major},{calssification},{gpa}\n")
                outfile.close()

print(studict)
print(f'Luke Brazzis GPA is {studict.get("Luke Brazzi",'student not here')}')





# create a csv object from the file object


#skip the header row


#create an outfile object for the pocessed record



#create a new dictionary named 'student_dict'



#use a loop to iterate through each row of the file


    #check if the GPA is below 3.0. If so, write the record to the outfile
    
        



    # append the record to the dictionary with the student Full name in proper case 
    # as the Key and the value as the GPA
    





#print the entire dictionary


#Print the corresponding GPA for student 'Luke Brazzi'



#close the outfile












