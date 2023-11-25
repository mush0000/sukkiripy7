import tkinter as tk
import pokeapi

# ボタンクリック時に実行する関数
def change_data(entry_id):
    pokemon = pokeapi.get_pokemon(entry_id)
    name_label["text"] = pokemon.ja_name
    data_label["text"] = f"高さ:{pokemon.height}m,重さ:{pokemon.weight}kg"
    img["file"] = pokemon.img
    flavor_text_msg["text"] = pokemon.flavor_text

if __name__ == "__main__": #実行ファイルか、インポートされたファイルなのかを判別
    font_size = 20  # ウィンドウ上の文字サイズ
    pokemon = pokeapi.get_pokemon(1)    #最初のポケモンデータを取得しておく

    # ウィンドウ作成
    root = tk.Tk()
    root.geometry("1280x720")

     # フレーム用意、配置
    entry_frame = tk.Frame(root)    # 入力欄フレーム
    pokemon_frame = tk.Frame(root)   # ポケモンデータ表示フレーム
    entry_frame.pack()
    pokemon_frame.pack()

    # 図鑑番号入力欄用のウィジェット用意
    entry_label = tk.Label(entry_frame, text="図鑑番号:", font=font_size)
    entry_id = tk.Entry(entry_frame,font=font_size)
    entry_button = tk.Button(
        entry_frame, text="検索", command=lambda: change_data(entry_id.get())   #lambda(ラムダ式) 入力された内容をidに渡す
    )

    # ウィジェット配置
    entry_label.grid(row=0, column=0)
    entry_id.grid(row=0,column=1)
    entry_button.grid(row=0,column=2)

    # ポケモンデータ表示用のウィジェット用意
    name_label = tk.Label(pokemon_frame, text=pokemon.ja_name, font=font_size)
    img = tk.PhotoImage(file=pokemon.img)
    image_label = tk.Label(pokemon_frame, image=img)
    data_label = tk.Label(
        pokemon_frame,
        text=f"高さ:{pokemon.height}m,重さ:{pokemon.weight}kg",
        font=font_size,
    )
    flavor_text_msg = tk.Message(
        pokemon_frame,
        text=pokemon.flavor_text,
        font=font_size,
        width=400,
    )

    # ウィジェット配置
    name_label.pack()
    image_label.pack()
    data_label.pack()
    flavor_text_msg.pack(pady=(10,0))


    def key(e):     #(e)動きをまとめておいた関数
        print(e.keysym) #どのキーを押したかを取得→if文で条件分岐させて動かせる

    def mouse(e):   #マウスをクリック
        print(e.x)  #どのアタリをクリックしたかを取得
    
    # tkinter イベント検知
    root.bind("<key>",key)  #画面内で動かすための記述
    root.bind("<button-1>",mouse)
    root.bind("<Motion>",mouse) #マウスの動きを検知



    # メインループ
    root.mainloop()