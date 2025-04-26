def health_assistant_v2():
    print("Welcome to the More Detailed Simple Health Assistant!")
    print("Please describe your symptoms or health concern.")
    user_input = input("> ").lower()

    if "chest pain" in user_input and "shortness of breath" in user_input:
        print("\nThese symptoms could indicate a serious respiratory or cardiac issue.")
        print("Seek immediate medical attention.")
    elif "abdominal pain" in user_input and "fever" in user_input and "vomiting" in user_input:
        print("\nThis combination of symptoms might suggest a gastrointestinal infection or other serious condition.")
        print("Consult a doctor as soon as possible.")
    elif "sore throat" in user_input and "difficulty swallowing" in user_input and "fever" in user_input:
        print("\nThese symptoms could indicate strep throat or another infection.")
        print("It's recommended to see a doctor for diagnosis and potential treatment.")
    elif "headache" in user_input and "blurred vision" in user_input:
        print("\nA headache with blurred vision could have several causes. Monitor your symptoms and consult a doctor if they persist or worsen.")
    elif "runny nose" in user_input and "sneezing" in user_input:
        print("\nThese are common symptoms of a cold or allergies. Rest and over-the-counter remedies might help.")
    else:
        print("\nThank you for describing your symptoms.")
        print("Based on the information, it's difficult to give specific advice. If you are concerned, please consult a doctor.")

symptom_checker = {
    ("fever", "cough"): "Possible cold or flu. Rest, hydrate, monitor.",
    ("stomach pain", "nausea"): "Possible mild gastrointestinal issue. Rest, hydrate, avoid heavy meals.",
    ("headache", "tired"): "Possible fatigue or mild headache. Rest, hydrate.",
    ("chest pain", "shortness of breath"): "Seek immediate medical attention!",
    ("abdominal pain", "fever", "vomiting"): "Consult a doctor as soon as possible.",
    ("sore throat", "difficulty swallowing", "fever"): "Recommended to see a doctor.",
    ("headache", "blurred vision"): "Monitor symptoms and consult a doctor if persistent or worsening.",
    ("runny nose", "sneezing"): "Common cold or allergies. Rest and over-the-counter remedies might help."
}

def health_assistant_v3():
    print("\nWelcome to the Symptom-Based Health Assistant!")
    print("Please list your symptoms, separated by commas (e.g., fever, cough, headache).")
    user_input = input("> ").lower()
    symptoms = tuple(sorted([s.strip() for s in user_input.split(',')]))

    if symptoms in symptom_checker:
        print(f"\nBased on your symptoms: {symptom_checker[symptoms]} Consult a doctor if concerned.")
    else:
        print("\nYour combination of symptoms is not recognized in our current knowledge base.")
        print("It's best to consult a doctor for proper diagnosis and guidance.")

if __name__ == "main":
    health_assistant_v2()
    health_assistant_v3()