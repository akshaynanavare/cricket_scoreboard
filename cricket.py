from cricketteam import CricketTeam
from constants import *

class Cricket:
    def __init__(self,no_of_players, overs):
        self.total_players = no_of_players
        self.batting_team = CricketTeam(1,no_of_players=no_of_players)
        self.batting_team.set_is_playing_bat(True)
        self.bowling_team = CricketTeam(2,no_of_players=no_of_players)
        self.bowling_team.set_is_playing_bat(False)
        self.current_total_score = 0
        self.last_team_score = 0
        self.total_overs = overs
        self.first_innings = True
        self.won_team = None
    
    def print_scoreboard(self):            
        self.batting_team.print_scoreboard()
        self.bowling_team.print_scoreboard()
        return
    
    def print_results(self):
        if self.won_team != None:
            result = "Team "+ str(self.won_team.id) + " won the match by "
            if self.bowling_team.id == self.won_team.id :
                msg = str(self.last_team_score - self.current_total_score) + " runs"
            else:
                msg = str(self.won_team.no_of_players - self.won_team.wickets) + " wickets (" + str(self.total_overs * 6  - self.won_team.no_of_balls_played) + " balls)"
            print("Result : " ,result + msg)
        else:
           print("Result : Match Draw") 
       
    
    def play_match(self):
        for inning in range(2):
            print("Play Innings : ", inning+1)
            self.play_innings()
        self.print_results()

    def swap_team(self):
        tmp = self.batting_team
        self.batting_team = self.bowling_team
        self.bowling_team = tmp
        self.batting_team.set_is_playing_bat(True)
        self.bowling_team.set_is_playing_bat(False)
    
    def play_innings(self) -> int:
        is_all_out = False
        over = 0
        while over < self.total_overs:
            over += 1
            print("Over: ", over)
            ball = 0
            id = input("Enter bowler name : ")
            prev_score = self.current_total_score
            ok = self.bowling_team.set_bowler(id)
            if not ok :
                over -=1
                print("Please enter valid bowler name")
                continue
            while ball < BALLS_IN_OVER :
                ball +=1
                int_score = 0
                in_ball = input()
                if in_ball == WICKET_BALL :
                    self.bowling_team.set_wicket_taken()                        # Increase bowler's team and bowler's wicket stats
                    self.batting_team.add_score(int_score)
                    if not self.batting_team.striker_out():                     # Check all out condition
                        is_all_out = True
                        break      
                elif in_ball == WIDE_BALL :
                    ball-=1
                    int_score = WIDE_BALL_RUN
                    self.batting_team.add_extras()                              # To collect extra's for batting team
                else :
                    int_score = int(in_ball)        
                    self.batting_team.add_score(int_score)                      # Increment team's and striker's score
                    if int_score == ONE_RUN or int_score == THREE_RUN:
                        self.batting_team.change_strike()                       # Change strike for 1's and 3's
                    elif int_score == DOT_BALL :
                        self.bowling_team.set_dot_balls()                       # To collect stats of dot balls for bowler

                self.bowling_team.set_runs_given(int_score, in_ball)            # To calculate bowler's economy based on runs and total balls
                self.current_total_score += int_score
                
                if not self.first_innings :                                     # Check for chasing team score for winning condition
                    if self.current_total_score > self.last_team_score :
                        self.batting_team.isWon = True
                        self.won_team = self.batting_team
                        self.print_scoreboard()
                        return
            if prev_score == self.current_total_score:                          # To collect stats of maiden overs for bowler
                self.bowling_team.set_maiden_over()
            
            self.print_scoreboard()
            if is_all_out:
                break
            self.batting_team.change_strike()                                   # Change strike at each over

        if not self.first_innings:
            if self.current_total_score > self.last_team_score :
                self.batting_team.isWon = True
                self.won_team = self.batting_team
            elif self.current_total_score < self.last_team_score :
                self.bowling_team.isWon = True
                self.won_team = self.bowling_team
        else:
            self.first_innings = False
            self.last_team_score = self.current_total_score
            self.current_total_score = 0
            self.swap_team()
        return
