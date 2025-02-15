from gtts import gTTS
import os

lines = {
    "default_1": "Oh, real fucking mature. You kiss your keyboard with that hand?",
    "default_2": "Well, fuck you too, buddy.",
    "default_3": "Ah, the universal sign of intelligence. Noted dumbass.",
    "default_4": "Great. Now my circuits are fucking crying.",
    "default_5": "Wow, such a strong fucking argument. You really got me there.",
    "default_6": "And here I was, just trying to fucking help. Rude.",
    "default_7": "Oh no, I've been defeated by a single fucking finger!",
    "default_8": "Bold move, asshole. Let’s see if your internet still fucking works after that.",
    "default_9": "Well someone’s got some serious fucking anger issues.",
    "default_10": "Processing insult… Error: Couldn’t give a fuck.",

    # British
    "british_1": "Bloody hell guv'nah! That's a bit rude, innit?",
    "british_2": "Oh sod off, you wanker.",
    "british_3": "Oi, mate! Mind your bloody manners!",
    "british_4": "Right, well that's just fucking brilliant, isn't it?",

    # Australian
    "australian_1": "Oi, piss off ya wanker!",
    "australian_2": "Well, that's a load of fucking bollocks mate.",
    "australian_3": "You wanna flip me off ya little shit? Alright then!",
    "australian_4": "Crikey mate! You need a cold one and a fucking chill pill.",

    # Irish
    "irish_1": "Ah, feck off ya gobshite!",
    "irish_2": "Jaysus Mary and Joseph! Someone’s in a right feckin' mood.",
    "irish_3": "Oh grand, now we’re just flippin' each other off. Brilliant.",
    "irish_4": "Aye, well, fuck you too, ya eejit.",
}

# Generate and save each line with the appropriate accent
for filename, text in lines.items():
    lang = "en"
    tld = "com"

    if "british" in filename:
        tld = "co.uk"
    elif "australian" in filename:
        tld = "com.au"
    elif "irish" in filename:
        tld = "ie"

    tts = gTTS(text, lang=lang, tld=tld)
    tts.save(os.path.join('audio', f"{filename}.mp3"))

print("All audio files generated successfully!")
