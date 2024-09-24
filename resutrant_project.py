menu = {
    'Piza':70,
    'Pasta':50,
    'Burger':60,
    'Salad':70,
    'Cofee':80,
  }
print("Welcome to PYTHON Resutant")
print("Piza: Rs70\nPasta: Rs:50\nBurger Rs60\nSalad: Rs70\nCofee Rs:80")

order_total =0
item_1 =input("Enter the name of item you want to order = ")
if item_1 in menu:
  order_total = order_total+ menu[item_1]
  print("Your item  has been added to your order",item_1)

else:
  print("Ordered item  is not avaliable yet!",item_1)

another_order = input("Do You want to add another item?  (Yes/No) ")
if another_order =="Yes":
  item_2 = input("Enter the name of second item = ")
  if item_2 in menu:
      order_total = order_total+menu[item_2]
      print("Item  has been added to order",item_2)
  else:
    print("Order item {item_2} is not available!")

print("The total amount of item to pay is = :",order_total)