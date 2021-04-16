import json

from lib.mixlib import dprint
from config import *

import os
import sys

def save_new_unl_node(id):
    id = id
    node = None

<<<<<<< HEAD
    from node.myownp2pn import MyOwnPeer2PeerNode
    for inbound_node in MyOwnPeer2PeerNode.main_node.nodes_inbound:
        if id in (inbound_node.id):
            node = inbound_node
    for outbound_node in MyOwnPeer2PeerNode.main_node.nodes_outbound:
=======
    from node.myownp2pn import mynode
    for inbound_node in mynode.main_node.nodes_inbound:
        if id in (inbound_node.id):
            node = inbound_node
    for outbound_node in mynode.main_node.nodes_outbound:
>>>>>>> 4e9cb25a3168dc85c23cdc983e683ce93fb8e7f8
        if id in (outbound_node.id):
            node = outbound_node
    if node != None:
        nodes_list = get_unl_nodes()

        already_in_list = False

        for element in nodes_list:
            if element == node.id:
                already_in_list = True

        if not already_in_list:

     
         nodes_list[node.id] = {}
         nodes_list[node.id]["host"] = node.host
         nodes_list[node.id]["port"] = node.port

         

         sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

         from lib.config_system import get_config


         old_cwd = os.getcwd()
         os.chdir(get_config()["main_folder"])
         with open(UNL_NODES_PATH, 'w') as unl_nodes_file:
<<<<<<< HEAD
             json.dump(nodes_list, unl_nodes_file)
=======
             json.dump(nodes_list, unl_nodes_file, indent=4)
>>>>>>> 4e9cb25a3168dc85c23cdc983e683ce93fb8e7f8
         os.chdir(old_cwd)

def get_unl_nodes():

        sys.path.append(os.path.join(os.path.dirname(__file__), ".."))


        from lib.config_system import get_config
        
        if not os.path.exists(UNL_NODES_PATH):
            return {}
 


        os.chdir(get_config()["main_folder"])
        with open(UNL_NODES_PATH, 'rb') as unl_nodes_file:
            return json.load(unl_nodes_file)



def get_as_node_type(id_list):
        temp_list = []
        from node.myownp2pn import mynode
        for list_node in id_list:
            for inbound in mynode.main_node.nodes_inbound:
                if list_node in inbound.id:
                    temp_list.append(inbound)
            for outbound in mynode.main_node.nodes_outbound:
                if list_node in outbound.id:
                    temp_list.append(outbound)
        return temp_list


def node_is_unl(node_id):
    node_id = node_id
    for unl in get_unl_nodes():
        temp_unl = unl
        if node_id == temp_unl:
            return True
    return False

def unl_node_delete(node_id):
    saved_nodes = get_unl_nodes()
    if node_id in saved_nodes:
        del saved_nodes[node_id]
        from lib.config_system import get_config
    

        os.chdir(get_config()["main_folder"])
        with open(UNL_NODES_PATH, 'w') as connected_node_file:
<<<<<<< HEAD
            json.dump(saved_nodes, connected_node_file)
=======
            json.dump(saved_nodes, connected_node_file, indent=4)
>>>>>>> 4e9cb25a3168dc85c23cdc983e683ce93fb8e7f8
