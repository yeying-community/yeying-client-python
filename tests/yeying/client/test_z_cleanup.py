# -*- coding:utf-8 -*-
import os


from tests.yeying import option
from yeying.api.asset import namespace_pb2
from yeying.client.provider.namespace_provider import NamespaceProvider
from yeying.client.utils import log_utils
import pytest


log = log_utils.get_logger(__name__)


@pytest.fixture
def before():
    log.info("delete namespace start test")
    namespace_provider = NamespaceProvider(option=option)
    yield namespace_provider


def test_delete(before):
    log.info("start delete namespace")
    namespace_provider = before
    log.info(namespace_provider)
    namespace_id1 = os.environ.get("namespace_id")
    assert namespace_id1 is not None
    assert isinstance(namespace_id1, str)
    res: namespace_pb2.DeleteNamespaceResponse = namespace_provider.delete(uid=namespace_id1)
    log.info(f"res={res}")
    log.info("success delete namespace")