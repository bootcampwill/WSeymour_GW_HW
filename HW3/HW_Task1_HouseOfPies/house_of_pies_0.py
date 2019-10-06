#define pie list
pies = ["Pecan",
        "Apple Crisp",
        "Bean",
        "Banoffee",
        "Black Bun",
        "Blueberry",
        "Buko",
        "Burek",
        "Tamale",
        "Steak"]

#print welcome message
print('''
    Welcome to the House of Pies! Here are our pies:
    ---------------------------------------------------------------------
    (1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee,  (5) Black Bun, 
    (6) Blueberry, (7) Buko, (8) Burek,  (9) Tamale, (10) Steak)''')

#set initial conditions
another = 'y'
n_ordered = 0
pie_purchases = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

while another == 'y':
    
    #ask for pie choice
    selection = int(input("Select the number of the pie you would like to order"))-1
    print(f"Great! We'll have that {pies[selection]} pie right out for you.")
    n_ordered += 1        
    pie_purchases[selection] += 1
        
    another = input("Would you lik to order another pie? (y/n)")

print(f'**********************************************\nTotal number of pies ordered = {n_ordered}\n**********************************************')

for x in pies:
    index = pies.index(x)
    print(f'{pies[index]}: {pie_purchases[index]}')
    
  
    

