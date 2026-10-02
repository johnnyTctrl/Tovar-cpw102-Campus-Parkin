# Engineering Design
the program design will  collect and store the students/drivers information. 
it will then ask the students how many hours the students/driver parked.
the program will multiply the number of hours by $2 and display the students information along the total parking cost.
 there will be no payment plan because the program only caculates the total cost.

**Project:** Campus Parking Helper  
**Team members:** johnny tovar 
**Date:** september 30 2026

## Problem Summary
Create a program that caculates the total cost and keeps track of time that the student/drivers have been parked 

## Proposed solution
create a program that asks the students/drivers to enter their details to keep track on how long they have been parked to caculate the total cost of their parking visit 


## Technical design
The program will use variables to the students information and parking hours. it will use input() to collect information, multiplication to caculate the parking cost,and print() to display the student's information and total cost.

### Inputs
_What data and information will go into the program? What data types will the program use to represent that data?_
student name = input("whats your name")
student ID = input("what is your student ID")
numbers of hours parked = input("how long will you be parked")
**parked hours** (float) the user entered the number of hours they anticipate parking or have parked

### Processing
_What will the program do with the data? What calculations will it perform?_ 
the program will take the number of hours the student parked and multiply it by the parking rate of $2 per hour to caculate the total parking cost. it will also store the students information ID.
estimated cost = cost per hour * parked hours
estimated cost = 2.00 * 2.5

### Output
_What will the program return or print to the user?_
Student name
student ID
Parking hours
Total parking cost 

### Functions
_What function(s) could this program use to modularize the logic? What actions belong together?_

get user input 
caculate the cost
display the information and total cost


## Example interaction

```text
User input: 
Enter student name: john Doe
Enter student id: 2597154
Enter number of parking hours: 6


Program output:
```Student: John Doe
Student id: 2597154
Total Parking Cost: $12.00

## Implementation plan

1. create variables to store the student's name and student id
2. ask the student to enter their information 
3. ask the student how many hours they are parked 
4. store the parking rate as $2 per hour
5. multiply the number of hours by $2 to caculate the total cost
6. display the student's information and total parking cost
7. test the program with different numbers of parking hours to make sure the caculations are correct

