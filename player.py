from constants import *
class Player :
    def __init__(self) -> None:
        self.name = None
        self.score = 0
        self.fours = 0
        self.sixes = 0
        self.balls_played = 0
        self.is_out = False
        self.strike_rate = 0
        self.maiden_over = 0
        self.dot_balls = 0
        self.balls_delivered = 0
        self.wickets_taken = 0
        self.economoy = 0
        self.runs_given = 0
    
    ### Batting functions start ###
    def get_score(self)-> int:
        return self.score
    
    def set_score(self, score):
        self.score += score
        self.balls_played +=1
        self.calculate_strike_rate()
    
    def calculate_strike_rate(self):
        self.strike_rate = round((self.score/self.balls_played) * 100,2)
    
    def get_strike_rate(self)-> float:
        return self.strike_rate

    def get_fours(self)-> int:
        return self.fours
    
    def set_fours(self):
        self.fours += 1
    
    def get_sixes(self)-> int:
        return self.sixes
    
    def set_sixes(self):
        self.sixes += 1

    def get_balls_played(self)-> int:
        return self.balls_played
    
    def set_balls_played(self):
        self.balls_played +=1 

    def out(self):
        self.is_out = True

    ### Batting functions end ###


    ### Bowling functions start ###
    def get_overs_delievered(self)-> int:
        over = self.balls_delivered // 6
        over += ((self.balls_delivered % 6)/10)
        return over

    def get_economy(self)-> float:
        return self.economoy

    def get_wickets_taken(self)-> int:
        return self.wickets_taken

    def set_wicket_taken(self) :
        self.wickets_taken +=1
        self.balls_delivered +=1
 
    def get_runs_given(self):
        return self.runs_given

    def set_runs_given(self, score, ball_type):
        self.runs_given += score
        if ball_type != WIDE_BALL :
            self.balls_delivered +=1
        self.calculate_economy()
    
    def calculate_economy(self) :
        if self.balls_delivered > 0:
            economy = self.runs_given / self.balls_delivered
            self.economoy = round(economy * 6,2)

    def get_maiden_over(self)-> int:
        return self.maiden_over

    def set_maiden_over(self):
        self.maiden_over +=1

    def get_dot_balls(self)-> int:
        return self.dot_balls

    def set_dot_balls(self):
        self.dot_balls += 1


    ### Bowling functions end ###