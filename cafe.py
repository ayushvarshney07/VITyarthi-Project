Menu = {
    'Pizza':40,
    'Pasta':50,
    'Burger':60,
    'Salad':80,
    'Coffee':70,
    'Momos':60,
    'Dosa':110,
    'Butter Paneer':130,
    
    
    }
print("Welcome to PYTHON restaurant")
print("Menu\npizza:40Rs\nPata:50Rs\nBurger:60Rs\nSalad:80Rs\nCoffee:70Rs\nMomos:60Rs\nDosa:110Rs\nButter Paneer:130Rs")
order_total=0

Item_1=input("Enter the name of item you want to order =")
if Item_1 in Menu:
    order_total +=Menu[Item_1]
    print(f"Your Item {Item_1} has been added to your order")

else:
    print(f"Ordered Item {Item_1} is not available yet!")
    
another_order=input("Do you want to add another Item?(Yes/No)")
if another_order =="Yes":
    Item_2=input("Enter the name of Second Item= ")
    if Item_2 in Menu:
        order_total+=Menu[Item_2]
        print(f"Item {Item_2} has been added to order")
    else:
         print(f"Ordered Item {Item_2} is not avaialabel!")
       
print(f"The total amount of Items to pay is {order_total}\nThanks For visting us")

        
