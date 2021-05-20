# The script of the game goes in this file.

init python:
    config.screen_width = 1280
    config.screen_height = 720

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# main cast and their variations
define Jean = Character("Jean")
define Moody_Medic = Character("Moody Medic")
define Ciel = Character("Ciel")
define Radiant_Redhead = Character("Radiant Redhead")
define Claude = Character("Claude")
define Rambunctious_Ragamuffin = Character("Rambunctious Ragamuffin")

# side characters
define question_marks = Character("???")
define Worried_Protester = Character("Worried Protester")
define Dehydrated_Protester = Character("Dehydrated Protester")
define Agitated_Protester = Character("Agitated Protester")
define Frustrated_Youth = Character("Frustrated Youth")
define Downtrodden_Worker = Character("Downtrodden Worker")
define Disgruntled_Worker = Character("Disgruntled Worker")
define Young_Parisian_Lieutenant = Character("Young Parisian Lieutenant")
define Angry_Young_Parisian = Character("Angry Young Parisian")
define Frustrated_Young_Parisian = Character("Frustrated Young Parisian")
define Mousat = Character("Mousat")
define Wounded_Protester = Character("Wounded Protester")
define Frustrated_Protester = Character("Frustrated Protester")
define Helpful_Agitator = Character("Helpful Agitator")
define Newscaster = Character("Newscaster")

# images

# backgrounds
image bg champs_elysees = "champs-elysees.jpg"

# main characters and their variations
image Jean = "macaron.jpg"
image Moody_Medic = "macaron.jpg"
image Jean flip = im.Flip("macaron.jpg", horizontal="True")
image Ciel = "Ciel Base.png"
image Radiant_Redhead = "Ciel Base.png"
image Claude = "macaron.jpg"
image Rambunctious_Ragamuffin = "macaron.jpg"

# side characters
image Worried_Protester = "fondue.jpg"
image Dehydrated_Protester = "fondue.jpg"
image Agitated_Protester = "fondue.jpg"
image Frustrated_Youth = "fondue.jpg"
image Downtrodden_Worker = "fondue.jpg"
image Disgruntled_Worker = "fondue.jpg"
image Young_Parisian_Lieutenant = "fondue.jpg"

# The game starts here.

label start:
    jump scene2

label scene1:
    show bg champs_elysees
    with None

    "16 March, 2019 - Champs-Elysées - First Aid Station"

    show Worried_Protester at left with dissolve
    show Jean at right with dissolve
    show Moody_Medic at right

    Moody_Medic "Come on, mec. I’m not here to coddle you -- are you ready or not?"

    Worried_Protester "I...I guess, but...is it going to hurt?"

    Moody_Medic "Oh, no! No, not at all. Why would you even think it would?"

    Worried_Protester "Are you being sarc--"

    Moody_Medic "Bête! Of fucking course I am! Of course it will hurt! You should have thought about that before your little parkour stunt, no?"

    Worried_Protester "Hey, no need to be un connard, yeah? That’s some bedside manner you have there, Jean."

    hide Moody_Medic

    Jean "Yeah, yeah, whatever. Do you want me to fix your arm or not?"

    Worried_Protester "Ah! You never change. Fine, just make it quick."

    Jean "What would make you think I intend to do otherwise? We will go on three. Ready?"

    Worried_Protester "As ever."

    Jean "Ok. One."

    Jean "Two."

    "*crack*"

    Worried_Protester "Ah-- Merde!"

    Worried_Protester "Huff Huff"

    Worried_Protester "Merde! What happened to “on three”?"

    Jean "You asked for me to make it quick, no? Only the slowpokes get a full three count."

    Worried_Protester "You are real piece of wor--"

    Jean "Save it, I have too much to do, unless you would like me to put it back?"

    Worried_Protester "NO! No. Fine, have it your way. Can I go now?"

    Jean "Please do. We need your stool. Here, take some ice, keep it pressed close, and make sure not to fall off any more telephone poles."

    Worried_Protester "Lamp pole. It was a lamp po--"

    Jean "I don’t care if it was a fucking May pole! Stay off any kind of pole, con!"

    Worried_Protester "Fine, fin-- Wha!"

    show Dehydrated_Protestor at left with moveinleft
    show Worried_Protester at center with move

    Dehydrated_Protester "Hey Jean, I...I don’t feel s--"

    "*Thunk*"

    Jean "Hey, hey! Watch where you’re falling! Here, have a seat! This idiot was just leaving!"

    Worried_Protester "I was? What about my i--"

    Jean "What are you, a child? Stop whining, and just come back if it still hurts. Can’t you see I have other work to do?"

    hide Worried_Protester with dissolve

    Dehydrated_Protester "T-thank you. I-I can barely keep my eyes…"

    Jean "You’re fine, mec. You’re fine. I’ve got you. Just let me take a look at you, and we’ll figure out what’s wrong."

    Dehydrated_Protester "O-ok."

    Jean "Let me see… Hmm…."

    Jean "You’re so warm! So fever...Now, look in my eyes...Ah, dilated pupils...Ugh, this is no good."

    Dehydrated_Protester "Oi? No good? Am I dying?"

    Jean "Hardly. Does it sound like I’m worried?"

    Dehydrated_Protester "Well.. A bit..."

    Jean "Believe me, were I worried, you would know. Now, when is the last time you had some water?"

    Dehydrated_Protester "T-this morning, I think."

    Jean "Mon p’tit Chriss! You did not bring any water? Did you think you would be home from the barricade in time for tea?! That the gendarmes would just let you walk on home for some refreshment?"

    Dehydrated_Protester "Hadn’t really though--"

    Jean "No, of course you didn’t! Bête! Here, drink this, or I’ll have to stick an IV in you! And I warn you...My aim is terrible."

    Dehydrated_Protester "Ok, ok. I will! Thank you."

    "*Glug glug glug*"

    Jean "Better?"

    Dehydrated_Protester "A little. Merci."

    Jean "God in heaven, ss if there weren’t enough idiots injuring themselves already... Where did you come from, anyways? There was supposed to be water across the whole Champs today!"

    Dehydrated_Protester "Up the way a bit, by the Fouquet’s. I wouldn’t go up there now, they’ve set the whole place ablaze."

    Jean "They did what?! At the Fouquet’s? Merde! Ciel, what are you…"

    Jean "You say you just came from there, no? Did you see a woman there?"

    Dehydrated_Protester "Well, yes. There were quite a few. But you need to be more specific. THey all kind of blurred together."

    Jean "Yes, yes. I’m sure. But this one...I do not think you would forget seeing her. She’s a tall girl, red hair, about my age? I bet she was the one who threw the first torch."

    Dehydrated_Protester "Hmm, yeah. Yeah.I think there was a woman like that. Fiery girl, right? Real true believer type? There was one at the front of the crowd."

    Jean "Oh, merde...Ciel...What are you doing?"

    Jean "Yeah, yeah. That sounds like the one. Was she still there when you left?"

    Dehydrated_Protester "Yeah, yeah. Probably still there now. She had quite a speech going when I left. Not a fan of the bougies, is she? Your girl?"

    Jean "Sometimes. Other times she’s more like my personal pain in the--"

    Jean "Ah, nevermind. Are you able to get back on your feet now?"

    Dehydrated_Protester "I think so. You got more water?"

    Jean "Down the block, right by the broken lamp post. Just follow the idiot who just left."

    Dehydrated_Protester "Broken lamp--"

    Jean "Don’t even ask about it. There is more than enough stupidity to go around today."

    hide Jean
    show Jean flip at right

    Dehydrated_Protester "Hey! Where you runnin’ off to? Aren’t you the nurse here?"

    Jean "Fouquet’s! Haven’t you heard? There’s a fire! Who else will make sure the children do not torch themselves?"

    Dehydrated_Protester "And what if someone needs you here?"

    Jean "Then send them after me and I’ll look after them there!"

    Dehydrated_Protester "What? Hey! Hey!"

    hide Jean flip with moveoutright

    Dehydrated_Protester "Putain! I knew I should have stayed home. This always happens to me."

    hide Dehydrated_Protester with dissolve

    hide bg champs_elysees with dissolve

