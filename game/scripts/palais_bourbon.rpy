screen ciel_office():
    imagemap:
        ground "Daniel - Ciel Office.jpg"
        hover "Ciel Office Highlighted.png"
        hotspot (754, 369, 116, 116) clicked Jump("palaisb_desktop")
        hotspot (641, 460, 95, 65) clicked Jump("palaisb_desk")
        hotspot (880, 471, 77, 54) clicked Jump("palaisb_photo")
        hotspot (216, 238, 134, 87) clicked Jump("palaisb_painting")
        hotspot (407, 108, 316, 307) clicked Jump("palaisb_poster")


label palais_bourbon:
    scene palais bourbon outside with fade
    show Jean at left with dissolve

    Jean "(... Doesn’t seem like anybody else is around.)"

    Jean "(Alright, up the stairs then, and down to the East wing. Damn, Ciel’s office is far.)"

    hide Jean with moveoutright

    scene palais bourbon hallway with fade

    show Jean at left with moveinleft

    Jean "(Nearly ten years of this and this place still feels like a maze. Hold on a second- is someone coming?)"

    menu:
        "Run down another corridor":

            jump palaisb_run

        "Hide":

            jump palaisb_hide

        "Act Natural":

            jump palaisb_act_natural


label palaisb_run:
    Jean "(Let’s book it.)"

    hide Jean with moveoutright

    scene palais bourbon hallway with fade

    show Jean at left with moveinleft

    Jean "*Huff* *Huff*"

    Jean "(Doesn’t look like they followed me, but where the hell am I?)"

    Jean "(This sign for this corridor says… Southern Wing. So then I need to go…)"

    menu:
        "Left":
            jump palaisb_run_left

        "Right":

            jump palaisb_run_right


label palaisb_run_left:
    Jean "Well, I want to go east, so I should go left from here...."

    question_marks "Stop right there!"

    Jean "Oh, Baise moi."

    show Security_Guard at right with moveinright

    Security_Guard "Oh, Minister Hobier! Were you the one running around?"

    Jean "Yes, it was me.  I am in a bit of a hurry, so if you’ll excuse m--"

    Security_Guard "Ah, I see.  I didn’t mean to startle you, sir, but we’re on high alert. Representative Touti came by earlier and notified security about a suspicious individual lurking around the South Wing..."

    Jean "(Merde! So that was Claude back there, don’t know if I made it easier for myself.)"

    Jean "Well, I haven’t seen anyone else up here. It’s just me."

    Security_Guard "Alright then, just… be careful, Minister. Wouldn’t want anything to happen to you when nobody’s around."

    Jean "Will do."

    hide Security_Guard with moveoutleft

    Jean "(Alright, to Ciel’s office.)"

    jump palaisb_coffice


label palaisb_run_right:

    Jean "Well, I want to go east, so I should go right from here..."

    Jean "Wait… Merde! What am I thinking? That’s not rig--"

    question_marks "Hey, hold it right there!"

    Jean "Oh, Baise moi."

    show Claude at right with moveinright

    Claude "Oh! Mon ami? You the madman who’s been making all that noise?"

    Jean "Wouldn’t say I’m insane just yet, but yes."

    Claude "Well baise moi mor! I know you’re the Minister of Health and all, but there’s gotta be a better way to get your exercise in."

    Claude "Do you have any idea how creepy it is to hear some abruti running around when this place is supposed to be locked up tight?"

    Claude "Wait... No one is supposed to be here, so what are you doing here, anyways?"

    jump palaisb_claude


