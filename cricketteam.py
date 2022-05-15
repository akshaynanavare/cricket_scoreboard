
from player import Player
from constants import *


class CricketTeam:
    def __init__(self, id, no_of_players) -> None:
        self.id = id
        self.no_of_players = no_of_players
        self.players = []
        print("Enter Team ",self.id ," Player Names : ")
        for index in range(self.no_of_players ) :
            player = Player()
            name = input()
            player.name = name
            self.players.append(player)

        self.overs_played = 0
        self.no_of_balls_played = 0
        self.striker = self.players[0]
        self.non_striker = self.players[1]
        self.isWon = None
        self.total_score = 0
        self.current_player_index = 1
        self.no_of_fours = 0
        self.no_of_sixes = 0
        self.wickets = 0
        self.extras = 0
        self.bowler = None
        self.dot_balls_delivery = 0
        self.wickets_taken = 0
        self.is_playing_bat = True

    def get_is_playing_bat(self):
        return self.is_playing_bat
    
    def set_is_playing_bat(self, status):
        self.is_playing_bat = status    

    def set_wicket_taken(self) :
        if self.bowler != None:
            self.bowler.set_wicket_taken()
        self.wickets_taken +=1

    def change_strike(self):
        tmp = self.striker
        self.striker = self.non_striker 
        self.non_striker = tmp

    def get_no_of_balls_played(self) -> int:  
        return self.no_of_balls_played
    
    def set_runs_given(self, score, ball_type) :
        self.bowler.set_runs_given(score, ball_type)

    #striker_out : Return false if all out otherwise true
    def striker_out(self) :
        is_all_out = False
        self.current_player_index += 1
        if self.current_player_index >= self.no_of_players :
            self.striker = None
            is_all_out = True
        else :
            self.striker.out()
            self.striker = self.players[self.current_player_index]
        self.wickets +=1
        
        return not is_all_out


    def set_dot_balls(self):
        if self.bowler != None:
            self.bowler.set_dot_balls()
        self.dot_balls_delivery +=1

    def set_bowler(self,id):
        # We can use maps here to improve time complexity
        for player in self.players:
            if player.name == id:
                self.bowler = player
                return True
        return False
    
    def add_extras(self) :
        if self.is_playing_bat :        
            self.extras +=1           
            self.total_score += 1
            
    def add_score(self, score) :
        score = int(score)
        if score == FOUR_RUN :
            self.no_of_fours +=1 
            self.striker.set_fours()
        elif score == SIX_RUN :
            self.no_of_sixes +=1 
            self.striker.set_sixes()
        
        self.total_score += score
        self.no_of_balls_played +=1
     
        self.striker.set_score(score)
    
    def get_overs_played(self):
        over = self.no_of_balls_played // 6
        over += ((self.no_of_balls_played % 6)/10)
        self.overs_played = over
        return self.overs_played
    
    def set_maiden_over(self):
        self.bowler.set_maiden_over()

    def print_scoreboard(self):
        print("Scoreboard for team : ", self.id)
        print("Player Name         Score            4s  \
                6s           BP \
         SR                OD       Eco.         MO.       Wick.T        DB")

        for player in self.players:
            name = player.name
            if self.is_playing_bat == True and (player == self.striker or player == self.non_striker) :
                name += "*"
            score_data = name + "                 " \
                + str(player.get_score()) + "                "\
                + str(player.get_fours()) + "               " \
                + str(player.get_sixes()) + "                "\
                + str(player.get_balls_played()) + "          "\
                + str(player.get_strike_rate()) +" %         " \
                + str(player.get_overs_delievered()) + "       "\
                + str(player.get_economy())+ "          " \
                + str(player.get_maiden_over()) +"         " \
                + str(player.get_wickets_taken())+ "                  " \
                + str(player.get_dot_balls())

            print(score_data)
        print("Total Score : ", self.total_score, "/", self.wickets)
        print("Total overs : ", self.get_overs_played())
        print("Team Extras : ", self.extras)
        print("\n")
