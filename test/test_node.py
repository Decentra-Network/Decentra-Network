#!/usr/bin/python3
# -*- coding: utf-8 -*-
import unittest


class Test_Node(unittest.TestCase):

    def test_node_connection_saving_and_unl(self):

        temp_private_key_class = Wallet_Create()


        node_1 = ndstart("127.0.0.1",10001)
        

        temp_private_key = temp_private_key_class.toPem()

        saved_wallets = get_saved_wallet()

        for each_wallet in saved_wallets:
            if temp_private_key == saved_wallets[each_wallet]["privatekey"]:
                Wallet_Delete(each_wallet)  


        temp_private_key_class2 = Wallet_Create()

        node_2 = ndstart("127.0.0.1",10002)

        temp_private_key2 = temp_private_key_class2.toPem()

        saved_wallets2 = get_saved_wallet()

        for each_wallet in saved_wallets2:
            if temp_private_key2 == saved_wallets2[each_wallet]["privatekey"]:
                Wallet_Delete(each_wallet) 


        ndconnect("127.0.0.1", 10001)

        finded_node = False
        in_unl_list = False
        get_as_node = False

        nodes_list = get_connected_node()

        for element in nodes_list:
            if element == node_1.id or element == node_2.id:
                finded_node = True
                save_new_unl_node(node_1.id)
                save_new_unl_node(node_2.id)
                temp_unl_node_list = get_unl_nodes()
                temp_get_as_node_type = get_as_node_type(temp_unl_node_list)
                for unl_element in temp_unl_node_list:
                    if unl_element == node_1.id or unl_element == node_2.id:
                        for node_element_of_unl in temp_get_as_node_type:
                            if node_1.host == node_element_of_unl.host or node_2 == node_element_of_unl.host:
                                if node_1.port == node_element_of_unl.port or node_2 == node_element_of_unl.port:
                                    get_as_node = True
                        in_unl_list = True
                        unl_node_delete(unl_element)
                connected_node_delete(element)
        
        node_1.stop()
        node_2.stop()



        self.assertEqual(finded_node,True,"Problem on connection saving system.")
        self.assertEqual(in_unl_list,True,"Problem on UNL node saving system.")
        self.assertEqual(get_as_node,True,"Problem on UNL get as node system.")


if __name__ == '__main__':
    import os
    import sys
    sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
    from wallet.wallet import Wallet_Create, get_saved_wallet, Wallet_Import, Wallet_Delete
    from func.node_connection import ndstart, ndconnect, ndstop
    from node.node import get_connected_node, connected_node_delete
    from node.unl import save_new_unl_node, get_unl_nodes, get_as_node_type, unl_node_delete
    unittest.main()
