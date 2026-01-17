🏏 Hand Cricket Game (Python)
A nostalgic, terminal-based implementation of the classic Hand Cricket (or Odd/Even) game. Built with Python, this project simulates a cricket match between a human player and a computer opponent using simple numerical inputs.

📝 Description
This project recreates the popular schoolroom game where players use their fingers (represented here by numbers 1-6) to score runs or take wickets. It includes a complete game loop: from the initial "Odd or Even" toss to determine who bats or bowls, through two innings of play, and finally calculating the winner based on the score difference.

✨ Features
Realistic Toss Logic: Decide who bats or bowls first using a randomized "Odd or Even" system.
Robust Input Validation: The game handles non-numeric inputs and numbers outside the 1–6 range without crashing.
Dynamic Innings: Supports both batting-first and bowling-first scenarios.
AI Opponent: A randomized computer logic that keeps the game unpredictable.
Clean CLI Interface: Easy-to-read score updates and game status messages.

🎮 How to Play
The Toss: * Choose "Odd" or "Even."
Enter a number between 1 and 6.
If the sum of your number and the computer's matches your choice (Odd/Even), you win the toss and choose to Bat or Bowl.

Batting: * Enter a number from 1 to 6.
If your number matches the computer's "ball," you are Out.
Otherwise, your number is added to your total score.

Bowling:
Try to guess the computer's number.
If your "ball" matches the computer's "run," the computer is Out.

Winning:
The player with the highest total score at the end of both innings wins!

🛠️ Code Structure
The project is organized into modular functions for better readability:
user_batting() / computer_batting(): Core logic for scoring runs and detecting "Outs."
user_batting_1() / computer_batting_1(): Wrapper functions to manage the sequence of the two innings and compare final scores.
Main Logic: Handles the toss and initiates the game flow based on the result.
