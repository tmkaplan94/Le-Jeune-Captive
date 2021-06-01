##################################################
# Scene 3: The Pigs Arrive
##################################################

label scene3:
    scene bg frontline with fade

    "16 March, 2019 - Champs-Elysées - The Frontlines"

    show Claude at left with moveinright
    show Ciel at center with moveinright
    show Jean flip at right with moveinright

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

        scene bg frontline with fade

        "Moments later..."

        show Claude at center with moveinright
        show Jean flip at right with moveinright

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
        show Jean flip at right with moveinright

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


        scene bg frontline with fade

        "*A Few Hours Later*"

        question_marks "You are in violation of a citywide curfew. Leave this area now, or we will be forced to remove you forcefully!"

        Angry_Young_Parisian "Avale mes couilles, pigs!"

        Frustrated_Young_Parisian "This is a public space! We’re not going anywhere!"

        show Claude at right with dissolve
        show Jean flip at center with dissolve

        Jean "You’d think they’d have figured out by now that yapping on a loudspeaker isn’t going to accomplish anything."

        Claude "Well, mon ami, they are the pigs. They are not known for being smart, no? They could just tax the rich and fix the fuel prices, then none of this would be happening."

        Jean "Right. Let me know when you manage to convince the rich to tax themselves. It’s not like the representatives are the ones in bread lines."

        show Ciel flip at left with moveinleft

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
        show Jean flip at right with move
        show Ciel at center with move
        show Young_Parisian_Lieutenant at left with moveinleft

        Young_Parisian_Lieutenant "Yes, Ciel?"

        Ciel "Go around and make sure everyone gets their masks on. Move anyone without a working mask further south down the Champs."

        Young_Parisian_Lieutenant "Are we being gassed?"

        Jean "If we’re luck--"

        Ciel "Ignore him. I don’t know, but we should be prepared. Now hurry, it sounds like they’re not wasting any time."

        hide Young_Parisian_Lieutenant with moveoutleft
        show Ciel at left with move
        show Jean flip at center with move
        show Claude at right with moveinright

        Mousat "This is your last warning. Begin leaving now, or face arrest!"

        Jean "Ciel…"

        Ciel "You know I’m not leaving."

        Jean "That doesn’t mean we have to stand in the front lines! Claude, talk some sen--"

        show Claude at left with move
        show Ciel at center with move
        show Jean flip at right with move

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

##################################################
# End Scene
##################################################
    jump scene4
