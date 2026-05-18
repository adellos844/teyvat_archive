import os
import requests

API = "https://genshin-impact.fandom.com/api.php"

def create_dirs(character):
    folders = [
        "Cumpleaños",
        "Iconos principales",
        "Stickers",
        "Tarjetas-Constelación",
        "Wallpaper"
    ]
    for f in folders:
        os.makedirs(f"{character}/{f}", exist_ok=True)

def classify(character, name):
    n = name.lower()

    char = character.lower()
    char_underscore = char.replace(" ", "_")
    char_nospace = char.replace(" ", "")

    if not (
        char in n or
        char_underscore in n or
        char_nospace in n
    ):
        return None

    if "birthday" in n:
        return "Cumpleaños"

    if any(x in n for x in ["icon", "profile", "wish", "side_icon", "avatar"]):
        return "Iconos principales"

    if "emoji" in n:
        return "Stickers"

    if "namecard" in n or "card" in n:
        return "Tarjetas-Constelación"

    if "wallpaper" in n:
        return "Wallpaper"

    return None

def get_images(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "images",
        "format": "json",
        "imlimit": "500",
        "redirects": 1
    }

    res = requests.get(API, params=params).json()
    pages = res["query"]["pages"]

    images = []

    for page in pages.values():
        if "images" in page:
            for img in page["images"]:
                images.append(img["title"])

    return images

def get_image_url(filename):
    params = {
        "action": "query",
        "titles": filename,
        "prop": "imageinfo",
        "iiprop": "url",
        "format": "json"
    }

    res = requests.get(API, params=params).json()

    pages = res["query"]["pages"]
    for p in pages.values():
        if "imageinfo" in p:
            return p["imageinfo"][0]["url"]

    return None

def download(url, path):
    try:
        data = requests.get(url).content
        with open(path, "wb") as f:
            f.write(data)
        return True
    except:
        return False

def process_character(character):
    print(f"Procesando {character}...")
    create_dirs(character)

    char_page = character.replace(" ", "_")

    print("🔍 Buscando en página principal...")
    main_images = get_images(char_page)

    print("🔍 Buscando en Gallery...")
    gallery_images = get_images(f"{char_page}/Gallery")

    all_files = list(set(main_images + gallery_images))

    print(f"📦 Total encontrados: {len(all_files)}")

    descargados = 0

    for file in all_files:
        name = file.replace("File:", "")

        folder = classify(character, name)
        if not folder:
            continue

        url = get_image_url(file)
        if not url:
            continue

        path = f"{character}/{folder}/{name}"
        if download(url, path):
            print(f"✅ {name}")
            descargados += 1

    print(f"🎉 Descargados para {character}: {descargados}")
    return descargados

def main():
    print("🚀 SCRIPT IMÁGENES GENSHIN - TODOS LOS PERSONAJES JUGABLES\n")

    # Lista completa de personajes jugables (Genshin Impact - Versión Natlan 2026)
    personajes = [
        "Albedo", "Alhaitham", "Aloy", "Amber", "Arataki Itto", "Arlecchino", 
        "Baizhu", "Barbara", "Beidou", "Bennett", "Candace", "Charlotte", 
        "Chevreuse", "Chiori", "Chongyun", "Clorinde", "Collei", "Cyno", 
        "Dehya", "Diluc", "Diona", "Dori", "Emilie", "Eula", "Faruzan", 
        "Fischl", "Freminet", "Furina", "Gaming", "Ganyu", "Gorou", 
        "Hu Tao", "Jean", "Kachina", "Kaedehara Kazuha", "Kaeya", 
        "Kamisato Ayaka", "Kamisato Ayato", "Kaveh", "Keqing", "Kinich", 
        "Kirara", "Klee", "Kujou Sara", "Kuki Shinobu", "Layla", "Lisa", 
        "Lynette", "Lyney", "Mavuika", "Mika", "Mona", "Mualani", "Nahida", 
        "Navia", "Neuvillette", "Nilou", "Ningguang", "Noelle", "Ororon", 
        "Qiqi", "Raiden Shogun", "Razor", "Rosaria", "Sangonomiya Kokomi", 
        "Sayu", "Sethos", "Shenhe", "Shikanoin Heizou", "Sigewinne", 
        "Sucrose", "Tartaglia", "Thoma", "Tighnari", "Traveler", "Venti", 
        "Wanderer", "Wriothesley", "Xiangling", "Xianyun", "Xiao", 
        "Xingqiu", "Xinyan", "Yae Miko", "Yanfei", "Yaoyao", "Yelan", 
        "Yoimiya", "Yun Jin", "Zhongli"
    ]

    total_descargados = 0

    for idx, personaje in enumerate(personajes, 1):
        print(f"\n[{idx}/{len(personajes)}] {personaje}")
        total_descargados += process_character(personaje)

    print(f"\n🎉 TOTAL DESCARGADOS: {total_descargados}")

if __name__ == "__main__":
    main()