label palaisb_hide:
    Jean "(Hide! But where? These halls are practically bare! There’s just...Oh no...)"

    Jean "(Well, nothing for it. Hope this planter is big enough.)"

    show Jean at center with move

    "..."

    question_marks "C'est quoi ce bordel? Is that you, Jean? The hell are you doing, mon ami? Watering the ficus?"

    show Claude at right with dissolve
    show Jean at left with move

    Jean "Claude?! I, uh... "

    menu:
        "Yes, I was. And giving it a good inspection, too.":

            Claude "Right. Of course you were. Well, does it mean government standards?"

            Jean "Green leaves, strong stem, wet soil, I’d say so, yes."

            Claude "Good, good. Glad to hear it. Now cut the crap, mon ami. What’s really up?"

        "What am I doing here? What are YOU doing here, Claude?":

            Claude "Well, you know… I was sittin’ at my desk, getting some good work done, you know? And before I knew it, my eyes got just a bit heavy…"

            Claude "And now I have to get all caught u-- Wait, I’m not the suspicious one here. What are you sneaking around for?"

        "Just taking a break.":

            Claude "Getting tired just from walking over here? I suppose it is not a requirement for the Minister of Health to be healthy, then?"

            Jean "Haha. You truly have a gift for comedy. Remind me, when was the last time you did a full day’s work?"

            Claude "Hey, hey, hey! Low blow, mon ami. I just work at my own pace, ok? So, what are you doing here, anyways?"

    jump palaisb_claude


label palaisb_act_natural:
    Jean "Just act natural, Jean. You’re the Minister of Health, nothing strange about you being here."

    show Claude at right with moveinright

    Jean "Oh, of all the rott--."

    Claude "Mon Ami! Didn’t expect to see you here over the weekend."

    Jean "Didn’t expect to see you either. Not that we see you here during the week, either."

    Claude "Me? The work must get done some time, eh mon ami? I prefer having the office all to myself. It would be weirder if I wasn’t around. Security doesn’t even bat an eye."

    Claude "What are you doing here, though? Your office is on the other side of the building."

    jump palaisb_claude


label palaisb_claude:
    Jean "Ciel forgot a few things on her desk. She was too busy to get them herself, and so here I am."

    Claude "Not like her to forget something, nor is it like her to ask someone to do something for her."

    Jean "First time for everything."

    Claude "Hmm…I wonder... Are you sure everything is alright, mon ami? You two aren’t fighting are you? I can talk to her for you!"

    Jean "Even if something was wrong -- which it isn’t -- why would I come to a virgin for relationship advice?"

    Claude "I’m serious, Mon ami! You know you can tell me anything, right?"

    Jean "*sigh*"

    Jean "Yes, yes... Everything’s fine, Claude. I’ll figure things out."

    Claude "Ok, ok. I know better than to get in your way, Jean. Just promise me that you’ll call on me if it gets to be too much for you. Without you, I’d be the ugliest connard in Paris, yeah?"

    Jean "I- Thanks, Claude. And you’ll always be the ugliest connard in Paris."

    hide Claude with moveoutleft

    Jean "(I’m sorry, Claude. This is something I need to do myself.)"

    Jean "(Alright, to Ciel’s office.)"

    hide Jean with moveoutright

    jump palaisb_coffice

label palaisb_coffice:

    scene ciel office with fade

    show Jean flip at right with moveinright

    Jean "(Here we are. Now… where to look?)"

    init python:
        desk = False
        painting = False
        poster = False
        photo = False

label palaisb_investigation:

    call screen ciel_office

label palaisb_desktop:

    Jean "(Ciel’s computer, I don’t know what her password is though. Ah, there’s a password hint.)"

    Jean "(\"4 digits, a special day.\")"

label palaisb_password:
    menu:
        "0130" if desk:
            Jean "(January 30th… Let’s give it a shot. … No dice.)"
            jump palaisb_password
        "0512" if painting:
            Jean "(Let’s try my birthday. … Nope.)"
            jump palaisb_password
        "0901" if poster:
            Jean "(Let’s try her birthday. … It was really that easy.)"
            jump palaisb_documents
        "1214" if photo:
            Jean "(Our wedding day, maybe? … Nope.)"
            jump palaisb_password
        "EXIT":
            Jean "(Maybe something around her office will help me.)"
            jump palaisb_investigation

