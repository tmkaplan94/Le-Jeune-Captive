screen hotel_room():
    imagemap:
        ground "champs-elysees.jpg"
        hover "champs-elysees.jpg"
        if camera_there:
            hotspot (315, 272, 275, 185) clicked Jump("hotel_camera")
        if notepad_there:
            hotspot (315, 272, 275, 185) clicked Jump("hotel_notepad")
        if receipts_there:
            hotspot (315, 272, 275, 185) clicked Jump("hotel_receipts")
        if drawer_there:
            hotspot (315, 272, 275, 185) clicked Jump("hotel_drawer")
        if laptop_there:
            hotspot (315, 272, 275, 185) clicked Jump("hotel_laptop")

init python:
    camera_there = True
    notepad_there = True
    receipts_there = True
    drawer_there = True
    laptop_there = True


label hotel:
    scene HotelLobby with fade

    show Jean at right with dissolve

    show Ciel_Dress at left with dissolve

    Jean "Must we really attend these silly parties? There must be better ways for you to advance your influence across France."

    Ciel "Oh, you are always so grumpy, ma moitié. It is not a silly party, but a formal gathering of the most important political and influential figures in all of France! This is a chance for us to make some beneficial relationships."

    Jean "Perhaps you may be right."

    Ciel "We are at the luxurious hôtel de luxe! If you will not enjoy the people, at least enjoy the food."

    Jean "The only thing I will enjoy is your presence. And…"

    Jean "...I think you are dressed beautifully today."

    Ciel "You flatter me, ma moitié. I chose this outfit out myself!"

    Ciel "Now come along, they are awaiting our arrival."

    Jean "Yes, ma moitié."

    Politician "If it isn't Ciel Rousseau! I haven't seen you in so long."

    Ciel "Oh, Politician, it is a pleasure to see you again. How have you been?"

    Politician "I have been great, just recently I --"

    Business_Person "Ciel! Nice to see you again! I see you're wearing the earrings from my company's latest jewelry line."

    Ciel "Business Person! Of course, the Argent Jewelry is a company that I truly admire."

    Jean "You are quite the popular figure. I will give you a chance to catch up with them and get something to drink."

    Ciel "You are too kind. I won't be too long, my love. I will see you soon."

    hide Ciel_Dress with moveoutleft

    Jean "I know myself that Ciel will be talking with politicians until the evening. It is alright, Ciel is advancing her career in her own way."

    Jean "Now to grab myself a drink."

    show Gaston at left with moveinleft

    question_marks "They always make me do these things..."

    Jean "That voice, I've heard it before… It is a most distasteful voice, if I recall correctly."

    Jean "That is politician Gaston Lacroix!  What business does he have here at a high profile party like this? As far as I know, he spends his time attaining all his influences by merely spending some money. Or some other illegal means."

    Jean "What strange behavior he is doing… He is constantly peering left and right, as if he is anxious of someone watching him."

    Jean "Or is he perhaps looking for someone?"

    "*ring ring*"

    Gaston "Baise moi, calling me so suddenly! I have to get out of here."

    Jean "He's leaving!"

    menu:
        "Follow Gaston Lacroix":
            jump hotel_phoneCall
        "Go back to Ciel":
            jump hotel_backToCiel

label hotel_backToCiel:

    Jean "I am suspicious, but there is no need to follow him. Ciel must be waiting for me."

    Jean "I will go back to her."

    hide Gaston with dissolve

    show Ciel_Dress at left with moveinleft

    Ciel "Jean!"

    Jean "I was just about to look for you."

    Ciel "I have terrible news! I...I have lost my other emerald earring!"

    Ciel "I must have dropped it outside. I will look for it right now."

    Jean "Be calm! Do not worry, Ciel. Continue to speak to the other guests. I will look for it."

    Ciel "You will?"

    Jean "Yes, now go along."

    Ciel "What would I do without you, ma moitié."

    Jean "And I without you. I will see you again shortly."

    Ciel "Farewell, I will see you soon."

    hide Ciel_Dress with moveoutleft

    Jean "Strange. Ciel had never been so into jewelry before, nonetheless, became frantic over it. "

    jump hotel_phoneCall

