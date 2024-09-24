student_grade ={}

def student_add(name,grade):
  student_grade[name] =grade
  print("Added",name)
  print("with a grade ",grade)

#here update the data student grade
def upadte_student(name , grade):  #here take student name  argument
    if name in student_grade: #here cheack wheather student present or not in student grade
       student_grade[name]=grade #if present the student name so that update ur grade
       print(name,"with marks are updated",grade)
    else:
       print(name," is not found!")

 
 
#delete the student data  
def del_student(name):
   if name in student_grade: #here this code cheack wheather name present or add in student
        del student_grade[name]  #here present the data in stduent_grade then delete the data student_garde
        print(name,"has been successfully deleted")
   else:
        print("{name} is not found!")

def display_all_student_grade():
    if student_grade:
         for name ,grade in student_grade.items():
             print("NAME =",name ,"GRADE =",grade)
    else:
        print("No students founded /added")


while True:
        print("\n STUDENT GRADES MANAGEMENT SYSTEM :")
        print("1. Add Student")    
        print("2. Update Student")    
        print("3. Delete Student")    
        print("4. View Student")    
        print("5. Exit")
        choice =int(input("PLEASE ENTER UR CHOICE  ="))
        if choice ==1:
           name =input("PLEASE ENTER UR NAME =")
           grade =int(input("PLEASE ENTER UR MARKS ="))
           student_add(name,grade)
        elif choice ==2:
            name =input("PLEASE ENTER UR NAME =")
            grade =int(input("PLEASE ENTER UR MARKS ="))
            upadte_student(name,grade)
        elif choice ==3:
            name =input("PLEASE ENTER UR NAME =")
            del_student(name)
        elif choice ==4:
            display_all_student_grade()
        elif choice ==5:
            print("Closing the program")
            break
        else:
            print("INVALID CHOICE")

           

           



           


             

   
          
          
           



        
      

    
  
             


      






