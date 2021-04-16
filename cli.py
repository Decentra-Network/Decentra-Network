#!/usr/bin/python3
# -*- coding: utf-8 -*-
import hashlib
import datetime
import json

import uuid

from hashlib import sha256


from sys import version_info as pyVersion
from binascii import hexlify, unhexlify

from wallet.wallet import *

from func.send_coin import send_coin
from func.node_connection import *

from lib.mixlib import *

import pickle

from blockchain.block.block_main import get_block , create_block, get_block_from_other_node, sendme_full_node_list



import os
from lib.settings_system import the_settings, test_mode, debug_mode

def show_menu():

    print(banner_maker(sc_name="Decentra Network", description="This is an open source decentralized application network. In this network, you can develop and publish decentralized applications.", author="Decentra Network Developers"))

    if the_settings()["test_mode"]:
        print(menu_maker(menu_number="cbl", menu_text="Create block"))
    else:
        print(menu_maker(menu_number="connectmainnetwork", menu_text="Connect to Main Network"))

    print(menu_space() + \
	   menu_maker(menu_number="cw", menu_text="Create wallet")+ \
	   menu_space() + \
	   menu_maker(menu_number="sc", menu_text="Send Coin")+ \
       menu_space() + \
       menu_maker(menu_number="gb", menu_text="Get Balance")+ \
       menu_space() + \
       menu_maker(menu_number="ndstart", menu_text="Node Start")+ \
       menu_maker(menu_number="ndstop", menu_text="Node Stop")+ \
       menu_maker(menu_number="ndconnect", menu_text="Node Connect")+ \
       menu_maker(menu_number="connectmainnetwork", menu_text="Connect to Main Network")+ \
       menu_maker(menu_number="ndconnectmixdb", menu_text="Node Connect from mixdb")+ \
       menu_maker(menu_number="ndnewunl", menu_text="Add new UNL node")+ \
       menu_space() + \
       menu_maker(menu_number="testmodeon", menu_text="Test mode ON")+ \
       menu_maker(menu_number="testmodeoff", menu_text="Test mode OF")+ \
       menu_maker(menu_number="debugmodeon", menu_text="Debug mode ON")+ \
       menu_maker(menu_number="debugmodeoff", menu_text="Debug mode OF")+ \
       menu_space() + \
       menu_maker(menu_number="getfullnodelist", menu_text="Get Full Node List")+ \
       menu_maker(menu_number="getblock", menu_text="Get block From Other Nodes")+ \
       menu_space())

    for folder_entry in os.scandir('apps'):
        if ".md" not in folder_entry.name:
            for entry in os.scandir("apps/"+folder_entry.name):
                if entry.is_file():
                    if entry.name[0] != '_' and ".py" in entry.name and "_main" in entry.name:
                        print(entry.name)
                        import_command = f"from apps.{folder_entry.name}.{entry.name.replace('.py','')} import {entry.name.replace('.py','')}_cli"
                        tx_command = f"{entry.name.replace('.py','')}_cli()"
                        exec (import_command)
                        exec (tx_command)

    print(quit_menu_maker(mode="main"))


def menu():
    while True:
        show_menu()
        choices_input = question_maker(mode="main")

        if the_settings()["test_mode"]:
            if choices_input == "cbl":
                create_block()
        else:
            if choices_input == "connectmainnetwork":
                from func.node_connection import connect_to_main_network
                connect_to_main_network()
        if choices_input == "cw":
            Wallet_Create()
        if choices_input == "sc":
            temp_coin_amount = input("Coin Amount (ex. 1.0): ")
            type_control = False
            try:
                float(temp_coin_amount)
                type_control = True
            except:
                print("This is not float coin amount.")

            if type_control:
                send_coin(float(temp_coin_amount), input("Please write receiver adress: "))

        if choices_input == "gb":
            print(get_block().getBalance(Wallet_Import(0,0)))
        if choices_input == "help":
            show_menu()
        if choices_input == "ndstart":
            ndstart(str(input("ip: ")), int(input("port: ")))
        if choices_input == "ndstop":
            ndstop()
        if choices_input == "ndconnect":
            ndconnect(str(input("node ip: ")), int(input("node port: ")))

        if choices_input == "ndconnectmixdb":
            ndconnectmixdb()
        if choices_input == "ndnewunl":
            from node.unl import save_new_unl_node
            save_new_unl_node(input("Please write ID of the node: "))
        if choices_input == "testmodeon":
            test_mode(True)
        if choices_input == "testmodeoff":
            test_mode(False)
        if choices_input == "debugmodeon":
            debug_mode(True)
            # from node.myownp2pn import mynode
            # mynode.main_node.debug = True
        if choices_input == "debugmodeoff":
            debug_mode(False)
            # from node.myownp2pn import mynode
            # mynode.main_node.debug = False

        if choices_input == "getfullnodelist":
            sendme_full_node_list()
        if choices_input == "getfullblock":
            get_block_from_other_node()

        for folder_entry in os.scandir('apps'):
            if ".md" not in folder_entry.name:
                for entry in os.scandir("apps/"+folder_entry.name):
                    if entry.is_file():
                        if entry.name[0] != '_' and ".py" in entry.name and "_main" in entry.name:
                            print(entry.name)
                            import_command = f"from apps.{folder_entry.name}.{entry.name.replace('.py','')} import {entry.name.replace('.py','')}_cli_command"
                            tx_command = f"{entry.name.replace('.py','')}_cli_command(choices_input)"
                            exec (import_command)
                            exec (tx_command)

        if choices_input == "0":
            exit()


def start():
    menu()

if __name__ == '__main__':
    start()
