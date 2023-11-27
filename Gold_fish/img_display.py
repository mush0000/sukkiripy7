import tkinter as tk
import os

#フレーム定義
# root = tk.Tk()
# frame_width = 500
# frame_height = 500
# feame =tk.Frame(root,width=frame_width,height=frame_height)

#タイトル画面--------------------------------------------------------------------
#画像定義
#背景画像
# def titele(frame):
bg01_titele = tk.PhotoImage(file="img/bg01_titele.png")

    #ロゴ
titele_rogo = tk.PhotoImage(file="titele_rogo.png")
bg01_titele_label = tk.Label(feame, image=titele_rogo)
    #スタートボタン
titele_botton = tk.PhotoImage(file=f"{os.path.dirname(__file__)}/img/titele_botton.png")
print(titele_botton["file"])


#育成画面
#画像定義
#背景画像
# bg02_breeding = tk.PhotoImage(file="bg02_breeding.png")
# bg02_breeding_label = tk.Label(feame, image=bg02_breeding)
# #金魚
# breeding_fish = tk.PhotoImage(file="titele_rogo.png")
# bg01_titele_label = tk.Label(feame, image=titele_rogo)
# #スタートボタン
# titele_botton = tk.PhotoImage(file=f"{os.path.dirname(__file__)}/img/titele_botton.png")



    #memoフレーム定義-------------------------------------------------------------
#   pokemon_frame = tk.Frame(root)
#   pokemon_frame.pack()
    #画像を定義
#   img = tk.PhotoImage(file=pokemon.img)
#   image_label = tk.Label(pokemon_frame, image=img)
    #画像を表示
#   image_label.pack()