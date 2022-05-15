Code workflow : 
1. main.py is the first driving function
2. This function is creating Cricket class's object and initializing all the team's (CricketTeam) and respective player's(Player) objects
3. After initializing Cricket class we are calling play_match() function to start the game
4. This function is responsible for every innings played and every over of that inning
5. After each over, batting's team and bowling team's scoreboard is displayed
6. All the team stats and player stats are controlled by CricketTeam class objects and Player class objects respectively

```
Terms used in scoretable :
BP : Balls played
SR : Strike rate
OD : Overs delivered
Eco. : Economy
MO. : Maiden Over
Wick.T:  Wicket Taken
DB : Dot balls

Run command : python main.py
Note : Refer input.txt for input format (or copy paste data after running cmd)

Sample Input and Output : 
    No. of players for each team :5
    No. of overs : 2
    Enter Team  1  Player Names :
    kohli
    dhoni
    raina
    harbhajan
    zaheer
    Enter Team  2  Player Names :
    gayle
    pravin
    omraj
    hardik
    pandey
    Play Innings :  1
    Over:  1
    Enter bowler name : gayle
    1
    0
    0
    0
    6
    4
    Scoreboard for team :  1
    Player Name         Score            4s                  6s           BP          SR                OD       Eco.         MO.       Wick.T        DB
    kohli*                 1                0               0                1          100.0 %         0.0       0          0         0                  0
    dhoni*                 10                1               1                5          200.0 %         0.0       0          0         0                  0
    raina                 0                0               0                0          0 %         0.0       0          0         0                  0
    harbhajan                 0                0               0                0          0 %         0.0       0          0         0                  0
    zaheer                 0                0               0                0          0 %         0.0       0          0         0                  0
    Total Score :  11 / 0
    Total overs :  1.0
    Team Extras :  0


    Scoreboard for team :  2
    Player Name         Score            4s                  6s           BP          SR                OD       Eco.         MO.       Wick.T        DB
    gayle                 0                0               0                0          0 %         1.0       11.0          0         0                  3
    pravin                 0                0               0                0          0 %         0.0       0          0         0                  0
    omraj                 0                0               0                0          0 %         0.0       0          0         0                  0
    hardik                 0                0               0                0          0 %         0.0       0          0         0                  0
    pandey                 0                0               0                0          0 %         0.0       0          0         0                  0
    Total Score :  0 / 0
    Total overs :  0.0
    Team Extras :  0


    Over:  2
    Enter bowler name : pravin
    1
    0
    2
    1
    4
    W
    Scoreboard for team :  1
    Player Name         Score            4s                  6s           BP          SR                OD       Eco.         MO.       Wick.T        DB
    kohli                 6                1               0                4          150.0 %         0.0       0          0         0                  0
    dhoni*                 13                1               1                8          162.5 %         0.0       0          0         0                  0
    raina*                 0                0               0                0          0 %         0.0       0          0         0                  0
    harbhajan                 0                0               0                0          0 %         0.0       0          0         0                  0
    zaheer                 0                0               0                0          0 %         0.0       0          0         0                  0
    Total Score :  19 / 1
    Total overs :  2.0
    Team Extras :  0


    Scoreboard for team :  2
    Player Name         Score            4s                  6s           BP          SR                OD       Eco.         MO.       Wick.T        DB
    gayle                 0                0               0                0          0 %         1.0       11.0          0         0                  3
    pravin                 0                0               0                0          0 %         1.1       6.86          0         1                  1
    omraj                 0                0               0                0          0 %         0.0       0          0         0                  0
    hardik                 0                0               0                0          0 %         0.0       0          0         0                  0
    pandey                 0                0               0                0          0 %         0.0       0          0         0                  0
    Total Score :  0 / 0
    Total overs :  0.0
    Team Extras :  0


    Play Innings :  2
    Over:  1
    Enter bowler name : harbhajan
    4
    0
    1
    Wd
    4
    1
    6
    Scoreboard for team :  2
    Player Name         Score            4s                  6s           BP          SR                OD       Eco.         MO.       Wick.T        DB
    gayle*                 11                1               1                4          275.0 %         1.0       11.0          0         0                  3
    pravin*                 5                1               0                2          250.0 %         1.1       6.86          0         1                  1
    omraj                 0                0               0                0          0 %         0.0       0          0         0                  0
    hardik                 0                0               0                0          0 %         0.0       0          0         0                  0
    pandey                 0                0               0                0          0 %         0.0       0          0         0                  0
    Total Score :  17 / 0
    Total overs :  1.0
    Team Extras :  1


    Scoreboard for team :  1
    Player Name         Score            4s                  6s           BP          SR                OD       Eco.         MO.       Wick.T        DB
    kohli                 6                1               0                4          150.0 %         0.0       0          0         0                  0
    dhoni                 13                1               1                8          162.5 %         0.0       0          0         0                  0
    raina                 0                0               0                0          0 %         0.0       0          0         0                  0
    harbhajan                 0                0               0                0          0 %         1.0       17.0          0         0                  1
    zaheer                 0                0               0                0          0 %         0.0       0          0         0                  0
    Total Score :  19 / 1
    Total overs :  2.0
    Team Extras :  0


    Over:  2
    Enter bowler name : zaheer
    W
    1
    0
    0
    W
    0
    Scoreboard for team :  2
    Player Name         Score            4s                  6s           BP          SR                OD       Eco.         MO.       Wick.T        DB
    gayle                 11                1               1                7          157.14 %         1.0       11.0          0         0                  3
    pravin                 5                1               0                3          166.67 %         1.1       6.86          0         1                  1
    omraj*                 1                0               0                1          100.0 %         0.0       0          0         0                  0
    hardik*                 0                0               0                1          0.0 %         0.0       0          0         0                  0
    pandey                 0                0               0                0          0 %         0.0       0          0         0                  0
    Total Score :  18 / 2
    Total overs :  2.0
    Team Extras :  1


    Scoreboard for team :  1
    Player Name         Score            4s                  6s           BP          SR                OD       Eco.         MO.       Wick.T        DB
    kohli                 6                1               0                4          150.0 %         0.0       0          0         0                  0
    dhoni                 13                1               1                8          162.5 %         0.0       0          0         0                  0
    raina                 0                0               0                0          0 %         0.0       0          0         0                  0
    harbhajan                 0                0               0                0          0 %         1.0       17.0          0         0                  1
    zaheer                 0                0               0                0          0 %         1.2       0.75          0         2                  3
    Total Score :  19 / 1
    Total overs :  2.0
    Team Extras :  0


    Team 1 won the match by 1 runs
```
