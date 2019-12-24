from Fighter import*

from random import*

class HelperMethods:
    #Keep track of a lot of booleans
    booleansCH1 = {"womenDA": False,
    "meetSheriffDA" : False,
    "confrontManDA" : False,
    "clinicDA" : False
    }

    booleansCH3 = {"metSheriff" : False
    ,"metJack" : False , "Fought" : False , "talkJack" : False
    }

    booleansCH4 = {"thirdMeeting" : False}
    #Keep track of our inventory
    inventory = {"weapons" : [], "other" : []}
    drawers = {"weapons" : [] , "other" : []}

    #Create a Fighter for our player
    myFighter = Fighter("Levi" , 100 , 10 , "")

    #adds a new weapon to our inventory
    def addToWeapons(weapon):
        HelperMethods.inventory["weapons"].append(weapon)

    #This method asks the player to continue
    def askContinue():
        valid = False
        while not valid:
             if input("Type : \"c\" and press enter : \n") == "c" :
                 valid = True
             else:
                 print("Sorry that wasn't a valid command...\n")

    #This method asks you to make a decision takes an array of string represting the options
    def makeDecision(options):
        valid = False
        while not valid:
            if not options:
                print("Looks like they're no options...")
                return""
            index = 1
            print("You have a decision to make...\n")
            for option in options:
                print(str(index) + " - " + option)
                index+= 1

            decision = input()
            if decision in options:
                return decision
            else:
                print("Sorry that wasn't a valid command...\n")

    #This method handles a fight between you and someone else
    def Fight(player , enemy):
        fight = True
        turn = True
        dodge = False
        prob = -1
        print("\n\n A fight has started !")
        while fight:
            print("\n Your health : " + str(player.health))
            print(" Enemy's health : " + str(enemy.health))
            if turn:
                print("\nWill you fight or try and dodge the ennemy's attack ? : \n")
                fightDecision = HelperMethods.makeDecision(["Fight" , "Dodge"])
                if fightDecision == "Dodge":
                    prob = randint(0,1)
                    print(prob)
                    dodge = True
                    turn = False
                    continue
                print("It's your turn to fight. Pick a weapon.\n")
                decision = HelperMethods.makeDecision(HelperMethods.inventory["weapons"])
                if decision == "":
                    print("\nYou throw a viscous punch.\n")
                elif decision =="gun":
                    print("\n\nYou take aim and shoot\n\n")
                elif decision == "knife":
                    print("\n\n You stab the ennemy\n\n")
                player.weapon = decision
                damage = player.giveDamage()
                enemy.health -= damage
                turn = False
                print("Oof, the enemy took " + str(damage) + " damage!")
            else:
                print("\nIt's the enemy's turn to fight!\n")
                if dodge and prob ==1:
                    turn = True
                    dodge = False
                    prob = -1
                    print("\nWell I'll be damned! The enemy attacked but he missed!\n")
                    continue
                damage = enemy.giveDamage()
                player.health -= damage
                turn = True
                print("Oof, you took " + str(damage) + " damage!")
            if player.health <=0 :
                print("\n\nThe wild west isn't for everyone. You died.\n\n")
                player.reset(100, 10 , "")
                return "enemy"
            if enemy.health <=0 :
                print("\n\nYou won the fight !\n\n")
                return "player"

    # This method helps us transfer an item from drawers to bag
    def transferToBag():
        print("\n Is the item you want to transfer a weapon ?\n")
        transferDecision = HelperMethods.makeDecision(["weapons" , "other"])
        if transferDecision == "weapons":
            print("\n Which item is it ?\n")
            itemDecisionW = HelperMethods.makeDecision(HelperMethods.drawers["weapons"])
            if itemDecisionW == "" or itemDecisionW not in HelperMethods.drawers["weapons"] :
                return
            HelperMethods.drawers["weapons"].remove(itemDecisionW)
            HelperMethods.inventory["weapons"].append(itemDecisionW)
        elif transferDecision == "other":
            print("\n Which item is it ?\n")
            itemDecisionO = HelperMethods.makeDecision(HelperMethods.drawers["other"])
            if itemDecisionO == "" or itemDecisionWO not in HelperMethods.drawers["other"]:
                return
            HelperMethods.drawers["other"].remove(itemDecisionO)
            HelperMethods.inventory["other"].append(itemDecisionO)

    # This method helps us transfer an item from bag to drawers
    def transferToDrawers():
        print("\n Is the item you want to transfer a weapon ?\n")
        transferDecision = HelperMethods.makeDecision(["weapons" , "other"])
        if transferDecision == "weapons":
            print("\n Which item is it ?\n")
            itemDecisionW = HelperMethods.makeDecision(HelperMethods.inventory["weapons"])
            if itemDecisionW == "" or itemDecisionW not in HelperMethods.inventory["weapons"]:
                return
            HelperMethods.inventory["weapons"].remove(itemDecisionW)
            HelperMethods.drawers["weapons"].append(itemDecisionW)
        elif transferDecision == "other":
            print("\n Which item is it ?\n")
            itemDecisionO = HelperMethods.makeDecision(HelperMethods.inventory["other"])
            if itemDecisionO == "" or itemDecisionO not in HelperMethods.inventory["other"]:
                return
            HelperMethods.inventory["other"].remove(itemDecisionO)
            HelperMethods.drawers["other"].append(itemDecisionO)
