
from cricket import Cricket


def main():
    players_per_team = int(input("No. of players for each team :"))
    no_of_overs = int(input("No. of overs : "))

    cricket_game = Cricket(no_of_players=players_per_team, overs=no_of_overs)
    cricket_game.play_match()

    ### 
    # Note : Code work flow mentioned in README.md file.
    #
    # Future enhancement and improvements : 
    # 1. Currently all inputs param are taken care inside the play_match() function but we can passed through the driver's function.
    # 2. All inputs will be validated and passed from this function to Cricket object
    # 3. All stats properties are currently in respective player and team classes. we can divide further in stats class and inherit to player's stats and team's stats
    # 4. We can inherit then bowler's and batsman's stats from player's stats class
    # 5. We can read inputs from file as well.
    ###  

if __name__ == "__main__":
    main()
  