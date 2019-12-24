from HelperMethods import*
from ChapterThree import*

class Locations:

    #Keeps track of what room we're in and what room is exis state when in free roam
    state = ""
    exit = ""
    #In room
    def Room():
        print("\n\nYou're sat on your bed in your room...\n\n")
        room = True
        while room:
            options = ["Open drawers" , "Look in bag" , "Go Town Square" , "Transfer to bag", "Transfer to drawers"]
            decision = HelperMethods.makeDecision(options)
            if decision == "Go Town Square":
                return "Town Square"
            elif decision == "Look in bag":
                print(HelperMethods.inventory)
            elif decision == "Open drawers":
                print(HelperMethods.drawers)
            elif decision == "Transfer to bag":
                HelperMethods.transferToBag()
            elif decision == "Transfer to drawers":
                HelperMethods.transferToDrawers()

    #In the town square
    def townSquare():
        ts = True
        options = ["Go to Sheriff's building" , "Go to room"]
        print("\n\n The town square.. exactly as it was the last time you were here. The women are still chatting"+
        "\n in their little circle. The bar is still empty. The sheriff's building still has a very distinctive"+
        "\n yellow roof and that man you saw on your first day is still no where to be seen. Oh! And no "+
        "\n tumbleweed in sight.")
        while ts:
            if HelperMethods.booleansCH3["metSheriff"]:
                options.append("Go to bar")
            if HelperMethods.booleansCH3["metJack"]:
                options.append("Go to Clear Springs")
            if HelperMethods.booleansCH4["thirdMeeting"]:
                options.append("Go to Western Hills")

            decision = HelperMethods.makeDecision(options)

            if decision == "Go to Sheriff's building":
                return "Sheriff's building"
            if decision == "Talk to Sally" and HelperMethods.booleansCH3["metSally"]:
                return "Sally"
            if decision == "Go to room":
                return "room"
            if decision == "Go to bar":
                return "bar"
            if decision == "Go to Clear Springs":
                return "Clear Springs"
            if decision == "Go to Western Hills":
                return "Western Hills"

    # In Cooper's office
    def CooperOffice():
        co = True
        print(" \n\n You're stood in Cooper's office, in front of you there is his desk. Completely "+
        "\n covered in paperwork. To your left is a safe with probably the biggest lock you've ever seen."+
        "\n What could Cooper be hiding in there ? Weapons ?"+
        "\n To your right there is the door that leads to the interrogation room.")
        while co:
            options = ["Go to IR" , "Go Town Square"]
            decision = HelperMethods.makeDecision(options)
            if decision == "Go to IR":
                return "Interrogation room"
            if decision == "Go Town Square":
                return "Town Square"

    #In interrogation room
    def InterrogationRoom():
        ir = True
        print("\n\n The interrogation room in all it's glory. You wonder how Cooper got this place built."+
        "\n A large room divided in two by a wall size glass panel. A chair on each side. Fancy.")
        while ir:
            options = ["Go to Cooper's office"]
            decision = HelperMethods.makeDecision(options)
            if decision == "Go to Cooper's office":
                return "Sheriff's building"

    def bar():
        bar = True
        print("\n\n The bar empty as always. Well, except for Jack who's constant presence has made you come to terms with the fact"+
        "\n that he probably lives here.")
        while bar:
            options = ["Talk to Jack" , "Go Town Square"]
            decision = HelperMethods.makeDecision(options)
            if decision == "Talk to Jack":
                return ChapterThree.talkToJack("talk")
            if decision == "Go Town Square":
                return "Town Square"

    def ClearSprings():
        cs = True
        print("\n\n You get off your horse and stand admiring the beauty that is Clear Springs. You shove"+
        "\n old memories about your father away and focus on the task at hand. Right next to you lies your horse,"+
        "\n you look over to your right and notice a small cabin not too far away. That cabin and Durango"+
        "\n are the only man made structures in sight. The rest is just grass and hills. Just nature. As it"+
        "\n should be.")
        while cs:
            options = ["Go to cabin" , "Go to Durango"]
            decision = HelperMethods.makeDecision(options)
            if decision == "Go to cabin":
                return "cabin"
            if decision == "Go to Durango":
                return "Town Square"

    def cabin():
        cabin = True
        if HelperMethods.booleansCH3["Fought"]:
            print("\n\n Nothing but dead bodies here. You should leave before anyone sees you and adds two"+
            "\n and two together.")
        else:
            print("\n\n You need a weapon, can't go back there without one.")
        while cabin :
            options = ["Go to Clear Springs"]
            decision = HelperMethods.makeDecision(options)
            if decision == "Go to Clear Springs":
                return "Clear Springs"


    def WesternHills():
        wh = True
        print("\n\n The vibrant city of Silverstone. You're still shocked by how vibrant it is."+
        "\n Durango has really lowered your standards. The town hall is straight ahead.")
        while wh:
            options = ["Go to Town Hall" , "Go to Durango"]
            decision = HelperMethods.makeDecision(options)
            if decision == "Go to Town Hall":
                return "Town Hall"
            if decision == "Go to Durango":
                return "Town Square"

    def TownHall():
        th = True
        print("The Town Hall , where you uncovered everything. The leader's are here going about their"+
        "\n business.")
        while th:
            options = ["Go outside"]
            decision = HelperMethods.makeDecision(options)
            if decision == "Go outside":
                return "Western Hills"


    #This method allows us to free roam around the world
    def freeRoam(exit, initial):
        roam = True
        state = initial
        while roam:
            if state == "room":
                state = Locations.Room()
                if state == exit:
                    return
                if state != "room":
                    continue
            if state == "Town Square":
                state = Locations.townSquare()
                if state == exit:
                    return
                if state != "Town Square":
                    continue
            if state == "Sheriff's building":
                state = Locations.CooperOffice()
                if state == exit:
                    return
                if state != "Sheriff's building":
                    continue
            if state == "Interrogation room":
                state = Locations.InterrogationRoom()
                if state == exit:
                    return
                if state != "Interrogation room":
                    continue
            if state == "bar":
                state = Locations.bar()
                if state == exit:
                    return
                if state != "bar":
                    continue
            if state == "Clear Springs":
                state = Locations.ClearSprings()
                if state == exit:
                    return
                if state!= "Clear Springs":
                    continue
            if state == "cabin":
                state = Locations.cabin()
                if state == exit:
                    return
                if state != "cabin":
                    continue
            if state == "Western Hills":
                state = Locations.WesternHills()
                if state == exit:
                    return
                if state != "Western Hills":
                    continue
            if state == "Town Hall":
                state = Locations.TownHall()
                if state == exit:
                    return
                if state!= "Town Hall":
                    continue
