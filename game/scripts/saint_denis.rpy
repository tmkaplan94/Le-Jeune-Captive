screen poll_office():
    imagemap:
        ground "pollOffice.jpg"
        hover "pollOfficeHighlighted.jpg"
        if box_there:
            hotspot (1095, 393, 184, 312) clicked Jump("saint_denis_empty_box")
        if trash_there:
            hotspot (432, 456, 118, 155) clicked Jump("saint_denis_trash")
        if ballots_there:
            hotspot (391, 198, 171, 157) clicked Jump("saint_denis_suspicious_ballots")

init python:
    box_there = True
    trash_there = True
    ballots_there = True


label saint_denis:

    scene alley with fade

    show Claude at right with dissolve
    show Jean at left with dissolve

    Claude "…Achoo!"

    Jean "Quiet connard! Do you want to be caught?"

    Claude "Do I want to be caught? You’re hiding here with me too, aren’t you? Going to be hard to explain why the Minister of Health is hiding behind the Saint-Denis election office with a toy gun."

    Jean "It’s the best I can do on short notice, we have to get into this building before the original paper ballots are moved off site. It’s good enough to threaten some under-paid security guard."

    Claude "I hope you aren’t expecting a birthday present from me this year, mon ami. Did you have to choose one that was this expensive? I don’t have a minister’s salary."

    Jean "It needs to look real, debile. And how would I explain to Ciel why I bought an airsoft replica? At least you seem like the kind of person to have this hobby."

    Claude "Yes, of course mon ami. You’ve never been interested in anything in your entire—OW!"

    Jean "Shush! He’s supposed to be locking up the rear exit any second now. Do you remember what to do when we get the keys from him?"

    Claude "Yes, yes. You threaten the guard with your toy and I take the keys. You will do all the talking and I will just keep quiet."

    Jean "Yes, say nothing. I can handle this my—"

    Claude "—unless it’s a lady security guard, of course. In that case I can seduce her into giving us the keys painlessly. Maybe she can give us a tour of the—OW! You don’t have to keep doing that!"

    "*Crash*"

    Guard "Merde! What branleur put these damn trash cans here?!"

    Claude "Tch, it’s a guy."

    Jean "Put on your mask. C’est parti."

    show Claude at center with move

    show Guard at right with moveinright

    "*Gun clicks*"

    Jean "Hands up, don’t you fucking move."

    Guard "Ah—! C'est quoi ce bor-"

    Jean "Put your goddamn hands up against the door or you’re a fucking dead man!"

    Guard "…"

    Jean "Okay Claude—"

    Claude "…he really just said my name."

    Jean "I mean—uh, Claudio. Take the keys."

    Claude "…Sure thing, Jeanelle. Whatever you say, Jeanelle."

    Guard "…"

    Claude "Uh, he won’t let go of them."

    Jean "Let go of the keys mec. Not unless you want to see your family tomorrow."

    Guard "…Is this your first time threatening someone at gunpoint, Jeanelle?"

    Claude "Pfft..."

    Guard "You two lose a bet or something? Because this has to be the worst shakedown I’ve ever seen."

    Jean "…Claude, help me out here."

    Claude "…I think I’ll let you handle this one."

    menu:
        "Explain":
            jump saint_denis_explain
        "Threaten":
            jump saint_denis_threaten

label saint_denis_explain:

    Jean "Okay look, we both know you aren’t paid enough to die in this alleyway, so give us the keys and we won’t hurt you. My friend here and I just want to take a quick look inside. Nothing suspicious."

    Guard "Like I can believe that. I know what this building is for."

    Jean "Then you know the election is already over. The results are already in and the ballots have already been scanned and saved elsewhere. Anything we do in there won’t change anything."

    Guard "What goes on in there is above my pay but it’s clear to me that you two bouffons shouldn’t be snooping around in there."

    Jean "*sigh* Why are you being so difficult? Give us the keys and we won’t kill you! Is this really the hill you want to die on?"

    jump saint_denis_int

