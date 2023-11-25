import tkinter as tk
import tkinter.ttk as ttk
import gold_fish

#1  タイトル画面表示(タイトルロゴ、スタートボタン、背景)-------------------------------------
root = tk.Tk()
root.title("金魚の飼い方")
root.geometry("500x500")
frame_width = 500
frame_height = 500
feame =tk.Frame(root,width=frame_width,height=frame_height)

fish = gold_fish.gold_fish()
#fish.counter() デバック用

#画面を作る
#ネットから引用(画面切り替え)
#タイトル画面
def show_screen_title():
    screen_title.pack()
    # screen_result.pack_forget()
#飼育画面
def show_screen_breeding():
    screen_title.pack_forget()
    screen_breeding.pack()
    screen_breeding_button.pack()#育成コマンドを表示    
    
#結果画面(金魚死亡)
def show_screen_result():
    screen_breeding_button.pack_forget()#育成コマンドを非表示
    screen_breeding.pack_forget()
    screen_result.pack()

#結果画面(育成終了)
def show_screen_result():
    screen_breeding_button.pack_forget()#育成コマンドを非表示
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
#育成画面
screen_breeding = tk.Frame(root,width=frame_width,height=frame_height)#背景
screen_breeding.pack()
screen_breeding.propagate(False)

label_breeding = tk.Label(screen_breeding, text="ScreenBreeding")
label_breeding.pack()

#行動選択ボタン用フレームキャンバス
screen_breeding_button = tk.Frame(screen_breeding,bg="aquamarine",width=500,height=500)
screen_breeding_button.pack(side="bottom")
screen_breeding_button.propagate(False)





#2  育成(ボタンで選択_エサA(虫),B(人口エサ),c(水替え))--------------------------------------

#A 金魚が大きく育つ# worm:金魚がでかくなるエサ
    #金魚の画像を2px大きくする
    #1ターン経過してループから外れる
button_worm = tk.Button(screen_breeding_button, text="worm", width=20, height=5,command=fish.use_worm())
button_worm.grid(row = 0,column=0)

# #B  金魚の色が鮮やかになる# food:金魚の体色が鮮やかになるエサ
#     # 金魚の色を鮮やかにする
#     # 1ターン経過してループから外れる
button_food = tk.Button(screen_breeding_button, text="food", width=20, height=5,command=fish.use_food())
button_food.grid(row = 0,column=1, pady=(20))


# #C  水の濁りが解消    # water:金魚のlifeが回復する水
# #     #lifeが20回復する
# #     #1ターン経過してループから外れる
button_water = tk.Button(screen_breeding_button, text="water", width=20, height=5,command=fish.use_water())
button_water.grid(row = 0,column = 2)



#3  結果画面表示(ss~Fまでの評価結果,金額表示)
#ゲーム終了判定------------------------------------------------------------------------------

fish.die_judge()
judge = fish.die_judge()
#judge = True   #デバック用
if (judge == True):     #金魚死亡を判定、死んでいたら『リザルト：死亡』へ
    #ScreenResurtボタンが表示され、クリックで結果画面に切り替える
    button_breeding = tk.Button(screen_breeding, text="Result", command=show_screen_result,width=30, height=5)
    button_breeding.pack(side=tk.BOTTOM)

    screen_result = tk.Frame(root,width=frame_width,height=frame_height)
    screen_result.pack()
    screen_result.propagate(False)

    #S結果画面に切り替える
    label_result = tk.Label(screen_result, text="ScreenResult")
    label_result.pack()

    button_breeding = tk.Button(screen_result, text="title", command=show_screen_title,width=30, height=5)
    button_breeding.pack(side=tk.BOTTOM)

if(fish.count == 0):    #残りターン数字を判定、『リザルト：通常』へ
    #ScreenResurtボタンが表示され、クリックで結果画面に切り替える
    button_breeding = tk.Button(screen_breeding, text="Result", command=show_screen_result,width=30, height=5)
    button_breeding.pack(side=tk.BOTTOM)

    screen_result = tk.Frame(root,width=frame_width,height=frame_height)
    screen_result.pack()
    screen_result.propagate(False)

    #ScreenTitleボタンクリックで結果画面に切り替える
    label_result = tk.Label(screen_result, text="ScreenResult")
    label_result.pack()

    button_breeding = tk.Button(screen_result, text="title", command=show_screen_title,width=30, height=5)
    button_breeding.pack(side=tk.BOTTOM)

#4  リザルト画面-------------------------------------------------------------------------------
# 最初はタイトル画面を表示
show_screen_title()

root.mainloop()