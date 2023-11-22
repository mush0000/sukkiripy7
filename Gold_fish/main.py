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
    screen_breeding.pack_forget()
#飼育画面
def show_screen_breeding():
    screen_title.pack_forget()
    screen_breeding.pack()
#結果画面
def show_screen_resurt():
    screen_title.pack_forget()
    screen_resurt.pack()

# タイトル画面のフレーム
screen_title = tk.Frame(root,width=frame_width,height=frame_height)
screen_title.propagate(False)
screen_title.pack()

label_title = tk.Label(screen_title, text="ScreenTitle")
label_title.pack()

#スタートボタンクリックで育成画面に切り替える
button_title = tk.Button(screen_title, text="Start", command=show_screen_breeding,width=30, height=5)
button_title.pack(side=tk.BOTTOM)

#   育成画面のフレーム
screen_breeding = tk.Frame(root)
screen_breeding.pack()
screen_title.propagate(False)

label_breeding = tk.Label(screen_breeding, text="ScreenBreeding")
label_breeding.pack()

    #   B→Aへの切り替えはないのでコメントアウト
    # button_breeding = tk.Button(screen_breeding, text="To a", command=show_screen_title)
    # button_breeding.pack()

#   結果画面のフレーム←ここから


# 最初はタイトル画面を表示
show_screen_title()


#2  育成画面表示(ボタンで選択_エサA(虫),B(人口エサ),c(水替え))
#選択によってステータスが変化

#A  金魚がでかくなる
#B  色が鮮やかになる
#C  水の濁りが解消
#飼育ターンを使用(経過で水が濁る80超えると金魚死亡)
if(fish_life < 0):
    show_screen_resurt()

#3  飼育ターンが0または金魚が死ぬと、結果画面表示
#ss~Fまでの評価結果,金額表示

#4  リザルト画面

root.mainloop()