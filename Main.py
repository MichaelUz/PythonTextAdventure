from HelperMethods import*
from Locations import*

from ChapterOne import*
from ChapterTwo import*
from ChapterThree import*
from ChapterFour import*
from ChapterFive import*

game = True
chapter = True

while game:
    while chapter:
        #Chapter 1 -----------------------------------------------------------
        ChapterOne.Introduction()
        HelperMethods.makeDecision(["Save town"])
        #Arriving at Durango
        ChapterOne.durangoArrival()
        #Looking for the sheriff
        while not HelperMethods.booleansCH1["meetSheriffDA"]:
            if not HelperMethods.booleansCH1["womenDA"] and not HelperMethods.booleansCH1["clinicDA"]:
                townDecision = HelperMethods.makeDecision(["Go to women" , "Go to clinic" , "Confront man"])
            else:
                townDecision = HelperMethods.makeDecision(["Go to women" , "Go to clinic" , "Confront man", "Go to building"])
            if townDecision == "Go to women":
                ChapterOne.goToWomen(HelperMethods.booleansCH1["womenDA"])
            elif townDecision == "Confront man":
                fight = ChapterOne.confrontMan(HelperMethods.booleansCH1["confrontManDA"])
                if fight == "enemy":
                    ChapterOne.reset()
                    continue
            elif townDecision == "Go to clinic":
                ChapterOne.gotToClinic(HelperMethods.booleansCH1["clinicDA"])
            elif townDecision == "Go to building" and (HelperMethods.booleansCH1["womenDA"] or HelperMethods.booleansCH1["clinicDA"]):
                ChapterOne.gotToBuilding()
                chapter = False
                print("\n\n-----------------------------------------------------------------------\n"+
                "                            END OF CHAPTER ONE"+
                "\n\n-----------------------------------------------------------------------")

    HelperMethods.askContinue()
    chapter = True

    while chapter:
        #Chapter 2-----------------------------
        ChapterTwo.wakeUp()
        Locations.freeRoam("Sheriff's building" , "room")
        ChapterTwo.meetSheriffInterrogation()
        Locations.freeRoam("Interrogation room" , "Sheriff's building")
        ChapterTwo.interrogation()
        ChapterTwo.interrogationGame()
        print("\n\n-----------------------------------------------------------------------\n"+
        "                            END OF CHAPTER TWO"+
        "\n\n-----------------------------------------------------------------------")
        chapter = False

    HelperMethods.askContinue()
    chapter = True

    while chapter:
        #Chapter 3-----------
        ChapterThree.wakeUp()
        Locations.freeRoam("Sheriff's building" , "room")
        ChapterThree.meetSheriff()
        Locations.freeRoam("bar" , "Sheriff's building")
        ChapterThree.meetJack()
        Locations.freeRoam("cabin" , "bar")
        end = ChapterThree.cabin(False)
        if end == "end":
            ChapterThree.reset()
            print("\n\n\n                      GAME OVER")
            continue
        if HelperMethods.booleansCH3["Fought"]:
            Locations.freeRoam("bar" , "Clear Springs")
        else:
            Locations.freeRoam("Town Square" , "Clear Springs")
            ChapterThree.noFight()
            Locations.freeRoam("cabin" , "Town Square")
            ChapterThree.cabin(True)
            Locations.freeRoam("bar", "Clear Springs")
        ChapterThree.talkToJack("story")
        print("\n\n-----------------------------------------------------------------------\n"+
        "                            END OF CHAPTER THREE"+
        "\n\n-----------------------------------------------------------------------")
        chapter = False

    HelperMethods.askContinue()
    chapter = True
    while chapter:
        #Chapter 4----------------
        ChapterFour.wakeUp()
        Locations.freeRoam("Sheriff's building" , "room")
        ChapterFour.meeting()
        Locations.freeRoam("room" , "Town Square")
        ChapterFour.secondWakeUp()
        Locations.freeRoam("Sheriff's building" , "room")
        ChapterFour.secondMeeting()
        Locations.freeRoam("room" , "Town Square")
        print("\n\n March 7th 1872----------"+"\n\n You wake up the next day.\n\n")
        Locations.freeRoam("Sheriff's building" , "room")
        ChapterFour.thirdMeeting()
        Locations.freeRoam("Western Hills" , "Sheriff's building")
        ChapterFour.WesternHills()
        Locations.freeRoam("Town Hall" , "Western Hills")
        ChapterFour.TownHall()
        ChapterFour.receiveSupplies(True)
        Locations.freeRoam("room" , "Town Hall")
        ChapterFour.room()
        Locations.freeRoam("Town Hall" , "Town Square")
        ChapterFour.receiveSupplies(False)
        Locations.freeRoam("room" , "Town Hall")
        print("\n\n Tomorrow , someone will answer for what they've done.")
        print("\n\n-----------------------------------------------------------------------\n"+
        "                            END OF CHAPTER FOUR"+
        "\n\n-----------------------------------------------------------------------")
        chapter = False

    HelperMethods.askContinue()
    chapter = True
    while chapter :
        #Chapter 5-----
        print("\n\n\n\n\n\n-----------------------------------------------------------------------\n"+
        "                            THE FINAL CONFRONTATION"+
        "\n-----------------------------------------------------------------------")
        decision = ChapterFive.wakeUp()
        if decision == "Confront Cooper":
            ChapterFive.Cooper()
        elif decision == "Confront Jack":
            ChapterFive.Jack()
            ChapterFive.duel()

        print("\n\n\n\n\n\n------------------------------------------------------------------------------------------------\n"+
        "                                           THE END"+
        "\n------------------------------------------------------------------------------------------------")
        HelperMethods.askContinue()
        chapter = False
        game = False
