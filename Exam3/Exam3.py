##PLEASE FILL OUT THE BELOW DETAILS
##Student Name: 
##Course Number:
##Student Number: 

##complete each task which is shown as a comment. 
#complete each task directly below the comment
#each task shows a task number, and number of marks awarded
#on each task requiring an output, ensure the task goes on a separate line (unless stated)
#and ensure that it states the task number prior to any output e.g. Task 11 
#upload your final file to your assigned folder share on class.net
# \\192.168.130.21\chshare\regiNumber

#####################################################
#Section 1 20 Marks


#1) Create and Assign a type float variable called fltOne the value 10 (2)
fltOne = float(10)

#2) Create and Assign a type float variable called fltTwo the value 20 (2)
fltTwo = float(20)

#3) Create and Assign a type float variable called fltThree with the product of fltTwo and fltOne(3)
fltThree = float(fltOne * fltTwo)

#4) Create and assign a variable called stringOne with the value "The product of fltOne and fltTwo = "(2)
stringOne = "The product of fltOne and fltTwo = "

#5) On the console, output stringOne and fltThree (in that order) (4)
print(stringOne,fltThree)

#6) increment fltOne  (3)
fltOne = fltOne + 1

#7)  prompt the user to provide an input to fltTwo with the message "Please provide another number for fltTwo" (4)
fltTwo = float(input("Please provide another number for fltTwo"))

#####################################################
#Section 2 30 Marks

#8) take the input from fltTwo and apply a decision based on the number inputted . 
#The decision should be based on if the user inputs a number below 100 
#the code should output "below 100" (5)
if fltTwo < 100:
    print("below 100")

#9) take the product of fltTwo and fltOne.
#If the product is below 0, output "below 0"
#if the product is 0 or above and below 100, output "from 0 to 100"
#if the product is above 100 output "above 100" (6)
if fltOne * fltTwo < 0:
    print("below 0")
elif fltOne * fltTwo >= 0 and fltOne * fltTwo < 100:
    print("from 0 to 100")
else:
    print("above 100")


#10) create a list called listOfInts (4)
listOfInts = []

#11 part a) create a for loop to iterate through the above list and populate the list with 
#{4,6,8,10,12,14,16,18,20,22} 
#(6)
for i in range(4,23,2):
    print(i)
    listOfInts.append(i)

#11 part b) create a for loop to iterate through the above list and 
#multiply each value by two assigning the new value to the respective 
#index in the list. The list should now look like {8,12,16.....} (7)
counter = 0
for i in listOfInts:    
    listOfInts[counter] = i * 2
    counter = counter + 1

#11 part c )output listOfInts to the screen (2)
print(listOfInts)

#####################################################
#Section 3 20 marks

#14) create a function which calculates an increase of a given percentage (10)
# the function should be called calcPerc
#the function should take a cost parameter and a percentage parameter
#it should return the cost plus the percentage increas. 
#For example if the paramenters are cost = 100 and percentage = 50, it should return 150. 
#For another example, if the parameters are cost = 50 and percentage = 10, it should return 55.
#The percentage value should assume 10% if no value is given
#test the function here:
def calcPerc(cost,percentage=10):
    return cost + cost*(percentage/100)
print(calcPerc(50,10))


#15) create a function called caseChanger which takes a string argument written all in lower case
#and returns a string where any e found, it will convert it to a capital E (10)
#For example, caseChanger("hello") prints hEllo to the console

def caseChanger(word):
    for i in word:
        if i == "e":
            print(i.upper(),end="")
        else:
            print(i,end="")
caseChanger("hello")


##################################################### 
#Section 4 30 marks

#16)a) Create a list that represents a set of students. The tuple should contain the following
#students: Clark,Cox,Horan,Rai,Smith,White,Cooper,Jones,,
nonOrderedStudents= ["Clark","Cox","Horan","Rai","Smith","White","Cooper","Jones"]
print(nonOrderedStudents)
#b) create a Tuple with the students now ordered alphabetically
students = ()
students = nonOrderedStudents.sort()
print(students)


#17) create a tuple that represents exam marks with the following data. 
#These are the respective exam marks for the alphabetically ordered student list
# 65,66,67,80,90,65,65,93
scores = (65,66,67,80,90,65,65,93)
print(scores)

#18) Dictionary question 1 
#create a dictionary which joins the student with their corresponding mark. 
#There are a number of ways to achieve this. You will be awarded marks for 
#the most efficient method
studentMarks= {}
for i in range(8):
    studentMarks[students[i]] = scores[i]
print(studentMarks)



