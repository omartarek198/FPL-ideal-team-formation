from fpl import FPL
import aiohttp
import asyncio
from Player import  *



async def main():
    session = aiohttp.ClientSession()
    fpl = FPL(session)
    players = await fpl.get_players()
    x = 1
    ListOfPlayers = []
    print (dir (players[0]))

    for player in players:
        temp =  Player(player.code,player.web_name,ln=player.first_name,totalPts= player.total_points,ptsPergame=player.points_per_game,
                       minutes=player.minutes,postion=player.element_type,selectedBy=player.selected_by_percent,cost=player.now_cost)
        ListOfPlayers.append(temp)

    for i in ListOfPlayers:
        print(i.firstName)

    await session.close()

asyncio.run(main())
