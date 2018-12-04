"""
ID 27799964

"""


class Item:
    def __init___(self, itemId=0, name='', price=0, profit=0):
        self.itemId = itemId
        self.name = name
        self.price = price
        self.profit = profit

    def __str__(self):
        return "{}:{}:{}:{}".format(self.itemId, self.name, self.price, self.profit)


class EbaySolution:
    def __init__(self, price=0, profit=0, itemIds=[]):
        self.price = price  # Represents how much there is left of the price_limit to spend
        self.profit = profit
        self.itemIds = itemIds

    def isEmpty(self):
        return len(self.itemIds) == 0 or self.itemIds is None

    def numberItems(self):
        if self.itemIds is None:
            return 0
        return len(self.itemIds)

    def __str__(self):
        return str(self.profit)

    def __copy__(self):
        return EbaySolution(self.price, self.profit, self.itemIds)


def solve_task1(product_list, price_limit):
    # Create table. Each cell will contain an instance of the EbaySolution class.
    # Rows represent item; columns represent $ remaining.
    profitTable = []
    for i in range(len(product_list)):
        profitTable.append([0])
        for j in range(price_limit):
            profitTable[i].append(0)

    item = product_list[0]

    # Calculate initial value for first cell in top left
    profitTable[0][0] = EbaySolution()

    # Populate first row, considering inclusion of first item only
    for col in range(1, price_limit + 1):    # For all columns
        prev = profitTable[0][col-1]
        if col-prev.price > item[2]:  # Case where we add another item
            profitTable[0][col] = EbaySolution(prev.price+item[2], prev.profit+item[3], prev.itemIds)
            profitTable[0][col].itemIds.append(item[0])
        else:   # If we can't add another item
            profitTable[0][col] = profitTable[0][col-1]



def solve_task2(product_list, price_limit, item_limit):
    # write your solution for the task 1 here.
    # feel free to create and utilize functions as required
    None


#####################################################
# DO NOT CHANGE/WRITE ANYTHING BELOW THIS LINE
#####################################################

# This function prints the results in the required format.
# to_sell is a list of lists representing the products to be sold. Each item in to_sell is a list where item[1] is the product ID and item[0] is the quanity of the product.
def print_solution(to_sell,product_list):
    total_items, total_price, total_profit = 0, 0, 0
    for value in to_sell:
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

i=0
for line in input_file:
    line = line.strip()
    line = line.split(":")
    product_list.append([i,line[1],int(line[2]),int(line[3])])
    i+=1

    
price_limit = int(input("Enter the price limit: "))
print() # the sample solution shown in assignment sheet doesn't have an extra line. But don't worry about it. This is required for the tester. Do not remove this.
item_limit = input("Enter the item limit: ")
print()


if item_limit == "infinity":
    solve_task1(product_list,price_limit)
else:
    try:
        item_limit = int(item_limit)
        solve_task2(product_list,price_limit,item_limit)
    except ValueError:
        print("You must either enter an integer OR infinity")
        
    

