#!/usr/bin/python
# coding: utf8
"""
Autor: Renato Machado
Objetivo: Function to convert mask and cidr, returns dictionary with address, mask and cidr
Alterações:
"""

import socket
import struct


def convert_cidr(address):

    network, net_bits = address.split('/')
    host_bits = 32 - int(net_bits)
    netmask = socket.inet_ntoa(struct.pack('!I', (1 << 32) - (1 << host_bits)))

    mask = address.split('/')[0] + ' ' + netmask

    cidr_mask = {
        'address': address.split('/')[0],
        'mask': str(mask).split(' ')[1],
        'cidr': '/'+str(address.split('/')[1])
    }

    print(cidr_mask)
    return cidr_mask


if __name__ == "__main__":

    convert_cidr('172.15.15.0/24')
