
screen transaction():
    imagemap:
        ground "bg transaction.jpg"
        hover "bg transaction2.jpg"
        if seal_there:
            hotspot (858, 92, 242, 178) clicked Jump("seal_found")
        if scratches_there:
            hotspot (1017, 418, 168, 106) clicked Jump("scratches_found")
        if amount_there:
            hotspot (333, 369, 285, 54) clicked Jump("amount_found")
        if date_there:
            hotspot (260, 258, 304, 48) clicked Jump("date_found")

init python:
    seal_there = True
    scratches_there = True
    amount_there = True
    date_there = True

label tresor_nationale:

    scene bg office with fade

    show Jean at center with dissolve

    Jean "Finally…"

    Jean "Ah merde! Is it already past 12? Ciel will have m-"

    "*RING RING RING*"

    Jean "Who’s calling me?"

    Jean "... of course."

    Jean "What do you want?"

    Claude "Ah! Mon ami! I assume you are not busy?"

    Jean "Actually I-"

    Claude "Très bien! Come to La Femme Merveilleuse! You must simply try this spinach quiche! It is the most exquisite thing I have ever tasted! Besides of course-"

    Jean "Don’t finish that thought. Ciel and I had planned to get lunch at 12 and I’m already running behind."

    Claude "Then come join me! You know how long it takes for her to decide where to eat. Women, am I right or am I right?"

    Jean "There's the reason you’re single."

    Jean "...but you make a fair point. I’ll give her the option."

    Claude "Don’t forget to mention the quiche-"

    "*beep*"

    Jean " *sighs* Here we go..."

    "*beep beep beep*"

    Jean "Hello? Sorry I’m la-"

    Ciel "I can’t believe you! I’ve been starving for the past thirty minutes and only now do you respond? I sent you eight texts and you responded to none! NONE!"

    Jean "What? I didn’t get any..."

    Jean "Oh."

    Ciel "Ma moitié, I know you are working hard, but do you not remember our plans? We had planned to get lunch together..."

    Jean "Of course I remembered. I was just swamped is all. Not to mention that Claude called me about a quiche or something..."

    Ciel "Ooh a quiche! Good thing you mentioned that, I wouldn’t have known what to get!"

    Jean "Of course..."

    Jean "It’s called La Femme Merveilleuse. I just wanted to warn you that-"

    Ciel "Wonderful! I’ll see you there in fifteen!"

    Jean "Wait! Claude is-"

    Ciel "I love you!"

    "*beep*"

    Jean "*sighs*"

    Jean "I’d best hurry up then..."

    hide Jean with dissolve

    scene bg cafe with fade

    show Jean at right with moveinright

    Jean "Hah hah… Fifteen minutes is much too fast..."

    show Claude at left with dissolve

    show Ciel at center with dissolve

    Claude "...And then she dumped me on the spot. Women these days can’t appreciate a true gentleman, no?"

    Claude "It’s a shame, lovely lady she was. If only-"

    Claude "Ah! Look who decided to show up!"

    Ciel "Ma moitié! Look who happened to be here! Claude and I had a bit of a chat since you were so late!"

    Jean "I don’t think I’m late, I think you’re just too fast..."

    Jean "And besides, this wasn’t quite what I had envisioned for lunch..."

    Claude "What’s the harm mon ami? It has been a while since the three of us had a meal together!"

    Ciel "I haven’t had much time to spend with Claude recently. You wouldn’t mind would you? Perhaps I can pay you back tonight…?"

    menu:
        "But we had planned this...":
            jump sadge_restaurant

        "As long as it’s paid in full.":
            jump yikes_restaurant

label sadge_restaurant:

    Ciel "I know, I know. After such a busy week, we do deserve some time alone. Trust me, I want that as much as you, ma moitié. Though, it would mean a lot to me if we could spend some time with Claude, just like the old days."

    Claude "You remember the college days, no? Just us three, some shitty bar, and the world ahead of us!"

    Jean "You two..."

    Jean "Well I can’t say no to faces like that. Ciel, you’d better impress me tonight. And Claude, you’re paying."

    Claude "Huh???"

    Ciel "Don’t you worry, I’ve got a trick or two up my sleeve… Hehe~"

    Claude "I’d be worried if I were you, mon ami. Or very excited, depending on your speed."

    Jean "What’s she gonna do? Be my jetpack?"

    Ciel "Hey!"

    Claude "Ah, just like the good old days."

    hide Claude
    show Claude_flip at left

    Claude "Excuse me my dear, can I bother you for a moment? I’d like to order two spinach quiches and a round of mimosas."

    Claude "And your number too, if I may."

    jump continue_restaurant

