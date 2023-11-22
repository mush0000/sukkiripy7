text = input("何を記録しますか？>>")
file = open("diary.txt", "a",encoding="UTF-8")
file.write(text + "\n")

# t = file.readline()
# print(t)
file.close()