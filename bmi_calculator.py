import time
print("\n------------------------------------------------------------------------")
print("                Welcome to ZumTheZazaKing's BMI Calculator!               ")
print("------------------------------------------------------------------------")

def main():

  time.sleep(3)

  try:
    height = float(input("\nEnter your height in meters: "))
  except:
    print("""
          \nYou're not suppossed to do that.\n
As Punishment, you'll automatically be kicked from the transaction.\n
          """)
    time.sleep(3)
    exit()
  try:
    weight = float(input("\nEnter your weight in kilograms: "))
  except:
    print("""
          \nYou're not supposed to do that.\n
As Punishment, you'll automatically be kicked from the transaction.\n
          """)
    time.sleep(3)
    exit()
  
  bmi = round(weight/(height ** 2), 2)
  ans = [ "\nYou're BMI is {}. You are underweight. You should eat more.\n",
          """\nYou're BMI is {}. Congratulations!
You are normal, like how a NORMAL human is supposed to be.\n
          """,
          "\nYou're BMI is {}. You're overweight. Go on a diet already.\n",
          "\nYou're BMI is {}. You're obese. Sayonara.\n"
          ]

  time.sleep(3)

  if bmi <= 18.5:
      try:
          print(ans[0].format(bmi))
      except:
          print("An error occured during the process. Please call the creator.")
  elif 18.5 < bmi <=24.9:
      try:
          print(ans[1].format(bmi))
      except:
          print("An error occured during the process. Please call the creator.")
  elif 25.0 < bmi <= 29.9:
      try:
          print(ans[2].format(bmi))
      except:
          print("An error occured during the process. Please call the creator.")
  else:
      try:
          print(ans[3].format(bmi))
      except:
          print("An error occured during the process. Please call the creator.")

while True:
    main()
    time.sleep(2)
    if str(input("""Would you like to calculate again?
(Type Y(Yes) or N(No))\n
""")).strip().upper() != "Y":
      print("\nGoodbye!\n")
      time.sleep(1)
      break