label yikes_restaurant:

    Ciel "Daring today, are you? Then I’ll have a wonderful surprise for you tonight. I have the perfect outfit for the job. And a new set of lingerie."

    Ciel "Just. For. You."

    Claude "Mon ami, will you be okay?"

    Ciel "Oh, he’ll be more than okay."

    Claude "I pray for you, my friend. May you see tomorrow in good health."

    Jean "Come on, Claude. What’s the worst she can do? Be my jetpack?"

    Ciel "Hey!"

    Claude "Oh, you two haven’t aged a day."

    hide Claude
    show Claude_flip at left

    Claude "Excuse me my dear, can I bother you for a moment? I’d like to order two spinach quiches and a round of mimosas."

    Claude "And your number too, if I may."

label continue_restaurant:

    scene bg cafe with fade

    show Claude at left with dissolve
    show Ciel at center with dissolve
    show Jean at right with dissolve

    Ciel "No wonder you’re single! Treat a woman like that and she’s ditching you before you can say ‘Ah, la vache’!"

    Claude "No way! Jean, mon ami, please tell me you do that to her."

    Jean "I-"

    Ciel "Don’t. Even. Think about it."

    Claude "Too much spice? Ah… It’s not as easy as it was in college."

    Claude "Speaking of college, congratulations mon ami! I heard your funds for the new law school went through."

    Ciel "Uhhh, who?"

    Claude "You, my dear! Did you not allocate ten million euros for building a new prestigious law school in the heart of Paris? The interview said you were inspired by your past struggles to help educate young Parisians about the world and its politics!"

    Jean "This is news to me, when did this happen?"

    Ciel "Ah... I just remembered. It happened last week, I think?"

    Claude "Today is the 20th, no? Perhaps the mimosas got to you. The news said you made the transaction yesterday."

    Jean "Ciel, it isn’t like you to forget something as important as this. This was one of the things you dreamed of. You would’ve told me immediately about this."

    Ciel "Ma moitié, I’m… I’m sorry. Things have just been so busy that it completely slipped my mind, I..."

    Jean "Is there something wrong?"

    Ciel "N-n-no, I..."

    Jean "Ciel, if there’s something wrong you need to trust me. I’m here for you! We should know better than anyone that we have to support each other!"

    Ciel "I..."

    Claude "Jean, mon ami, that is enough. We don’t want to make a scene, no? Let us finish our mimosas and quiches. I did pay for them."

    Jean "...Okay."

    Claude "Maybe it was the mimosas. How many did you have?"

    Ciel "...I think four? Maybe five? I can’t remember."

    Claude "Bordel de merde! Perhaps it is true. Let’s get her some water."

    Jean "Hmm..."

    Claude "What is the matter? Call the good lady! Maybe put in a good word for me…?"

    Jean "Of course not."

    Jean "Excuse me, can we get some water?"

    scene bg cafe2 with fade

    "The next day..."

    show Jean at left with moveinright
    show Claude at right with moveinright

    Claude "What’s the occasion, mon ami? You never take me out to lunch anymore. You are paying aren’t you?"

    Jean "Of course not. Anyway, there’s something I want to discuss with you."

    Claude "Come on, I paid for lunch yesterday. We can at least split it, no?"

    Jean "I was kidding, I owe you one for yesterday. Plus the quiche was actually quite delicious."

    Claude "That’s what I wanted to hear. And was Ciel not invited? I did enjoy yesterday quite a bit."

    Jean "Idiot! That’s why it’s just us two!"

    Jean "You see, there’s something that’s been bothering me. I know Ciel. I know her from the bottom of my heart. And I know her more than enough to know that something’s wrong. She would’ve told me the second that project started and especially the second it finished."

    Claude "Do you mean the incident from yesterday?"

    Jean "Yes, precisely. "

    Claude "You don’t think it was from the mimosas?"

    Jean "Trust me, Claude."

    Claude "I am unsure of how I feel going behind her back. Should we not just talk to her?"

    Jean "I will take full responsibility for anything that happens. I just need answers."

    Claude "Okay, mon ami. If you say so, I shall follow you to the end. What do you propose we do?"

    Jean "I’m curious about the transaction. Ciel got the transaction date off by a whole week."

    Claude "Ah, that was quite the pretty penny, wasn’t it? Are you worried there is more to it than it seems?"

    Jean "That’s why I’m talking to you."

    Claude "You didn’t have to phrase it like that, mon ami. You’ll break someone’s heart one day!"

    Jean "Yes, okay, understood. Anyway, since it is a government transaction, it had to have gone through the treasury."

    Claude "Oho! So we sneak through the night like roguish devils and swipe the information from under their noses!"

    Jean "This is serious Claude."

    Claude "Then we break out of the treasury and run on the rooftops under the full moon, with a breeze of excitement at our backs!"

    Jean "Claude, we don’t even have to-"

    Claude "I have decided. At 2, we meet at the treasury!"

    Jean "The terminal is accessible throughout the day for government officials. We don’t even have to break into anywhere."

    Claude "But where’s the drama in that?! Come mon ami, let us live a little."

    Jean "Maybe it was a mistake to ask you to come..."

    Jean "But fine. We meet at 2 at the front of the Trésor National. Don’t forget."

    Claude "C'est compris, I will see you there."

    scene bg tresor_national with fade

    "That night..."

    show Jean at left with dissolve

    Jean "Everything is in order. I’m at the rendezvous point. Lockpicks, check. Mask, check. Gun, check. Claude… where are y-"

    Jean "Oh."

    show Claude at right with moveinright

    Claude "Ah, mon ami! Get down quickly! We cannot be spotted!"

    Jean "Claude, crawling on the floor is stupid. What you’re wearing is even more stupid."

    Claude "Ah! You have noticed my cape! I must simply dress for the occasion! And what are you wearing!? How drab!"

    Jean "You shouting about my clothing will definitely get us spotted."

    Claude "Hmph! I will give you fashion tips later. First, let us infiltrate the building!"

    Jean "I’ll check if it’s clear. If I give the signal, we move."

    Claude "C'est compris."

    Jean "..."

    Jean "It’s clear, let’s go."

    "*huff huff*"

    "*STOMP STOMP STOMP*"

    Claude "Oop I tripped-"

    "*CRASH*"

    Jean "Claude, what are you doing!? Ah, a guard-"

    Jean "Come on, idiot! Hurry! There’s someone coming!"

    Claude "Mon ami, I have scraped my knee! It appears I can’t go on… Go without me!"

    Jean "Tu te fous de ma gueule?! Fine, I’m carrying you!"

    Claude "Ah-"

    Claude "This is strangely comforting…"

    Jean "Shut up. You’re already heavy enough as it is."

    scene bg tresor_door with fade

    "*huff huff huff*"

    show Jean at left with moveinright
    show Claude at right with moveinright

    Jean "We made it..."

    Claude "Amazingly done team! I-"

    Jean "You! Why were you stomping so loudly!? Why did you fall and make a ruckus? Why did I have to bail you out?"

    Jean "And how did we get to the front door without anyone noticing?"

    Claude "Good questions, mon ami. But I-"

    Jean "Never mind. I’m gonna try to pick this lock..."

    show Jean at center with move

    Jean "..."

    Jean "..."

    Jean ". . ."

    Jean "Merde! It can’t be done. I suppose I must look around for alternative methods..."

    show Jean at left with move
    show Claude at center with move

    Jean "Claude, come help! We need to find a window or something!"

    Jean "Claude?"

    "*door opens*"

    Jean "Claude, how did you..."

    Claude "Ah, before you got here, I asked the kind man over there for the keys."

    Jean "That’s the guard-"

    Claude "Hello my friend! Thank you again for the keys!"

    Jean "I cannot believe you..."

    scene bg inside_tresor with fade

    "*huff huff*"

    "*stomp stomp*"

    show Claude at right with moveinleft
    show Jean at left with moveinleft

    Jean "Alright, we reached the terminal. We should be able to find the transaction history in here."

    Claude "Wonderful. What do we have here…?"

    show bg transaction with fade

    Claude "Nothing seems out of the ordinary to me… Do you notice anything, mon ami?"

    jump treasury_search

