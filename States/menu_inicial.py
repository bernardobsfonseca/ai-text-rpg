from random import randint
from Characters.hero import Hero
from Misc import misc
from States.menu_base import MenuBase
from Ai.SceneEnemy import scene_enemy as se
from Ai.SceneAmbient import scene_ambient as sa


class MenuInicial(MenuBase):
    def __init__(self):
        super().__init__()

        print("Carregando gerador cenário...")
        sa.initialize_scene_embient()

        print("\n")

        print("Carregando gerador batalha...")
        se.initialize_scene_enemy()

        misc.clear()

    def draw_menu(self):
        misc.draw_logo()
        misc.draw_line()
        print("1 - Novo Jogo")
        print("2 - Carregar Jogo")
        print("3 - Como Jogar")
        print("4 - Sair")
        misc.draw_line()

        choice = input("# ")

        if choice == "1":
            return self.new_game()
        elif choice == "2":
            return self.load_game()
        elif choice == "3":
            return self.how_to_play()
        elif choice == "4":
            self.sair()
            misc.clear()
        else:
            print('Opção inválida')
            input('> ')
            return None, None

    def new_game(self):
        name = input("Digite o nome de seu personagem: ")
        hero = Hero(name=name)
        seed_value = randint(0, 1000)

        return hero, seed_value

    def load_game(self):
        name_character = input("Insira o nome do personagem: ")
        hero, seed_value = misc.load_game(name_character)

        return hero, seed_value

    def how_to_play(self):
        print("""
Inputs:
    > O sinal '>' espera a tecla 'Enter' para trocar de tela
    > O sinal de '#' espera um input do jogador

Movimentação e itens:
    > O 'P' é o jogador
    > Mova-se pelo mapa utilizando as teclas '1', '2', '3' e '4'
    > Use poções utilizando a tecla '5'
    > Salve o estado atual e saia do jogo utilizando a tecla '0'

Terrenos:
    > Os '.'s são terrenos de planice
    > Os '8's são florestas
    > Os '~'s são terrenos alagados
    > Os 'A's são terrenos montanhosos
    > Os 'M's são florestas de pinheiros
    > A cada mudança de terrenos será gerada uma nova descrição

Batalha:
    > Use '1' para atacar
    > Use '2' para usar uma poção
    > use '3' para tentar fugir do inimigo

Mercador:
    > Representado pelo 'M' no mapa
    > É possível ter um dialogo com ele
    > O momento de falar é indicado pelo 'You:' no input
    > Para comprar poções digite 'potion'/'potions' e o número de poções na mesma frase. Ex: 'i want 5 potions'
    > Para comprar ataque digite 'sharpen'/'sharpness' e o número de 'ataques' na mesma frase. Ex: 'i want 5 sharpness'

Objetivo - O Dragão:
    > Para vencer você deve matar o Dragão
    > Representado pela letra 'D' no mapa
    > Boa sorte
        """)
        input('> ')
        return None, None

    def sair(self):
        choice_sair = input("# Realmente deseja sair (s/n)?: ")
        if choice_sair.lower() == "s":
            quit()