label palaisb_desk:
    Jean "(Hmm… There’s mostly just old memos in her desk compartments…)"

    Jean "(Oh? What’s this?)."

    Jean "(A crumpled sticky note. \"January 30th, usual place, come alone.\")"

    Jean "..."

    $ desk = True

    jump palaisb_investigation

label palaisb_photo:

    Jean "(It’s a photo of our wedding day... December 14th. I’ll never forget the sight of her in that wedding dress.)"

    $ photo = True

    jump palaisb_investigation

label palaisb_painting:

    Jean "(It's a painting we bought on our trip to Spain.)"

    Jean "(When I told her I always wanted to go there I didn't think she'd book us a vacation for my birthday.)"

    Jean "(Hmm... My birthday... May 12th.)"

    $ painting = True

    jump palaisb_investigation

label palaisb_poster:

    Jean "(This poster… Claude gave it to Ciel on her birthday a few years ago. I half expected her to to roll it up and smack him upside the head with it. Instead she just started laughing so hard tears started coming out.)"

    Jean "(Maybe her birthday is the password? September 1st. Nah, it couldn’t be that simple… Could it?)"

    $ poster = True

    jump palaisb_investigation


label palaisb_documents:
    Jean "(Well, I’m in. Now what?)"

    Jean "(I don’t think there would be anything to hide in her emails, not like she only uses this computer for it. Let’s check the document folders.)"

    Jean "(Meeting minutes, proposals, correspondences, reports…)"

    Jean "(... And an untitled folder. Hmm. Let’s check that out.)"

    Jean "(Jackpot. Now, what should I look at?)"

    $ proof = 0

    jump palaisb_pc


label palaisb_pc:
    menu:
        "TAX CUTS":
            jump palaisb_tax

        "MILITARY BUDGET":
            jump palaisb_military

        "ELECTION RIGGING":
            jump palaisb_election

        "<EXIT>":
            jump palaisb_end


label palaisb_tax:
    nvl_narrator """
    Minister Rousseau,

    We are displeased with the proposal of higher income tax rates on the upper brackets. We understand that the bill has immense popular support, and will not demand its outright repeal.

    Be that as it may, the bill as it stands now is unacceptable for many of our councillors. We ask that you cooperate with us to introduce a set of amendments to the bill to allow for tax write-offs

    equivalent to the increase in taxation. We will send the specific instructions in a separate missive.

    DELETE THIS MISSIVE ASAP"""

    nvl clear

    $ proof += 1

    jump palaisb_pc

label palaisb_military:
    nvl_narrator """
    Minister Rousseau,

    Many councillors are invested in enterprises related to the production of military armaments. Ensure that there will be a substantial increase in the military budget, at minimum a 20%% from last year.

    Rest assured we have no interest in antagonizing other nations with our armed forces.

    DELETE THIS MISSIVE ASAP
    """

    nvl clear

    $ proof += 1

    jump palaisb_pc

label palaisb_election:
    nvl_narrator """
    Minister Rousseau,

    Concerns have emerged over the current election projections in the Seine Department. We are confident in our ability to retain our political hold over the department, but there are too many

    liabilities with the current selection of political candidates. We ask that you use your influence to secure our victory. Attached is a list of candidates we desire to hold office.

    Memorize it and destroy the evidence.

    DELETE THIS MISSIVE ASAP"""

    nvl clear

    $ proof += 1

    jump palaisb_pc

label palaisb_end:

    if proof < 3:
        Jean "(There’s still some documents to look at.)"
        jump palaisb_pc

    else:
        Jean "(This is… quite a lot to take in.)"

        Jean "(I need to copy the evidence. Where’s my flash drive? Ah, here.)"

        Jean "(... Alright, got it. Time to leave.)"

        hide Jean with moveoutright

        scene palais bourbon outside with fade

        show Jean with moveinright

        Jean "(That felt… almost too easy. It’s almost like Ciel wanted me to find it.)"

        Jean "(Seriously, her birthday as the pin, all of the evidence into one obvious folder, and all of it intact? Not to mention that they all should have been deleted.)"

        Jean "(That woman is simply unfathomable.)"

        jump tresor_nationale
