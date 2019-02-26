# https://www.reddit.com/r/dailyprogrammer/comments/8xzwl6/20180711_challenge_365_intermediate_sales/

'''
    Sales people get paid using the following formula for the total 
commission: commission is 6.2% of profit, with no commission for 
any product to total less than zero.

    You'll be given two matrices showing the sales figure per 
salesperson for each product they sold, and the expenses by product 
per salesperson. Example:

Revenue

            Johnver Vanston Danbree Vansey  Mundyke
Tea             190     140    1926     14      143
Coffee          325      19     293   1491      162
Water           682      14     852     56      659
Milk            829     140     609    120       87

Expenses

            Johnver Vanston Danbree Vansey  Mundyke
Tea             120      65     890     54      430
Coffee          300      10      23    802      235
Water            50     299    1290     12      145
Milk             67     254      89    129       76



Output

            Johnver Vanston Danbree Vansey  Mundyke
Commission       92       5     113     45       32
'''

def sales_comissions(revenue, expenses):
    
    '''
    The total comission for a given worker is the sum\
    of the comissions received for each product,\
    calculated as such:
        total_com = (prod1_rev - prod1_exp) * 0.062 +\
            (prod2_rev - prod2_exp) * 0.062 +\
            ...
            (prodn_rev - prodn_exp) * 0.062
    given that the difference between a product's\
    revenue and expense is bigger than zero, otherwise\
    the worker doesn't receive a comission for that product
    '''
    
    # Create the output matrix. The first row (the column headers)\
    # will the same as the one from the input matrices. The second\
    # row is a row with the total comission each worker will receive
    com_matrix = [revenue[0], [], []]
    com_matrix[1] = ['Comission'] + [0 for i in range(len(com_matrix[0])-1)]

    '''
        For each product, check if each worker makes profit with it.
    For those that do make profit, increment those workers' comissions 
    with 6.2% of the profit they made for that product.
        e.g.: Worker1 makes 50 profit selling Tea (revenue=100, expense=50).
    Then increment Worker1's comission by 6.2% of 50 (3.1). This process is
    repeated for each worker, for each product.
    '''
    
    # Loop through each product in the revenue/expenses matrix (rather,\
    # it's index). We start at index 1 because the first row contains just\
    # the column headings
    for product in range(1, len(revenue)):

        # Loop through each worker in the revenue/expenses matrix (rather,\
        # it's index). We start at index 1 because the index 0 of each row\
        # corresponds to a product name
        for worker in range(1, len(revenue[1])):
            
            # Get the revenue and expense for this product
            prod_revenue = revenue[product][worker]
            prod_expense = expenses[product][worker]
            
            # If the worker made profit on this product, then it receives\
            # 6.2% of the profit as a comission
            if (prod_revenue - prod_expense) > 0:
                # This product's comission is simply added to the already\
                # existing comission
                com_matrix[1][worker] += (prod_revenue - prod_expense) * 0.062            
        

    # This loop is used simply to round the comissions to 2 decimal units.
    # We only call the str() function on each comission to allow the output\
    # formatting outside the function
    for i in range(1, len(com_matrix[1])):
        com_matrix[1][i] = str(round(com_matrix[1][i], 2))
    
    return com_matrix


revenue_sample1 = [
    ['', 'Frank', 'Jane'],
    ['Tea', 120, 145],
    ['Coffee', 243, 265]
]

expenses_sample1 = [
    ['', 'Frank', 'Jane'],
    ['Tea', 130, 59],
    ['Coffee', 143, 198]
]

revenue_sample2 = [
    ['', 'Johnver', 'Vanston', 'Danbree', 'Vansey', 'Mundyke'],
    ['Tea', 190, 140, 1926, 14, 143],
    ['Coffee', 325, 19, 293, 1491, 162],
    ['Water', 682, 14, 852, 56, 659],
    ['Milk', 829, 140, 609, 120, 87]
]

expenses_sample2 = [
    ['', 'Johnver', 'Vanston', 'Danbree', 'Vansey', 'Mundyke'],
    ['Tea', 120, 65, 890, 54, 430],
    ['Coffee', 300, 10, 23, 802, 235],
    ['Water', 50, 299, 1290, 12, 145],
    ['Milk', 67, 254, 89, 129, 76]
]

samples = [revenue_sample1, expenses_sample1, revenue_sample2, expenses_sample2]

for i in range(0, 3, 2):
    comissions_received = sales_comissions(samples[i], samples[i+1])
    for row in comissions_received:
        print(('{:>13}' * len(row)).format(*row))
    print()