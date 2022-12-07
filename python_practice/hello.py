# Udemy python course

# # Exercise 1
# animal = 'cat'
# vegetable = 'banana'
# mineral = 'gold'
# print('Here is an animal, a vegetable and a mineral')
# print(animal)
# print(vegetable)
# print(mineral)

# # Exercise 2
# user_input = input('Please type something and press enter: ')
# print('You entered: ')
# print(user_input)

# # # Exercise 3
# # Price based on one server
# price_per_hour = 0.51
# daily_cost = price_per_hour * 24
# price_per_month = daily_cost * 30
# print(f'The daily cost of operating one server per day is: ${daily_cost}')
# print(f'The daily cost of operating one server per month is: ${price_per_month}')
# # Price based on 20 servers
# daily_cost_twenty = daily_cost * 20
# price_per_month_twenty = price_per_month * 20
# print(f'The daily cost of operating twenty servers per day is: ${daily_cost_twenty}')
# print(f'The daily cost of operating twenty servers per month is: ${price_per_month_twenty}')
# funds = 918
# fund_runway = funds / daily_cost
# print(f'The number of days I can operate one server with $917 is {fund_runway}')

# # Exercise 4
# distance = input('How far would you like to travel in miles?: ')
# distance = int(distance)

# if distance <= 3:
#     print('You can walk')
# elif distance < 300: 
#     print('You should drive')
# else:
#     print('You should fly')

# # Exercise 5
# def create_story():
#     print(f'There once was a {noun} who wanted to go {verb} because they were very {adjective}')

# noun = input('Type a noun: ')
# verb = input('Type a verb: ')
# adjective = input('Type an adjective: ')
# create_story()

# # Exercise 6
# # Creating a list to hold the to-do items
# to_do_list = []
# completed = False
# while not completed:
#     to_do_item = input('Enter a task for your to-do list. Press <enter> when done: ')
#     if len(to_do_item) == 0:
#         completed = True
#     else:
#         to_do_list.append(to_do_item)
#         print('Task added.')

# # Displaying the to-do list
# print('Your To-Do List:')
# print('----------------')
# for to_do_item in to_do_list:
#     print(to_do_item)

# # Exercise 7
# facts = {
#     'Jeff': 'Is afraid of clowns.',
#     'David': 'Plays the piano.',
#     'Jason': 'Can fly an airplane.'
# }

# # displaying facts
# def show_facts(facts):
#     for fact in facts:
#         print(f'{fact}: {facts[fact]}')

# show_facts(facts)

# # changing a fact
# facts['Jeff'] = 'Is afraid of bananas.'

# show_facts(facts)

# # Exercise 8
# # create a list of airports
# aiports = [
#     ('Heathrow Airport', 'LHR'),
#     ('Los Angeles Aiport', 'LAX'),
#     ('Kuala Lumpur Aiport', 'KUL')
# ]

# for (airport, code) in aiports:
#     print(f'The code for {airport} is {code}.')

# # Exercise 9
# with open('/Users/kavita.adm/Desktop/hello/file.txt') as file:
#     line_no = 1
#     for line in file:
#         print(f'{line_no}: {line.rstrip()}')
#         line_no += 1

