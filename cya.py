name = input("Type Your Nickname.   ")
print("Hello", name, "Welcome To This Adventure!")

answers = input("You are at the crossroad, but there is two sides, the left or right. Which would you choose:   ").lower()

if answers == "left":
    answers = input("You come across old gray house with a doorbell. You ring the bell and a man will hockey mask opens the door. Do You stay or run away:   ")
    if answers == "stay":
       input("Now You Must Fight To The Death. You have the options to choose a weapon. Sword or Super Shogun Mode. Which would you choose:   ")
       if answers == "Sword":
        print("Good Choice, Let's Fight!!!!")
       elif answers == "Super Shogun Mode":
          print("Power Of The Ancestors!!!")

    elif answers == "Run":
         input("You Live To Fight Another Day! You Must Now Walk 100FT. Do Run or Fly:")
         if answers == "Run":
            print("Now You Are Offf")
         elif answers == "Fly":
            print("FLY LIKE THE EAGLE!!!!")
    else:
        print("Not a Vaild Choice")
elif answers == "right":
    input("You see a bridge of a river. The bridge is old and falling apart. Do you walk the bridge or stay for help: ")
    if answers == "walk":
       input("You made it over the bridge. It is very late. Do you set up camp or keep walking:  ")
       if answers == "Set up camp":
          input("Now you can rest. What is the first thing that you are doing. Making a Fire or Finding Food?  ")
          if answers == "fire":
             print("Fire is Ready.")
          elif answers == "food":
             print("Pick Your Meal.")
    elif answers == "Stay":
       print("You Pussy")


else:
  print("You Made A Mistake,  YOU LOSE DUMMY!!!!")