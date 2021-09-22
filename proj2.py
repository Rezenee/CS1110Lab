'''Comment
more detail
'''
def main():
    looping = True 
    while looping:

        # Defaults for while loops
        tier = 'invalid'
        valid_tiers = ['B', 'M', 'P']
        insufficient_items_sold = 0

        items_sold = -1

        employee_name = input("Enter Employee's Name: ")
        monthly_base_salary = float(input("Enter Monthly Base: "))
        tier = input("Enter Tier (B, M, or P): ")
        tier = tier[0].upper()
        while not (tier in valid_tiers):
            print("Tier {} is not a legitimate tier value".format(tier))
            tier = input("Enter Tier (B, M, or P): ")
            tier = tier[0].upper()
        
        items_sold = int(input("Enter Items Sold: "))
        while items_sold < 0:
            print("Invaled number for Items Sold.")     
            items_sold = int(input("Enter Items Sold: "))
        tier = tier.upper()

        item_sale_profit = 0

        if tier == 'B':
            if items_sold <= 9:
                item_sale_profit = 0
                insufficient_items_sold = 1
            elif 9 < items_sold <= 15:
                item_sale_profit = items_sold * 50
            elif 15 < items_sold:
                item_sale_profit = items_sold * 75

        elif tier == 'M':
            if items_sold <= 15:
                item_sale_profit = 0
                insufficient_items_sold = 1
            if 15 < items_sold <= 20:
                item_sale_profit = items_sold * 60
            if 20 < items_sold:
                item_sale_profit = items_sold * 100

        elif tier == 'P':
            if items_sold <= 19:
                item_sale_profit = 0
                insufficient_items_sold = 1
            if 19 < items_sold <= 25:
                item_sale_profit = items_sold * 75
            if 25 < items_sold:
                item_sale_profit = items_sold * 125

        total_profit = monthly_base_salary + item_sale_profit
        print("{}, Tier: {}, Sold {} items, Monthly Payment: {}\n".format(employee_name, tier,  items_sold, total_profit))
        if insufficient_items_sold == 1:
            print("WARNING Sales must improve to stay in Tier {}".format(tier))

        continue_question = input("Do you want to enter another employee? ")
        if continue_question[0].upper() == 'Y' :
            looping = True 
        else:
            looping = False

        print('')
if __name__ == '__main__':
    main()
