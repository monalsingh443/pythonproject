contacts = {};
while True:
  print("Contact Bool App:")
  print("1. Creatte contact:")
  print("2. View contact:")  
  print("3. Upadate contact:")
  print("4. Delete contact:")
  print("5. Search contact:")
  print("6. Count contact:")
  print("7. Exit the program:")



  choice = input("Enter your choice = ")

  if choice == '1':
   name = input("Enter yor name = ")
   if name in contacts:
    print('contact name {name} already exists')
   else:
    age = int (input("Enter your age:"))
    email =  input("Enter your email id:")
    mobile = input("Enter your mobile number:")
    contacts[name] = {'age':age, 'email':email ,'mobile' :'mobile'}
    print('contact name {name} has been created sucessfully')

  elif choice == '2':
    name =input("Enter contact name to view:")
    if name in contacts:
      contact =contacts[name]
      print("Name",name ,"Age",age , "mobile number",mobile)
     #here check input name present in contacts dictnary r not  
    else:
     print("Contact detail doest not present in contact:")

  elif choice == '3':
   name = input("Enter name to updtate contact:")
   if name in contacts:
    age = input("Enter updated age = ") # here input take from keyboard
    email = input("Enter updated email =")
    mobile = input("Enter updated mobile number =")
    contacts[name] = {'age':age, 'email':email ,'mobile' :mobile}  # here dictnary updated
   else:
    print("Contact does not found:")
  
  elif  choice == '4':
   name = input("Enter contact name to delete = ")
   if name in contacts:
    del contacts[name]
    print("Contact name has been deleted sucessfully!", name)
   else:
    print("Contact not found:")

  elif choice == '5':
   search_name =input("Enter contact name to search =")
   found =False
   for name,contact in contacts.item():
    if search_name.lower() in name.lower():
        print("Name",name ,"Age",age , "mobile number",mobile)
        found =True
    if not found:
      print("No contact found with that name")

  elif choice == '6':
   print("Total contact in your contact book is :",len(contacts))
 
  elif choice == '7':
   print("Good bye...closeing the program")
   break

      
  





