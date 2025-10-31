# college_chatbot.py
# A simple rule-based chatbot for college queries

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "admission" in user_input:
        return "Our college admissions open in June. You can apply online through the official portal."
    elif "fees" in user_input:
        return "The annual fee for most programs is around ₹1,00,000."
    elif "courses" in user_input:
        return "We offer B.Tech, B.Sc, B.Com, and M.Tech programs."
    elif "placement" in user_input:
        return "Our top recruiters include Infosys, TCS, and Wipro with an average package of ₹6 LPA."
    elif "hostel" in user_input:
        return "We have separate hostels for boys and girls with all basic amenities."
    elif "contact" in user_input:
        return "You can reach us at contact@college.com or call +91 9876543210."
    elif "thank" in user_input:
        return "You're welcome! 😊"
    else:
        return "Sorry, I don't have information about that. Please try asking something else."

print("Welcome to College Chatbot! Type 'bye' to exit.")

while True:
    user = input("You: ")
    if user.lower() == "bye":
        print("Chatbot: Goodbye! 👋")
        break
    print("Chatbot:", chatbot_response(user))
