from Ai.Merchant.scene_merchant import SceneMerchant
from Misc import misc
from States.menu_base import MenuBase


class MenuMerchant(MenuBase):
    def __init__(self, hero):
        super().__init__()
        self.hero = hero
        self.scene_merchant = SceneMerchant()

        self.phrase = ''
        self.chat_list = []

        self.scene_loaded = False
        self.first_dialog = False
        self.chat = None

    def draw_menu(self):
        if not self.scene_loaded:
            misc.draw_line()
            self.start_chat()
            resp = self.chat.invoke(input=self.phrase)
            self.draw_market()
            print(f' Mechant: {resp['text']}')
            self.chat_list.append(f' Mechant: {resp['text']}')
            self.phrase = input("> ")
            misc.clear()
            self.scene_loaded = True

        self.draw_market()

        for line in self.chat_list:
            print(line)

        self.phrase = input(" You: ")
        self.chat_list.append(f' You: {self.phrase}')

        resp = self.chat.invoke(input=self.phrase)
        print(f' Merchant: {resp['text']}')
        self.chat_list.append(f' Merchant: {resp['text']}')

        self.phrase = input("> ")

        return True

    def draw_market(self):
        misc.draw_line()
        print('The Happy Merchant')
        misc.draw_line()
        print('Potion: 5 gems each')
        print('Sharpen Sword: 10 gems each')
        misc.draw_line()

    def start_chat(self):
        self.chat = self.scene_merchant.create_chain()
