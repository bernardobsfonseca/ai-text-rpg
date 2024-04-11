from States.menu_base import MenuBase


class MenuBattle(MenuBase):
    def __init__(self, hero):
        super().__init__()

        self.hero = hero

    def draw_menu(self):
        print("EM BATALHA")
        input("# ")
        return False
