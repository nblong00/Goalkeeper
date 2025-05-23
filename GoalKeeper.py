def main():
    players = []
    add_player = input("Would you like to add a player to the list? (Yes/No) ")
    while add_player.title() == "Yes":
        player_name = input("Enter the name of the player to add to the team: ")
        players.append(player_name)
        add_player = input("Would you like to add a player to the list? (Yes/No) ")
    print("There are {} players on the team.".format(len(players)))
    for index, player in enumerate(players, 1):
        print("Player {} : {}".format(index, player))
    goal_keeper = int(input("Please select the goal keeper by selecting the player number. (ex. 1) "))
    print("Great!!! The Goalkeeper for the game will be {}".format(players[goal_keeper - 1]))
