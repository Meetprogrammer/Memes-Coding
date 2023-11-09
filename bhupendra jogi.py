def chatbot_response(user_input):
    responses = {
        "apka naam": "bhupendra jogi",
        "ap us me kaha kaha gaya hoa": "bahut sari jagah",
        "naam bataya": "bhupendra jogi"
    }
    user_input_clean = user_input.strip().lower()
    return responses.get(user_input_clean, "mujhe samjh nahi aya kripya fir se poocha")

print("namaste mujhe kuch bhi pucho mera jwab hai bhupendra jogi (type 'exit' to quit):")

while True:
    user_input = input()
    if user_input.lower() == 'exit':
        print("us me mila gai")
        break
    print(chatbot_response(user_input)) 