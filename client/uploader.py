# -*- coding:utf-8 -*-
import binascii
import hashlib
import math
from typing import List
from client.model.file import File
from client.model.option import ProviderOption
from client.provider.asset_provider import AssetProvider
from client.provider.block_provider import BlockProvider
from client.provider.config_provider import ConfigProvider
from client.utils.date_utils import get_current_iso_string
from client.utils.digital_format_utils import get_digital_format_by_name
from yeying.api.asset import AssetMetadata, BlockMetadata
from yeying.api.config import ConfigTypeEnum
from utils import log_utils
from typing import Callable, Protocol, TypedDict, Optional

log = log_utils.get_logger(__name__)


class Progress(TypedDict):
    """进度接口"""

    total: int
    completed: int


class UploadResult(TypedDict):
    """上传结果接口"""

    block: BlockMetadata
    progress: Progress


# 定义回调类型
UploadCallback = Callable[[UploadResult], None]

"""
资产仓库的客户端实现
文件上传
"""


class Uploader(object):

    def __init__(self, option: ProviderOption):
        # 资产元信息
        self.asset_provider = AssetProvider(option=option)
        # 文件操作
        self.block_provider = BlockProvider(option=option)
        # 字典配置
        self.config_provider = ConfigProvider(option=option)
        # 文件单个块的大小，从系统配置表中动态获取
        config_res = self.config_provider.get("chunk.size", ConfigTypeEnum.CONFIG_TYPE_SYSTEM)
        self.chunkSize = int(config_res.body.config.value)
        self.is_abort: bool = False

    def abort(self):
        self.is_abort = True

    def put(
        self,
        namespace_id: str,
        file: File,
        encrypted: bool = False,
        block_callback: UploadCallback = None,
        description: str = None,
        parent_hash: str = None,
    ):
        """
        上传文件,将文件分块处理，加密（可选），并逐块上传到区块链网络中
        :param namespace_id:命名空间 ID
        :param file:要上传的文件对象
        :param encrypted:是否对文件进行加密（默认为 false）
        :param block_callback:可选，通知当前成功的块元信息和进度信息
        :param description:资产描述（可选）
        :param parent_hash:父资产的哈希值（可选）
        :return:
        """
        asset = AssetMetadata(
            namespaceId=namespace_id,
            owner=self.block_provider.get_owner(),
            parentHash=parent_hash,
            hash=None,
            version=None,
            name=file.name,
            chunks=None,
            description=description,
            format=get_digital_format_by_name(file.name),
            size=file.size,
            createdAt=get_current_iso_string(),
            updatedAt=get_current_iso_string(),
            chunkCount=math.ceil(file.size / self.chunkSize),
            chunkSize=self.chunkSize,
            isEncrypted=encrypted,
            signature=None,
        )

        if parent_hash:
            parent_res = self.asset_provider.detail(namespace_id, parent_hash)
            asset.version = parent_res.body.asset.version + 1

        log.info(f"File last modified time={file.last_modified}")
        #            const chunkList = new Array(asset.chunkCount) // 用于存储每个块的元数据
        #        const blockList: BlockMetadata[] = new Array(asset.chunkCount)
        chunkList: List[str] = ["" for _ in range(asset.chunkCount)]
        blockList: List[BlockMetadata] = [BlockMetadata() for _ in range(asset.chunkCount)]
        for index in range(asset.chunkCount):
            if self.is_abort:
                return
            start = index * self.chunkSize
            end = min(file.size, start + self.chunkSize)
            log.info(f"Try to read the index={index} chunk, size={end - start}")
            data = file.slice(start, end)
            # assetDigest.update(data) // 更新资产的哈希
            if encrypted:
                # // 对数据进行加密（可选）
                # todo
                # data = await this.assetCipher.encrypt(data)
                pass
            put_res = self.block_provider.put(namespace_id=namespace_id, data=data.stream())
            # todo
            # mergeDigest.update(decodeHex(block.hash)) // 更新合并哈希
            chunkList[index] = put_res.body.block.hash
            blockList[index] = put_res.body.block
            if block_callback:
                upload_result = UploadResult(
                    block=put_res.body.block, progress=Progress(total=asset.chunkCount, completed=index + 1)
                )
                block_callback(upload_result)

        # 资产块的元数据
        asset.chunks = chunkList
        # asset.hash = encodeHex(assetDigest.sum()) // 资产哈希
        # asset.hash = binascii.hexlify(hashlib.sha256(assetDigest.sum()).digest()).decode('ascii'),
        # 创建资产信息
        return self.asset_provider.sign(asset)

    def download(self):
        pass
