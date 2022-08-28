# FPL-ideal-team-formation
## Used the offical premier league api to retrive all players data.
### Evaluated the players based on :
#### Total points scored by the player
#### Total minutes played by the player
#### The percantage of other users who selected the player
#### The cost of the player 
### Constraints ( Rules of the squad )
#### There has to be 15 players in total
#### Budget for squad is 100 million
#### Cannot select more than 3 players from the same team in the squad

### Using the previous data, and using the BackTrack algorithm, the following squad was generated. 


<img width="596" alt="fpl" src="https://user-images.githubusercontent.com/87566788/187094366-719c224c-c73e-4ca4-b568-bfe5ea7ef118.png">


### The algorithm chose this squad with no human factor involved and ended up scoring 7 points higher than average and ranking 3.4 million out of 9+ million players


## Important note : the api for FPL resets it's player data every new season and this squad was selected based on the data from season 2021/2022, as a result, same code might generate different squad later
