from HelperMethods import*

class ChapterTwo:

    def reset():
        pass

    #WHen the player wakes up the next day
    def wakeUp():
        print("\n\n-------------Chapter Two------------\n\n")
        print("\n March 3rd 1872----------")
        print(" You wake up the next day in the room the sheriff has allocated you. It is a nice and"+
        "\n cozy room. A bit small for your taste , but it will get the job done. Beside your bed there are drawers"+
        "\n which you think will come in handy because you won't be able to fit that many items in your backpack."+
        "\n You get yourself cleaned up and get ready to find the sheriff to start this \"interrogation\""+
        "\n process. But first you want to make sure you have everything you need...")

    #When we meet sheriff for interrogation
    def meetSheriffInterrogation():
        print("\n\n You arrive at the sheriff's building. Cooper is casually sat at his desk ravaging"+
        "\n through a pile of paperwork. You tell yourself you've got no time to waste and decide to interrupt him."+
        "\n\n You : I'm really sorry to interrupt you Cooper but we've got to get going. Your town is"+
        "\n slowly dying."+
        "\n\n Cooper : Yes I know Levi, that's why we're starting the interrogation process now. The thing"+
        "\n is, I didn't want to go overboard with my \"methods\" so I only \"convinced\" four people to help."+
        "\n\n You : FOUR PEOPLE ?!! What am I supposed to do with FOUR PEOPLE ?! Cooper, your town is dying !"+
        "\n\n Cooper : And you think I don't know that ?! Just do your job properly and we'lle be fine."+
        "\n\n You : There is a difference between doing my job and working miracles Cooper."+
        "\n\n Cooper : *chuckles* look Levi , you don't have a choice."+
        "\n\n You : Well without me, your town is as good as dead. So maybe it's time you start giving me a choice ?!"+
        "\n\n Cooper : Follow me, I'll take you to the interrogation room."+
        "\n\n You : You didn't answer my question..."+
        "\n\n Cooper : I'm aware.\n\n")

    #When we follow Cooper into the interrogation room
    def interrogation():
        print("\n\n Cooper : Today you will be talking to Bill , Stacy, Clara and Buck. Four people, as we agreed. "+
        "\n\n You : \"agreed\"."+
        "\n\n Cooper : Quit the attitude princess. Get to work."+
        "\n\n Cooper leaves the room. You sit down on the chair"+
        "\n in front of you. You gesture for the first person to sit down on the other side of the glass panel "+
        "\n that seperates you from them. \n\nIt's time to interrogate.\n\n")

    def interrogationGame():
        game = True
        options = ["Where are you from ?",
        "Do you know how you got the disease ?",
        "How have you been feeling lately ?",
        "Do you know how long you have left ?"
        ]
        print("\n\n\n---------- The interrogation game ----------")
        print("You're trying to find out four things about this disease : where it came from, "+
        "\n how it spreads , the symptoms , and how long does an untreated person have to live."+
        "\n Each person will reveal one of these things.")
        while game:
            print("\n\n\n The first person comes in : "+
            "\n Bill : ..."+
            "\n\n You : Hiya there Bill, I'm going to ask you a few questions okay ?"+
            "\n\n Bill : It would be nice if you could be less condescending while your at it."+
            "\n At least let me live my final days with a high self esteem."
            "\n You : ....")
            decision = HelperMethods.makeDecision(options)
            if decision == "Do you know how long you have left ?":
                print("\n\n Bill : Well , my cousin Martha got the disease herself and died within three weeks."+
                "\n That's why I'm afraid I won't be able to live for too long."+
                "\n\n You : I'm really sorry to hear that. I'll try my best to find a cure."+
                "\n\n Bill : Hurry up then.")
                game = False
            else:
                print("\n\n Bill : Why should I talk to a condescnending man."+
                "\n\n You : Oh grow up will you ?! I'm only trying to help!"+
                "\n\n Bill : Maybe we don't need your help ?!"+
                "\n\n Bill storms up and leaves. This didn't go as planned...........")
                continue
        game = True
        while game:
            print("\n\n\n The second person comes in : "+
            "\n\n Stacy : HI! ARE YOU A DOCTOR ?!"+
            "\n\n You : Yes I am."+
            "\n\n Stacy : Nice to be somewhere where there's a doctor for a change!!!")
            decision = HelperMethods.makeDecision(options)
            if decision == "Where are you from ?":
                print("\n\n Stacy : I'm from the North East, my family travelled all the way"+
                "\n down here a few months ago actually. This town is a dump though, "+
                "\n me and my father have been ill since we got here, my mother luckily has been fine though!"
                "\n\n You : ...Good to know")
                game = False
            else:
                print("\n\n Stacy : WHY DID YOU DECIDE TO BEOCOME A DOCTOR ?"+
                "\n\n You : Stacy please remain focu"+
                "\n\n Stacy : TIME FOR LUNCH, I HAVE TO GO!"+
                "\n\n This didn't go as planned..........")
                continue
        game = True
        while game:
            print("\n\n\n The third person comes in : "+
            "\n\n Clara : Can we get this over with. I have places to be."+
            "\n\n You : I'm trying to save your life..."+
            "\n\n Clara : And I'm trying to enjoy it.")
            decision = HelperMethods.makeDecision(options)
            if decision == "Do you know how you got the disease ?":
                print("\n\n Clara : I'm convinced the northener gave it to me."+
                "\n\n You : You mean Stacy's dad ?"+
                "\n\n Clara : Yes."+
                "\n\n You : How ?"+
                "\n\n Clara : It was the night after we \"got to know each other\". "+
                "\n\n You : Is he not married ?!"+
                "\n\n Clara : Yes."+
                "\n You : ? "+
                "\n Clara : ?")
                game = False
            else:
                print("\n\n Clara : UGH! This is obviously going to be a waste of my time."+
                "\n Goodluck Mr.Docor , I'm out."+
                "\n\n You : WAIT!"+
                "\n\n Clara left the room... this didn't go well.......")
                continue
        game = True
        while game:
            print("\n\n\n The fourth person comes in : "+
            "\n\n Buck : Hello there."+
            "\n\n You : How have you been feeling lately ?"+
            "\n\n Buck : Well, ever since I got this disease I have been really cold and vomiting a lot."+
            "\n To the point that recently it's gotten so bad that the constant vomiting"+
            "\n is causing me to starve."+
            "\n You : So just the vomiting then ?"+
            "\n Buck : Yes."
            "\n\n You : Thanks Buck.")
            game = False

        print("\n\n\n\n Afterwards you go and meet Cooper in his office."+
        "\n\n You : Good news! I know what I need to know!"+
        '\n\n Cooper : Nicely done! What was that thing you said about working miracles ?'+
        "\n\n You : Oh, shut up will you!")
