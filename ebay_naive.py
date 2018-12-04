"""
ID 27799964

"""
import numpy as np

INF = float('inf')


def solve_task1(product_list, price_limit):
    # For each item in product_list, compute profit-to-cost ratio ('margin') and append to corresponding item in list.
    # Simultaneously compute max margin.
    max_margin = -1
    for i in range(len(product_list)):
        margin = float(product_list[i][3]) / float(product_list[i][2])
        margin = margin * 100  # Multiply by 100 to get an integer. The actual number does not matter; the order does.
        margin = round(margin)  # Round the margin (this may decrease accuracy but allows counting sort).
        if margin > max_margin:
            max_margin = margin
        product_list[i].append(margin)

    # Create count array in preparation for counting sort.
    count = []
    for i in range(max_margin + 1):
        count.append([0])

    # Sort product_list in order of increasing margin using counting sort.
    for i in range(len(product_list)):
        count[product_list[i][4]][0] += 1
        count[product_list[i][4]].append(product_list[i])
    output = []
    for i in range(len(count)):
        for j in range(1, len(count[i])):
            output.append(count[i][j])

    # Append as many of highest margin as possible, moving onto next highest when value is close to being exceeded
    to_sell = [[0, None]] * len(product_list)
    i = len(output) - 1
    prev_item = None
    current_item = output[i]
    while i >= 0 and price_limit > 0:
        item_id = int(output[i][0])
        if output[i][2] <= price_limit:
            if current_item == prev_item:
                to_sell[item_id][0] += 1
            else:
                to_sell[item_id] = [1, item_id]
                prev_item = current_item
            price_limit -= output[i][2]
        else:
            i -= 1
            prev_item = current_item
            current_item = output[i]

    print_solution(to_sell, product_list)


def solve_task2(product_list, price_limit, item_limit):
    # Create table
    profit_table = np.zeros(len(product_list) + 1, price_limit)


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
            print(str(quantity) + " X [" + str(value[1]) + ":" + product[1] + ":" + str(product[2]) + ":" + str(
                product[3]) + "]")
            total_items += quantity
            total_price += product[2] * quantity
            total_profit += product[3] * quantity

    print("Total items sold:", total_items)
    print("Total price of items sold:", total_price)
    print("Total profit of items sold:", total_profit)


input_file = open("products.txt")
product_list = []

for line in input_file:
    line = line.strip()
    line = line.split(":")
    product_list.append([line[0], line[1], int(line[2]), int(line[3])])  # ID, name, cost, profit

price_limit = int(input("Enter the price limit: "))
print()  # the sample solution shown in assignment sheet doesn't have an extra line. But don't worry about it. This is
# required for the tester. Do not remove this.
item_limit = input("Enter the item limit: ")
print()

if item_limit == "infinity":
    solve_task1(product_list, price_limit)
else:
    try:
        item_limit = int(item_limit)
        solve_task2(product_list, price_limit, item_limit)
    except ValueError:
        print("You must either enter an integer OR infinity")

if __name__ == "__main__":
    pass