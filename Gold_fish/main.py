import tkinter as tk

#1  タイトル画面表示(タイトルロゴ、スタートボタン、背景)
root = tk.Tk()
root.title("金魚の飼い方")
root.geometry("500x500")
frame_width = 500
frame_height = 500
feame =tk.Frame(root,width=frame_width,height=frame_height)



#画面を作る
#ネットから引用(画面切り替え)
#タイトル画面
def show_screen_title():
    screen_title.pack()
    screen_result.pack_forget()
#飼育画面
def show_screen_breeding():
    screen_title.pack_forget()
    screen_breeding.pack()
#結果画面
def show_screen_result():
    screen_breeding.pack_forget()
    screen_result.pack()
    

# タイトル画面のフレーム-------------------------------------------------------------------------------
screen_title = tk.Frame(root,width=frame_width,height=frame_height)
screen_title.propagate(False)
screen_title.pack()

label_title = tk.Label(screen_title, text="ScreenTitle")
label_title.pack()

#Startボタンクリックで育成画面に切り替える
button_title = tk.Button(screen_title, text="Start", command=show_screen_breeding,width=30, height=5)
button_title.pack(side=tk.BOTTOM)



#   育成画面のフレーム-------------------------------------------------------------------------------
screen_breeding = tk.Frame(root,width=frame_width,height=frame_height)
screen_breeding.pack()
screen_breeding.propagate(False)#←???

label_breeding = tk.Label(screen_breeding, text="ScreenBreeding")
label_breeding.pack()

#2  育成(ボタンで選択_エサA(虫),B(人口エサ),c(水替え))



#選択によってステータスが変化、カウントが進行

#def use_worm():     # worm:金魚がでかくなるエサ(command=use_worm,)
    #金魚の画像を2px大きくする
    #1ターン経過してループから外れる


#def use_food():     # food:金魚の体色が鮮やかになるエサ(command=use_food,)
    #金魚の色を鮮やかにする
    #1ターン経過してループから外れる
# button_food = tk.Button(screen_breeding, text="food", width=20, height=5)
# button_food.grid(row = 500,column = 0,anchor="SW")

# #def use_water():     # water:金魚のlifeが回復する水(command=use_water,)
#     #lifeが20回復する
#     #1ターン経過してループから外れる
# button_water = tk.Button(screen_breeding, text="water", width=20, height=5)
# button_water.grid(row = 500,column = 0,anchor="SW")

#C  水の濁りが解消

#飼育ターンを使用(経過で水が濁る80超えると金魚死亡)

# #ゲーム終了判定
# if(fish_life <= 0):
# #   show_screen_resurt()
#     screen_breeding.propagate(False)
# elif(fish_time ==0):
#     screen_breeding.propagate(False)

#3  飼育ターンが0または金魚が死ぬと、結果画面表示(ss~Fまでの評価結果,金額表示)
#ScreenResurtボタンクリックで結果画面に切り替える
# button_breeding = tk.Button(screen_breeding, text="Result", command=show_screen_result,width=30, height=5)
# button_breeding.pack(side=tk.BOTTOM)

# button_worm = tk.Button(screen_breeding, text="worm", width=20, height=5,anchor="sw")
# button_worm.grid(column=0,padx=(0), pady=(100))

button_food = tk.Button(screen_breeding, text="food", width=20, height=5)
button_food.pack(side = "bottom")

button_water = tk.Button(screen_breeding, text="water", width=20, height=5)
button_water.pack(side = "bottom")

#4  リザルト画面
#   結果画面のフレーム-------------------------------------------------------------------------------
screen_result = tk.Frame(root,width=frame_width,height=frame_height)
screen_result.pack()
screen_result.propagate(False)

#ScreenTitleボタンクリックで結果画面に切り替える
label_result = tk.Label(screen_result, text="ScreenResult")
label_result.pack()

button_breeding = tk.Button(screen_result, text="title", command=show_screen_title,width=30, height=5)
button_breeding.pack(side=tk.BOTTOM)

# 最初はタイトル画面を表示
show_screen_title()

root.mainloop()