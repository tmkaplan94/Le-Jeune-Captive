# The script of the game goes in this file.

init python:
    config.screen_width = 1280
    config.screen_height = 720

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# main cast and their variations
define Jean = Character("Jean")
define Moody_Medic = Character("Moody Medic")
define nvl_narrator = Character("", kind=nvl)

# side characters
define Worried_Protester = Character("Worried Protester")
define Dehydrated_Protester = Character("Dehydrated Protester")

# images

# backgrounds
image bg champs_elysees = "champs-elysees.jpg"

# main characters and their variations
image Jean = "macaron.jpg"
image Moody_Medic = "macaron.jpg"
image Jean flip = im.Flip("macaron.jpg", horizontal="True")

# side characters
image Worried_Protester = "fondue.jpg"
image Dehydrated_Protester = "fondue.jpg"

label scene1:

    scene bg champs_elysees with None

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