label treasury_search:
    call screen transaction



label amount_found:

    $ amount_there = False

    Jean "Fifteen million euros… That doesn’t seem familiar."

    Claude "Didn’t the news say ten million euros?"

    Jean "Then where did these five million euros come from?"

    Claude "And where did they go…?"

    if not seal_there and not scratches_there and not date_there:
        jump transaction_done

    jump treasury_search

label scratches_found:

    $ scratches_there = False

    Jean "What are these scratches… they look like a mess of dots and dashes."

    Claude "I know not, mon ami. Perhaps those are accidents?"

    Jean "Maybe… I suppose I can come back to this later."

    if not seal_there and not date_there and not amount_there:
        jump transaction_done

    jump treasury_search

label seal_found:

    $ seal_there = False

    Jean "The seal of the prime minister… Ciel was directly involved in this transaction."

    Claude "I would hope so. This was a project of hers."

    if not date_there and not scratches_there and not amount_there:
        jump transaction_done

    jump treasury_search

label date_found:

    $ date_there = False

    Jean "This date… It’s from a week ago."

    Claude "But the news said she made the transaction two days ago."

    Jean "Interesting..."

    if not seal_there and not scratches_there and not amount_there:
        jump transaction_done

    jump treasury_search

label transaction_done:

    scene bg inside_tresor with fade
    show Jean at left with dissolve
    show Claude at right with dissolve

    Jean "Some of these things don’t line up..."

    Claude "Indeed mon ami. Something may be afoot here..."

    Claude "I’m kind of getting excited!"

    Jean "For some reason, I just can’t get over those scratches. They look too..."

    Jean "Intentional."

    Claude "But what could these scratches even mean?"

    Both "Hmm…"

    Claude "It feels a little like we are detectives cracking a code, no?"

    Jean "A code, huh? I wonder what kind of code could it be..."

