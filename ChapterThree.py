from HelperMethods import*
from Fighter import*

class ChapterThree:

    #resets the chapter
    def reset():
        for bool in HelperMethods.booleansCH3:
            HelperMethods.booleansCH3[bool] = not HelperMethods.booleansCH3[bool]

    def wakeUp():
        print("\n\n-------------Chapter Three------------\n\n")
        print("\n March 4th 1872----------")
        print("\n\n Well yesterday was eventful. After the interrogation you and Cooper caught up"+
        "\n on a lot of things. He's changed a lot since you last saw him. He's rutheless and will"+
        "\n protect this town at all costs, and maybe that's a good thing for the people of this town.")

    def meetSheriff():
        print("\n\n Cooper : There he is! The MIRACLE WORKER!"+
        "\n\n You : Very funny. So what's the plan for today ?"+
        "\n\n Cooper : Today you'll meet Jack. The best detective in this darn town."+
        "\n\n You : My guess is he's the only one ?"+
        "\n\n Cooper : Let Jack ask the questions and we should be fine. You'll find him at the bar.")
        HelperMethods.booleansCH3["metSheriff"] = True

    def meetJack():
        HelperMethods.booleansCH3["metJack"] = True
        print("\n\n You arrive at the bar, it's mostly empty and very quiet. Jack won't be hard to find."+
        "\n You quickly find Jack and walk towards him. You tell yourself that he's shorter than what you imagined."+
        "\n He's sat at his stool whirling his drink in his glass with a defeated expression on his face."+
        "\n You tell yourself that this really doesn't look like the best time to bother him, but you don't"+
        "\n really have a choice."+
        "\n\n You : Are you Jack ?"+
        "\n\n Jack : *Cough* *Cough* Maybe. Depends on who's asking."+
        "\n\n You : I'm asking, and so is the Sheriff."+
        "\n\n Jack : Jack Rivens. Nice to meet you doc."+
        "\n\n You : How'd you"+
        "\n\n Jack : You're not the only one here that knows the Sheriff."+
        "\n\n You : It would seem so. Well we need your help. It has to do with the disease that's slowly killing this town."+
        "\n\n Jack : Not my problem."+
        "\n\n You : Not mine either, but you don't see me spending my days drinking alone at a bar feeling"+
        "\n sorry for myself."+
        "\n\n Jack: *chuckles* I like your style doc. Tell you what. If you help me , I'll help you."+
        "\n\n You : Depends on what sort of help you're talking about."+
        "\n\n Jack : Some people over at Clear Springs have owed me money for a long time now I need you to"+
        "\n \"take care of them\" for me."+
        "\n\n You : You want me to murder people because they havn't paid you back ?"+
        "\n\n Jack : Would you rather pay me on their behalf then ? It's only a few thousands."+
        "\n\n You : You people have a wicked sense of humour."+
        "\n\n Jack : I'm not forcing you to do anything. Just don't expect me to help."+
        "\n\n You : The thing is Jack. I don't like killing people. So you'll have to think of something else."+
        "\n\n Jack : There is nothing else."
        "\n\n You take a deep breath and wonder what you're going to do now. Yo're not a murderer."+
        "\n You're not capable of murdering someone and feeling completely fine afterwards."+
        "\n\n \"Well .........it's just one job. Do it and get it over with\", you tell yourself."+
        "\n If you don't do this, the entire town will die. And you know you'll blame yourself for it."+
        "\n You pick your poison and decide you'll do it."+
        "\n\n Jack : ... *cough cough* \"This darn disease\" , Jack mumbles under his breath."+
        "\n Look. You deal with them, and I'll help you. Deal ?"+
        "\n\n You : ..."+
        "\n You : Deal."+
        "\n\n As you get ready to leave you realize you really don't know that much about Jack."+
        "\n Maybe you can spare some time and talk to him.")

    def cabin(back):
        if not back:
            print("\n\n You arrive at the cabin, you figured the people that live here are probably the people"+
            "\n that Jack was talking about. You stand in front of the cabin's door. The cabin was small and white"+
            "\n it had marks on its wooden walls that suggested the cabin was old. You inspect further and notice"+
            "\n holes in the walls... Are those bullet holes ?")
            if not HelperMethods.inventory["weapons"]:
                print("\n WHAT ARE YOU THINKING ?! You don't have a gun ?! But then again, you NEED jack's help.")
                decision = HelperMethods.makeDecision(["Fight" , "Leave"])
                if decision == "Leave":
                    print("\n\nYou tell yourself you're not quite ready and leave.")
                    return""
            else :
                print("\n You realize that this will be harder than what you thought it would be.")
        print("\n\n You take a deep breath and knock on the cabin door."+
        "\n A lanky man walks out the door."+
        "\n\n Lanky Man : Who the hell are ya ?!"+
        "\n\n You : Jack sent me. You owe him money , do you have it ?"+
        "\n\n Lanky Man : Uh... I have no idea what your talking about. "+
        "\n\n You : If that's how it's going to be. I have no choice but to use violence."+
        "\n\n Lanky Man : *Facing inside the cabin* Guys come over here!"+
        "\n\n Two men appear behind the lanky man."+
        "\n\n Lanky Man : Don't try anything funny, it's three against one. Walk away while you still can."+
        "\n\n\n              ...           ")
        cabin = True
        while cabin:
            print("\n\n You : I'm afraid that isn't an option."+
            "\n\n Lanky Man : Good. The only one that should be afraid here is you. We'll make it quick.")
            Levi = HelperMethods.myFighter
            Man = Fighter("Man1",60,5,"gun")
            for i in range(0,3):
                Man.reset(60,5,"gun")
                winner = HelperMethods.Fight(Levi , Man)
                if winner == "player" and i == 2:
                    cabin = False
                    break
                elif winner == "enemy":
                    decision = HelperMethods.makeDecision(["Try Again" , "Give Up"])
                    if decision == "Give Up":
                        return "end"
                    break
        HelperMethods.booleansCH3["Fought"] = True
        print("\n\n As soon as the adrenaline dies down, you come to terms with fact that"+
        "\n you've killed people that had nothing to do with you. You got your hands dirty"+
        "\n for someone else. Your heart starts racing. You quickly look for your horse. You "+
        "\n need to clear your mind.")
        print("\n\n Time to leave before anyone sees you.")
        return "won"

    def noFight():
        print("\n\n You're just being sensible. What are you supposed to do ? This is literally worse"+
        "\n than bringing a knife to a gun fight. You stand there wondering what you're going to do now."+
        "\n You notice the same women you saw on the first day. You approach them and think to yourself"+
        "\n that there is nothing to lose"+
        "\n\n You : Excuse me ladies, sorry to disturb you. I need a weapon."+
        "\n\n Woman : That is a very odd thing to ask for. Especially to people you don't even know."+
        "\n\n You : I don't have that much time."+
        "\n\n Woman : Who are you killing ?"+
        "\n\n You : I never said I was killing anyone. I just want one to protect myself. As a last resort"+
        "\n of course."+
        "\n\n Woman : ... Fair enough , the best I can do is a knife though, my guns are at home."+
        "\n\n You : I'll take whatever I can get. Thank you."+
        "\n\n ------ You received a new item ------\n\n")
        HelperMethods.addToWeapons("knife")
        print("Time to go fight those bandits... with a knife.")

    def talkToJack(reason):
        if reason == "story":
            print("\n\n You walk back into the bar like a man on a mission. You quickly find Jack and"+
            "\n sit down on the stool next to him."+
            "\n\n You : Your friends have been taken care of."+
            "\n\n Jack : Nicely done doc. Me and the Sheriff will meet you tomorrow at his office."+
            "\n\n You : The Sheriff knew about this ?!"+
            "\n\n Jack : He's the one that asked for it.")
        elif not HelperMethods.booleansCH3["talkJack"] and not HelperMethods.booleansCH3["Fought"] :
            print("\n\n You walk over to Jack and sit down next tom him."+
            "\n\n You : I know we have a town to save , but unlike Cooper I don't know you."+
            "\n If I do as you say, and we end up on the same team. I need to know who you are"+
            "\n and what's your deal."+
            "\n\n Jack : Well, I'm Jack Rivens. I have been a detective in this town for the past"+
            "\n *cough* *cough* four years."+
            "\n\n You : Four years ? How'd you find this place."+
            "\n\n Jack : *cough* You'll have to *cough* excuse my coughing. I've been hit by this"+
            "\n disease as well. That's why I don't care what happens. I'll die soon anyway."+
            "\n But to answer your question doc, no I'm not from here. I was called here by the sheriff to investigate a robbery"+
            "\n but the investigation went south. We couldn't find the culprits. The worst part is they're"+
            "\n probably still here. Living their lives as if everything was normal. They escaped justice."+
            "\n\n You : If they haven't been any major robberies since then I guess it shouldn't really"+
            "\n be that much of an iss"+
            "\n\n Jack : You better shut that trap of yours before I change my mind about the little"+
            "\n deal we have. People escaped justice. It's the first case I've failed. It IS a very"+
            "\n BIG issue doc."+
            "\n You : If I were you I'd let it go. You can't change the past."+
            "\n Jack : Trust me doc , I've let it go. I'm dying soon anyway."+
            "\n\n You :What about if you got saved by a cure. Would you stay here or do you plan"+
            "\n on leaving at some point."+
            "\n\n Jack : Cooper has been good to me. It wouldn't be right if I left."+
            "\n\n You : So you do have morals after all."+
            "\n\n Jack : *chuckles* We're not all crazy down here doc.")
            HelperMethods.booleansCH3["talkJack"] = True
            return "bar"
        else:
            print("\n\n You've already spoken to him, no need to bother him now.")
            return "bar"
