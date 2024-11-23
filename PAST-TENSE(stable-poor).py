def askCabinet():
     try:
        drawNo = int(input("Choose a drawer by entering 1, 2, or 3: "))
        return drawNo
     except ValueError:
        print("Invalid input. Please enter a number between 1 and 3.")
        cabinet() # Restart the cabinet function if input is invalid

def chCabinet2(ans):
    if ans == "bookshelf":
         bookshelf()  # Proceed to the bookshelf section
    else:
        while ans!="bookshelf":
            print("That's not quite right. Perhaps think about what Alistair likes to do in his free time.")
            ans=input()
        else:             
             chCabinet2(ans)
cipher1=""
clue1=0
def cabinet():
   
    # user to choose a drawer
    c=askCabinet() 
    global cipher1
    if c == 1:
        print("The drawer is filled with random papers.Taking a closer look, you realise that one if them is a torn page from alistair's journal.")
        print("There are those who write stories to entertain, and then there are those who write to unmask the human soul. Agatha Christie does both with such elegance that one wonders if she wasn’t, in truth, an investigator masquerading as a novelist.\nHer characters are archetypes, yes, but never caricatures. Each carries a piece of the puzzle: a hidden pain, a forbidden desire, or a carefully buried sin. She reminds us that everyone is capable of deceit—not out of malice, but out of fear. Fear of being seen, fear of losing something they hold dear. It is that fear I look for in every case.\nChristie’s true genius lies not in her twists but in her truths. The culprit, more often than not, is someone you thought you understood. Someone you trusted. It is a lesson I have learned the hard way and one I am doomed to relearn with every betrayal.\n‘The truth, however ugly it may be, is always curious and beautiful to the seeker.’ Poirot said that once, and I’ve carried it with me ever since. If there is beauty in solving a crime, it is not in the revelation of guilt but in the restoration of order to a fractured world.\nBut there is one thing Christie never taught me: what happens when you cannot trust your own instincts? When the story you are reading begins to twist in ways even you cannot foresee? What then? Perhaps that is the final mystery—the one even she could not solve.\n—Alistair Quinn, Journal Entry #47")
        print("As interesting as this journal entry seems to be, you quicky realise that it doesn't seem to tell you what you really need-more information about the last case he was working on, to figure out why he disappeared.Undeterred, you decide to search another drawer.")
        cabinet()
        # Placeholder for any further storyline or hints
    elif c == 2:
        print("You find a file about a case that you never knew existed, which is odd since you're usually the one who takes care of all the paperwork.")
        print("Curious, you open the file and are met with a jumble of unintelligible letters.However, working with Alistair fro so long has made you familiar to his methods. The script is evidently a cipher of some sort, one that you will have to decode when you figure out the key.You decide to keep the file with you until then.")
        cipher1="Apzawp le 'Esp Glfwe' dppx wtvp espj vyzh dzxpestyr."
        print("However, something that confuses you is the utter lack of case details in the file.No suspects, no witnesses, no locations-nothing. The only things you found were the encrypted sentence and another riddle.")
        print(cipher1,"\nYou decide to keep it aside for later")
        # Ask for the answer to the riddle
        ans = input("Solve the riddle:\n'I stand against the wall, but I'm not a piece of art.\nI hold many stories, but I don't speak a word.\nI carry knowledge, yet I have no mind of my own.\nWhat am I?'").strip().lower()
        chCabinet2(ans)          
    elif c== 3:
             print("Unfortunately,the drawer is locked tight.")
             cabinet()
             # Placeholder for any further storyline or hints
    elif c not in [1,2,3] :
             print("Oops!There are only 3 drawers. Please try again")
             cabinet()
def caesarCipherDecrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
           
            base = ord('A') if char.isupper() else ord('a')
            decrypted_text += chr((ord(char) - base - shift) % 26 + base)
        else:
            
            decrypted_text += char
    return decrypted_text



