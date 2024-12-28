menu={"Pizza":170,
      "Pasta":120,
      "Burger":90,
      "Salad":50,
      "Coffee":70}
# print(menu)      

print("Welcome to Python Restaurant!")
print("Our menu's are: \nPizza: Rs170\nPasta: Rs120\nBurger: Rs90\nSalad: Rs50\nCofee: Rs70")

order_total= 0

item_1= input("Enter the name of item that you want to order= ")
if item_1 in menu:
      order_total= order_total+ menu[item_1]
      print(f"Your item {item_1} has been added to your order.")
else:
      print(f"Ordered item {item_1} is not available yet.")      

another_order= input("Do you want to add another item?(Yes/No)")
if another_order == "Yes":
      item_2= input("Enter the name of second item=")
      if item_2 in menu:
            order_total= order_total+ menu[item_2]
            print(f"Your item {item_2} has been added to your order.")
      else:
           print(f"Ordered item {item_2} is not available yet.") 

print(f"The total amount of your items is to pay {order_total}")
     