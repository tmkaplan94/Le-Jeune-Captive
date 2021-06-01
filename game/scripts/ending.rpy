##################################################
# Scene Ending: Le Grand Roi
##################################################

label ending:

    scene bg LeGrandRoi sidewalk with None

    "Walking to Le Grand Roi theatre."

    show Ciel_Dress at right with moveinright

    Ciel "I still can’t believe I let you talk me into this."

    show Ciel_Dress at center with moveoutleft
    show Jean flip at right with moveinright

    Jean "Every month a new film comes out and every month you make excuses not to go with me. Do you not remember the joy we once had at the cinemas?"

    Ciel "… I do."

    Jean "Do you not miss those nights?"

    Ciel "Of course I do my love, just…"

    show Ciel_Dress at left with moveinright
    show Jean flip at center with moveinright

    Ciel "not on a night like tonight."

    Jean "Excuse me?"

    Ciel "I mean, I would have much preferred kicking your ass at chess under tonight’s moonlight. Maybe I would have let you win for a change."

    Jean "What do you mean by, ‘not on a night like tonight’?"

    Ciel "It’s nothing, I just want tonight to be special, that’s all… and these films bore me half to death!"

    hide Ciel_Dress with moveoutleft
    show Jean flip at left with moveoutleft

    Jean "Hmm..."

    hide Jean flip with moveoutleft

    scene bg LeGrandRoi protest with Pause(2)
    scene bg LeGrandRoi front with fade
    show Ciel_Dress at center with moveinright
    show Jean flip at right with moveinright

    Ciel "No no, why are they protesting here?"

    show Ciel_Dress flip at center

    Ciel "Let’s skip the film tonight."

    Jean "What’s gotten into you, it looks like you’ve seen a ghost?"

    Ciel "I’m just worried that things will escalate."

    Jean "Why would things escalate? It seems peaceful enough to me."

    Jean "I just don’t understand why they’re protesting. After everything we’ve fought for, everything we’ve struggled to achieve… we should be on the same side."

    show Ciel_Dress at center

    Ciel "We once were... fighting for the same thing. But now it seems I’ve lost my way."

    Jean "Seriously Ciel, what’s wrong?"

    scene bg LeGrandRoi riot1 with fade

    Ciel "It wasn’t supposed to end like this."

    Jean "Wow, you were right about the escalation, huh Ciel? Wait, they sent a riot squad??"

    scene bg LeGrandRoi riot2 with fade

    Ciel "Jean, quick, I must tell you something!"

    Jean "Ciel, we have to stop this!"

    Ciel "No wait!"

    show Police_Chief flip at left with dissolve
    show Jean flip at right with moveinright

    Jean "Stop immediately! I am Jean Hobier, a member of The Council. I am ordering you to stop this at once!"

    Police_Chief "Sorry sir, we have orders to deescalate all unauthorized political gatherings."

    Police_Chief "...by ANY and ALL means necessary."

    Jean "What are you saying! On whose authority!?"

    Police_Chief "Ciel Rousseau, now please step aside unless you would like to join them!"

    show Jean at right
    hide Jean with moveoutright

    scene bg LeGrandRoi front with fade
    show Ciel_Dress at center
    show Jean at left with moveinleft

    menu:
        "Confront":
            jump confront_dialogue

        "Console":
            jump console_dialogue

label confront_dialogue:

    Jean "Ciel! How could you?!"

    Ciel "It’s not what you think."

    Jean "Look at what you’ve done. These people are being attacked like animals. How is this not what I think?"

    Ciel "It wasn’t supposed to go this far."

    Jean "What wasn’t supposed to go this far?"
    Ciel "..."

    Jean "Just tell me the truth and stop lying!"

    Ciel "I made a deal a long time ago with some very powerful people. They offered me a chance to make a difference. A chance to actually change things."

    Jean "At what cost Ciel? You made a deal with the devil, and now this blood is on your hands."
    Ciel "I was trapped! I had no one to turn to."

    Jean "Really? Nobody at all?"

    Ciel "I never meant to hurt anyone… least of all you."

    Jean "Well we’re far past that, aren’t we?"

    Ciel "I didn’t want it to end this way. I wanted one last night with you."

    Ciel "...one last night to remember us the way we once were."

    Jean "You were gonna run away!"

    Ciel "I have no choice! They’re never going to let me escape their control."

    Ciel "Come with me…"

    menu:
        "Run away with Ciel.":
            jump ending_leave

        "Stay and leave Ciel behind.":
            jump ending_stay


label console_dialogue:

    Jean "Ciel, what’s going on? The officer said you ordered this, is it true?"

    Ciel "I am so sorry you had to find  out this way."

    Jean "I can’t help you if you don’t tell me what’s going on."

    Ciel "Nobody can help me. I’m trapped and there’s no going back now."

    Jean "How are you trapped, are you in danger??"

    Ciel "I made a deal a long time ago with some very powerful people. They offered me a chance to make a difference. A chance to actually change things."

    Jean "This is what you’ve been doing behind my back? Why didn’t you come to me for help?"

    Ciel "I didn’t want to involve you, you deserve better than this."

    Jean "I know that look… what are you planning Ciel?"

    Ciel "I have no choice but to run. They’re never going to let me escape their control."

    Ciel "Come with me…"

    menu:
        "Run away with Ciel.":
            jump ending_leave

        "Stay and leave Ciel behind.":
            jump ending_stay

label ending_leave:

    Jean "And what, leave everything behind... everything we've worked so hard to achieve??"

    Ciel "And would you be okay leaving me behind?"

    Jean "There has to be another way..."

    Ciel "You don't understand, I have no choice. They'll kill me!"

    Ciel "I can't live like this, people are suffering because of me."

    Ciel "It goes against everything I stand for."

    Jean "Ciel..."

    Jean "You leave me no choice. Who's going to be there to protect you?"

    Ciel "*smiles*"

    Jean "*smirk*"

    Jean "We can figure this out together. When do we leave?"

    scene bg start Paris with fade
    "La Fin"

    return

label ending_stay:

    Jean "And what, leave everything behind... everything we've worked so hard to achieve??"

    Ciel "And would you be okay leaving me behind?"

    Jean "Don't turn this around on me!"

    Ciel "You don't understand, I have no choice. They'll kill me!"

    Ciel "I can't live like this, people are suffering because of me."

    Ciel "It goes against everything I stand for."

    Jean "Ciel..."

    Jean "If we run now, they'll never stop chasing us."

    Jean "I can't follow you down this path any longer."

    Jean "I'm sorry, but I need to go."

    Ciel "*sobs*"

    scene bg start Paris with fade
    "La Fin"

    return