def bookshelf():
    def askBookshelf():
        global clue1
        print("Moving towards the bookshelf, you find a letter nestled among the jumbled books.")
        print("Agatha Christie’s work always intrigued me, not just for the cleverness of her mysteries, but for how she portrayed her characters. In her stories, the true killer is often the person closest to us—someone we trust, someone we think we know. But there’s a deeper truth: the one we should fear most is often the one we’ve chosen to ignore—the part of ourselves we refuse to confront.\nChristie understood this well. The murderer often walks right beside us, unseen, even by themselves. But what happens when you look in the mirror and realize the killer is staring back? That the secrets you’ve buried, the guilt you refuse to acknowledge, are the very things that hold you captive?")
        print("Shaking off the sudden chills that seem to creep down your spine, you decide to press on further.You decide to examine the oddly jumbled books.Two of them seem to stand out to you.")
        c=input("Do you want to examine the 'Agatha Christie' or 'Sherlock Holmes'?").strip().title()
        if c=="Agatha Christie":
            print("You open the book to find a little hollowed-out space containg a worn-out picture,a small key and an envelope, containg a folded piece of paper.")
            print("You open the little chit, expecting it contain a hint on how to solve the cipher.As expected, you're met with a riddle.\n\n'I am not alive, but I can grow.\nI do not have lungs, but I need air.\nWhat am I?'\nBelow it, you find the sentence-'Add the letters of the answer to find the shift.'")
            print("Realising it's a simple caesar cipher, you get to work making the key.")
            def cipherAsk():
                global cipher1
                shift=input("What is the shift?(Enter the number you get when you add the letters of your answer completely)")
                txt=input("Considering the shift, what letter does 'A' correspond to?").lower()
                if shift== "11" and txt=="l":
                    clue1=caesarCipherDecrypt(cipher1,11)
                    print(cipher1,"Decrypts to",clue1)
                    
                    print("You realise that the picture is of a familiar street, known for housing a notorious mafia.")  
                    print("Bolstered by your recent victory, you decide to go there, since you've exhauseted the clues you could find here.")
                    street()
                elif shift=="11" and txt!="l":
                    print("Youre not sure about the answer youve got, but..",caesarCipherDecrypt(cipher1,10))
                    print("Perhaps count from the first letter after 'A'?")
                    cipherAsk()
                else:
                    print("Youre not sure about the answer youve got, but..",caesarCipherDecrypt(cipher1,int(shift)))
                    print("Perhaps count again?Think of something that's really hot.")
                    cipherAsk()
            cipherAsk()    

           
        elif c=="Sherlock Holmes":
            print("Your mentor has long since admired another iconic detective. Maybe try another book? ")
            askBookshelf()
        else:
            print("Hmm, that book doesn't seem to be out of place.")
            askBookshelf()        
    print("You approach the bookshelf, trying to make out if anything looked different. You notice that a couple books have been placed hapazhardly, a far cry from the usual level of organisation you expected from Alistair.")
    # Placeholder for bookshelf storyline or riddle
    askBookshelf()
paranoia = 0
overconfidence = 0
self_doubt = 0
def exploreBar():
    global paranoia
    print("Inside, the air is thick with smoke and tension. Shadows move against dim walls, and hushed conversations pause as you step in.The bartender gives you a fleeting glance before returning to his task. In the far corner, a group of men watches you with thinly veiled interest.")
    paranoia = 1
    print("\n(Your paranoia increases:",paranoia)
    print("You think back to everything you've done to reach this point. What should you do next?\n"
        "1. Approach the bartender to ask subtle questions.\n"
        "2. Eavesdrop on the group in the corner.\n"
        "3. Examine the bar for anything connected to Alistair.\n")
    ch = input("What do you do? (Enter 1, 2, or 3): ").strip()
    if ch=="1":
                     
        bartenderInteraction()
    elif ch == "2":
        eavesdropOnGroup()
    elif ch == "3":
        searchForClues()
    else:
        print("Invalid choice. Please try again.")
        exploreBar()
def bartenderInteraction():
    global overconfidence
    print("Your curiosity overtakes you, and you decide to question the one person in the room who you think you can overcome. The bartender.")
    overconfidence+=1
    print("You walk up to him confidently.'I'm looking for someone,' you say, keeping your voice low.\n"
        "He wipes the counter slowly, avoiding eye contact. 'You’re not the first to ask,' he mutters. 'But asking too much in this place gets people hurt.'\n"
        "You notice his hand tremble slightly before he points to the corner group. 'They might know more than me,' he says before walking away hurriedly.")
    print("\n(Your overconfidence increases:",overconfidence)
    groupFight()
def groupFight():
    global overconfidence
    print("You think of how smooth your investigation has been till now. You pat yourself on the back for improving so much, and go over to the group dominating the tiny bar.Striding up to them, you don't realise how much you've ****** up until the leader approaches you.")
    overconfidence+=1
    print("\n(Your overconfidence increases:",overconfidence)
    print("Still high on your feeling of overconfidence,you speak with much less tact than usual, and end up in a situation you never thought you'd find yoourself in- a bar fight.")
    c=input("Do you:\n1.Believe in your abilities and attempt to win so you can extract information?\n2.Try to escape even though you've been spotted?\n3.Lie and say you're there to join them?")
    end(c)
