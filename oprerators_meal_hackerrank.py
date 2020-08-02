




# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    meal_tip = meal_cost * tip_percent/100
    meal_tax = meal_cost * tax_percent/100

    final_bill = round(meal_cost + meal_tip + meal_tax)

    return print(final_bill)

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)

    
