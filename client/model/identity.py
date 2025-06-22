import codecs
from typing import Optional, Union

from client.utils.signature_utils import verify
from yeying.api.web3 import (
    NetworkTypeEnum,
    IdentityCodeEnum,
    SecurityConfig,
    IdentityServiceExtend,
    IdentityOrganizationExtend,
    IdentityPersonalExtend,
    IdentityApplicationExtend,
    Registry,
    BlockAddress,
)


def encode_key(key):
    return codecs.decode(key[2:] if key.startswith("0x") else key, "hex")


def convert_did_to_publickey(did):
    public_key = did.split(":")[-1]
    return public_key[2:] if public_key.startswith("0x") else public_key


def verify_identity(identity):
    signature = identity.signature
    try:
        identity.signature = ""
        public_key = encode_key(convert_did_to_publickey(identity.metadata.did))
        return verify(public_key=public_key, data=identity.SerializeToString(), signature=signature)
    finally:
        identity.signature = signature


class IdentityTemplate(object):
    """身份模板数据类"""

    language: str  # 语言代码
    network: NetworkTypeEnum  # 网络类型
    parent: str  # 父级身份标识符
    code: IdentityCodeEnum  # 身份类型代码
    name: str  # 身份名称
    description: str  # 身份描述
    avatar: str  # 头像(base64|URL)

    # 可选字段
    security_config: Optional[SecurityConfig] = None
    extend: Optional[
        Union[IdentityServiceExtend, IdentityOrganizationExtend, IdentityPersonalExtend, IdentityApplicationExtend]
    ] = None
    registry: Optional[Registry] = None


defaultPath: str = "m/44'/60'/0'/0/0"

from abc import ABC, abstractmethod
import re
from typing import List


class Wordlist(ABC):
    """
    抽象词列表基类，用于实现不同语言的词列表

    子类必须实现抽象方法：
    - get_word: 将索引映射到单词
    - get_word_index: 将单词映射到索引

    子类可以重写以下方法：
    - split: 将短语拆分为单词
    - join: 将单词组合为短语
    """

    def __init__(self, locale: str):
        """
        创建新的 Wordlist 实例

        参数:
            locale: 语言区域代码 (例如 "en", "zh", "es")
        """
        self.locale = locale

    def split(self, phrase: str) -> List[str]:
        """
        将短语拆分为单词列表

        默认使用空白字符分割，并转换为小写

        参数:
            phrase: 要拆分的短语字符串

        返回:
            单词列表
        """
        # 使用正则表达式分割连续空白字符
        return re.split(r"\s+", phrase.lower())

    def join(self, words: List[str]) -> str:
        """
        将单词列表组合为短语

        默认使用单个空格连接

        参数:
            words: 要组合的单词列表

        返回:
            组合后的短语字符串
        """
        return " ".join(words)

    @abstractmethod
    def get_word(self, index: int) -> str:
        """
        将索引映射到单词 (抽象方法)

        子类必须实现此方法

        参数:
            index: 要获取的单词索引 (0-2047)

        返回:
            对应的单词
        """
        pass

    @abstractmethod
    def get_word_index(self, word: str) -> int:
        """
        将单词映射到索引 (抽象方法)

        子类必须实现此方法

        参数:
            word: 要查找的单词

        返回:
            对应的索引 (0-2047)
        """
        pass


from mnemonic import Mnemonic

# 创建不同语言的助记词生成器
mnemo_en = Mnemonic("english")  # 英语 (LangEn)
mnemo_es = Mnemonic("spanish")  # 西班牙语 (LangEs)
mnemo_fr = Mnemonic("french")  # 法语 (LangFr)
mnemo_it = Mnemonic("italian")  # 意大利语 (LangIt)
mnemo_ja = Mnemonic("japanese")  # 日语 (LangJa)
mnemo_ko = Mnemonic("korean")  # 韩语 (LangKo)
mnemo_zh = Mnemonic("chinese-traditional")  # 中文繁体 (LangZh)
mnemo_tw = Mnemonic("chinese-traditional")  # 中文繁体 (LangZh)


# 创建全局词表字典
wordlists: dict[str, Wordlist] = {
    "en": mnemo_en.wordlist(),
    "es": mnemo_es.wordlist(),
    "fr": mnemo_fr.wordlist(),
    "it": mnemo_it.wordlist(),
    "ja": mnemo_ja.wordlist(),
    "ko": mnemo_ko.wordlist(),
    "zh_cn": mnemo_zh.wordlist(),
    "zh_tw": mnemo_tw.wordlist(),
}


def create_block_address(
    network: NetworkTypeEnum = NetworkTypeEnum.NETWORK_TYPE_YEYING,
    language: str = "LANGUAGE_CODE_ZH_CH",
    password: str = "",
    path: str = defaultPath,
) -> BlockAddress:
    wordlist: Wordlist
    # 根据语言代码选择对应的词汇表
    if language == "LANGUAGE_CODE_ZH_CH":
        wordlist = wordlists["zh_cn"]
    elif language == "LANGUAGE_CODE_EN_US":
        wordlist = wordlists["en"]
    else:
        wordlist = wordlists["zh_cn"]  # 默认中文

    # 使用 HDNodeWallet 创建一个随机的钱包
    wallet = HDNodeWallet.createRandom(password, path, wordlist)

    # 构建并返回 BlockAddress 对象
    return buildBlockAddress(network, wallet, path)
