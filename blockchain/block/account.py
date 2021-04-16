#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json

class Account:
    def __init__(self, PublicKey, balance, sequance_number=0):
        self.PublicKey = PublicKey

        from blockchain.block.block_main import get_block

        try:
            self.id = len(get_block().Accounts) + 1
        except:
            self.id = 0
        self.sequance_number = sequance_number
        self.balance = balance

    def dump_json(self):
        data = {
            "public_key": self.PublicKey,
            "id": self.id,
            "sequence_number": self.sequance_number,
            "balance": self.balance
        }
        return data

    @staticmethod
    def load_json(data):
        return Account(data["public_key"], data["balance"], data["id"], data["sequance_number"])