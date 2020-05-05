# BlackJack

**Design and Implementation:**
The first method, Intro, informs the player about the rules of the game and asks whether they want to play. The next method, BlackJack, begins by printing the amount of coins the player has. It then deals by randomizing 2 numbers between 1 and 10 and adding them to UCards, or user's cards, and CCards, or computer cards. The program proceeds to ask the player if they would like to hit; if accepted, Hit is then added to UCards and a total sum higher than 21 results in a bust. Whenever the player stops hitting, the computer takes its turn. If the user has a closer total to 21, the computer will continue to Hit until it has a better score than the user or loses. The program terminates if the player coins reaches 0 or if the player quits.

**Challenges:**
Ensuring the user's decisions were within the rules of the game was difficult as they could stem off to several possiblities. These included the user not having enough coins to hit or having the option to hit if they did not exceed 21 points. Also, ensuring the computer (dealer) made intelligent decisions was another challenge.
