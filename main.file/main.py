import tkinter as tk

#画面を作る
root = tk.Tk()
root.geometry("1280x720")

#label  変数にLabel(テキスト)を入れる
# label = tk.Label(root,text="こんにちはまっしゅだよ",font=("Araial",30))
# label.place(x=40,y=100)

# labe2 = tk.Label(root,text="こんにちはまっしゅだよ",font=("Araial",30))
# labe3 = tk.Label(root,text="こんにちはまっしゅだよ",font=("Araial",30))
# labe4 = tk.Label(root,text="こんにちはまっしゅだよ",font=("Araial",30))
# labe2.place(x=40,y=110)
# labe3.place(x=40,y=120)
# labe4.place(x=40,y=130)
#テキストを画面に配置
#pack   label.pack() 真ん中上寄せに積めて置かれていく(packした順番から)
#grid   label.grid(row = 0,column = 0) オセロのようにグリッド配置
#place  label.place(x=40,y=100) 画面左上を0,0として数値で指定

#
def button_click():
    text = entry.get()
    print(text)

button = tk.Button(root,text="ボタンだよ",font=("Araial",30),command=button_click)
#button.pack()

entry = tk.Entry(root,font=("Araial",30))
#entry.pack()

#画像を画面に表示
load_image = tk.PhotoImage(file="main.file/lamin.png")  #読み込み処理
img = tk.Label(root,image=load_image)                   #Labelオブジェクトに入れる
#img.pack()                                              #画像を表示

#   複数行のメッセージ
msg = tk.Message(
    root,
    text="ぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼぼ",
    font=("Arial",20),
    bg = "white",
    width=300
)
#msg.pack()


#
canvas = tk.Canvas(root,bg="black",width=500,height=500)
canvas.pack()

canvas.create_text(0,0,text="ちょこくぅん",fill="white",font=("Arial",20),anchor="nw")
canvas.create_text(canvas["width"],canvas["height"],text=("Arial",20),anchor="center")

#一番最後に記載
root.mainloop()

