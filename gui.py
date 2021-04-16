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

from blockchain.block.block_main import get_block, create_block, get_block_from_other_node, sendme_full_node_list

from lib.settings_system import the_settings, test_mode, debug_mode

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import simpledialog, messagebox

import os


class main_gui:
    def __init__(self, master=None):
        self.toplevel = tk.Tk() if master is None else tk.Toplevel(master)

        self.toplevel.columnconfigure(0, weight=1)
        self.toplevel.rowconfigure(0, weight=1)

        self.frame = ttk.Frame(self.toplevel)

        self.block_44x50_png = tk.PhotoImage(file='gui/icons/ledger_38x50.png')
        self.cellmolecule_50x50_png = tk.PhotoImage(file='gui/icons/cell-molecule_50x50.png')
        self.computerinternetnetwork_68x50_png = tk.PhotoImage(file='gui/icons/computer-internet-network_68x50.png')
        self.money_67x50_png = tk.PhotoImage(file='gui/icons/money_67x50.png')

        self.get_block_button = ttk.Button(self.frame)
        self.get_block_button.configure(compound = 'top', image = self.block_44x50_png, text = 'Get block From Other Nodes')
        self.get_block_button.grid(column='0', padx='25', pady='20', row='1', sticky='n')
        self.get_block_button.configure(command=self.get_block_command)

        self.button2 = ttk.Button(self.frame)
        self.button2.configure(compound='top', image=self.computerinternetnetwork_68x50_png, text='Start Node Server')
        self.button2.grid(column='0', padx='25', pady='20', row='2', sticky='n')
        self.button2.configure(command=self.start_node_server)

        self.button3 = ttk.Button(self.frame)
        self.button3.configure(compound='top', image=self.cellmolecule_50x50_png, text='Connect Node \nfrom MIX Database')
        self.button3.grid(column='0', padx='25', pady='20', row='3', sticky='n')
        self.button3.configure(command=self.connect_node_fba_algorithm_infrustructure)

        self.send_coin_button = ttk.Button(self.frame)
        self.send_coin_button.configure(compound='top', image=self.money_67x50_png, text='Send Coin')
        self.send_coin_button.grid(column='1', padx='25', pady='20', row='3', sticky='n')
        self.send_coin_button.configure(command=self.send_coin)

        self.create_wallet_button = ttk.Button(self.frame)
        self.wallet_60x50_png = tk.PhotoImage(file='gui/icons/wallet_60x50.png')
        self.create_wallet_button.configure(compound='top', image=self.wallet_60x50_png, text='Create Wallet')
        self.create_wallet_button.grid(column='1', padx='25', pady='20', row='1', sticky='n')
        self.create_wallet_button.configure(command=self.Wallet_Create)

        self.balance_label = ttk.Label(self.frame)
        self.balance_label.configure(text='Balance: ')
        self.balance_label.grid(column='0', ipadx='25', padx='25', pady='20', row='4', sticky='n')
        self.reflesh_balance_button = ttk.Button(self.frame)
        self.reflesh_balance_button.configure(compound='top', text='Reflesh Balance')
        self.reflesh_balance_button.grid(column='0', padx='25', pady='20', row='5', sticky='n')
        self.reflesh_balance_button.configure(command=self.reflesh_balance)
        self.button1 = ttk.Button(self.frame)

        self.button1.configure(compound='top', image=self.cellmolecule_50x50_png, text='Connect Node')
        self.button1.grid(column='2', padx='25', pady='20', row='1', sticky='n')
        self.button1.configure(command=self.connect_node)

        self.buttonunl = ttk.Button(self.frame)
        self.buttonunl.configure(compound='top', image=self.cellmolecule_50x50_png, text='Add New UNL')
        self.buttonunl.grid(column='2', padx='25', pady='20', row='2', sticky='n')
        self.buttonunl.configure(command=self.add_new_unl)

        self.button_get_node_list = ttk.Button(self.frame)
        self.button_get_node_list.configure(compound='top', image=self.cellmolecule_50x50_png, text='Get Full Node List')
        self.button_get_node_list.grid(column='2', padx='25', pady='20', row='3', sticky='n')
        self.button_get_node_list.configure(command=self.get_node_list_command)

        self.button4 = ttk.Button(self.frame)
        self.button4.configure(compound='top', text='Test Mode ON')
        self.button4.grid(column='2', padx='25', pady='20', row='4', sticky='n')
        self.button4.configure(command=self.test_mode_on)
        self.button6 = ttk.Button(self.frame)
        self.button6.configure(compound='top', text='Test Mode OFF')
        self.button6.grid(column='2', padx='25', pady='20', row='5', sticky='n')
        self.button6.configure(command=self.test_mode_off)

        self.buttondebugmodeon = ttk.Button(self.frame)
        self.buttondebugmodeon.configure(compound='top', text='Debug Mode ON')
        self.buttondebugmodeon.grid(column='1', padx='25', pady='20', row='4', sticky='n')
        self.buttondebugmodeon.configure(command=self.debug_mode_on)
        self.buttondebugmodeoff = ttk.Button(self.frame)
        self.buttondebugmodeoff.configure(compound='top', text='Debug Mode OFF')
        self.buttondebugmodeoff.grid(column='1', padx='25', pady='20', row='5', sticky='n')
        self.buttondebugmodeoff.configure(command=self.debug_mode_off)

        self.button7 = ttk.Button(self.frame)
        self.button7.configure(compound='top', image=self.computerinternetnetwork_68x50_png, text='Stop Node Server')
        self.button7.grid(column='1', padx='25', pady='20', row='2', sticky='n')
        self.button7.configure(command=self.stop_node_server)
        self.frame.configure(height='200', width='200')
        self.frame.grid(column='0', row='0')
        self.toplevel.configure(height='200', takefocus=True, width='200')
        self.icon_50x50_png = tk.PhotoImage(file='gui/icons/icon_50x50.png')
        self.toplevel.iconphoto(True, self.icon_50x50_png)
        self.toplevel.resizable(True, True)
        self.toplevel.title('Decentra Network')

        from lib.settings_system import the_settings
        if the_settings()["test_mode"]:
            self.Test_Mode_Menu_Label = ttk.Label(self.frame, text="Test Mode Menu").grid(column='3', padx='25', pady='20', row='1', sticky='n')
            self.create_block_button = ttk.Button(self.frame)
            self.create_block_button.configure(compound='top', image=self.block_44x50_png, text='Create block')
            self.create_block_button.grid(column='3', padx='25', pady='20', row='2', sticky='n')
            self.create_block_button.configure(command=self.create_block)
        else:
            self.connect_to_main_network = ttk.Button(self.frame)
            self.connect_to_main_network.configure(compound='top', image=self.computerinternetnetwork_68x50_png, text='Connect to Main Network')
            self.connect_to_main_network.grid(column='3', padx='25', pady='20', row='1', sticky='n')
            self.connect_to_main_network.configure(command=self.connect_to_main_network_command)

        row = 7
        for folder_entry in os.scandir('apps'):
            if ".md" not in folder_entry.name:
                for entry in os.scandir("apps/"+folder_entry.name):
                    if entry.is_file():
                        if entry.name[0] != '_' and ".py" in entry.name and "_main" in entry.name:
                            self.App_Menu_Label = ttk.Label(self.frame, text="APP Menu").grid(column='0', padx='25', pady='20', row='6', sticky='n')
                            import_command = f"from apps.{folder_entry.name}.{entry.name.replace('.py','')} import {entry.name.replace('.py','')}_gui"
                            tx_command = f"{entry.name.replace('.py','')}_gui(self,0,row)"
                            exec (import_command)
                            exec (tx_command)

                            row += 1

        self.mainwindow = self.toplevel

    def connect_to_main_network_command(self):
        from func.node_connection import connect_to_main_network
        connect_to_main_network()

    def apps_func(self, import_arguments, func_name):
        exec (import_arguments)
        command = f"{func_name}(self)"
        exec (command)

    def create_block(self):
        create_block()
        messagebox.showinfo('Wallet', 'block are created.')

    def get_block_command(self):
        get_block_from_other_node()
        messagebox.showinfo('Wallet', 'Taked the blockchain.')

    def Wallet_Create(self):
        Wallet_Create()
        messagebox.showinfo('Wallet', 'Wallet are created.')

    def send_coin(self):

        received_adress = simpledialog.askstring("Input", "Please write receiver adress: ", parent=self.toplevel)
        if received_adress is not None:
            print("Receiver adress: ", received_adress)
        else:
            print("You don't write a receiver adress ?")

        amount = simpledialog.askfloat("Input", "Coin Amount: ", parent=self.toplevel)

        if amount is not None:
            print("Coin Amount (ex. 1.0): ", amount)
        else:
            print("You don't write a coin amount ?")

        try:
            float(amount)
        except:
            messagebox.showinfo('Send Coin', "This is not float coin amount.")
            return None
        if amount > 0:
            if messagebox.askokcancel("Okey", ("Receiver adress: "+received_adress+"\n"+"Amount: "+str(amount))):
                send_coin(amount, received_adress)
        else:
            messagebox.showinfo('Send Coin', "This is negative coin amount.")

    def reflesh_balance(self):
        self.balance_label.configure(text = ("Balance: "+str(get_block().getBalance(Wallet_Import(0,0)))))

    def connect_node(self):
        ip = simpledialog.askstring("Input", "IP: ", parent=self.toplevel)
        if ip is not None:
            print("IP: ", ip)
        else:
            print("You don't write ip ?")

        port = simpledialog.askinteger("Input", "Port: ", parent=self.toplevel, minvalue=0, maxvalue=65353)
        if port is not None:
            print("Port: ", port)
        else:
            print("You don't write port ?")

        ndconnect(ip, port)

        messagebox.showinfo('Node', ("Connected Node on "+"IP: "+ip+" PORT: "+str(port)+"."))

    def add_new_unl(self):
        id = simpledialog.askstring("Input", "ID: ", parent=self.toplevel)
        if id is not None:
            print("Pubkey: ", id)
        else:
            print("You don't write ID ?")

        from node.unl import save_new_unl_node
        save_new_unl_node(id)

        messagebox.showinfo('Node', ("Added new node. "+"ID: "+id))

    def get_node_list_command(self):
        sendme_full_node_list()

        messagebox.showinfo('Node', "Ok")

    def start_node_server(self):
        ip = simpledialog.askstring("Input", "IP: ", parent=self.toplevel)
        if ip is not None:
            print("IP: ", ip)
        else:
            print("You don't write ip ?")

        port = simpledialog.askinteger("Input", "Port: ", parent=self.toplevel, minvalue=0, maxvalue=65353)
        if port is not None:
            print("Port: ", port)
        else:
            print("You don't write port ?")

        ndstart(ip, port)
        messagebox.showinfo('Node', ('Node server is started on '+str(port)+"."))

    def connect_node_fba_algorithm_infrustructure(self):
        ndconnectmixdb()
        messagebox.showinfo('Node', 'Connected Node or Nodes from decentra_network database.')

    def test_mode_on(self):
        test_mode(True)
        messagebox.showinfo('System', 'Test mode is ON')

    def test_mode_off(self):
        test_mode(False)
        messagebox.showinfo('System', 'Test mode is OFF')

    def debug_mode_on(self):
        debug_mode(True)
        messagebox.showinfo('System', 'Debug mode is ON')

    def debug_mode_off(self):
        debug_mode(False)
        messagebox.showinfo('System', 'Debug mode is OFF')

    def stop_node_server(self):
        ndstop()
        messagebox.showinfo('Node', 'Node server is stoped.')

    def run(self):
        self.mainwindow.mainloop()


def start():
    app = main_gui()
    app.run()

if __name__ == '__main__':
    start()
