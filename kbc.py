import tkinter as tk
from tkinter import simpledialog, messagebox


questions = [
            ["what is the name of the President of the united states?", "Donald Trump", "Narendra Modi", "Joe Biden", "Rahul Gandhi", 1],
            ["what is the name of the Prime Minister of the india?", "Benjamin Netanyahu", "narendra modi", "george biden", "rahul gandhi", 2],
            ["what is the name of the Prime Minister of the united kingdom?", "boris johnson", "tory johnson", "queen elizabeth", "david cameron", 1],
            ["what is the name of the Prime MInister of the italy?", "matteo renzi", "greta thunberg", "giuseppe conte", "georgia meloni", 4],
            ["what is the name of the President of the france?", "gaten matarazoo", "joshua pearce", "emanuel macron", "rahul gandhi", 3],
            ["what is the name of the President of the south africa?", "cyril ramaphosa", "Donald Trump", "joe biden", "rahul gandhi", 1],
            ["what is the name of the Chief Minister of Uttar Pradesh?", "yogi adityanath", "manmohan singh", "narendra modi", "kejriwal", 1],
            ["what is the name of the Chief Executive Officer of Nvidia?", "Jensen Huang", "Satya Nadella", "Tim Cook", "Elon Musk", 1],

]
levels = [1000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000]


for i in range(0, len(questions)):
    # print(f"question for rs, {levels[i]}")
    question = questions[i]
    optiontext = ""
    for j in range(1, 5):
        optiontext += f"{j}. {question[j]}\n"

    reply = simpledialog.askinteger(
        f"Question for ₹{levels[i]}",

        f"{question[0]}\n\n"
        f"{optiontext}\n"

        "Enter answer (1-4)"
    )
    if (reply == question[5]):
        print("correct answer")
        if(i == 0):
            money = 1000
            messagebox.showinfo("Result", f"Your Prize = {money}")
        elif(i == 1):
            money = 5000
            messagebox.showinfo("Result", f"Your Prize = {money}")

        elif(i == 2):
            money = 10000
            messagebox.showinfo("Result", f"Your Prize = {money}")

        elif(i == 3):
            money = 20000
            messagebox.showinfo("Result", f"Your Prize = {money}")

        elif(i == 4):
            money = 40000
            messagebox.showinfo("Result", f"Your Prize = {money}")
        
        elif(i == 5):
            money = 80000
            messagebox.showinfo("Result", f"Your Prize = {money}")
        
        elif(i == 6):
            money = 160000
            messagebox.showinfo("Result", f"Your Prize = {money}")
        
        elif(i == 7):
            money = 320000
            messagebox.showinfo("Result", f"Your Prize = {money}")
        
        elif(i == 8):
            money = 640000
            messagebox.showinfo("Result", f"Your Prize = {money}")
    else:
        print("wrong answer")
        messagebox.showinfo("Result", f"Your Prize = {money}")
        break
messagebox.showinfo("Result", f"Your take home money is: ₹{money}")