label hotel_phoneCall:

    scene HotelOutside with fade

    show Jean at left with moveinleft

    Jean "Now where do I look first…"

    Gaston "...bon sang, I'm doing my best! What can I do when she's always surrounded by people?"

    Jean "That voice… It sounds like Gaston Lacroix! It sounds like a shady phone call, I'll hide behind the corner of this wall and listen in."

    show Jean at right with move

    Gaston "My expertise is doing work behind the scenes, like messing with the poll results. You can't just stick me in such a high profile environment doing your work."

    Gaston "...no, no, I'm not defying you at all! It's just, you know, a bit difficult when Ciel is always seen in the public eye."

    Jean "'Ciel?!' What does he have to do with her? Gaston and Ciel have never spoken a word to one another."

    Gaston "...do not worry, everything will happen as planned. Ciel is acting as she should."

    Gaston "...yes, yes, I know. … Of course, I have it in my room. I will give it to you later tonight."

    Gaston "My room number? It is room 315. … Yes, understood. Now if you must excuse me, I must return back to the party. I already look suspicious merely attending it."

    Jean "Sounds like Gaston left to head back inside."

    Jean "But what in the hell was that conversation? Poll results? And Ciel?"

    Jean "I cannot even bear to comprehend the outrageousness of what I've just heard. His hotel room may give me some answers."

    hide Jean with moveoutleft

    jump hotel_hallway

label hotel_hallway:

    scene HotelHallway with fade

    show Jean at right with moveinright

    Jean "Now to look for Gaston's room."

    Jean "Hotel staff was kind enough to give me his room key. Well, with some of my political influence of course."

    Jean "Now what was the room number again...  Ah, yes, 315."

    Jean "I've checked the other hallways and they seem to be clear. If I turn right, the room should be down this hall."

    Jean "What?! There's a person right in front of room 315."

    Jean "That looks to be a familiar figure..."

    question_marks "Curses! I was planning on picking the lock but this door requires a key card!"

    Jean "Dammit."

    question_marks "Mon ami! To what pleasure do I have seeing you here?"

    Jean "Claude… What do you think you are doing here?"

    show Claude at left with dissolve

    Claude "Oh, I forgot my room key! I am just trying to get back in."

    Jean "Your lies do not work on me."

    Claude "You have caught me. As expected from my smart best friend!"

    Jean "Explain yourself."

    Claude "The owner of this room is Gaston Lacroix, who...you and I both know his infamous reputation. With the investigations of the recent poll tampering, the evidence pointed back to him."

    Claude "I did a few investigating on my own and discovered all of the recent travels he's gone to were the same destinations Ciel and I had traveled to these past few months. And to see that he's here today..."

    Jean "He's been following you two?!"

    Claude "Seems so."

    Jean "I've got to hand it to you, Claude. You're not as stupid as you seem you are."

    Claude "A rare compliment from my best friend!"

    Jean "And the only one at that. Move aside, I acquired a copy of the hotel key card for Gaston's room. It appears he's hiding something in here."

    Claude "My savior!"

    jump hotel_room

label hotel_room:
    scene HotelRoomMap with fade
    # this will be the image called HotelRoom (no items)
    # And then the pngs that will placed on it will be numbered in my image folder

    show Claude at left with moveinright
    show Jean at right with moveinright

    Claude "This room is a pigsty!"

    Jean "Even more so than your own."

    Claude "There must be some clues in here telling us what he has to do with Ciel."

    # Scene of a hotel room. In the hotel room there are receipts, a drawer, a camera, a notepad, and a laptop.

label hotel_investigation:
    call screen hotel_room

label hotel_drawer:

    $ drawer_there = False

    Claude "Find anything in the drawer?"

    Jean "Looks to just be some illegal substances."

    Claude "Oh, I must see it!"

    Jean "Mince, we have to keep searching, mec."

    jump hotel_investigation