label scene2:
    show bg champs_elysees with dissolve

    "16 March, 2019 - Champs-Elysées - Fouquets’"

    show Radiant_Redhead at left with dissolve

    Radiant_Redhead "..And will we stand by while these dogs bleed us, the real citizens of France, dry?!"

    show Agitated_Protester at right with moveinright

    Agitated_Protester "NO!"

    Radiant_Redhead "Will we watch while they take and take from us until we have nothing left to give?!"

    hide Agitated_Protester with moveoutright
    show Frustrated_Youth at right with moveinright

    Frustrated_Youth "Hell no!"

    Radiant_Redhead "Will we say nothing while these file de putes drive their boots unto our necks?!"

    hide Frustrated_Youth with moveoutright
    show Downtrodden_Worker at right with moveinright

    Downtrodden_Worker "NO!"

    hide Downtrodden_Worker with moveoutright

    Radiant_Redhead "No! No we will not, Pairisans. We will stand! We will fight! We will take back what they’ve stolen from us -- take back the work of our hands that they’ve so thoroughly polluted."

    show Jean at right with moveinright

    Radiant_Redhead "Parisians! Who is with m--"

    Jean "Ciel!"

    Radiant_Redhead "*cough*"

    Radiant_Redhead "I said, Parisians, who is with me?!"

    Jean "CIEL!"

    hide Jean with moveoutright
    show Frustrated_Youth at right with moveinright

    Frustrated_Youth "I am!"

    hide Frustrated_Youth with moveoutright
    show Downtrodden_Worker at right with moveinright

    Downtrodden_Worker "And I am!"

    hide Downtrodden_Worker with moveoutright
    show Jean at right with moveinright

    Jean "CIEL!!!"

    Radiant_Redhead "*sigh*"

    show Ciel at left
    hide Radiant_Redhead

    Ciel "Jean. Ma moitié. Can you not see I am a bit preoccupied?"

    Jean "Oh, you’re preoccupied. Well, while you’ve been busy grandstanding, I’ve had a nonstop parade of patients in my tent. Broken legs, burns, dislocated shoulders, heatstroke…"

    Ciel "Jean, there must be ten thousand people out here today. Of course some of them are going to get a little bit hurt."

    Jean "This was not what you promised. You said we would keep it safe. Peaceful. And now you’re lighting luxury stores on fire! For what? Are you trying to bring the gendarmes down on us?"

    Ciel "No. Of course not, but they have to know we’re serious."

    Jean "And do you think that getting ten thousand vandal-prone idiots to loiter about hasn’t already done that?"

    show Jean at center with move
    show Disgruntled_Worker at right with moveinright

    Disgruntled_Worker "Hey, what’s your problem, mec? Who are you calling an idiot?!"

    Agitated_Protester "Yeah! Who are you supposed to be? You don’t look tough to me!"

    Frustrated_Youth "He must be one of the dogs’ pets! Let’s get him!"

    show Ciel at center with move
    show Jean at left with move

    Ciel "Get him? And do what?! You mean to beat him? Bruise his pretty little doll face?"

    Ciel "Is this the kind of people we are? Would we turn a man into walking pulp without even knowing where he stands??"

    Ciel "If this is our way, then we are better than the capitalist dogs and the pigs who protect them. Are we?"

    Agitated_Protester "N-no…"

    Frustrated_Youth "I guess not…"

    Ciel "No. So let’s be better than them, shall we? Let us lift each other up, rather than beating each other down. Is that not our way?"

    Disgruntled_Worker "Yeah!"

    Frustrated_Youth "S-sorry there mec. It’s been quite a day, you know? We just got a bit ahead of ourselves."

    Agitated_Protester "Yeah, the blood just got to our heads!"

    Jean "Then maybe you sh--"

    show Ciel at left with move
    show Ciel at center with move

    Jean "oof"

    Ciel "What my friend means is that he understands completely. He is just as excited as you all about this historic day, right Jean?"

    Jean "I did--"

    show Ciel at left with move
    show Ciel at center with move

    Jean "oof"

    # smalltext if possible
    Jean "Yes, yes! What she said!"

    Ciel "See? The heat must have just gotten to him. Now Jean, apologize to these good fellows."

    Jean "You want me to wh--"

    show Ciel at left with move
    show Ciel at center with move

    Jean "oof"

    Jean "(smalltext) Ok, ok. I’m sorry..."

    Ciel "Good! Now please, give me a moment to catch up with my friend here."

    hide Disgruntled_Worker with dissolve
    show Jean at right with move
    show Ciel at left with move

    Ciel "You know, Jean, one day your unwillingness to ever give an inch is going to get you killed. I can’t always be here to protect you, you know."

    Ciel "Would it kill you to just open up a bit? If you keep it up, everyone will just think you’re a asshole."

    Jean "So what? It’s not my responsibility to think for them."

    Ciel "*sigh*"

    Ciel "If they knew you were just upset because of how much you care about all of this, they wouldn’t harass you. Instead, they just think you’re a punk."

    Jean "Well maybe I am a punk. Wouldn’t be the worst look for me, don’t you think?"

    Ciel "Ossstie, and here I thought you were the cautious one. Tell me ma moitié, what has you so riled up?"

    Jean "I already told you. You promised me you would try to keep things calm. Do you think that starting a riot is going to make us look like the good guys here?"

    Ciel "I have been trying…"

    Jean "You have been trying? Ciel, there is a burning storefront right there! You expect me to believe you had nothing to do with that?"

    Ciel "No, I wouldn’t. But we made sure no one was hurt. It’s a symbol of our frustrations, nothing more."

    Jean "Then why are there burn victims in my tent?!"

    Ciel "Do you think we were the only ones to light a fire? Other crowds lit the Xiaomi, the Huge Boss…"

    Jean "Mon Chriss...There’s more?! You said you would keep this under control, Ciel."

    Ciel "And I have, as much as I can. Those fires were not lit by Young Pairisians, only this one. I’m not in charge of everyone, you know."

    Jean "*sigh*"

    Ciel "Come now, ma moitié, you were never one to shy away from setting a few broken limbs. What are you really worried about?"

    Jean "…"

    Jean "The gendarmes. With all of this chaos, you know they will have no choice but to act, and if we burn down half the town, it’s going to look justified."

    Ciel "And if they do, we will meet them. Show them that we will not be silenced. Make sure everyone watching knows the truth."

    Jean "Yes, I know all of this! Can you not see that’s what I am afraid of? I can fix broken bones, but bullet holes?"

    Ciel "It won’t come to that. They would never dare. Not in the city center."

    Jean "I wish I had your confidence. You heard Macron. The military is in the city now!"

    Jean "Who knows what they will dare do, especially if half the lane is in flames?"

    Ciel "Jean."

    Jean "And then what if one of these idiot connards were to piss them off, huh?"

    Ciel "Jean."

    Jean "One stone, Ciel! One stone is all it would take to start a bloodbath!"

    Ciel "Jean...Calm down."

    Jean "I am calm! Can you not see how calm I am?!"

    Ciel "You’re not. You’re shouting. People are starting to stare."

    Jean "Let them stare, then! This is important!"

    Jean "...What are you smiling at! I am serious!"

    Ciel "You’re just so cute when you get worked up, that’s all."

    Jean "Cute? Wha...Bah. It must be nice to be so carefree."

    Ciel "It is. I’ve accepted that what will happen, will happen. I’m just here to play my part. You should try it."

    Jean "You wouldn’t last the week if I did. Someone has to keep you safe from yourself."

    Ciel "And I appreciate it, mon canari. Just...Live a little sometimes, that’s all."

    Ciel "Look around us. We planned for what, two thousand to come out? Three?"

    Jean "Speak for yourself. I would have been surprised if we had much over on."

    Ciel "Right, right. But look at how many have answered the call. There are fifteen thousand voices gathered here today, mon bonheur. A multitude beyond imagination."

    Ciel "Isn’t this what we always dreamed of? Does this not vindicate what we’ve fought for so far?"

    Jean "*sigh*"

    Jean "Yes, yes, but…."

    Ciel "But?"

    Jean "But in my dreams, there were more water bottles."

    Ciel "…"

    Ciel "Pft! Hahaha!"

    Ciel "You win, you win. I’ll send for more water, and make sure the other sectors do too. Will that make you happy?"

    Jean "Happier. I will not be happy until we are both back home and asleep in our bed."

    Ciel "Oh, then I am sorry to say you will not be happy until dawn, Mon cœur. You are mad if you think I will be letting you do any sleeping tonight. Not after a day like this one."

    Jean "So you mean to stay out all night long? The bars may be a bit rowdy tonight."

    Ciel "No, no. You misunderstand. We’ll be seeing plenty of our bed, do not worry. Just not for sleeping. I’m afraid you will be otherwise engaged. Professionally engaged."

    Jean "Oh will I? You have need for a doctor?"

    Ciel "Yes, terribly. I’m afraid I will need an examination. A very thorough examination."

    Jean "Well, Ms. Augustin, I believe you’re in luck. I do have an opening to--"

    question_marks "JEAN! CIEL!"

    Ciel "Is that…?"

    Jean "With timing like that, do you even need to ask?"

    Ciel "Oh, don’t look so upset. We did get our appointment booked, right?"

    Jean "Of course. I live to serve."

    show Jean at center with move
    show Rambunctious_Ragamuffin at right with moveinright

    Rambunctious_Ragamuffin "huff huff"

    Rambunctious_Ragamuffin "Oh...Tt-thank god I found you both. Tt-t-t-hey--"

    Rambunctious_Ragamuffin "huff huff"

    Jean "Câlise, Claude, what happened to you? You look like you just finished a marathon."

    Ciel "He doesn’t look that bad. Go ahead Claude, catch your breath."

    show Claude at right
    hide Rambunctious_Ragamuffin

    Claude "The ge--"

    Claude "huff huff"

    Claude "THE GENDARMES!"

    Jean "Mon Chriss…"

    Ciel "Already? They aren’t wasting any time. Where are they Claude?"

    Jean "Who cares? Ciel, let’s get out of here, while we still can!"

    Claude "huff huff"

    Claude "The...The north end...At the north end of the Champs-Elysées…"

    Ciel "Then are we waiting for? Lead the way, Claude."

    Jean "What? You want to go towards the gendarmes? Why?"

    Ciel "Because I came here to stand for what I believe in, not run away for it. You two go, but I’m staying."

    Jean "You are serious?"

    Ciel "Do I look like I am joking?"

    Jean "…"

    Jean "Fine! Let’s go get ourselves killed, then. Claude! Lead us on!"

    Ciel "You’re coming? But--"

    Jean "Of course I’m coming, you impossible woman! How else will I make sure you stay safe?"

    Claude "huff huff"

    Claude "Coming too…"

    Jean "Yes, yes. No one asked you, mon gros. Of course you are coming. Now get your butt moving, and show us the way!"

    hide Claude with moveoutright

    Ciel "Are you sure about this? You can still go."

    Jean "Is your mind totally made up?"

    Ciel "Completely."

    Jean "Then there is nothing to talk about. Now let’s go before Claude steals all your glory."

    Ciel "...Merci beaucoup. I wou--"

    Jean "No, no. Save it for when we are safe. You start talking like that, and tragedy will be a step behind us."

    Ciel "Then let’s go! Viva la Revolución!"

    Jean "Well, for the next hour or so, at least…"

    hide Ciel with moveoutright
    hide Jean with moveoutright

    hide bg champs_elysees with dissolve

