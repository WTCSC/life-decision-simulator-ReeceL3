from time import sleep

print("Welcome to choose your own adventure")

# First question
question1 = input("What do you do when you get out of bed? Would you like to [1] Play clash royale or [2] Take a shower: ")

if question1 == "1":
    # If you played clash royale
    question2 = input("You may have played some clash royale but you are late for school. Do you [1] Brush your teeth or [2] Run to school because you're late: ")

    if question2 == "1":
        print("You brushed your teeth quickly, but now you're EXTRA late. Your grumpy teacher gives you detention!")
    elif question2 == "2":
        print("You sprint to school and barely make it on time. You're tired, but at least you avoided detention but your teacher is grumpy.")
    else:
        print("That wasn't a valid option.")

elif question1 == "2":
    # If you took a shower
    question2a = input("You smell good for school but you are late. Do you [1] Brush your teeth or [2] Beg your mom to take you because you missed the bus: ")

    if question2a == "1":
        print("You brushed your teeth and feel fresh, but you missed the bus. You have to walk, and you're late anyway and now you have to deal with your grumpy teacher.")
    elif question2a == "2":
        print("Your mom drives you to school just in time. You smell great and avoided detention but ur not so lucky you have to deal with your grumpy teacher")
    else:
        print("That wasn't a valid option.")
else:
    print("That wasn't a valid option.")

# Question 3 (always happens since teacher is grumpy)
question3 = input("With your grumpy teacher do you [1] prank him or [2] ask to go to the bathroom since you couldn't use it before school: ")

if question3 == "1":
    question3a = input("Now you're in even more trouble and now you have detention. In detention do you [1] be a good boy and do what you're told or [2] just don't go to detention: ")

    if question3a == "1":
        print("You made it past detention but now you have to go home and deal with your parents.")
    elif question3a == "2":
        print("You go home but your parents got a call that you skipped detention.")
    else:
        print("Not a valid option.")

elif question3 == "2":
    question3b = input("Your teacher says no and now you really are in trouble. Do you [1] leave the room to go to the bathroom or [2] pee your pants: ")

    if question3b == "1":
        print("Since you decided to leave the room and go to the bathroom anyways you were marked absent and now your parents are gonna be mad when you get home because they got a call.")
    elif question3b == "2":
        print("Now that you have succesfully peed yourself in school you have angry parents who don't really wanna pick you up but have to since you can't hold it in.")
    else:
        print("Not a valid option.")
else:
    print("Not a valid option.")

# Question 4 (home with angry parents)
question4 = input("You get home and now your parents are super mad at you because of what you did at school. Do you [1] fight back with them or [2] accept your fate: ")

if question4 == "1":
    question4a = input("You were never gonna win that fight with your parents. Do you [1] keep talking back or [2] go to your room and be a good boy: ")

    if question4a == "1":
        print("Well you are grounded now and they have installed cameras in your room so your fate is sealed.")
    elif question4a == "2":
        print("Your parents are proud of you for owning your actions but you're still grounded for the rest of the day so you aren't gonna do anything worse.")
    else:
        print("Not a valid option.")

elif question4 == "2":
    question4b = input("You have accepted your fate and you go to your room, but you're a rebellious kid. Do you [1] jump out of your window or [2] sneak out of your room and find your phone: ")

    if question4b == "1":
        print("You broke your ankle and now you're grounded till your ankle heals up.")
    elif question4b == "2":
        print("You successfully snuck out of your room but your parents noticed your phone was gone and caught you. You are now grounded for a month. GGS.")
    else:
        print("Not a valid option.")

else:
    print("Not a valid option.")

