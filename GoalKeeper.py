# TODO Create an empty list to maintain the player names
players = []
player_number = 1

# TODO Ask the user if they'd like to add players to the list.
# If the user answers "Yes", let them type in a name and add it to the list.
# If the user answers "No", print out the team 'roster'

add_player = input("Would you like to add a player to the list? (Yes/No) ")

while add_player.title() != "No":
    player_name = input("Enter the name of the player to add to the team: ")
    players.append(player_name)
    add_player = input("Would you like to add a player to the list? (Yes/No) ")

# TODO print the number of players on the team
print("There are {} players on the team.".format(len(players)))

# TODO Print the player number and the player name
# The player number should start at the number one
for player in players:
    print("Player {} : {}".format(player_number, player))
    player_number += 1

# TODO Select a goalkeeper from the above roster

goal_keeper = int(input("Please select the goal keeper by selecting the player number. (ex. 1) "))


# TODO Print the goal keeper's name
# Remember that lists use a zero based index

print("Great!!! The Goalkeeper for the game will be {}".format(players[goal_keeper - 1]))
