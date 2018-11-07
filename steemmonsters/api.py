from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import sys
from datetime import datetime, timedelta, date
import time
import io
import json
import requests
from timeit import default_timer as timer
import logging


class Api(object):
    """ Access the steemmonsters API
    """
    __url__ = 'https://steemmonsters.com/'

    def get_card_details(self):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            response = requests.get(self.__url__ + "cards/get_details")
            if str(response) != '<Response [200]>':
                time.sleep(2)
            cnt2 += 1
        return response.json()

    def get_purchases_stats(self):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            response = requests.get(self.__url__ + "purchases/stats")
            if str(response) != '<Response [200]>':
                time.sleep(2)
            cnt2 += 1
        return response.json()

    def settings(self):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            response = requests.get(self.__url__ + "settings")
            if str(response) != '<Response [200]>':
                time.sleep(2)
            cnt2 += 1
        return response.json()

    def players_leaderboard(self):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            response = requests.get(self.__url__ + "players/leaderboard")
            if str(response) != '<Response [200]>':
                time.sleep(2)
            cnt2 += 1
        return response.json()

    def find_cards(self, card_ids):
        if isinstance(card_ids, list):
            card_ids_str = ','.join(card_ids)
        else:
            card_ids_str = card_ids
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            response = requests.get(self.__url__ + "/cards/find?ids=%s" % card_ids_str)
            if str(response) != '<Response [200]>':
                time.sleep(2)
            cnt2 += 1
        return response.json()
    
    def get_open_all_packs(self, player, edition, token):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            response = requests.get(self.__url__ + "cards/open_all_packs/%s?player=%s&edition=%d&token=%s&username=%s" % (player, player, edition, token, player))
            cnt2 += 1
        return response.json()

    def get_open_packs(self, uuid, player, edition, token):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            response = requests.get(self.__url__ + "cards/open_pack/%s?player=%s&edition=%d&token=%s&username=%s" % (uuid, player, edition, token, player))
            cnt2 += 1
        return response.json()

    def get_cards_packs(self, player, token):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            response = requests.get(self.__url__ + "cards/packs/%s?token=%s" % (player, token))
            cnt2 += 1
        return response.json()

    def get_collection(self, player):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            response = requests.get(self.__url__ + "cards/collection/%s" % player)
            cnt2 += 1
        return response.json()

    def get_player_login(self, player):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            response = requests.get(self.__url__ + "players/login?name=%s" % player)
            cnt2 += 1
        return response.json()

    def get_player_details(self, player):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            response = requests.get(self.__url__ + "players/details?name=%s" % player)
            cnt2 += 1
        return response.json()

    def player_save_team(self, name, team, player, token, mana_cap):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            response = requests.get(self.__url__ + "players/save_team?name=%s&team=%s&mana_cap=%d&token=%s&username=%s" % (name, team, mana_cap, token, player))
            cnt2 += 1
        return response.json()

    def player_delete_team(self, name, player, token, mana_cap):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            response = requests.get(self.__url__ + "players/delete_team?name=%s&mana_cap=%d&token=%s&username=%s" % (name, mana_cap, token, player))
            cnt2 += 1
        return response.json()

    def get_player_saved_teams(self, player, token, mana_cap):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            response = requests.get(self.__url__ + "players/saved_teams?mana_cap=%d&token=%s&username=%s" % (mana_cap, token, player))
            cnt2 += 1
        if str(response) == '<Response [500]>':
            print(response.content)
            return {}
        return response.json()

    def get_player_teams_last_used(self, player, mana_cap):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            response = requests.get(self.__url__ + "players/saved_teams?mana_cap=%d&team=Last%%20Used&player=%s" % (mana_cap, player))
            cnt2 += 1
        if len(response.content) == 0:
            return ""
        return response.json()

    def get_player_quests(self, player):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            response = requests.get(self.__url__ + "players/quests?username=%s" % player)
            cnt2 += 1
        return response.json()

    def get_for_sale(self):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            response = requests.get(self.__url__ + "market/for_sale")
            if str(response) != '<Response [200]>':
                time.sleep(2)
            cnt2 += 1
        return response.json()

    def get_purchases_settings(self):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            response = requests.get(self.__url__ + "purchases/settings")
            if str(response) != '<Response [200]>':
                time.sleep(2)
            cnt2 += 1
        return response.json()
    
    def get_purchases_status(self, uuid):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            response = requests.get(self.__url__ + "purchases/status?id=%s" % uuid)
            if str(response) != '<Response [200]>':
                time.sleep(2)
            cnt2 += 1
        return response.json()

    def get_from_block(self, block_num):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            response = requests.get(self.__url__ + "transactions/history?from_block=%d" % block_num)
            if str(response) != '<Response [200]>':
                time.sleep(2)
            cnt2 += 1
        return response.json()

    def get_transaction(self, trx):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            response = requests.get(self.__url__ + "transactions/lookup?trx_id=%s" % trx)
            if str(response) != '<Response [200]>':
                time.sleep(2)
            cnt2 += 1
        return response.json()

    def get_cards_stats(self):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            response = requests.get(self.__url__ + "cards/stats")
            if str(response) != '<Response [200]>':
                time.sleep(2)
            cnt2 += 1
        return response.json()

    def get_market_for_sale_by_card(self, card_detail_id, gold, edition):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            response = requests.get(self.__url__ + "market/for_sale_by_card?card_detail_id=%d&gold=%s&edition=%d" % (card_detail_id, gold, edition))
            if str(response) != '<Response [200]>':
                time.sleep(2)
            cnt2 += 1
        return response.json()

    def get_market_for_sale_grouped(self):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            response = requests.get(self.__url__ + "market/for_sale_grouped")
            if str(response) != '<Response [200]>':
                time.sleep(2)
            cnt2 += 1
        return response.json()

    def get_market_status(self, market_id):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 10:
            response = requests.get(self.__url__ + "market/status?id=%s" % market_id)
            if str(response) != '<Response [200]>':
                time.sleep(2)
            cnt2 += 1
        return response.json()

    def get_battle_history(self, player="%24top"):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 20:
            response = requests.get(self.__url__ + "battle/history?player=%s" % player)
            if str(response) != '<Response [200]>':
                time.sleep(1)
            cnt2 += 1
        return response.json()

    def get_battle_result(self, ids):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 20:
            response = requests.get(self.__url__ + "battle/result?id=%s" % ids)
            if str(response) != '<Response [200]>':
                time.sleep(1)
            cnt2 += 1
        return response.json()

    def get_battle_status(self, ids):
        response = ""
        cnt2 = 0
        while str(response) != '<Response [200]>' and cnt2 < 20:
            response = requests.get(self.__url__ + "battle/status?id=%s" % ids)
            if str(response) != '<Response [200]>':
                time.sleep(1)
            cnt2 += 1
        return response.json()
