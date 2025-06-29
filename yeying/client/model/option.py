# -*- coding:utf-8 -*-
from yeying.api.web3 import BlockAddress


class ProviderOption(object):

    def __init__(self, proxy, block_address):
        self.proxy = proxy
        self.block_address: BlockAddress = block_address