label scene3:
    "16 March, 2019 - Champs-Elysées - The Frontlines"

    show bg champs_elysees with dissolve

    show Claude at left with moveinright
    show Ciel at center with moveinright
    show Jean at right with moveinright

    Claude "*huff* *huff*"

    Ciel "Come on Claude! You’ll miss the revolution!"

    Jean "No! No you won’t. This is not a revolution!"

    Claude "I...I’m sorry, M-Mon amis...G..Go on without me…"

    "*thump*"

    Ciel "Claude? Claude! Are you ok?"

    Claude "G...Goodbye, Mon gros…"

    Jean "Oh, Casse-toi, idiot. You’re not dying. Let me take a look at you."

    Claude "H-Hey! Be careful down there! Ey- ey! Oww!"

    Jean "See? He’s fine."

    Ciel "Parts of him, at least."

    Claude "Merde! You have the bedside manner of a troll, mon ami!"

    Ciel "That’s not quite fair. I haven’t seen him eat anyone. At least, not yet…"

    Jean "Ha ha. Funny. Let’s keep moving."

    Claude "Oy! I still need a minute to catch my breath, yeah? Don’t leave me alone. Please?"

    Ciel "What do you think, Ma moitié?"

    Jean "I think that I can see tanks from here, Ciel. They’ll need you at the front to keep things under control."

    Ciel "I think so too...But what about you?"

    menu:
        "I’m coming with you, of course.":
            jump gendarme_leave

        "You know Claude. Someone has to keep an eye on him.":
            jump gendarme_stay


    label gendarme_stay:

        Ciel "Ah yes, we wouldn’t want him running off to chase some tail, would we?"

        Claude "And yet, I found the two of you easily enough, no? Why must you hold such a low opinion of me?"

        Jean "Because she has eyes, connard. Go on, Ciel. We’ll catch up once this slacker is back on his feet."

        Ciel "Alright. Stay safe you two."

        Jean "Yes, yes. Go! And remember, Ciel, don’t do anything I wouldn’t!"

        Ciel "When have I ever?"

        Jean "You nev-- Hey! Are you listening?"

        hide Ciel with moveoutleft

        Claude "Ah...She is quite a woman, is she not, mon ami?"

        Jean "What’s that supposed to mean?"

        Claude "Nothing, nothing. I just never expected to see you caught up in something like this, yeah? Never quite seemed your style."

        Jean "‘My style’? What do you know about my style?"

        Claude "Ah...do not give me that, mon ami. Our mothers rocked us to sleep in the same cradle, no?"

        Claude "If you had told me a year ago that my moody and boring best friend would be on the front lines of a revolution, I’d have laughed at you!"

        Jean "It’s not a revolution, and it’s no big deal. I’m just here to make sure no one gets hurt. That’s all."

        Claude "Whatever you say, mon ami. That girl has changed you, admit it."

        Jean "Tch. You sure have a lot to say for being out of breath."

        Claude "Ah, I am never too out of breath to talk to my mo--"

        question_marks "You are in violation of a citywide curfew. Leave this area now, or we will be forced to remove you forcefully!"

        Claude "Merde! Did you hear that? It does not sound like we are swimming in the kiddie pool any more, does it?"

        Jean "No. Not at all…"

        Jean "Dammit Ciel, don’t do anything stupid…"

        Claude "You know she won’t. She might not do what you want, but never something stupid. That girl is smarter than us both put together."

        Jean "If only because you subtract from the whole. Get up, we have to get to the front if I have to carry you."

        Claude "No need, no need! I’m better now. Let’s go, before we miss the fun!"

        hide Claude with moveoutleft
        hide Jean with moveoutleft

        "Moments later..."

        show Claude at center with moveinright
        show Jean at right with moveinright

        Jean "CIEL! Where are you?"

        show Agitated_Protester at left with moveinleft

        Agitated_Protester "Baise toi, pigs!"

        hide Agitated_Protester with moveoutleft
        show Frustrated_Youth at left with moveinleft

        Frustrated_Youth "Down with Macron!"

        hide Frustrated_Youth with moveoutleft
        show Downtrodden_Worker at left with moveinleft

        Downtrodden_Worker "Justice now!"

        Claude "Can you see her, mon ami? It is starting to get dangerous out here, no?"

        Jean "Just keep moving to the front. There’s no way she won’t b--"

        hide Downtrodden_Worker with moveoutleft
        show Ciel at left with moveinleft

        Ciel "Ah! There you two are!"

        Jean "Ciel, what the hell is going on?"

        Ciel "It’s like you said, they didn’t send the gendarmes. Look."

        jump gendarme_conclusion


    label gendarme_leave:

        Claude "bruh moment"

        jump gendarme_conclusion


    label gendarme_conclusion:

        Claude "Oh...Baise moi mor! Is that a tank?!"

        Jean "They brought the military?! Ciel, we need to get out of here. They aren’t messing around."

        Ciel "No. We’re not leaving. Not now."

        Jean "Ciel, this isn’t a game! These aren’t Parisians. They don’t care what happens to us."

        Ciel "It never was a game, Jean. Everyone here came to stand up for what they believe in, and I’m not going to dishonor that by buckling the second the wind blows!"

        Claude "She has a point, mon ami. Besides, they’re still Frenchmen. They would not fire into a crowd."

        Jean "Fine. Fine. You’re right. But if they start shooting, I’m dragging you out of here if it’s the last thing I do."

        Ciel "Give me some credit. I’m brave, not stupid, ma moitié. I have no more desire to ge--"

        hide Jean with moveoutright
        show Claude at right with move
        show Ciel at center with move
        show Young_Parisian_Lieutenant at left with moveinleft

        Young_Parisian_Lieutenant "Ciel! There you are! What should we do?"

        Ciel "What do you mean? This is why we came here, no? We stand up, and let them know that we will not be intimidated!"

        Young_Parisian_Lieutenant "But...The military is here, Ciel! Half the club has already fled!"

        Ciel "Are you afraid?"

        Young_Parisian_Lieutenant "Y-yes. Kind of. I know I shouldn’t be...but the military? Here?"

        Ciel "Shh, don’t be ashamed. Fear is normal, but not something to run from. Not if what you’re doing is right. Do you think it is?"

        Young_Parisian_Lieutenant "Of course! We cannot go on like this. Things must change, I know, but...I feel so weak."

        Ciel "And you are. We all are, alone. But we’re not alone. Go, get the others. We’ll stand here together, and show them how strong we can be together, yeah?"

        Young_Parisian_Lieutenant "Y-Yeah! I’ll go get them right now! Right now!"

        hide Young_Parisian_Lieutenant with moveoutleft
        show Ciel at left with move
        show Claude at center with move
        show Jean at right with moveinright

        Claude "Ah, Ciel...You have such a gift for words! Why do you waste them on this dull ingrate?"

        Jean "Better to be dull than dead, no?"

        Ciel "Relax. No one will die today. They still haven’t moved. They’re just here to intimidate us, nothing more."

        Ciel "And Claude? It’s because sometimes it’s nice to have someone you can’t sway around. Someone to keep your feet on the ground."

        Claude "Ahh...So he is like an iron weight strapped to your leg, I see, I see…And you like this?"

        Jean "It’s truly amazing how fast you turned her romantic words mundane."

        Claude "Oh, was it? Thank you, sir. Thank you."

        Jean "That was no compliment."

        Claude "Just because you did not mean it as one does not mean it can’t become one, mon ami."

        Jean "Whatever you say...So, what do we do now, Ciel?"

        Ciel "We gather together, make sure they can hear our message, and wait."

        Jean "I was afraid you’d say that…"

        hide Ciel with dissolve
        hide Claude with dissolve
        hide Jean with dissolve
        hide bg champs_elysees with dissolve

        "*A Few Hours Later*"

        show bg champs_elysees with dissolve

        question_marks "You are in violation of a citywide curfew. Leave this area now, or we will be forced to remove you forcefully!"

        Angry_Young_Parisian "Avale mes couilles, pigs!"

        Frustrated_Young_Parisian "This is a public space! We’re not going anywhere!"

        show Claude at right with dissolve
        show Jean at center with dissolve

        Jean "You’d think they’d have figured out by now that yapping on a loudspeaker isn’t going to accomplish anything."

        Claude "Well, mon ami, they are the pigs. They are not known for being smart, no? They could just tax the rich and fix the fuel prices, then none of this would be happening."

        Jean "Right. Let me know when you manage to convince the rich to tax themselves. It’s not like the representatives are the ones in bread lines."

        show Ciel at left with dissolve

        Ciel "Yes, but the voters who put them there are, and it couldn’t hurt to make sure they remember that, don’t you think?"

        Claude "Ah, Ciel, you have returned. What word from the other groups?"

        Ciel "No word, really. We’re all staying put, all night if we have to. Word is the protest has made global news, and Macron has spent all afternoon pacing the capital."

        Claude "You think he will crack?"

        Ciel "He won’t have a choice if we’re the only thing playing on CNN all night. The world can’t ignore this many protestors."

        Jean "Well, let just hope that when he caves, he finally cracks rather than losing it. There must be a battalion of soldiers over there…"

        Ciel "You worry too much, ma moitie. Even if they do resort to force it will only be gas, and we have plenty of safeguards against that."

        Jean "If only we all had your confidence. You brought your mask, right Claude?"

        Claude "Of course. What kind of idiot do you take m--"

        question_marks "Attention demonstrators!"

        Ciel "That is a new voice, is it not?"

        Jean "It is. Come on, Claude. On your feet. Something’s happening."

        Claude "Yeah, yeah...Can you guys see him? Looks like he’s right over there!"

        # introduce him here

        question_marks "I am Brigadier General Mousat. I have been ordered to clear the Champs-Elysées of all authorized personnel by any means necessary."

        Mousat "Please begin exiting the Champs-Elysées immediately. Violaters will be subjected to nonlethal munitions and face arrest!"

        Claude "Looks like a bit of a hardass, eh mon ami?"

        Jean "Dangerously so. Ciel, I have a bad feeling about this…"

        Ciel "It will be fine. Hey, you!"

        hide Claude with moveoutright
        show Jean at right with move
        show Ciel at center with move
        show Young_Parisian_Lieutenant at left with moveinleft

        Young_Parisian_Lieutenant "Yes, Ciel?"

        Ciel "Go around and make sure everyone gets their masks on. Move anyone without a working mask further south down the Champs."

        Young_Parisian_Lieutenant "Are we being gassed?"

        Jean "If we’re luck--"

        Ciel "Ignore him. I don’t know, but we should be prepared. Now hurry, it sounds like they’re not wasting any time."

        hide Young_Parisian_Lieutenant with moveoutleft
        show Ciel at left with move
        show Jean at center with move
        show Claude at right with moveinright

        Mousat "This is your last warning. Begin leaving now, or face arrest!"

        Jean "Ciel…"

        Ciel "You know I’m not leaving."

        Jean "That doesn’t mean we have to stand in the front lines! Claude, talk some sen--"

        show Claude at left with move
        show Ciel at center with move
        show Jean at right with move

        Claude "Hey! Hey You! Yeah, you with the megaphone! Head pig!"

        Jean "Oh, merd--"

        Claude "If you want us to leave, how about you come over here and kiss my sweet chocolate ass, eh head pig?"

        Jean "Oh my...Claude, put your pants back on…"

        Ciel "Haha, you have the spirit of a true revolutionary, Claude!"

        Claude "Ah, but do you think I have the ass of a true revolutionary? Perhaps they know, eh?"

        Claude "What do you think, head pig? Do I have a revolutionary as--"

        "*bang bang bang bang*"

        Claude "Ah! Baise moi!"

        show Claude at center with move
        show Ciel at left with move

        "*thunk*"

        Ciel "Claude! What happened?"

        Claude "Ahh…I think my ass is broken…"

        Jean "You can already see the bruise...Rubber bullets. Ciel, they are no--"

        "*bang bang bang bang*"

        Angry_Young_Parisian "Ah!"

        Wounded_Protester "Gah! Va te faire foutre, pigs!"

        Jean "Ciel! We have to get out of here! They’re shooting into the crowd!"

        Ciel "No! Not until the rest of our people are safe!"

        Jean "Then what abou--Oh, putain! Claude, get your pants back on, we have to get out of here!"

        Young_Parisian_Lieutenant "Ciel! What do we do? There’s already a few injured…"

        Ciel "C'est des conneries! They can’t do this! It’s madness!"

        Jean "Madness or not, they are! Ciel, you have to tell them to run!"

        Ciel "But we were so close…"

        Jean "And we still are, Ciel! Or, we will be as long as we get out of here! Look at Claude! Do you want the whole club to look like him?"

        "*bang bang bang bang*"

        Ciel "..."

        Ciel "Everyone, gather the injured and head down the Champs! Stay in cover as much as you can!"

        Ciel "I’m going to make sure everyone makes it out of here. Take care of Claude!"

    menu:
        "I’m not going to leave you here!":
            jump gendarme_comingWith

        "Okay, but swear you will meet us at the safehouse by morning!":
            jump gendarme_takeClaude

    label gendarme_comingWith:

        Ciel "Yes, ma moitie. You are! I must take care of my people, and you must take care of Claude."

        Jean "No, I need to take care of you! I’ve seen that idiot stagger his way out of worse."

        Ciel "Look at him! He can’t even stand! I can take care of myself too, love. I would never forgive myself if anything happened to him, or anyone else."

        Jean "Bu--"

        Ciel "No buts. Get him out of here."

        Jean "..."

        "*bang bang bang bang*"

        Jean "Fine, but if you’re not in the safehouse by morning you best be in the ground!"

        Ciel "I will be there, I promise. I have to do this."

        Jean "Ok. Ok. Merde. I know. Of course you do. Go. I’ll make sure Claude makes it out."

        Ciel "Ok. And, Jean?"

        Jean "Yes?"

        Ciel "I love you."

        Jean "Not the time! Of course I love you too, as long as you don’t get yourself killed! Go, do what you must!"

        hide Ciel with moveoutleft

        jump gendarme_aftermath


    label gendarme_takeClaude:

        Ciel "I will be there, I promise. I have to do this."

        Jean "I know. Of course you do. You always do. Go! I’ll make sure Claude makes it out."

        Ciel "Ok. And, Jean?"

        Jean "Yes?"

        Ciel "I love you, mon canari."

        Jean "And I love you, mon fou! Now go, before it’s too late!"

        hide Ciel with moveoutleft

        jump gendarme_aftermath


    label gendarme_aftermath:

        Angry_Young_Parisian "Come on, let’s go!"

        Frustrated_Protester "Run!"

        Helpful_Agitator "Come on, mec. I have you!"

        Jean "Come now, Claude. It’s time for us to go!"

        Claude "I think this is the end of me, mon ami…Just leave me..."

        Jean "You’re a lucky fool. It’s just a bruise. They didn’t hit a bone. You’ll be fine in a week. Can you walk?"

        Claude "I don’t think so…"

        "*thump*"

        Jean "Merde. I guess there is no choice, then."

        Claude "W-what are you doing!"

        Jean "Ugh...What does it look like? I’m carrying you, you idiot!"

        Claude "What about Ciel?"

        Jean "She will...hah..catch up with us…"

        "*bang bang bang bang*"

        Jean "I hope…"

        hide Claude with moveoutright
        hide Jean with moveoutright
        hide bg champs_elysees with dissolve

