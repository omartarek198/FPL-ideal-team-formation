
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
        #returns computed evalutation
        eval = 0

        eval =self.totalPoints * self.minutesPlayed * float (self.SelectedPercantage) / self.cost



        return  eval