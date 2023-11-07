# Sequential Auction
Welcome to the Sequential Auction Game! This is a dynamic and strategic game where players compete to acquire the most items through a series of auction rounds.
## Game Overview

In each round of the game, players place bids to win an item. The highest bidder in each round secures the item. However, strategy is key, as your budget in one round carries over to the next. Thus, spending too much in a single round can hinder your bidding power in subsequent rounds.
## Objective

The primary objective is to accumulate the highest number of items by the end of the game. The player with the most items at the conclusion of all rounds is declared the winner.
## Gameplay

- Number of Players: There are **k** players participating in the game-
- Number of Rounds: The game consists of **N** rounds, with one item available for auction in each round.
- Budget: Each player **i** starts with a budget of **s<sub>i</sub>**. This budget is used to place bids (**b<sub>i</sub>**) in each round.
- Bidding: The player who places the highest bid in a round wins the item. Bids are secret, and the amount bid is deducted from the player's total budget.
- Carryover: Unspent budget from one round carries over to the next, allowing for strategic financial management across rounds.
- Tie-Breaking Condition: In the event of a tie, the player with the lowest index wins the item. The index is randomly assigned to each player at the start of the game.

## Strategy

A known weakly dominating strategy for this game occurs under the condition where all players have the same amount of budget. In such a scenario, the weakly dominating strategy is to bid b<sub>i</sub> = s<sub>i</sub> * (k / N) for every round.

## Get Started
![image](https://github.com/SophomoreSo/SequentialAuction/assets/57844175/9e38b7e7-fe77-4a7b-be43-de7ba4b0688a)

Install the following packages via pip
```
pip install pyqt5
```
1. Click 'New Game', and then you can set the number of rounds `N` and the number of players `k`.
2. Double-click the table widget to manipulate the game data, such as scores and budgets.
3. Press 'Start Game' to begin. You can view the remaining rounds in the top right corner.
4. If the game ends, you can start over by clicking 'New Game'.
