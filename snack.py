print("$ python snakes_cafe.py\n**************************************\n**    Welcome to the Snakes Cafe!   **\n**    Please see our menu below.    **")
print("**\n** To quit at any time, type \"quit\" **\n**************************************\n")
print("Appetizers\n----------\nWings\nCookies\n\nSpring Rolls\n\Entrees\n\n-------\n\nSalmon\nSteak\nMeat Tornado\nA Literal Garden\n")
print("Desserts\n\n--------\nIce Cream\n\nCake\nPie\n\nDrinks\n------\nCoffee\nTea\nUnicorn\n Tears")
print("what would you like to order?\n")

order_array = []
taken_arr = ["a"]
final_arr=[]
order = ""
order = input(">")
order_array.append(order)
def coffe():
    counter = 0
    
    for i in range(len(order_array)):
        
                for j in range(len(order_array)):
                    if (order_array[i] == order_array[j]):
                        counter += 1
                        taken_arr.append(order_array[i])

                print(f"{counter} of {order_array[i]} has been added to your menu\n")

                counter = 0
    
while order != "quit":
    print("what would you like to order?\n")
    order = input(">")
    order_array.append(order)
    coffe()
    
    
    


print(order_array)
