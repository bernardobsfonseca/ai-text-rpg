import os
from pathlib import Path
from Characters.hero import Hero


def draw_logo():
    print("""
      /$$$$$$  /$$$$$$       /$$$$$$$$                    /$$           /$$$$$$$  /$$$$$$$   /$$$$$$ 
     /$$__  $$|_  $$_/      |__  $$__/                   | $$          | $$__  $$| $$__  $$ /$$__  $$
    | $$  \ $$  | $$           | $$  /$$$$$$  /$$   /$$ /$$$$$$        | $$  \ $$| $$  \ $$| $$  \__/
    | $$$$$$$$  | $$           | $$ /$$__  $$|  $$ /$$/|_  $$_/        | $$$$$$$/| $$$$$$$/| $$ /$$$$
    | $$__  $$  | $$           | $$| $$$$$$$$ \  $$$$/   | $$          | $$__  $$| $$____/ | $$|_  $$
    | $$  | $$  | $$           | $$| $$_____/  >$$  $$   | $$ /$$      | $$  \ $$| $$      | $$  \ $$
    | $$  | $$ /$$$$$$         | $$|  $$$$$$$ /$$/\  $$  |  $$$$/      | $$  | $$| $$      |  $$$$$$/
    |__/  |__/|______/         |__/ \_______/|__/  \__/   \___/        |__/  |__/|__/       \______/
    """)


def save_game(hero, seed_value):
    caminho_pasta = Path("Saves")
    caminho_pasta.mkdir(parents=True, exist_ok=True)

    arquivo_txt = caminho_pasta / f"{hero.name}.txt"

    with open(arquivo_txt, "w") as arquivo:
        arquivo.write(f"{hero.name}\n")
        arquivo.write(f"{hero.hp}\n")
        arquivo.write(f"{hero.atk}\n")
        arquivo.write(f"{hero.potions}\n")
        arquivo.write(f"{hero.gems}\n")
        arquivo.write(f"{hero.x}\n")
        arquivo.write(f"{hero.y}\n")

        arquivo.write(f"{seed_value}\n")


def load_game(name_character):
    caminho_pasta = Path("Saves")
    caminho_pasta.mkdir(parents=True, exist_ok=True)

    arquivo_txt = caminho_pasta / f"{name_character}.txt"

    with open(arquivo_txt, "r") as arquivo:
        nome = arquivo.readline().strip()
        hp = int(arquivo.readline().strip())
        atk = int(arquivo.readline().strip())
        potions = int(arquivo.readline().strip())
        gems = int(arquivo.readline().strip())
        x = int(arquivo.readline().strip())
        y = int(arquivo.readline().strip())

        seed_value = int(arquivo.readline().strip())

        hero = Hero(nome, hp, atk, potions, gems, x, y)

    return hero, seed_value


def draw_line():
    print("xX------------------------Xx")


def clear():
    os.system("cls")
