# Engineering Design
it will then ask the students how many hours the students/driver parked.
the program will multiply the number of hours by $2 and display the students information along the total parking cost.
 there will be no payment plan because the program only caculates the total estimated cost.

**Project:** Campus Parking Helper  
**Team members:** johnny tovar 
**Date:** september 30 2026

## Problem Summary
Create a program that caculates the total cost and keeps track of time that the student/drivers have been parked 

## Proposed solution
create a program that asks the students/drivers to enter their details to keep track on how long they have been parked to caculate the total cost of their parking visit 


## Technical design
The program will use variables for parking hours. it will use input() to caculate the parking cost,and print() to display the student's total estimated cost.

### Inputs
_What data and information will go into the program? What data types will the program use to represent that data?_
numbers of hours parked = input("how long will you be parked")
**parked hours** (float) the user entered the number of hours they anticipate parking or have parked

### Processing
_What will the program do with the data? What calculations will it perform?_ 
the program will take the number of hours the student parked and multiply it by the parking rate of $2 per hour to caculate the total parking cost. it will also store the students information ID.
estimated cost = cost per hour * parked hours
estimated cost = 2.00 * 2.5

### Output
_What will the program return or print to the user?_
Parking hours
Total estimated parking cost 

### Functions
_What function(s) could this program use to modularize the logic? What actions belong together?_

get user input 
caculate the cost
display the total estimated cost


## Example interaction

```text
User input: 
Enter Time Parked: 2 hours





Program output:
``` 
parking hours" 2
Total Parking Cost: $4.00

## Implementation plan

1. ask the student how many hours they are parked 
2. store the parking rate as $2 per hour
3. multiply the number of hours by $2 to caculate the total cost
4. display the student's total and estimated  parking cost
5. test the program with different numbers of parking hours to make sure the caculations are correct

