#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Transaction:
    def __init__(self, sequance_number, signature, fromUser, toUser, data, amount, transaction_fee):
        self.sequance_number = sequance_number
        self.signature = signature
        self.fromUser = fromUser
        self.toUser = toUser
        self.data = data
        self.amount = amount
        self.transaction_fee = transaction_fee

    def dump_json(self):
        data = {
            "sequance_number": self.sequance_number,
            "signature": self.signature,
            "fromUser": self.fromUser,
            "toUser": self.toUser,
            "data": self.data,
            "amount": self.amount,
            "transaction_fee": self.transaction_fee
        }
        return data

    @staticmethod
    def load_json(data):
        return Transaction(data["sequance_number"],data["signature"],data["fromUser"],data["toUser"],data["data"],data["amount"],data["transaction_fee"])