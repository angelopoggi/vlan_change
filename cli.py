#VLAN Change CLI
#2021 - Angelo Poggi

import click
from vlanchange import vlan_change

@click.group(help =
             '''Change a VLAN to a new VLAN on a switch with that VLAN tagged''')

def main():
    pass

main.add_command(vlan_change)