def eavesdropOnGroup():
    global paranoia,overconfidence
    print(
        "\nYou position yourself near the corner group, pretending to be absorbed in the old photographs on the wall. "
        "You catch snippets of their conversation: '...too curious...' and '...just like the last one.'\n"
        "Suddenly, one of them turns and looks directly at you. You try to look away, but it’s too late. They know you’ve been listening.\n"
    )

    paranoia += 1
    overconfidence+=1
    print(f"\n(Paranoia increases: {paranoia}, Overconfidence increases: {overconfidence})\n")
    print("You've been noticed!")
    c=input("Do you:\n1.Believe in your abilities and attempt to bluff so you can extract information?\n2.Try to escape even though you've been spotted?\n3.Convince yourself that you haven't done anything,and give up? ")
    end(c)
def searchForClues():
    global paranoia, self_doubt
    print(
        "\nYou move through the bar, inspecting the walls, shelves, and tables for anything unusual. Behind the bar, you spot a photograph of Alistair with someone unfamiliar. "
        "Just as you lean closer to examine it, a voice behind you growls, 'Looking for something?'\n"
        "You turn to see one of the men from the corner group, his expression cold and calculating. 'You’re drawing a lot of attention,' he says ominously."
    )

    
    self_doubt+= 2
    print(f"\n(Paranoia increases: {paranoia}, Self-doubt increases: {self_doubt})\n")
    print("You find yourself questioning everything. All your decisions till now seem to choke you. Are you really as good of a detective as you thought you were?")
    c=input("Do you:\n1.Believe in your abilities and attempt to bluff so you can extract information?\n2.Try to escape even though you've been spotted?\n3.Give yourself up and accept your fate as a failure of a detective? ")
    end(c)
    
def end(n):
    global paranoia, overconfidence, self_doubt

    print(
        "\nThe tension is suffocating. You feel eyes on you from every corner of the room. Each sound—the creak of the floorboards, the clink of glasses—feels amplified. "
        "The weight of your own thoughts bears down on you, and Alistair’s warning echoes in your mind: 'Trust no one—not even yourself.'"
    )

    if n=="2":
        paranoia+=1
        print("\n(Your paranoia increases:",paranoia)
        selfSabotage("paranoia")
    elif n=="1":

        print("\n(Your overconfidence increases:",overconfidence)
        selfSabotage("overconfidence")

    elif n=="3":
        self_doubt+=1
        print("\n(Your self-doubt increases:",self_doubt)
        selfSabotage("self-doubt")
    elif ord(n)>=48 and ord(n)<=57:
        print(
            "You have a choice to make:\n"
            "1. Confront the group directly and demand answers.\n"
            "2. Leave the bar quietly, regrouping outside.\n"
            "3. Double down and search for more clues, no matter the risk.\n"
        )
        choice = input("What do you do? (Enter 1, 2, or 3): ").strip()

        if choice == "1":
            confrontGroup()
        elif choice == "2":
            leaveBar()
        elif choice == "3":
            doubleDown()
        else:
            print("Invalid choice. Please try again.")
            end(choice)

    else:
        c=input("Enter a number")
        end(c)

def selfSabotage(reason):
    if reason == "paranoia":
        print(
            "\nYour paranoia consumes you. Convinced that everyone in the bar is watching your every move, you lash out. "
            "But your erratic behavior only confirms their suspicions. The group corners you, and before you realize it, you find yourself looking at the knife in your hand and a dead body at your feet.\n"
            "It wasn’t them—it was you. Your inability to trust, to stay composed, has undone you.\n"
            "You have become a murderer, one of the things you swore to destroy.Not only have you ruined yourself as a detective, you have now fallen to the point of no redemption."
        )
    elif reason == "overconfidence":
        print(
            "\nYour overconfidence leads you to confront the group without a plan. They were waiting for this moment, and you walked right into their hands. "
            "'Alistair warned us you’d be this reckless,' one of them says with a smirk. 'He always said you’d be your own undoing.'\n"
            "You realize too late that your determination to prove yourself, your no-fail attitude has betrayed you.\n"
            "Before you realise it, you you find yourself looking at the knife in your hand and a dead body at your feet.\n"
            "You have become a murderer, one of the things you swore to destroy.Not only have you ruined yourself as a detective, you have now fallen to the point of no redemption."
        )
    elif reason == "self_doubt":
        print(
            "\nYour self-doubt paralyzes you at the worst possible moment. Second-guessing every move, you hesitate when action is needed most. "
            "The group watches as your uncertainty betrays you. One of them chuckles darkly, 'Alistair told us you'd hesitate. Said you'd crumble under the weight of your own indecision.'\n"
            "You realize, too late, that your inability to trust your instincts has become your greatest weakness. In trying to avoid mistakes, you made the most fatal one of all—doing nothing."
        )
        
    gameOver()

