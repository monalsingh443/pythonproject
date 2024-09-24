#inputs we need from the user
#total rent
#total food ordered for snacking
#Electricity uinits spend
#charge per unit

#output 
#Total amount you have to pay is

print("HERE THIS SHOFTWARE TO CALCUALTE THE RENT OF HOUSE:")
   
rent =int(int(input("Enter your hostel/flat rent = ")))
food =int(input("Enter the amount of food ordered ="))
electricity_bill = int(input("Enter the total electricity spend ="))
charge_per_unit =int(input("Enter the charge per uint ="))
persons = int(input("Enter the number of persons living in room/flat = "))

total_bill =electricity_bill *charge_per_unit;
output =(food+rent+total_bill) //persons
print("Each person bill pay =",output)