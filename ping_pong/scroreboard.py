from turtle import Turtle

class Score(Turtle):  # Score inherits from Turtle superclass
    """a turtle that keeps track of the score and displays the score in the program"""

    def __init__(self):
        """initializes a new scoreboard object"""
        super().__init__()  # score inherits from Turtle superclass
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score=0
        self.updatescore()
    def updatescore(self):
        self.clear()
        self.goto(-100,300)
        self.write(self.l_score,align="center",font = ("Courier", 38, "normal") )
        self.goto(100,300)
        self.write(self.r_score,align="center",font = ("Courier", 38, "normal") )

    def reset(self):
        self.l_score = 0
        self.r_score=0
        self.updatescore()
    def l_update_score(self):
        """adds a point to the score and display new score"""
        self.l_score += 1
        self.updatescore()
    def r_update_score(self):
        """adds a point to the score and display new score"""
        self.r_score += 1
        self.updatescore()