import random

def main():
  dice_size = int(input('How many dice would you like to roll? '))
  die_sum =0
  for i in range( 0, dice_size):
    roll = random.randint(1,dice_size)
    if roll == 1 :
      print(f'you rolld a {roll}! critical fail')
    elif roll == dice_size :
      print(f'you rolled a {roll}! critical success')
    else:
      print(f'you rolled a {roll}.')
    die_sum = die_sum + roll
  
  print(f'you have rolled a total of {die_sum}')

if __name__== "__main__":
  main()