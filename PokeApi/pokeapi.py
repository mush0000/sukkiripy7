import requests
import os

# クラス定義
class Pokemon:
    def __init__(
            self, ja_name="", en_name="", weight=0.0, height=0.0, flavor_text="", img=None
    ):
        self.ja_name = ja_name
        self.en_name = en_name
        self.weight = weight
        self.height = height
        self.flavor_text = flavor_text
        self.img = img

# 関数定義
# PokeApiからポケモンデータ取得
def get_pokemon(id):
     # returnするPokemonクラスのインスタンス生成
    pokemon = Pokemon()

     # PokeApiにリクエスト、レスポンスをjson形式で受け取る
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
    pokeapi = response.json()

    species_url = pokeapi["species"]["url"]
    response = requests.get(species_url)
    pokeapi_species = response.json()

    # 各種データをレスポンスから取得
    # 英語名、重さ、高さ、画像URL取得
    pokemon.en_name = pokeapi["name"]
    pokemon.weight = float(pokeapi["weight"])/10
    pokemon.height = float(pokeapi["height"])/10
    pokemon.img = pokeapi["sprites"]["other"]["official-artwork"]["front_default"]

    # 日本語の名前取得
    names = pokeapi_species["names"]
    for name in names:
        if name["language"]["name"] == "ja":
            pokemon.ja_name = name["name"]
            break

    # 日本語のフレーバーテキスト取得
    flavor_text_entries = pokeapi_species["flavor_text_entries"]
    for text in flavor_text_entries:
        if text["language"]["name"] == "ja":
            pokemon.flavor_text = text["flavor_text"]
            break
    # 画像をダウンロード、インスタンスのimg属性をダウンロードした画像ファイルのパスに変更
    download_img(pokemon)
    return pokemon

# 画像のパスを取得、インスタンスに設定
def download_img(pokemon: Pokemon):#型の指定
    current_dir = os.path.dirname(__file__)#フォルダの絶対パスを取得
    img_path = f"{current_dir}/img/{pokemon.en_name}.png"
    if not os.path.isfile(img_path):#画像が無い場合は
        image = requests.get(pokemon.img).content#画像・動画・contentで取得する
        with open(img_path, "wb") as f:#withは動作後自動でファイルを閉じる
            f.write(image)#imgフォルダに自動で追加
    else:
        print("既にダウンロード済みのポケモン画像です")

    pokemon.img = img_path

#print(get_pokemon(1).flavor_text)#デバック用
