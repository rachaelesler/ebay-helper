"""
ID 27799964

"""
import numpy as np
INF = float('inf')

def solve_task1(product_list, price_limit):
    assert price_limit > 0, "Price limit must be positive"

    # For each item in product_list, compute profit-to-cost ratio ('margin') and append to corresponding item in list.
    # Simultaneously compute max margin.
    max_margin = -1
    for i in range(len(product_list)):
        margin = float(product_list[i][3])/float(product_list[i][2])
        margin = margin * 100   # Multiply by 100 to get an integer. The actual number does not matter; the order does.
        margin = round(margin)  # Round the margin (this may decrease accuracy but allows counting sort).
        if margin > max_margin:
            max_margin = margin
        product_list[i].append(margin)

    # Create table
    profit_table = np.zeros(shape=(len(product_list), price_limit + 1))
    item = product_list[0]

    # Populate first row, considering only first item
    for i in range(price_limit + 1):
        new_limit = price_limit
        while item[2] < new_limit:
            profit_table[0, i] += item[3]
            new_limit -= item[2]

    # Populate remaining rows, taking the max value considering whether item should be included or not
    for i in range(1, len(product_list)):
        item = product_list[i]
        for j in range(price_limit+1):
            if item[2] > j:
                profit_table[i, j] = profit_table[i-1, j]
            else:
                optimal_item = item  # Find the item with max margin
                for k in range(i):
                    if product_list[k][4] > optimal_item[4]:
                        optimal_item = product_list[k]

                # Fill current cell with as many of the optimal item as possible
                local_profit = 0
                price_limit = j
                while optimal_item[2] < price_limit:
                    local_profit += optimal_item[3]
                    price_limit -= optimal_item[2]

                # Find the maximum profit you can make with remaining money
                if price_limit > 0:
                    rem_max = 0
                    n = len(profit_table[:, 0])
                    for i in range(n):
                        if profit_table[i, price_limit] > rem_max:
                            rem_max = profit_table[i, price_limit]
                    local_profit += rem_max

                # Take the maximum value considering whether or not to include this item
                profit_table[i, j] = max(profit_table[i-1, j], local_profit)

    for i in range(len(product_list)):
        print(profit_table[i, -1])

def solve_task2(product_list, price_limit, item_limit):
    None








#####################################################
# DO NOT CHANGE/WRITE ANYTHING BELOW THIS LINE
#####################################################
# This function prints the results in the required format.
# to_sell is a list of lists representing the products to be sold. Each item in to_sell is a list where item[1] is the
# product ID and item[0] is the quantity of the product.
def print_solution(to_sell, product_list):
    total_items, total_price, total_profit = 0, 0, 0
    for value in to_sell:
        if value[1] is not None:
            quantity = value[0]
            product = product_list[value[1]]
            print(str(quantity)+" X ["+str(value[1])+":"+product[1]+":"+str(product[2])+":"+str(product[3])+"]")
            total_items += quantity
            total_price += product[2]*quantity
            total_profit += product[3]*quantity
        
    print("Total items sold:",total_items)
    print("Total price of items sold:",total_price)
    print("Total profit of items sold:",total_profit)

input_file = open("products.txt")
product_list = []

for line in input_file:
    line = line.strip()
    line = line.split(":")
    product_list.append([line[0], line[1], int(line[2]), int(line[3])])  # ID, name, cost, profit

"""
price_limit = int(input("Enter the price limit: "))
print() # the sample solution shown in assignment sheet doesn't have an extra line. But don't worry about it. This is
# required for the tester. Do not remove this.
item_limit = input("Enter the item limit: ")
print()


if item_limit == "infinity":
    solve_task1(product_list, price_limit)
else:
    try:
        item_limit = int(item_limit)
        solve_task2(product_list,price_limit,item_limit)
    except ValueError:
        print("You must either enter an integer OR infinity")
"""

if __name__ == "__main__":
    solve_task1(product_list, 1500)