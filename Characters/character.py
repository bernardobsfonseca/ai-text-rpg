class Character:
    def __init__(self, name, hp, atk) -> None:
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.atk = atk

    def attack(self, target) -> None:
        target.hp -= self.atk
        target.hp = max(target.hp, 0)

        print(f"{self.name} atacou {target.name} e causou "
              f"{self.atk} de dano")
