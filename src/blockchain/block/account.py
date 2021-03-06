#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import hashlib
import json

class Account:
    def __init__(self, PublicKey, balance, sequance_number=0):
        self.PublicKey = PublicKey

        self.sequance_number = sequance_number
        self.balance = balance

    def get_hash(self, encoding="ascii"):
        account_data = json.dumps(self.dump_json()).encode(encoding)
        return hashlib.sha256(account_data).hexdigest()

    def dump_json(self):
        data = {
            "public_key": self.PublicKey,
            "balance": self.balance,
            "sequence_number": self.sequance_number
        }
        return data

    @staticmethod
    def load_json(data):
        return Account(data["public_key"], data["balance"], data["sequence_number"])
