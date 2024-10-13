def print_welcome(name):
    '''Takes name and outputs Hello, "name"! centered in a 20 space field'''
    
    message = f'Hello, {name}!'
    print(f'\'{message: ^20}\'')

####################################

def print_shop_menu(item1name, item1price, item2name, item2price):
    '''Takes two items and two prices and puts them into a nice little shop menu'''
    
    top_border = '/' + ('-' * 22) + '\\' 
    bottom_border = '\\' + ('-' * 22) + '/'
    #creates the top and bottom border variables
    
    item1dollar = f'${item1price:.2f}'
    item2dollar = f'${item2price:.2f}'
    #converts the input float into a float with dollar signs and two digits after the decimal
    
    print(top_border)
    print(f'| {item1name: <12}{item1dollar: >8} |')
    print(f'| {item2name: <12}{item2dollar: >8} |')
    print(bottom_border)

#####################################

print("print_welcome tests with names Bob, Ashley, and Bartholomew")
print_welcome('Bob')
print_welcome('Ashley')
print_welcome('Bartholomew')
print()
print("print_shop_menu tests with Pear, 1.56, Bucket, 5.2")
print_shop_menu("Pear",1.56,"Bucket",5.20)
print()
print("print_shop_menu tests with Broadsword, 20, Apple, 5.21111")
print_shop_menu("Broadsword",20,"Apple",5.21111)
print()
print("print_shop_menu tests with Donkey, 109.99, Orange, 6")
print_shop_menu("Donkey",109.99,"Orange",6)


    

    
