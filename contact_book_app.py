# Dictionary to save name as key and age,mobile no,email as values 
contacts = {}

while True:
    print('Contact Book Management App')
    print('1: Create Contact')
    print('2: View Contact')
    print('3: Update Contact')
    print('4: Delete Contact')
    print('5: Search Contact')
    print('6: Count Contact')
    print('7: Exit')    

    choice = input("Enter your choice (1-7) : ")

    if choice=='1':
        name = input("Enter Name : ")
        if name in contacts:
            print(f"Contact Name {name} already exists.")
        else:
            age = int(input("Enter age : ")) 
            email = input("Enter Email : ") 
            mobile = input("Enter Mobile No. : ")  
            contacts[name] = {'age':age , 'email': email,'mobile no.':mobile}
            print(f"New Contact {name} has been created successfully!")
     
    elif choice=='2':
        name = input("Enter contact name to view : ")
        if name in contacts:
            contact = contacts[name]
            print(f"name : {name}, age : {age}, email : {email}, mobile no. : {mobile}")
        else:
            print("Contact Not Found!")   

    elif choice=='3':
        name = input("Enter contact name to update : ")   
        if name in contacts:
            age=int(input("Enter updated age : "))      
            email = input("Enter updated email : ")
            mobile= input("Enter updated Mobile No. : ")
            contacts[name]={'age':age , 'email': email,'mobile no.':mobile}
        else:
            print("No Contact Found with this name!")    

    elif choice=="4":
        name = input("Enter contact name to delete : ")  
        if name in contacts:
            del contacts[name] 
            print(f"Contact {name} has been deleted successfully!") 
        else:
            print("Contact Not Found")        

    elif choice=='5':
        search_name = input("Enter contact name to search : ") 
        found = False
        for name,contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f"( Contact Found ) : Name = {name} , Age = {age} ,Email = {email}, Mobile No. = {mobile}")       
                found = True
        if not found:
            print("No Contact Found with that name!")  

    elif choice=='6':
        print(f"Total Number of Contacts = {len(contacts)}") 

    elif choice=='7':
        print("Good Bye...Closing the Program!")      
        break

    else:
        print("Invalid Input!")           
 