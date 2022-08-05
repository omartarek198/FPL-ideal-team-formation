from fpl import FPL
import aiohttp
import asyncio
from Player import  *
import sys

def GetRolesList(role,players):

    temp = []

    for i in players:
        if (i.Role == role):
            temp.append(i)


    return temp


def IsIdInSquad(id, squad):
    for i in squad:
        if (i.code == id):
            return True

    return False

def GetMinimumEval(players):

    min = 9999
    index = 0
    for i in range(0,len(players)):
        if players[i].Eval()  < min:
            min = players[i].Eval
            index  = i

    return index



async def main():
    session = aiohttp.ClientSession()
    fpl = FPL(session)
    players = await fpl.get_players()
    x = 1
    ListOfPlayers = []
    topGoalies = []
    topDefs = []
    topMids = []
    topAtk = []


    for player in players:
        if player.minutes ==0:
            continue
        temp =  Player(player.code,player.web_name,ln=player.first_name,totalPts= player.total_points,ptsPergame=player.points_per_game,
                       minutes=player.minutes,postion=player.element_type,selectedBy=player.selected_by_percent,cost=player.now_cost/10)
        ListOfPlayers.append(temp)

    if (len (ListOfPlayers) <250):
        print ("Cant Generate squad as we are in the middle of GW1")
        await session.close()

        sys.exit()

    top_performers = sorted(
        ListOfPlayers, key=lambda x: x.Eval(), reverse=True)


    topGoalies = GetRolesList(1,top_performers)
    topDefs = GetRolesList(2,top_performers)
    topMids = GetRolesList(3,top_performers)
    topAtk = GetRolesList(4,top_performers)


        # print(i.firstName, " ", i.cost)

    for i in topAtk:
        print(i.firstName)

    budget = 100


    req_gk = 2
    req_defs = 5
    req_mids = 5
    req_atks = 3
    req_sub_gk = 1
    req_sub_def = 1
    req_sub_mid = 1
    req_sub_atks = 1
    curr_N_gk =0
    curr_N_mid =0
    curr_N_def =0
    curr_N_atk =0

    for i in top_performers:
        print(i.firstName)


    print("tf")
    squad = []

    while(len(squad) < 15):

        if curr_N_mid < req_mids:

            while True:
                print ("stucm")

                selPlayer = topMids.pop(0)
                if budget - selPlayer.cost >= 0and IsIdInSquad(selPlayer.code,squad) == False:
                    squad.append(selPlayer)
                    budget -= selPlayer.cost
                    curr_N_mid += 1
                    break
                elif len (topMids) >0:
                    continue
                elif len(topMids) <=0:
                    #backtracking
                    targetCell = GetMinimumEval(squad)
                    if (squad[targetCell].Role == 1):
                        curr_N_gk -= 1
                    if (squad[targetCell].Role == 2):
                        curr_N_def -= 1
                    if (squad[targetCell].Role == 3):
                        curr_N_mid -= 1
                    if (squad[targetCell].Role == 4):
                        curr_N_atk -= 1
                    cost = squad[targetCell].cost
                    budget+=cost
                    print(len(squad), "before")
                    squad.remove(squad[targetCell])
                    print(len(squad), "afer")
                    topMids = GetRolesList(3,top_performers)



        if curr_N_atk < req_atks:

            while True:
                print ("stucj")
                selPlayer =       topAtk.pop(0)
                if budget - selPlayer.cost >=0 and IsIdInSquad(selPlayer.code,squad) == False:
                    squad.append(selPlayer)
                    budget-=selPlayer.cost
                    curr_N_atk+=1
                    break
                elif len(topAtk) > 0:
                    continue
                elif len(topAtk) <= 0:
                    # backtracking
                    targetCell = GetMinimumEval(squad)
                    if (squad[targetCell].Role == 1):
                        curr_N_gk-=1
                    if (squad[targetCell].Role == 2):
                        curr_N_def -= 1
                    if (squad[targetCell].Role == 3):
                        curr_N_mid -= 1
                    if (squad[targetCell].Role == 4):
                        curr_N_atk -= 1
                    cost = squad[targetCell].cost
                    budget += cost
                    squad.remove(squad[targetCell])
                    topAtk= GetRolesList(4,top_performers)



        if curr_N_def < req_defs:

            while True:

                selPlayer = topDefs.pop(0)
                if budget - selPlayer.cost >= 0 and IsIdInSquad(selPlayer.code,squad) == False:
                    squad.append(selPlayer)
                    budget -= selPlayer.cost
                    curr_N_def += 1
                    break
                elif len(topDefs) > 0:
                    continue
                elif len(topDefs) <= 0:
                    # backtracking
                    targetCell = GetMinimumEval(squad)
                    if (squad[targetCell].Role == 1):
                        curr_N_gk -= 1
                    if (squad[targetCell].Role == 2):
                        curr_N_def -= 1
                    if (squad[targetCell].Role == 3):
                        curr_N_mid -= 1
                    if (squad[targetCell].Role == 4):
                        curr_N_atk -= 1
                    cost = squad[targetCell].cost
                    budget += cost
                    squad.remove(squad[targetCell])

                    topDefs = GetRolesList(2,top_performers)
        if curr_N_gk < req_gk:

            while True:
                print ("stucj")
                selPlayer =       topGoalies.pop(0)
                if budget - selPlayer.cost >=0 and IsIdInSquad(selPlayer.code,squad) == False:
                    squad.append(selPlayer)
                    budget-=selPlayer.cost
                    curr_N_gk+=1
                    break
                elif len(topGoalies) > 0:
                    continue
                elif len(topGoalies) <= 0:
                    # backtracking
                    targetCell = GetMinimumEval(squad)
                    if (squad[targetCell].Role == 1):
                        curr_N_gk-=1
                    if (squad[targetCell].Role == 2):
                        curr_N_def -= 1
                    if (squad[targetCell].Role == 3):
                        curr_N_mid -= 1
                    if (squad[targetCell].Role == 4):
                        curr_N_atk -= 1
                    cost = squad[targetCell].cost
                    budget += cost
                    squad.remove(squad[targetCell])
                    topGoalies= GetRolesList(1,top_performers)

    print("done")

    for i in squad:
        print(i.firstName, "  ", i.Role)

    print(budget)
    await session.close()

asyncio.run(main())
