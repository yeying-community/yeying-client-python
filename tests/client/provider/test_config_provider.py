# -*- coding:utf-8 -*-
from client.model.option import ProviderOption
from client.provider.config_provider import ConfigProvider
from client.utils import log_utils
import pytest

from yeying.api.web3 import BlockAddress

log = log_utils.get_logger(__name__)


@pytest.fixture
def before():
    log.info("\n=== 测试开始 ===")
    block_address: BlockAddress = BlockAddress()
    option: ProviderOption = ProviderOption(proxy="127.0.0.1:8441", block_address=block_address)
    config_provider = ConfigProvider(option=option)
    yield config_provider


def test_get(before):
    config_provider = before
    log.info(config_provider)
    log.info("test test !!!")
