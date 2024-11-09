import re
from Ai.Merchant.scene_merchant import SceneMerchant
from Misc import misc, global_vars
from States.menu_base import MenuBase


class MenuMerchant(MenuBase):
    def __init__(self, hero):
        super().__init__()
        self.hero = hero
        self.scene_merchant = SceneMerchant()

        self.phrase = ''
        self.chat_list = []

        self.is_in_merchant = True
        self.scene_loaded = False
        self.first_dialog = False
        self.chat = None
        self.bought = None

    def draw_menu(self):
        if not self.scene_loaded:
            self.initialize_scene()
            misc.clear()

        self.draw_market()

        for line in self.chat_list:
            print(line)

        self.phrase = input("You: ")
        self.bought = self.process_dialogue(self.phrase)

        if self.bought is False:
            return self.is_in_merchant

        self.continue_chat()

        return self.is_in_merchant

    def initialize_scene(self):
        misc.draw_line()
        self.start_chat()
        response = self.get_merchant_response(self.phrase)
        self.draw_market()
        self.append_chat("Merchant", response['text'])
        self.scene_loaded = True

    def get_merchant_response(self, input_text):
        return self.chat.invoke(input=input_text)

    def append_chat(self, speaker, text):
        print(f'{speaker}: {text}')
        self.chat_list.append(f'{speaker}: {text}')
        self.phrase = input("> ")

    def draw_market(self):
        misc.draw_line()
        print('The Happy Merchant')
        misc.draw_line()
        self.draw_status_hero()
        misc.draw_line()
        print('Potion: 15 gems each')
        print('Sharpen Sword: 30 gems each')
        misc.draw_line()

    def start_chat(self):
        self.chat = self.scene_merchant.create_chain()

    def process_dialogue(self, phrase):
        if 'bye' in phrase.lower():
            self.quit_merchant()
            return False
        elif self.handle_transaction(phrase):
            return True
        return False

    def handle_transaction(self, phrase):
        potions, sharpness, quantity = self.parse_dialogue(phrase)

        if not quantity and not potions and not sharpness:
            return True

        if not quantity:
            print("Invalid quantity.")
            return False

        if potions:
            return self.purchase_item('Potion', global_vars.potion_price, quantity, self.hero.buy_potions)
        elif sharpness:
            return self.purchase_item('Sharpen Sword', global_vars.sharpen_price, quantity, self.hero.sharpen_sword)
        return True

    def parse_dialogue(self, phrase):
        potions = re.findall(r'\b(potion|potions)\b', phrase, re.IGNORECASE)
        sharpness = re.findall(r'\b(sharpen|sharpness)\b', phrase, re.IGNORECASE)
        numbers = re.findall(r'\d+', phrase)
        quantity = int(numbers[0]) if numbers else 0
        return potions, sharpness, quantity

    def purchase_item(self, item_name, price, quantity, purchase_method):
        total_cost = price * quantity
        if self.hero.gems < total_cost:
            print(f'>>> You don’t have enough money for {quantity} {item_name.lower()}s! <<<')
        else:
            purchase_method(quantity)
            print(f'>>> You bought {quantity} {item_name.lower()} <<<')
        input('> ')
        return self.hero.gems >= total_cost

    def quit_merchant(self):
        print('Merchant: Good Bye!')
        input('> ')
        self.is_in_merchant = False

    def draw_status_hero(self):
        print("STATUS")
        print(f"NAME: {self.hero.name}")
        print(f"HP: {self.hero.hp}")
        print(f"ATTACK: {self.hero.atk}")
        print(f"POTIONS: {self.hero.potions}")
        print(f"GEMS: {self.hero.gems}")

    def continue_chat(self):
        self.chat_list.append(f'You: {self.phrase}')
        print('[wait...]')
        response = self.get_merchant_response(self.phrase)
        self.append_chat("Merchant", response['text'])
