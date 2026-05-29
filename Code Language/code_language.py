import random
enter_ur_message = input("Enter your message: ")
code = enter_ur_message.split(" ")
random.shuffle(code)
new_text = []
for word in code:
    letters = list(word)
    random.shuffle(letters)
    new_text.append("".join(letters))
new_text0 = " ".join(new_text)
print("Generated language: ")
print(new_text0)