label code_choice:
    menu:
        "Binary code.":
            jump binary_code

        "Morse code.":
            jump morse_code

        "Braille.":
            jump braille_code

        "Wingdings.":
            jump wingdings_code

label binary_code:

    Jean "Binary…?"

    Claude "Argh, I despise binary! A friend dragged me into the intro computer science class in university and they threw those god damn ones and zeroes at me! Never speak of binary ever again!"

    Jean "Ones and zeroes… I guess not."

    jump code_choice

label braille_code:

    Jean "I wonder if it’s braille…?"

    Claude "I remember when I tried to learn braille. I met a wonderful blind lady once. I tried to ask her on a date and she threw the paper back at me. Maybe I got those dots wrong..."

    Jean "No mention of lines. I suppose my guess was off."

    jump code_choice

label wingdings_code:

    Jean "Wingdings… It’s been a while since I’ve thought of those."

    Claude "Ah wingdings! We used to write messages to each other in those weird symbols in high school! I remember when I told you I thought the girl that sat next to you in precalc was hot. You told me to shut up."

    Jean "Of course he remembers that. That’s out of the picture."

    jump code_choice

label morse_code:

    Jean "Hmm… Could it be morse code…?"

    Claude "Do you not remember morse code? I taught it to you when we were kids! I would shine a flashlight at your window at night and you wouldn’t respond!"

    Jean "What does that have to do with anything?"

    Claude "Remember? Long flashes and short flashes! They stood for the dashes and the dots in the-"

    Jean "That’s it! Dashes and dots! Those nights of waking up with a light in my face were for something after all!"

    Claude "Mon ami, you were supposed to come out when I signaled. I even spelled out ‘Let’s play’!"

    Jean "What you did was disturb the general public. Anyway, maybe if we translated the dashes and dots, we’d get somewhere."

    Claude "A wonderful idea. Do you remember anything I taught you?"

    Jean "No..."

    Claude "What a predicament we have ourselves in! A code with no translator! Whatever shall we do?"

    Jean "The internet exists."

    Claude "Ah, one step ahead of me I see! I was about to say that myself!"

    Jean "There’s no shot in hell you thought of that."

    Claude "Hush, mon ami. Let’s get to decoding shall we?"

$ correct = True

label decode_start:
    scene bg morse1 with fade
    menu:
        "S":
            jump decode2

        "A":
            $ correct = False
            jump decode2

        "X":
            $ correct = False
            jump decode2

        "P":
            $ correct = False
            jump decode2

label decode2:
    scene bg morse2 with fade
    menu:
        "Y":
            $ correct = False
            jump decode3

        "E":
            jump decode3

        "S":
            $ correct = False
            jump decode3

        "H":
            $ correct = False
            jump decode3

label decode3:
    scene bg morse3 with fade
    menu:
        "B":
            $ correct = False
            jump decode4

        "C":
            $ correct = False
            jump decode4

        "A":
            jump decode4

        "D":
            $ correct = False
            jump decode4

