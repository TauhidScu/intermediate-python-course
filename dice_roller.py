import random

def main():
  dice_rolls = 2
  die_sum =0
  for i in range( 0, dice_rolls):
    roll = random.randint(1,6)
    die_sum = die_sum + roll
    print(f'You rolled a {roll}')   
  #By putting an f right before the quotes of the string you're printing
  print(f'you have rolled a total of {die_sum}')

if __name__== "__main__":
  main()