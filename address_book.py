'''
Overview: The user wants to create an address book and downloads your program. 
How would you make it? Create a program that prompts the user for the information 
in most address books and then stores it in a .txt file! This program also inserts the data
into a table named addresses.
'''

import mysql.connector

print 'Welcome to your address Book!'
print 'Please get ready to enter information into your address book!\n'


def my_address_book():
    cnx = mysql.connector.connect(user='root', 
                              password='youngman15',
                              host='127.0.0.1',
                              database='addresses')
    cursor = cnx.cursor()
    
    my_book = {}
    iter = 1
    
    add_address = ("INSERT INTO my_address "
                    "(first_name,last_name,age,address_1,address_2,city,state)"
                    "VALUES(%s,%s,%s,%s,%s,%s,%s)")
    
    you_ready = raw_input('Are you ready? Please enter a Y or N: ')
    
    if you_ready.lower() == 'y':
        first_name = raw_input('Enter the first name of your contact: ')
        last_name = raw_input('Enter the last name of your contact: ')
        age = int(raw_input('Enter the age of your contact: '))
        address_1 = raw_input('Enter the address line 1 of your contact: ')
        address_2 = raw_input('Enter the address line 2 of your contact: ')
        city = raw_input('Enter the city of your contact: ')
        state = raw_input('Enter the state of your contact: ')
        
        
        my_book['Person ' + str(iter)] = {'First' : first_name , 'Last' : last_name, 'Age' : age, 'Address_1': address_1,
                'Address_2' : address_2, 'City' : city, 'State' : state }
        iter += 1
        
        enter_again = raw_input('Do you want to enter another contact? Please enter a Y or N: ')
        
        while enter_again.lower() == 'y':
           
            first_name = raw_input('Enter the first name of your contact: ')
            last_name = raw_input('Enter the last name of your contact: ')
            age = int(raw_input('Enter the age of your contact: '))
            address_1 = raw_input('Enter the address line 1 of your contact: ')
            address_2 = raw_input('Enter the address line 2 of your contact: ')
            city = raw_input('Enter the city of your contact: ')
            state = raw_input('Enter the state of your contact: ')
        
            my_book['Person ' + str(iter)] = {'First' : first_name , 'Last' : last_name, 'Age' : age, 'Address_1': address_1,
                    'Address_2' : address_2, 'City' : city, 'State' : state }
            iter += 1
        
            enter_again = raw_input('\nDo you want to enter another contact? Please enter a Y or N: ')
        
    elif you_ready.lower() == 'n':
        print 'bye'
        exit()

        
    with open('myfile.txt','w') as f:
        f.write('Here is the list of names you wrote: \n\n')
        for key in my_book:
            f.write(key+'\n')
            for i in my_book[key]:
                f.write((i + ': ' + str(my_book[key][i]) + '\n'))
                if i == 'First':
                    f.write(('\n'))

    add_items = ()

    
    for things in my_book:
        add_items = (my_book[things]['First'], my_book[things]['Last'],my_book[things]['Age'],
                    my_book[things]['Address_1'],my_book[things]['Address_2'],my_book[things]['City'],
                    my_book[things]['State'])
                    
        cursor.execute(add_address, add_items)
       
    cnx.commit()
    cursor.close()
    cnx.close()
    

my_address_book() 