label hotel_receipts:

    $ receipts_there = False

    Claude "What's this pile of crumpled papers?"

    Jean "It looks to be some receipts."

    Claude "Looks like Gaston's been shopping a lot at…'Argent Jewelry?'"

    Claude "Merde! These receipts are worth tens and thousands of dollars!"

    Jean "Diamond necklaces, gold bracelets...these purchases are ridiculous! And he also bought...emerald earrings?!"

    Claude "What is so shocking about emerald earrings?"

    Jean "Ciel was wearing a pair of emerald Argent earrings today!"

    if not laptop_there and not camera_there and not notepad_there:
        jump hotel_roomEnd

    jump hotel_investigation

label hotel_camera:

    $ camera_there = False

    Jean "A camera? This might have something to tell us."

    Claude "Turn it on, mec."

    Jean "This camera is filled with pictures of Ciel!"

    Claude "Dear lord. He seemed to be tailing her from a distance with all the angle of these shots."

    Jean "Looking at the dates of these pictures, you were right. He's been following her for months..."

    Jean "What could he possibly need pictures of Ciel for? Who is he sending them to?"

    if not laptop_there and not notepad_there and not receipts_there:
        jump hotel_roomEnd

    jump hotel_investigation


label hotel_notepad:

    $ notepad_there = False

    Claude "Good find! What does it say?"

    Jean "It says 'Stoney Clove Bakery 2:00 PM Tues,' 'Ble Sucre 9:00 AM Thur,' 'Boulangerie Croissant 7:00 PM Fri.'"

    Claude "Sounds like Gaston's been arranging meeting times with someone."

    Jean "..."

    Claude "Why do you look so bothered?"

    Jean "This is Ciel's handwriting."

    if not laptop_there and not camera_there and not receipts_there:
        jump hotel_roomEnd

    jump hotel_investigation

label hotel_laptop:

    $ laptop_there = False

    Claude "Good idea to check the laptop! Every suspicious person has something to hide in there."

    Jean "His email inbox is open."

    Jean "The emails are all titled 'Report' followed with a given timestamp."

    Jean "Gaston's been emailing someone named xmndjng@gmail.com. I suspect this is a throwaway email address."

    Claude "Read one aloud."

    Jean "'Report 5/16/xx 2:17 PM: Ciel is doing what was instructed. Looks like things are happening in our favor -Gaston'"

    Claude "Nom de dieu, what a vague and ominous email!"

    Jean "They're forcing Ciel to follow their commands? What are they making her do?!"

    Jean "Whoever they are, their identity is terrifyingly unknown. Gaston is responding to a mysterious authority figure. This problem may be bigger than we first thought."

    if not notepad_there and not camera_there and not receipts_there:
        jump hotel_roomEnd

    jump hotel_investigation

label hotel_roomEnd:

    scene HotelRoomMap with fade

    show Claude at left with dissolve
    show Jean at right with dissolve

    Claude "I can't believe this! Who are these people? Are they trying to control Ciel?"

    Jean "I share the same frustration."

    Claude "Investigating has brought more questions than answers."

    Claude "But what should we do? We need to tell Ciel!"

    Jean "We keep it from her for now. Ciel is under heavy surveillance and might even be in contact with them."

    Claude "..."

    Jean "I'm worried too. Do not look so serious, it doesn't suit you."

    Jean "We should return back to the party before Gaston comes back to his room."

    Claude "You're right. Let's leave this creepy room."

    Jean "I'll leave first."

    hide Jean with moveoutright

    jump hotel_lobby

label hotel_lobby:

    scene HotelLobby with fade

    show Ciel_Dress at left with dissolve
    show Jean at right with moveinright

    Ciel "Ma moitié! I have been looking all over for you."

    Jean "...Hello ma moitié."

    Ciel "Were you able to find my earrings?"

    Jean "No, I was not able to."

    Ciel "Merde."

    Jean "Do not worry, ma moitié. I will get you another pair."

    Ciel "No, that is much too expensive -- "

    Jean "Please. I insist."

    Ciel "...I do not deserve you."

    Jean "That is where you are wrong. I will always be here to help."

    Jean "From anything."
