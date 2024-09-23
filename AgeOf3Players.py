'''
It were the days of domination from the traditional metros in the team selections and everytime the team is announced for the Indian Squad, mere disappointment was left with this small town player. Dhoni’ill fate continued even during the team selections for the India A squad to tour to Zimbabwe.3 new players from Mumbai were on the list for the Indian team and it was claimed by the selectors that Dhoni was a bit younger than the 3 selected players.
  Assume the 3 players are Named X,Y and Z. The ages of the players X and Y are the same and the age of the Z is 10 more than other 2 players. Given the total age of the 3 players, find the age of the 3 players.
Input format:
First line of the input is an integer that corresponds to the total age of the 3 players.
'''
total_age = int(input("Enter the total age of the 3 players: "))
# Calculate the age of player X and Y
age_x = (total_age - 10) // 3
age_y = age_x
age_z = age_x + 10
# Output the ages of the players
print("Age of Player X:", age_x)
print("Age of Player Y:", age_y)
print("Age of Player Z:", age_z)
'''
Enter the total age of the 3 players: 70
Age of Player X: 20
Age of Player Y: 20
Age of Player Z: 30
