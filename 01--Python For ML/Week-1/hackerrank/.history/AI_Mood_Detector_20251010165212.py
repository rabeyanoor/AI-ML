message = input()

# Chellck for happy mood keywordsif "happy" in message or "joy" in message or "smile" in message:
    print("Happy Mood")
# Check for sad mood keywords
elif "sad" in message or "cry" in message or "angry" in message:
    print("Sad Mood")
# Otherwise, neutral mood
else:
    print("Neutral Mood")