label decode4:
    scene bg morse4 with fade
    menu:
        "Y":
            $ correct = False
            jump decode_end

        "J":
            $ correct = False
            jump decode_end

        "Z":
            $ correct = False
            jump decode_end

        "L":
            jump decode_end

label decode_end:
    if not correct:
        $ correct = True
        jump decode_fail
    jump decode_success

label decode_fail:
    scene bg inside_tresor with fade

    show Jean at left with dissolve
    show Claude at right with dissolve

    Jean "Argh! This is gibberish! This doesn't even make a coherent word!"

    Claude "Maybe it's an acronym, mon ami."

    Jean "Maybe... Let me take a look at the morse code again."

    Jean "And don't forget to show the symbols on the internet, Claude."

    jump decode_start


label decode_success:
    scene bg inside_tresor with fade

    show Jean at left with dissolve
    show Claude at right with dissolve
    Jean "Seal… What could that mean?"

    Claude "Ah, I love those little beasts. Best ocean animal if I do say so myself. I remember seeing them at the aquarium one time on a date and-"

    Jean "Enough of that! That makes absolutely no sense."

    Jean "Seal, seal… Blast! And we were so close too..."

    Claude "Uhh, mon ami… Look what’s happening."

    Jean "What-"

    scene bg encrypted with dissolve

    Jean "-the fuck?"

    Claude "Did I do something wrong? I just clicked on the seal of the prime minister..."

    Jean "Maybe you accidentally did something very right. Look! Among all the gibberish, there’s a set of numbers. 49°07'14.7''N 2°05'52.6''E… Those look like coordinates or something."

    scene bg inside_tresor with fade

    show Jean at left with dissolve
    show Claude at right with dissolve

    Claude "Did I help? Ah, it was all part of my plan all along! You’re glad you brought me along no?"

    Jean "Somehow your stupidity helped more than it hurt. The only thing we have to do now is get to those coordinates. Maybe there’s something there..."

    Claude "Only one way to find out. Let’s go tomorrow! I cannot wait to see the conclusion of this covert mission!"

    Jean "Whatever you say, Claude. Let’s get out of here."

    Claude "C'est compris. Ah, wait. There’s a security guard. Wait here."

    hide Claude with moveoutleft

    Claude "Thank you my good friend! We got lots of work done thanks to you!"

    Jean "*sighs* How aren’t we busted by now..."

    # New scene

    scene bg car with fade
    show Claude at left with dissolve
    show Jean at right with dissolve

    Claude "Never gonna give you up, never gonna let you down, never gonna-"

    Claude "Mon ami! Why aren’t you singing? This is one of my favorites!"

    Jean "I figured that out after the fourth time you played it..."

    Claude "Aren’t you having a wonderful time? Think of it as a little road trip!"

    Jean "I’m quite okay. Just let me sleep..."

    Claude "Ah, but we are here!"

    Jean "I’m running on three hours of sleep and caffeine. Please..."

    Claude "Mon ami, look up."

    Jean "Let me sleep-"

    Jean "That… doesn’t seem right."

    scene bg hangar with dissolve

    show Claude at right with dissolve
    show Jean at left with dissolve

    Jean "Why is that here? In the middle of nowhere?"

    Claude "Only one way to find out. Let’s go take a look!"

    hide Claude with moveoutright

    Jean "Alright, let’s be careful."

    Claude "This thing is massive..."

    Jean "It's so out of place. Why did the coordinates lead here?"

    Claude "Alright what’s in-"

    Jean "Claude, you fool! Be caref-"

    Claude "Jean."

    Jean "Hey, you never call me that!"

    Claude "Look."

    Jean "What’s the matter?"

    Claude "..."

    Jean "Alright. I guess I’ll take a look..."

    hide Jean with moveoutright

    scene bg tanks with fade

    show Claude at right with dissolve

    Jean "Claude, where are-"

    show Jean at left with moveinleft

    Jean "What..."

    Jean "What is this..."

    Jean "You don’t think it’s..."

    Claude "The five million euros."

    Claude "There's no other explanation."

    Jean "I..."

    Jean "Ciel..."

    Jean "The things we worked so hard for..."

    Jean "The virtues we swore to protect..."

    Jean "Was it all for nothing...?"

    Claude "Jean..."

    Jean "..."

    Jean "I’m gonna go take a walk."

    hide Jean with moveoutleft

    Claude "Mon ami, wait!"

    Claude "Just two days ago, it was just like old times..."

    Claude "Laughing together, drinking together, being together..."

    Claude "What happened…?"
