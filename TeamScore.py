'''
Extras are runs scored by a means other than a batsman hitting the ball. A batsman is not given credit for extras other than runs scored off the bat from a no ball, and the extras are tallied separately on the scorecard and count only towards the team’s score. the types of extras are No ball, Wide, Bye, Leg-bye and Penalty. 1 Penalty corresponds to 5 runs.
Find the total runs that the Extras contribute to the team’s score, given the number of No-balls, wides, byes, leg-byes and penalty given off by the bowlers in innings.
Input format:
First line of the input contains an integer that corresponds to the number of No-balls.
Second line of the input contain an integer that corresponds to the numbers of wides.
Third line of the input contains an integer that corresponds to the number of byes.
Fourth line of the input contain an integer that corresponds to the numbers of led-byes.
Fifth line of the input contains an integer that corresponds to the numbers of penalty runs.
'''
no_balls = int(input("Enter the number of No-balls: "))
wides = int(input("Enter the number of Wides: "))
byes = int(input("Enter the number of Byes: "))
leg_byes = int(input("Enter the number of Leg-byes: "))
penalty_runs = int(input("Enter the number of Penalty runs: "))
total_extras = (no_balls + wides + byes + leg_byes + (penalty_runs * 5))
print("Total runs contributed by Extras:", total_extras)
'''
4
7
3
10
3
39
