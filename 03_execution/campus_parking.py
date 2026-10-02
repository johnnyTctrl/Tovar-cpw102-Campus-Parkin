# use a named constant 
# by usuing 2.0 as its value, it is automatically stored as a float

cost_per_hour = 2.0 

def calculate_parking_cost(hours):
    estimated_cost = hours * cost_per_hour
    return estimated_cost


# define the main logic of my program
def main():
    # get the number of hours parked form the user
    # create a variable to store the user-entered parked hours
    # a variable is a namd space in memory
    Parked_hours = float(input("how many hours will you be / have you parked? "))
    # call the function to calculate the parking cost
    estimated_cost = calculate_parking_cost(Parked_hours)
    print(f"The estimated parking cost is: ${estimated_cost:.2f}")

main()




