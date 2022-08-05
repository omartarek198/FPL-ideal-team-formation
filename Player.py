
class Player:
    def __init__(self, code,fn,ln,totalPts,ptsPergame,minutes,postion,selectedBy,cost):
        self.code = code
        self.firstName = fn
        self.lastName = ln
        self.totalPoints = totalPts
        self.pointsPerGame = ptsPergame
        self.minutesPlayed = minutes
        self.Role = postion #aka player postion in squad
        self.SelectedPercantage = selectedBy
        self.cost = cost

    def Eval(self):
        #returns computed evalutation and player id
        eval = 0

        if (self.Role == 1):
            pass
        if (self.Role == 2):
            pass
        if (self.Role == 3):
            pass
        if (self.Role == 4):
            pass

        return  eval