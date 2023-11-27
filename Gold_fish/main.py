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
def show_screen_title(e):
    screen_title.pack()
    screen_result.pack_forget()
    print("title")

    #飼育画面
def show_screen_breeding(e):
    screen_title.pack_forget()
    screen_breeding.pack()
    #screen_breeding_button.pack(side="bottom")#育成コマンドを表示    
        
    #結果画面(金魚死亡)
def show_screen_result(e):
    #screen_breeding_button.pack_forget()#育成コマンドを非表示
    screen_breeding.pack_forget()
    screen_result.pack()

screen_result = tk.Frame(root,width=frame_width,height=frame_height)


# タイトル画面のフレーム-------------------------------------------------------------------------------
screen_title = tk.Frame(root,width=frame_width,height=frame_height)
screen_title.pack()
canvas = tk.Canvas(screen_title,bg="white",width=frame_width,height=frame_height)
canvas.pack()

# label_title = tk.Label(screen_title, text="ScreenTitle")
# label_title.pack()

#ロゴ
titele_rogo = tk.PhotoImage(file=f"{os.path.dirname(__file__)}/img/titele_rogo.png")
canvas.create_image(250,80, image = titele_rogo)


#スタートボタン(クリックで育成画面切り替え)
titele_botton = tk.PhotoImage(file=f"{os.path.dirname(__file__)}/img/titele_botton.png")
titele_botton = titele_botton.subsample(3,3)#画像サイズの縮小
start_botton = canvas.create_image(250,400, image = titele_botton)
canvas.tag_bind(start_botton,"<Button-1>",show_screen_breeding)

#titele_botton['bg'] = screen_title['bg']
#titele_botton = titele_botton.resize(60,60)

# button_title = tk.Button(screen_title, text="Start",image= titele_botton, command=show_screen_breeding)
# button_title['bg'] = screen_title['bg']
# button_title.pack(side=tk.BOTTOM)

#背景
bg01_titele = tk.PhotoImage(file=f"{os.path.dirname(__file__)}/img/bg01_titele.png")
canvas.create_image(240,220, image=bg01_titele)



#   育成画面のフレーム-------------------------------------------------------------------------------
#育成画面
screen_breeding = tk.Frame(root,width=frame_width,height=frame_height)#背景
screen_breeding.pack()
canvas_breeding = tk.Canvas(screen_breeding,bg="white",width=frame_width,height=frame_height)
canvas_breeding.pack()

# label_breeding = tk.Label(screen_breeding, text="ScreenBreeding")
# label_breeding.pack()

#背景
bg02_breeding = tk.PhotoImage(file=f"{os.path.dirname(__file__)}/img/bg02_breeding.png")
canvas_breeding.create_image(250,240, image = bg02_breeding)

#金魚
breeding_fish00 = tk.PhotoImage(file=f"{os.path.dirname(__file__)}/img/breeding_fish00.png")
breeding_fish00 = breeding_fish00.subsample(2,2)#画像サイズの縮小
canvas_breeding.create_image(200,200, image = breeding_fish00)

#育成ボタンで選択_エサA(虫),B(人口エサ),c(水替え))--------------------------------------
# 関数を動かす関数（行動＋死亡判定）
#wormを選択
def select_worm(e):
    fish.use_worm()
    total_judge()

def select_food(e):
    fish.use_food()
    total_judge()

def select_water(e):
    fish.use_water()
    total_judge()

#行動選択ボタン用フレーム
# screen_breeding_button = tk.Frame(screen_breeding,bg="aquamarine",width=500,height=500)
# screen_breeding_button.pack(side="bottom")
# screen_breeding_button.propagate(False)

    #A 金魚が大きく育つ# worm:金魚がでかくなるエサ,金魚の画像を2px大きくする
breeding_botton00 = tk.PhotoImage(file=f"{os.path.dirname(__file__)}/img/breeding_botton00.png")
breeding_botton00 = breeding_botton00.subsample(2,2)#画像サイズの縮小
worm_botton = canvas_breeding.create_image(150,380,image=breeding_botton00)
canvas_breeding.tag_bind(worm_botton,"<Button-1>",select_worm)



    # #B  金魚の色が鮮やかになる# food:金魚の体色が鮮やかになるエサ
breeding_botton01 = tk.PhotoImage(file=f"{os.path.dirname(__file__)}/img/breeding_botton01.png")
food_botton = canvas_breeding.create_image(250,380, image = breeding_botton01)
canvas_breeding.tag_bind(food_botton,"<Button-1>",select_food)


    # #C  水の濁りが解消    # water:金魚のlifeが回復する水,lifeが20回復する
breeding_botton02 = tk.PhotoImage(file=f"{os.path.dirname(__file__)}/img/breeding_botton02.png")
breeding_botton02 = breeding_botton02.subsample(2,2)#画像サイズの縮小
woter_button = canvas_breeding.create_image(350,380, image= breeding_botton02)
canvas_breeding.tag_bind(woter_button,"<Button-1>",select_water)

#画像を先に読み込み
button_breeding = tk.PhotoImage(file=f"{os.path.dirname(__file__)}/img/bg03_resultA.png")

#3  結果画面表示(ss~Fまでの評価結果,金額表示)
#ゲーム終了判定------------------------------------------------------------------------------

def total_judge():
    global button_breeding
    fish.die_judge()
    judge = fish.fish_die
    print(judge)
    #judge = True   #デバック用

    if (judge == True):     #金魚死亡を判定、死んでいたら『リザルト：死亡』へ
        #ScreenResurtボタンが表示され、クリックで結果画面に切り替える
        #初期のボタンサイズmemo button_result = tk.Button(screen_result, text="title",image= goTitele_botton, command=show_screen_title,width=30, height=5)

        # button_breeding = tk.PhotoImage(file=f"{os.path.dirname(__file__)}/img/bg03_resultA.png")
        breeding_button = canvas_breeding.create_image(250,250, image = button_breeding)
        canvas_breeding.tag_bind(breeding_button,"<Button-1>",show_screen_result)

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