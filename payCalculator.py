def calculatePay():
    # Adding in overtime values 
    overtimeModifier = 1.5
    overtimeHours = 0

    # Try except for wrong inputs on hours
    try:
        hrs = float(input("Enter Hours: ")) # converting to a float
    except:
        print("Error, please enter numeric input")
        return

    # Try except for wrong inputs on hourly rate
    try:
        rate = float(input("Enter Rate: ")) # converting to a float
    except:
        print("Error, please enter numeric input")
        return

    # Calculates how many overtime hours there are are sets normal hours to 40 if overtime is present
    if hrs > 40:
        overtimeHours = hrs - 40
        hrs = 40

    overtimeRate = overtimeModifier * rate # Calculating overtime rate based on the modifier defined above

    gross_pay = overtimeHours * overtimeRate + hrs * rate # Calculating gross pay based on normal and overtime hours and rates

    print(f"Pay: {gross_pay}")

    # end assignment

## if you want to test locally before you try to sync
## run > python payCalculator.py

#Ignore this for now. 
if __name__ == "__main__":
    calculatePay()