label scene4:
    "17 March, 2019 - The Safehouse"

    show bg champs_elysees with dissolve

    Newscaster "--the violence on the streets of the Champs-Elysées has reportedly left over 500 protestors and 15 military personnel injured. Eye witnesses report a few scattered fatalities, but authorities have yet to corroborate those reports. The President’s office did not reply to a request for comment."

    Newscaster "A curfew is now in effect on the streets of Paris between the hours of 19:00 and 4:00. We go now to footage of President Macron’s address to the nation, which he gave last night after sending in--"

    show Claude at left with dissolve
    show Jean at center with dissolve

    Claude "That’s enough of that, eh?"

    Jean "Hey! I was watching that."

    Claude "Aye, you were, mon ami. You’ve scarce done anything else since we got here. A break would do you some good, yeah?"

    Jean "..."

    Claude "Look, Jean. I know you are worried about her. We all are. But getting into a funk won’t help anything."

    Claude "Without Ciel, you are in charge now. At least try to look the part, yeah?"

    Jean "And why is that? I never asked to be in charge of anything! Look the part? I don’t want the part. I just want Ciel…"

    Claude "So do we all, but we will not find her by staying glued to the newscast all day, now will we?"

    Jean "*sigh*"

    Jean "I just...i just don’t know what to do, Claude. I am not Ciel. I cannot just go around and tell everyone it will be ok when I feel as though the sky has fallen!"

    Jean "She is a leader. She can lift people up. I am just a nurse. I can only put them back together."

    Claude "Well, Mr. Nurse, how about you start by putting yourself back together, then we can talk about what comes next, yeah? The way you look, you’d think you were the one to take a bullet."

    Jean "That bad, huh?"

    Claude "You smell like you just raided a liquor store, mon ami. Speaking of, you don’t have any of that brandy left, do you?"

    Jean "See for yourself…"

    Claude "Good god, Jean, I didn’t know you had it in you! The whisky too?"

    Jean "And the gin, the rum, the…"

    Claude "Okay, okay. I get the point. Clean yourself up, man. I’m surprised you’re still conscious."

    Jean "That’s funny, coming from you. Do you not remember the benders you used to drag me on? Where do you think I built up this tolerance?"

    Claude "No, mon ami, I do not. Remember, any night of debauchery you can remember the day after is a night poorly spent."

    Jean "Yeah, yeah. Ahh, merde! My head is about to explode. Get me some ice water, wil--"

    "*knock knock knock knock*"

    Jean "Baise moi! Who is that? The gendarme?"

    Claude "Relax, mon ami. The gendarme only knock with battering rams, not their fists. It is a friend."

    Jean "A friend?"

    Claude "Yeah. While you were busy drowning your sorrows, I was being a bit productive, yeah?"

    Claude "I’ve had our people out in all of the hospitals looking for Ciel. It was only a matter of time before she was found."

    Jean "Really? I..did not think you had it in you."

    Claude "Well, someone had to step up while you were drinking yourself into oblivion, no?"

    "*knock knock knock knock*"

    Claude "YEAH, YEAH, I’M COMING!"

    show Claude at right with move
    show Young_Parisian_Lieutenant at right with moveinright
    show Claude at left with move

    Young_Parisian_Lieutenant "*huff huff*"

    Young_Parisian_Lieutenant "Claude! Jean! Thank god I found…*huff huff*"

    Claude "Hey, hey, hey. Take a breath, yeah? You look as bad as he does."

    Jean "Casse-toi. I’m fine."

    Claude "Yeah? Then bring her some water, why don’t you?"

    Jean "Alright, alrigh--"

    Young_Parisian_Lieutenant "*huff huff* I found her!"

    Claude "You did?"

    Jean "Where?! Where is she? Come Claude, we have t--"

    Claude "Calm down, man. It is not safe for us outside. Did you not hear about the curfew?"

    Young_Parisian_Lieutenant "I’m..I’m sorry…"

    Jean "Why? What’s wrong?! Is she hurt?"

    Young_Parisian_Lieutenant "Badly. I talked to some other protestors who saw her get taken. They described her perfectly."

    Young_Parisian_Lieutenant "They said she made time for them to get away. She...They say she fought the gendarme with only her fists."

    Jean "Oh, Ciel…"

    Young_Parisian_Lieutenant "It...it gets worse. They..they beat her, and took her to a military hospital under arrest. I..I saw her there…"

    Jean "And? How is she?"

    Young_Parisian_Lieutenant "I...I couldn’t get close. There were so many guards...I didn’t want them to suspect…"

    Jean "How. Is. She?"

    Young_Parisian_Lieutenant "...Not good, Jean. It looks like they beat her pretty badly. She wasn’t conscious."

    Claude "Sweet god…"

    Jean "C'est des conneries! Come, Claude. We have to go!"

    Claude "Wha-- Mon ami, you must be kidding. To walk into there would mean certain capture…"

    Jean "Then what else do you want to do? We cannot just leave her there!"

    Claude "I don’t like it either, Jean, but think! Do you think marching in there and getting yourself killed will make Ciel any happier? Didn’t you hear her? That place is swarming with gendarme!"

    Young_Parisian_Lieutenant "I’ve never seen so many..."

    Jean "Allez, va t'en! I’ll not leave her to the pigs!"

    Claude "No one is saying we should, mon ami. But we cannot just walk in there without a plan, and you’re in no condition to make one!"

    Jean "Ugh! Merde! Baise moi! Fais Chier!"

    Claude "Jean! This is not like you. You need to calm down, yeah? Fuming will do nothing to help Ciel. We need your mind right now, not...whatever this is!"

    Jean "*sigh*"

    Jean "Sorry. You are right. It’s just, when I think about her being beaten like that…"

    Claude "I know, I know. I feel the same way, mon ami. She is my friend too. Feeling better now?"

    Jean "Of course not, idiote. I’ll not be better until we have her back. But you are right. We cannot move yet."

    Jean "..."

    Jean "Thank you, Claude. I was not myself."

    Claude "No, of course you were not. What kind of man would be, with his love snatched away?"

    Young_Parisian_Lieutenant "So what do we do, Jean?"

    Jean "...I do not like it, but we cannot move yet. We need to regroup, and we need a plan."

    Claude "What sort of plan?"

    Jean "I...don’t know yet. I can’t think. Every time I try to, I just see her there…"

    Claude "Then we must turn our minds to happier times, yeah? Then you will be able to think clearly."

    Jean "‘Happier times’? How do you propose we do that?"

    Claude "That is easy, mon ami. Just tell a story about happy times, yeah? Oh, I know! Tell the story of how you and Ciel met!"

    Jean "Why? You were there. You already know how it happened."

    Claude "Yes, but she was not. She probably has no idea how it happened, right?"

    Young_Parisian_Lieutenant "No, but…"

    Claude "See? It is settled! Tell us a story, Jean!"

    menu:
        "This is stupid.":
            jump refuse_storytime

        "Fine, fine.":
            jump accept_storytime

    label refuse_storytime:

        Claude "Ah, come on! Don’t be so close-minded, mon ami. Besides, what else have you to do?"

        Jean "Think of a plan to rescue Ciel?"

        Claude "And you think you will do a good job of it while you’re depressed and hung over? You are a smart man, Jean, but you are not a miracle worker. Well, I don’t think so, at least. Are you?"

        Jean "What? No, of course not!"

        Claude "Then take some time to set your mind at ease, yeah? You’ll think better that way, and you’ll entertain this lovely lady while you’re at it, right, my dear?"

        Young_Parisian_Lieutenant "Uhh…"

        Jean "Give it up, Claude. Can you not see she is married already? I can tell as romantic a story as you like, you still won’t score."

        Claude "What? Get your mind out of the gutter, Jean. I had no such int--"

        Jean "Don’t give me that. I saw where you were looking."

        Claude "At my best friend, with concern! Now will you tell the story, or not?"

        Jean "Fine, fine. But get me some ice water, first. I’m about to have the hangover of hangovers…"

        jump storytime_end

    label accept_storytime:

        Claude "Yes! I knew you would come around, mon ami. Now, my dear, listen closely. It’s truly a very romantic story."

        Young_Parisian_Lieutenant "Oh? Is it…? But…"

        Jean "Lay off, Claude. Can you not see she is not into you?"

        Young_Parisian_Lieutenant "What?! I, I didn’t--"

        Claude "Jean, you wound me! Do you think so low of me? Your mind is in the gutter, my friend."

        Jean "If it is, it is only because you dragged it there. Now, get me some water while I figure out where to start…"

    label storytime_end:

        hide Claude with dissolve
        hide Jean with dissolve
        hide Young_Parisian_Lieutenant with dissolve

        hide bg champs_elysees with dissolve







label end:
    return
