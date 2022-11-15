fan = input("Are you a fan of LOST? ")
if fan.lower() == 'yes':
  print("How cool is that! I love that show.")
  print("Let's see if you are really a fan.")
  air_date = input("What year did the show first air? ")
  if (air_date == '2004'):
    print("That's correct!")
    actor = input("Okay, one more question. What actor played the character James 'Sawyer' Ford? ")
    if actor.lower() == "josh holloway":
      print("Wow! You ARE a super fan.")
    else:
      print("Sorry, that's not correct. You must not be a fan")
  else:
    print("Sorry, that's not correct. You must not be a fan")
else:
  print("Bummer! It's such a great show. You should give it another chance.")