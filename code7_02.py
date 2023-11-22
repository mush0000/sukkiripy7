text = input("今日は何をした?>>")
with open("diary.txt","a",encoding="UTF-8") as file:
    file.write(text + "\n")