import random

die1 = random.randint(1,6)
die2 = random.randint(1,6)
die3 = random.randint(1,6)

print(f'Die1 {die1}')
print(f'Die2 {die2}')
print(f'Die3 {die3}')

if die1 == die2 and die2 == die3:
  print('three of a kind')
elif die1 == die2 or die2 == die3 or die1 == die3:
  print('1 pair')
else:
  print('better luck next time')
