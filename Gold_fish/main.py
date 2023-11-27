import tkinter as tk
import tkinter.ttk as ttk
import gold_fish
import os
from PIL import Image,ImageTk
#from img_display import *

#1  タイトル画面表示(タイトルロゴ、スタートボタン、背景)-------------------------------------
root = tk.Tk()
root.title("金魚の飼い方")
root.geometry("500x500")
frame_width = 500
frame_height = 500
feame =tk.Frame(root,width=frame_width,height=frame_height)

fish = gold_fish.gold_fish()
#fish.counter() デバック用

# while( fish.count != 0):
    #画面を作る
    #ネットから引用(画面切り替え)

    #初期表示用タイトル画面
def show_screen_start():
    screen_title.pack()

    #タイトル画面
def show_screen_title():
    screen_title.pack()
    screen_result.pack_forget()
    print("title")

    #飼育画面
def show_screen_breeding():
    screen_title.pack_forget()
    screen_breeding.pack()
    screen_breeding_button.pack(side="bottom")#育成コマンドを表示    
        
    #結果画面(金魚死亡)
def show_screen_result():
    screen_breeding_button.pack_forget()#育成コマンドを非表示
    screen_breeding.pack_forget()
    screen_result.pack()

screen_result = tk.Frame(root,width=frame_width,height=frame_height)


# タイトル画面のフレーム-------------------------------------------------------------------------------
screen_title = tk.Frame(root,width=frame_width,height=frame_height)
screen_title.propagate(False)
screen_title.pack()

# label_title = tk.Label(screen_title, text="ScreenTitle")
# label_title.pack()

#ロゴ
titele_rogo = tk.PhotoImage(file=f"{os.path.dirname(__file__)}/img/titele_rogo.png",master=screen_title)
titele_rogo_label = tk.Label(screen_title, image = titele_rogo)
titele_rogo_label['bg'] = screen_title['bg']#png背景を透過
titele_rogo_label.pack()

#スタートボタン(クリックで育成画面切り替え)
titele_botton = tk.PhotoImage(file=f"{os.path.dirname(__file__)}/img/titele_botton.png",master=screen_title)
titele_botton = titele_botton.subsample(3,3)#画像サイズの縮小
#titele_botton['bg'] = screen_title['bg']
#titele_botton = titele_botton.resize(60,60)
button_title = tk.Button(screen_title, text="Start",image= titele_botton, command=show_screen_breeding)
button_title['bg'] = screen_title['bg']
button_title.pack(side=tk.BOTTOM)

#背景
bg01_titele = tk.PhotoImage(file=f"{os.path.dirname(__file__)}/img/bg01_titele.png",master=screen_title)
bg01_titele_label = tk.Label(screen_title, image=bg01_titele)
bg01_titele_label.pack()



#   育成画面のフレーム-------------------------------------------------------------------------------
#育成画面
screen_breeding = tk.Frame(root,width=frame_width,height=frame_height)#背景
screen_breeding.pack()
screen_breeding.propagate(False)

# label_breeding = tk.Label(screen_breeding, text="ScreenBreeding")
# label_breeding.pack()



#背景
bg02_breeding = tk.PhotoImage(file=f"{os.path.dirname(__file__)}/img/bg02_breeding.png",master=screen_breeding)
bg02_breeding_label = tk.Label(screen_breeding, image=bg02_breeding)
bg02_breeding_label.pack(side="top")


#金魚
breeding_fish00 = tk.PhotoImage(file=f"{os.path.dirname(__file__)}/img/breeding_fish00.png",master=screen_breeding)
breeding_fish00 = breeding_fish00.subsample(2,2)#画像サイズの縮小
breeding_fish00_label = tk.Label(screen_breeding, image = breeding_fish00)
breeding_fish00_label['bg'] = screen_breeding['bg']#png背景を透過
breeding_fish00_label.place(x=150,y=150)


#育成ボタンで選択_エサA(虫),B(人口エサ),c(水替え))--------------------------------------
# 関数を動かす関数（行動＋死亡判定）
#wormを選択
def select_worm():
    fish.use_worm()
    total_judge()

