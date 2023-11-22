#7-6

from random import randint as ran

#(1)
print("数当てゲームを始めます。3桁の数を当ててください!")

#(2)
# answer = []
# for i in range(3):
#     answer.append(ran(0,9))

#内包表記
#answer = [ran(0,9) for i in range(3)]

#答えの重複を防ぐ(回答)
answer = []
while len(answer) <3:
    r = ran(0,9)
    if not(r in answer):
        answer.append(r)

#数字の重複を防ぐ
# while answer == answer[3]
# for i in range(3):
#     if (i == 0):
#         num_ran = ran(0,9)
#         answer.append(ran(0,9))
#     elif(i == 1):
#         num_ran = ran(0,9)
#         if(num_ran == answer[0]):
#             continue
#         else:
#              num_ran.append(ran(0,9))
#     elif(i == 2):
print(answer)#デバック用

game = False
while game == False:
    #(3)
    prediction = []
    for j in range(len(answer)):
        num = int(input("{}桁目の予想を入力(0~9)>>".format(j)))
        prediction.append(num)

    #(4)
    count_hit = 0
    count_ball = 0
    for index in range(len(answer)):
        if(answer[index] == prediction[index]):
            count_hit += 1
        elif(answer[index] == prediction[index]):
                count_ball += 1

    print("{}ヒット!{}ボール!".format(count_hit,count_ball))

    #(5)
    if(count_hit == 3):
        print("正解です!")
        game = True
        break
    #(6)
    else:
        play = int(input("続けますか? 1:続ける 2:終了>>"))
        if(play == 1):#(7)
            game = False
        else:
            game = True
            break
print("正解は{}でした".format(answer))        


