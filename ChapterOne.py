from HelperMethods import*

class ChapterOne:

    #resets the chapter
    def reset():
        for bool in HelperMethods.booleansCH1:
            HelperMethods.booleansCH1[bool] = not HelperMethods.booleansCH1[bool]

    def Introduction():
        print("------------ Chapter One of Five ------------")
        print("\nMarch 2nd 1872\n")
        print(" You're sat down in the grass looking over at the horizon. To your left your horse"+
        "\n Cassidy, drinks from a nearby lake." +
        "\n\n You think back to when you came here, to Clear Springs as a child with your father."+
        "\n You think back to how much you valued the time you two spent together." +
        "\n A strong warm breeze brings you back to reality. You whistle for Cassidy to get back and"+
        "\n and you get set to get back on your journey."+
        "\n\n You have a town to save after all.\n\n")

    def durangoArrival():
        print("\n You've arrived at Durango, a small quite forgetable town. But something tells you"+
        "\n you're not going to forget any part of this."+
        "\n\n It's the middle of the day so you'd think the town would be beaming with life at"+
        "\n this time of the day but the town was silent, eerily silent."+
        "\n Nothing but a few whispers and tumbleweed driven accross the main road by a breeze"+
        "\n that has gotten even warmer since when you left Clear Springs. You think to yourself"+
        "\n that the tumbleweed would be a cliché if this were fiction.\n")

        print(" The lack of activity in the town doesn't surprise you though as this is a town"+
        "\n recently plagued by a disease that no one is yet to understand."+
        "\n You're on your horse, in the middle of one of the town's main roads.\n"+
        "\n To your left there is a rather ordinary building with a bright yellow roof."+
        "\n You question the color choice."+
        "\n Not too far from this building a group of young women stand in a circle chatting"+
        "\n in front of what looks like a bar. An empty bar for that matter."+
        "\n To your right there is a large clinic. A man walks out vomiting violently with a"+
        "\n handkerchief to his mouth. He gives you a mean look and carries on." +
        "\n [Objective 1] : You need to find the sheriff of this town and start getting to work.\n\n")

    #If the player goes to talk to the women
    def goToWomen(hasBeen):
        HelperMethods.booleansCH1["womenDA"] = True
        if  not hasBeen:
            print("\n You go towards the women and ask them where the sheriff is."+
            "\n You : Excuse me ladies, I'm looking for the sheriff of this town."+
            "\n\n The women all look at each other with a puzzled look on their faces."+
            "\n Maybe they don't trust you..."+
            "\n\n...\n\n"+
            "\n One of the women breaks the silence."+
            "\n Woman : He is in that building over there with the fancy yellow roof."+
            "\n\n You : ...Thank you."+
            "\n\n As you leave you hear the other women angrily confront the woman who broke the awkward silence."+
            "\n They didn't appreciate the fact she told a stranger where the sheriff was.\n\n")
        else:
            print("\n Women: we've already spoken to you. Leave us alone!\n\n")

    #If the player decides to confornt the man
    def confrontMan(hasBeen):
        HelperMethods.booleansCH1["confrontManDA"] = True
        if not hasBeen:
            print("\n You try and catch up with the obviously sick man. He makes eye contact with"+
            "\n you but then quickly looks away. You quicken your pace and eventually catch up."+
            "\n\n You : Excuse me sir could"+
            "\n\n Man : NO.")
            decision = HelperMethods.makeDecision(["Leave", "Keep asking"])
            if decision == "Leave":
                print("You decide to leave.")
                return ""
            elif decision == "Keep asking":
                print("\n\n You : Sir I would really appreciate it if"+
                "\n Man : Are you blind, can't you see that I'm sick ? What part of \"NO\" did you not understand ?!"+
                "\n The man shoves you out of frustration."+
                "\n\n Instinctively, you shove him back."+
                "\n\n Man : ..."+
                "\n\n You : ...\n\n\n")
                Levi = HelperMethods.myFighter
                Man = Fighter("Man" , 30 , 5 , "")
                return HelperMethods.Fight(Levi,Man)
                print("\n\n You can't believe what you've just done. A man is dead. Because of you."+
                "\n Your heart starts racing. \"It was self defence... It was self defence\" you"+
                "\n repeat constantly to yourself. Time to find that sheriff.")
        else:
            print("\nThe man is gone... Time to find the sheriff.")

    #If the player decides to go to the clinic
    def gotToClinic(hasBeen):
        HelperMethods.booleansCH1["clinicDA"] = True
        if not hasBeen:
            print(" \n You approach the clinic and slowly open the main doors. That's when you"+
            "\n you see dozens of beds filled with ill people heavily outnumbering the amount"+
            "\n of nurses. You realize that until now, you hadn't quite grasped the severity of"+
            "\n the situation."+
            "\n\n \"Are you sick sir ?\" , said the nurse standing behind you."+
            "\n\n You : No, I'm actually looking for the sheriff. Could you point me towards him ?"+
            "\n\n Nurse : ..."+
            "\n\n You : ..."+
            "\n\n Nurse : WHO are you ?"+
            "\n\n You : I'm actually an old friend of the sheriff. He asked me to come help out with"+
            "\n\n your... epidemic. I'm a doctor."+
            "\n\n Nurse : Oh! He's in the building with the yellow roof. You can't miss it !"+
            "\n\n You : I won't..."+
            "\n\n You tell yourself that that encounter was weirder than it really needed to be."+
            "\n Time to find the sheriff, do your job , and get out of this town.")
        else:
            print("\nYou look at the clinic, the thought of all the sick people that were in there"+
            "\n reminds you that it's important you get on with your job. Now where is Mr.Sheriff...\n")

    #If the player decides to go to the building
    def gotToBuilding():
        HelperMethods.booleansCH1["meetSheriffDA"] = True
        print("\n You walk into the building, your eyes lock onto your old friend. You would've"+
        "\n never guessed he'd become a sheriff after all these years. Soon after he notices you."+
        "\n Sheriff : Hey hey hey! Nice to see you after all these years Levi!"+
        "\n Or is it Dr.Cornett nowadays ?"+
        "\n\n You : Nice to see you too Cooper. And most people still call me Levi."+
        "\n\n Cooper : Well I'll be Damned! Levi it is then. I'm surpried you found me...")
        print("\n\n I am as well to be honest. Why are people here so scared to give out information ?"+
        "\n\n Cooper : Because I told'em to."+
        "\n\n You : Okay ?")
        if HelperMethods.booleansCH1["confrontManDA"]:
            print("\n\n Cooper : Hold up right there mister , is that a scar on your fist ?"+
            "\n\n You : It was self defence."+
            "\n\n Cooper : No worries pal. Here is a gun, next time no need to scar your fists.")
            HelperMethods.addToWeapons("gun")
            print("\n---- You received a new item ! ---")
            print("\n\n You : ...I'll keep it as a last resort."+
            "\n\n Cooper : Oh hell no ! Don't be afraid to use it if anyone bothers you. If you won't,"+
            "\n I will. You can't save my town if your goddam DEAD. ")
        print("\n\n You : ...Anyways, I need to know the origin of this disease to be able to cure it."+
        "\n\n Cooper : You'll be able to interrogate some sick people."+
        "\n\n You : Now I'm surpried they agreed to be questioned on their personal lives by"+
        " a stranger."+
        "\n\n Cooper  : Having a gun to your head \"facilitates\" the decision process."+
        "\n\n You : Oh.")