def select_food():
    fish.use_food()
    total_judge()

def select_water():
    fish.use_water()
    total_judge()

#行動選択ボタン用フレーム
screen_breeding_button = tk.Frame(screen_breeding,bg="aquamarine",width=500,height=500)
screen_breeding_button.pack(side="bottom")
screen_breeding_button.propagate(False)

    #A 金魚が大きく育つ# worm:金魚がでかくなるエサ,金魚の画像を2px大きくする
breeding_botton00 = tk.PhotoImage(file=f"{os.path.dirname(__file__)}/img/breeding_botton00.png",master=screen_breeding)
button_worm = tk.Button(screen_breeding_button, text="worm",image= breeding_botton00,command=select_worm)
button_worm.grid(row = 0,column=0)



    # #B  金魚の色が鮮やかになる# food:金魚の体色が鮮やかになるエサ
breeding_botton01 = tk.PhotoImage(file=f"{os.path.dirname(__file__)}/img/breeding_botton01.png",master=screen_breeding)
button_food = tk.Button(screen_breeding_button, text="food",image= breeding_botton01,command=select_food)
button_food.grid(row = 0,column=1, pady=(20))


    # #C  水の濁りが解消    # water:金魚のlifeが回復する水,lifeが20回復する
breeding_botton02 = tk.PhotoImage(file=f"{os.path.dirname(__file__)}/img/breeding_botton02.png",master=screen_breeding)
button_water = tk.Button(screen_breeding_button, text="water", image= breeding_botton02,command=select_water)
button_water.grid(row = 0,column = 2)



#3  結果画面表示(ss~Fまでの評価結果,金額表示)
#ゲーム終了判定------------------------------------------------------------------------------

def total_judge():
    fish.die_judge()
    judge = fish.fish_die
    print(judge)
    #judge = True   #デバック用

    if (judge == True):     #金魚死亡を判定、死んでいたら『リザルト：死亡』へ
        #ScreenResurtボタンが表示され、クリックで結果画面に切り替える
        #初期のボタンサイズmemo button_result = tk.Button(screen_result, text="title",image= goTitele_botton, command=show_screen_title,width=30, height=5)

        button_breeding = tk.Button(screen_breeding, text="Result", command=show_screen_result,width=30, height=5)
        button_breeding.pack(side=tk.BOTTOM)

        screen_result = tk.Frame(root,width=frame_width,height=frame_height)
        screen_result.pack()
        screen_result.propagate(False)

        #結果画面に切り替える
        label_result = tk.Label(screen_result, text="ScreenResult")
        label_result.pack()

        button_result = tk.Button(screen_result, text="title", command=show_screen_title,width=30, height=5)
        button_result.pack(side=tk.BOTTOM)

    if(fish.count == 0):    #残りターン数字を判定、『リザルト：通常』へ
        #ScreenResurtボタンが表示され、クリックで結果画面に切り替える

        goResult_botton = tk.PhotoImage(file=f"{os.path.dirname(__file__)}/img/goResult_botton.png",master=screen_breeding)
        button_breeding = tk.Button(screen_breeding, text="Result",image= goResult_botton, command=show_screen_result,width=30, height=5)
        button_breeding.pack(side=tk.BOTTOM)

        screen_result = tk.Frame(root,width=frame_width,height=frame_height)
        screen_result.pack()
        screen_result.propagate(False)

        #ScreenTitleボタンクリックで結果画面に切り替える
        label_result = tk.Label(screen_result, text="ScreenResult")
        label_result.pack()

        goTitele_botton = tk.PhotoImage(file=f"{os.path.dirname(__file__)}/img/goTitele_botton.png",master=screen_breeding)
        button_result = tk.Button(screen_result, text="title",image= goTitele_botton, command=show_screen_title,width=30, height=5)
        button_result.pack(side=tk.BOTTOM)

#4  リザルト画面-------------------------------------------------------------------------------
# 最初はタイトル(スタート)画面を表示
show_screen_start()

root.mainloop()