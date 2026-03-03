# print user instructions for the game
def user_instructions():
    print('-'*60)
    print('Move through the rooms using the commands: "North", "South", "East", "West"')
    print('Each room contains an item to pick up, use command: Y or N')
    print('Good luck!')
    print('-'*60)

#opening greeting
print("A viral outbreak has occured causing the dead to walk the streets! The last broadcast from the government said to shelter in place"
        "\nuntil the military clears the area, but that was months ago.... Your supplies have begun to dwindle and you have begun to worry about"
        "\nyour surivial when a broadcast comes through your HAM radio. It tells you of a survivor camp across the city."
        "\nYour goal is to collect all 6 items to prepare for your journey to the camp."
        "\nTake the items to the Foyer when you are ready to leave or type 'Exit' to leave the game")

# A dictionary for the text game
# The dictionary links a room to other rooms
rooms = {
        'Living Room': {'North': 'Bedroom', 'South': 'Garage', 'East': 'Kitchen', 'West': 'Foyer', },
        'Bedroom': {'South': 'Living Room', 'East': 'Bathroom', 'Item': 'Paddle ball'},
        'Bathroom': {'West': 'Bedroom', 'Item': 'Medicine'},
        'Garage': {'North': 'Living Room', 'East': 'Attic', 'Item': 'License plates'},
        'Attic': {'West': 'Garage', 'Item': 'Candlestick'},
        'Kitchen': {'West': 'Living Room', 'North': 'Pantry', 'Item': 'Pot'},
        'Pantry': {'South': 'Kitchen', 'Item': 'Cheese Whiz'},
        'Foyer': {'East': 'Living Room', 'Boss': 'Zombies'}
    }

start = 'Living Room' # identify starting location
current_room = start #initialize start for gameplay loop
user_instructions()
inventory = [] #create empty list for inventory

while True:
    print('You are in the ', current_room)
    print('Inventory: ', inventory)
    move = input('What would you like to do? \n').capitalize() # user input direction between rooms
    if move == 'Exit': # exit program
        print('Thank you for playing!')
        break

    if move in rooms[current_room]: #move between rooms
        current_room = rooms[current_room][move]

    else:
        print('You cant go that way! Please choose a different direction.') #invalid move prompt
        continue

    if 'Boss' in rooms[current_room]:
        if rooms[current_room]['Boss'] == 'Zombies' and len(inventory) != 6: #losing condition
            print('You were not prepared to defend against the zombies and they eat your brains!')
            print('You lost the game! Hope you had fun!')
            break
    if 'Boss' in rooms[current_room]:
        if rooms[current_room]['Boss'] == 'Zombies' and len(inventory) == 6: # win condition
            print('\nYou double check your bag for your cheese whiz and medicine before opening the door.'
                '\nThen you leave your house weilding a candlestick with license plate armor, a pot shielding your head, '
                '\nand your trusty paddleball to keep you entertained as you battle your way through the undead.')
            print('You won! Hope you had fun!')
            break
    if ('Item' in rooms[current_room]) and (rooms[current_room]['Item'] not in inventory):
            current_item = rooms[current_room]['Item']
            print('You see', current_item)
            x = input('Would you like to pick it up? Y/N').capitalize()
            if x == 'Y':
                inventory.append(current_item) # add item to inventory


