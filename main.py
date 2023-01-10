print(" fill in the blanks with the missing Lyrics!")
print()
counter =0
while True:
  lyrics=input("---- around,every now an then i get a little bit lonely.")
  if lyrics =="Turn" or lyrics=="turn":
    print("You got it Congrats")
  else:
    print("Try again...")
  counter +=1
  if lyrics =="Turn" or lyrics=="turn":
    break
  print("Thank you for playing.")
print("It only took you",counter,"Tries!")
  