def confrontGroup():
    print(
        "\nYou confront the group, demanding to know what they know about Alistair. They exchange knowing glances before their leader stands. "
        "'Alistair told us about you,' he says, his tone mocking. 'Said you’d come looking and make all the wrong moves.'\n"
        "You realize too late that every choice you made played into their hands."
    )
    selfSabotage("paranoia")

def leaveBar():
    print(
        "\nYou leave the bar, but the feeling of being watched doesn’t leave you. Footsteps echo behind you, growing louder. "
        "Before you can react, someone grabs your shoulder. 'Alistair said you'd be predictable,' a voice sneers. "
        "You realize that in trying to stay safe, you’ve led them right to you."
    )
    selfSabotage("self_doubt")

def doubleDown():
    print(
        "\nDetermined to find answers, you ignore the growing tension and keep searching. But your persistence draws attention, and before long, "
        "the group has surrounded you. 'You should have left while you had the chance,' their leader says. "
        "You realize your own tenacity has sealed your fate."
    )
    selfSabotage("overconfidence")

def gameOver():

    print(
        "\n*** GAME OVER ***\n"
        "Your decisions and the traits you developed throughout your journey have led to this moment. "
        "In your quest for the truth, you became blind to the dangers—or worse, you became your own greatest threat.\n"
    )
    replay = input("Do you want to restart from the beginning? (yes/no): ").strip().lower()
    if replay == "yes":
        resetGame()
        cabinet()
    else:
        print("Thank you for playing!")

def resetGame():
    global paranoia, overconfidence, self_doubt
    paranoia = 0
    overconfidence = 0
    self_doubt = 0


def street():
   
    
    print("You reach the street and match the location you saw in the picture.Looking around, you find a dingy old sign advertising a bar called 'The Vault'")
    a=input("Do you want to:\n1. investigate further?\n2. Leave what's done alone and move on?").strip()
    if a=="1":
        
        print("Realising that this is what your mentor meant,you slide your key into the lock, ready to investigate.")
        print("Your earlier successes fill you with a sense of confidence. You remember the photograph and the cipher—everything led you here. But something feels off.Did you miss something? Or is this exactly what they wanted you to do?")
        exploreBar()
    else:
        gameOver()     

    

ascii_art = (
            "██████╗  █████╗ ███████╗████████╗    ████████╗███████╗███╗   ██╗███████╗███████╗\n"
            "██╔══██╗██╔══██╗██╔════╝╚══██╔══╝    ╚══██╔══╝██╔════╝████╗  ██║██╔════╝██╔════╝\n"
            "██████╔╝███████║███████╗   ██║          ██║   █████╗  ██╔██╗ ██║███████╗█████╗  \n"
            "██╔═══╝ ██╔══██║╚════██║   ██║          ██║   ██╔══╝  ██║╚██╗██║╚════██║██╔══╝  \n"
            "██║     ██║  ██║███████║   ██║          ██║   ███████╗██║ ╚████║███████║███████╗\n"
            "╚═╝     ╚═╝  ╚═╝╚══════╝   ╚═╝          ╚═╝   ╚══════╝╚═╝  ╚═══╝╚══════╝╚══════╝"
        )
print(ascii_art+"\n")

print("It had been weeks since Alistair Quinn, your mentor and partner in unraveling the darkest of mysteries, vanished without a trace. You’ve replayed that night in your mind countless times—the faint knock on his office door, the hurried rustle of papers, and the ominous warning he left before walking out.\nTrust no one—not even yourself.\nThe words hung in the air, heavy and cryptic. Quinn was always enigmatic, but this...this was different. There was no goodbye, no explanation, only a void where his presence used to be. His office remains untouched, a shrine to his brilliance and the secrets he carried.")
print("Now, you are left with nothing except a note pinned to the door of his office.\n")
print("I stand tall and wide with drawers to spare,\nOrganizing papers with diligent care.\nThough my shape is simple, I’m quite the clue,\nFor inside me, you’ll often find two by two\nMy purpose is dual—store and sort, it’s true.")
print("Below it, you find the letters A,B,C,E,I,N,T, giving you a nudge in the right direction.Where do you think you have to go?")
def intro():
    n=input()
    if n=="cabinet":
        print("You hurry over to the cabinet in the corner and are met with 3 drawers.")
        cabinet()
    else:
        intro()
intro()