label saint_denis_threaten:

    Jean "What did you say about me, petit connard? I’ll have you know I graduated top of my class from the Groupe d'intervention—"

    Claude "Pfft!"

    Guard "What the fuck are you even saying? For a prank, you two are taking this pretty—"

    Jean "You feel that? I can end your life right here, right now. We have to get into this building tonight and it seems we can no longer afford to waste our time, comarade."

    Guard "I don’t get paid enough to deal with bouffons like you, but it’s clear to me that you won’t kill me since I’ve been at your mercy for quite a while now, Jeanelle."

    Jean "Last chance, if you don’t want to die you will hand over the keys."

    jump saint_denis_int

label saint_denis_int:

    Claude "*sigh* Okay, I think that’s finally enough."

    "*click*"

    Jean "Is that a switchblade?! What are you—!"

    show Claude at right with move
    show Claude at center with move

    "*Slam*"

    Guard "OW! you little—"

    Claude "What my friend here is trying to say is…"

    Claude "Give us the fucking keys or I am going to open up your neck like a clam."

    Guard "You can’t scare—OW!"

    show Claude at right with move
    show Claude at center with move

    "*Slam*"

    Claude "I don’t like having to repeat myself. I’m going to count down from five, and if you don’t drop those keys, a new gravestone is going to suddenly appear in the nearest cemetery."

    Claude "Cinq, quatre, trois— "

    Guard "Baise moi, fine! Take the damn things."

    Claude "Merci beaucoup. Just one more thing..."

    Guard "—! Zip-ties?! Really?! C'est quoi ce bordel, I already—"

    show Claude at right with move

    Jean "Shush. No more talking from you."

    show Claude at center with move

    Guard "*angry muffled talking*"

    Claude "Sorry mec, but there’s one last thing we need from you. Last thing, I promise."

    "*Keys clink*"

    Claude "Which one of these goes to the supply closet?"

    jump saint_denis_office

label saint_denis_office:

    scene poll office with fade

    show Jean at left with moveinright
    show Claude at right with moveinright

    Jean "Finally. We’re finally inside this godforsaken building."

    Claude "We only got inside because of me, mon ami. Not to say I didn’t enjoy every second of your circus act with that guard."

    Jean "..."

    Claude "Why are you looking at me like that?"

    Jean "It’s just kind of weird seeing you all serious like that. If you acted like that more often...wait, why didn’t you just do that from the start?!"

    Claude "You were the one who told me not to say anything, didn’t you? Besides, I would be lying if I said I wasn’t looking forward to your little negotiation with the guard when you told me the plan."

    Jean "...Next time, you can play bank robber."

    Claude "Next time, I can come up with the aliases before we hold someone at gunpoint."

    Jean "Allez, va t'en."

    Jean "Now, Ciel…what are you hiding in here?"

label saint_denis_investigation:
    call screen poll_office


label saint_denis_trash:

    $ trash_there = False

    Jean "Claude, what are you—"

    Jean "Quit digging around in the trash like a raccoon and help me look around!"

    Claude "What do you think I’m doing here? There’s a bunch of shredded paper in here someone forgot to throw out. You might want to see this."

    Jean "*sigh* What is it?"

    Claude "Look at these paper shreds. When you put them together, don’t they look like the seal of the Prime Minister’s office?"

    Jean "...Yes they do. But it’s not like that by itself means Ciel rigged this election. We don’t even know what this piece of paper originally said."

    Claude "Then we better reconstruct the letter from these scraps then, eh?"

    Jean "You can’t be serious. We don’t have hours to spend here doing arts and crafts!"

    Claude "Calm down mon ami. Letters from government offices are printed on special archival papers that are easy to distinguish from normal copy paper. We can get this done quickly, as long as you quit moping and help me out too."

    Jean "Fine, fine. I get it."

    scene poll office with fade

    show Jean at left with dissolve
    show Claude at right with dissolve

    "*Some time passes*"

    Claude "Fini! Let’s see what this says…by order of the Prime Minister Ciel Rousseau… blah blah blah...the following districts shall be recounted...blah blah—"

    Jean "Give me that!...A recount was ordered over suspected ballot tampering at eight electoral districts in Seine-Saint-Denis. Personnel from the electoral committee will conduct the recount…?!"

    Jean "What ballot tampering? This is the first I’ve heard of this!"

    Claude "Yeah, this isn’t being reported in the news so knowledge of the alleged ballot tampering and this recount is being kept secret."

    Jean "...This is really happening, isn’t it? You really did do this..."

    Jean "...Ciel."

    if not box_there and not ballots_there:
        jump saint_denis_end

    jump saint_denis_investigation

