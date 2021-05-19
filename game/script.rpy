# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# main cast and their variations
define Jean = Character("Jean")
define Moody_Medic = Character("Moody Medic")
define Ciel = Character("Ciel")
define Radiant_Redhead = Character("Radiant Redhead")
define Claude = Character("Claude")
define Rambunctious_Ragamuffin = Character("Rambunctious Ragamuffin")

define question_marks = Character("???")

# side characters
define Worried_Protester = Character("Worried Protester")
define Dehydrated_Protester = Character("Dehydrated Protester")
define Agitated_Protester = Character("Agitated Protester")
define Frustrated_Youth = Character("Frustrated Youth")
define Downtrodden_Worker = Character("Downtrodden Worker")
define Disgruntled_Worker = Character("Disgruntled Worker")

# images

# backgrounds
image bg champs_elysees = "champs-elysees.jpg"

# main characters and their variations
image Jean = "macaron.jpg"
image Moody_Medic = "macaron.jpg"
image Jean flip = im.Flip("macaron.jpg", horizontal="True")
image Ciel = "macaron.jpg"
image Radiant_Redhead = "macaron.jpg"
image Claude = "macaron.jpg"
image Rambunctious_Ragamuffin = "macaron.jpg"

# side characters
image Worried_Protester = "fondue.jpg"
image Dehydrated_Protester = "fondue.jpg"
image Agitated_Protester = "fondue.jpg"
image Frustrated_Youth = "fondue.jpg"
image Downtrodden_Worker = "fondue.jpg"
image Disgruntled_Worker = "fondue.jpg"

# The game starts here.

label start:
    jump scene1

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
    


label end:
    return
