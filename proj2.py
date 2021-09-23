'''
Name: Zane Rickert
Project Number: 2
Lab Section: CS-1110-545

This program asks the user for information about an employee
it asks for the employees name, base salary, items sold, and their tier in the company
it takes this information to calculate their total income to be payed as well
as a warning if they are not making enough sales.
The program will ask the user if they want to input any extra employees, and will loop until they are finished.
'''
def main():
    while True:
        employee_name = getName() 
        monthly_base_salary = getMonthlyBaseSalary() 
        employee_tier = getTier()
        items_sold = getItemsSold()
        item_commission_profit, insufficient_items_sold = getCommissionProfit(employee_tier, items_sold)

        # Calculates the total profit based off of the monthly salary, and the profit from commissions.
        total_profit = monthly_base_salary + item_commission_profit

        print("{}, Tier: {}, Sold {} items, Monthly Payment: {}\n".format(employee_name, employee_tier,  items_sold, total_profit), end='')

        # If they haven't sold enough warn the user
        if insufficient_items_sold:
            print("WARNING: Sales must improve to stay in Tier {}".format(employee_tier))

        # Formatting
        print('')

        # Breaks out of loop if user choses to.
        continue_question = input("Do you want to enter another employee? ")
        if continue_question[0].upper() == 'Y' :
            print('')
            continue
        else:
            break



def getName():

    while True:
        name = input("Enter Employee's Name: ")
        # If the name is empty, re ask
        if len(name) < 1:
            continue
        else:
            break

    return name


def getMonthlyBaseSalary():

    while True:
        try:
            salary = float(input("Enter Monthly Base: "))
            break
        except ValueError:
            # Re-prompt the user if the input is empty
            continue

    return salary
        

def getTier():
    valid_tiers = ['B', 'M', 'P']

    while True:
        try:
            tier = input("Enter Tier (B, M, or P): ")
            tier = tier[0].upper()
        except IndexError:
            # If the user inputs nothing re-prompt
            continue
        # If the tier is not valid, tell the user and re-prompt
        if not tier in valid_tiers:
            print("Tier {} is not a legitimate tier value".format(tier))
            continue
        else:
            return tier


def getItemsSold():
    while True:
        try: 
            items_sold = int(input("Enter Items Sold: "))
        except ValueError:
            # If empty value is inputted, re-prompt
            continue

        # If they input negative value, re-prompt
        if items_sold < 0:
            print("Invalid number for Items Sold.")
            continue
        else:
            return items_sold 


def getCommissionProfit(tier, items_sold):

    item_sale_profit = 0
    insufficient_items_sold = False

    # Calculate income based on tier
    if tier == 'B':
        if items_sold <= 9:
            item_sale_profit = 0
            insufficient_items_sold = True
        elif 9 < items_sold <= 15:
            item_sale_profit = items_sold * 50
        elif 15 < items_sold:
            item_sale_profit = items_sold * 75

    elif tier == 'M':
        if items_sold <= 15:
            item_sale_profit = 0
            insufficient_items_sold = True
        if 15 < items_sold <= 20:
            item_sale_profit = items_sold * 60
        if 20 < items_sold:
            item_sale_profit = items_sold * 100

    elif tier == 'P':
        if items_sold <= 19:
            item_sale_profit = 0
            insufficient_items_sold = True
        if 19 < items_sold <= 25:
            item_sale_profit = items_sold * 75
        if 25 < items_sold:
            item_sale_profit = items_sold * 125

    return item_sale_profit, insufficient_items_sold


if __name__ == '__main__':
    main()