label saint_denis_empty_box:

    $ box_there = False

    Jean "Hey, come take a look at this."

    Claude "What’s up?"

    Jean "Look at all these boxes. They’re arranged in a line and numbered one through nine. All these boxes are filled with ballots...except number nine."

    Claude "Yep, this is the only one which is empty. Maybe they didn’t need to use this one?"

    Jean "Except this one was already opened when we got here. I had to break the seals on the other boxes to check inside. This box was definitely being used to store the remaining ballots."

    Claude "And now those ballots are missing...actually wait, you cut open those boxes? People are definitely going to know someone was here."

    Jean "*sigh* Did you already forget what we did? We jumped a guard and tied him up in the supply closet. When this place opens tomorrow, they’re gonna find him and he’ll tell everyone we were here. There’s no more time to worry about covering our tracks."

    Claude "Heh, I hope you’re prepared for a life of crime when this mess gets sorted out. Well, I’ll still be right there next to you whatever happens, Jean."

    Jean "Yeah, I know. I just hope we can drag Ciel out of this mess she’s gotten into before we get caught."

    if not trash_there and not ballots_there:
        jump saint_denis_end

    jump saint_denis_investigation

label saint_denis_suspicious_ballots:

    $ ballots_there = False

    Jean "...Are they even trying to hide this?"

    Claude "A clue, mon ami?"

    Jean "Forget clue, this is just obvious election tampering! Get your ass over here and look at these ballots."

    Claude "Hmmm...Richelieu was the opposition’s candidate? Hard to believe anyone actually voted for this hand puppet, huh?"

    Jean "Yeah, but look. All of these ballots are for Richelieu. The only ballots who aren’t marked for Richelieu are—"

    Claude "—empty ballots. These won’t be tallied for either side. So what, these ballot counters are pumping Richelieu’s numbers and replacing the other candidates’ with empty ballots?"

    Jean "I’m not sure, they can’t just add more ballots to Richelieu since it will conflict with the total number of people who actually voted here. So they might just be replacing ballots with empty ones and keeping Richelieu’s intact."

    Claude "If that’s true, just these ballots won’t change anything. There’s only got to be a few hundred ballots in here at most."

    Jean "But this is not the only election office in Saint-Denis, is it? This could be more serious than just a single building’s worth of votes."

    if not box_there and not trash_there:
        jump saint_denis_end

    jump saint_denis_investigation

label saint_denis_end:

    Jean "So it’s true. Ciel’s office ordered for this election to be rigged under the guise of a recount."

    Claude "And they destroyed opposing ballots and replaced them with useless empty ones. Even if a public recount is done later, the empty ballots wouldn’t raise anyone's suspicion since it’s a pretty common practice."

    Jean "But why? This is the opposite of what we wanted when we started our fight. We just wanted our voices to be heard, not trampled over."

    Claude "Then it appears we’ve become the boot, mon ami."

    Jean "...I just hope this is some terrible misunderstanding. Because if it isn’t…"

    Jean "...what else are you hiding, Ciel?"
