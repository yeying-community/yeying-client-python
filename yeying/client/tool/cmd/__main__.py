# -*- coding:utf-8 -*-
"""
资产仓库 cmd client
支持本地资产上传
支持下载服务端资产
"""
import argparse
import os.path
from yeying.api.asset import asset_pb2
from yeying.api.web3 import BlockAddress, Identity
from yeying.client.downloader import DownloadResult
from yeying.client.model.file import File
from yeying.client.model.option import ProviderOption
from yeying.client.provider.asset_provider import AssetProvider
from yeying.client.tool.identity_service import load, decrypt_block_address
from yeying.client.uploader import UploadResult
from yeying.client import uploader, downloader
from google.protobuf.json_format import ParseDict, MessageToJson


def arg_parse():
    parser = argparse.ArgumentParser(description="Yeying warehouse cli")
    sub_parser= parser.add_subparsers(dest="command")

    # 上传本地资源
    put_parser = sub_parser.add_parser("put", help="上传资源")
    put_parser.add_argument(dest="source", help="local file path")
    put_parser.add_argument(dest="namespace_id", help="namespace_id")
    put_parser.add_argument(dest="identity_file", help="identity file")
    put_parser.add_argument(dest="password", help="password")

    # 下载服务端资源
    get_parser = sub_parser.add_parser("get", help="下载资源")
    get_parser.add_argument(dest="namespace_id", help="namespace_id")
    get_parser.add_argument(dest="hash", help="hash")
    get_parser.add_argument(dest="output", help="local file out path")
    get_parser.add_argument(dest="identity_file", help="identity file")
    get_parser.add_argument(dest="password", help="password")

    # 删除服务端资源
    delete_parser = sub_parser.add_parser("delete", help="删除资源")
    delete_parser.add_argument(dest="namespace_id", help="namespace_id")
    delete_parser.add_argument(dest="hash", help="hash")
    delete_parser.add_argument(dest="identity_file", help="identity file")
    delete_parser.add_argument(dest="password", help="password")

    args = parser.parse_args()
    return args, parser


def package_dir(path):
    import uuid
    dst = "/tmp/%s.tar.gz" % str(uuid.uuid1().hex)[:8]
    cmd = "mkdir -p /tmp; tar -czf {dst} {src}".format(src=path, dst=dst)
    os.system(cmd)
    return dst


def upload(args, option):
    print("start upload")
    print(args.source)

    def upload_callback(result: UploadResult) -> None:
        print(f"[文件上传回调] 进度: {result['progress']['completed']}/{result['progress']['total']}")
        print(f"[文件上传回调] 区块namespaceId: {result['block'].namespaceId}")
        print(f"[文件上传回调] 区块大小: {result['block'].size} 字节")
        print(f"[文件上传回调] 区块哈希: {result['block'].hash}")
        print("-" * 40)

    if not os.path.exists(args.source):
        print("Invalid path %s" % args.source)
    else:
        path = args.source
        if os.path.isdir(path):
            print("packaging folder %s" % path)
            path = package_dir(path)
            print("packaging folder temp file %s" % path)
        upload_client = uploader.Uploader(option)
        file = File(name=os.path.basename(path), size=os.stat(path).st_size, stream=path, last_modified=int(os.stat(path).st_mtime * 1000))
        res: asset_pb2.SignAssetResponse = upload_client.put(namespace_id=args.namespace_id, file=file, block_callback=upload_callback)
        asset = res.body.asset
        print(f"upload success. asset={MessageToJson(asset)}")


def download(args, option):
    print("start download")
    print(args)
    download_client = downloader.Downloader(option)
    namespace_id = args.namespace_id
    chunk_files = []
    def download_callback(result: DownloadResult) -> None:
        print(f"[文件下载回调] 进度: {result['progress']['completed']}/{result['progress']['total']}")
        print(f"[文件下载回调] 区块namespaceId: {result['block'].namespaceId}")
        print(f"[文件下载回调] 区块大小: {len(result['data'])} 字节")
        print(f"[文件下载回调] 区块哈希: {result['block'].hash}")
        chunk_files.append(result['data'])
        print("-" * 40)
    asset = download_client.get(namespace_id=namespace_id, _hash=args.hash, block_callback=download_callback)

    def merge_files(chunks, output_path):
        """合并分块文件为完整文件"""
        with open(output_path, 'wb') as output:
            for chunk in chunks:
                output.write(chunk)
        print(f"文件已合并至: {output_path}")

    merge_files(chunk_files, args.output)
    print(f"download success. asset={MessageToJson(asset)}")


def get_proxy():
    return os.getenv("SERVICE_CODE", "localhost:8641")


def get_identify():
    identify = {
        "metadata": {
            "name": "test_user",
            "avatar": 'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyMzEgMjMxIj48cGF0aCBkPSJNMzMuODMsMzMuODNhMTE1LjUsMTE1LjUsMCwxLDEsMCwxNjMuMzQsMTE1LjQ5LDExNS40OSwwLDAsMSwwLTE2My4zNFoiIHN0eWxlPSJmaWxsOiMwMGE1OGM7Ii8+PHBhdGggZD0ibTExNS41IDUxLjc1YTYzLjc1IDYzLjc1IDAgMCAwLTEwLjUgMTI2LjYzdjE0LjA5YTExNS41IDExNS41IDAgMCAwLTUzLjcyOSAxOS4wMjcgMTE1LjUgMTE1LjUgMCAwIDAgMTI4LjQ2IDAgMTE1LjUgMTE1LjUgMCAwIDAtNTMuNzI5LTE5LjAyOXYtMTQuMDg0YTYzLjc1IDYzLjc1IDAgMCAwIDUzLjI1LTYyLjg4MSA2My43NSA2My43NSAwIDAgMC02My42NS02My43NSA2My43NSA2My43NSAwIDAgMC0wLjA5OTYxIDB6IiBzdHlsZT0iZmlsbDojZThiYzg2OyIvPjxwYXRoIGQ9Im0xNDEuODkgMTk1YTExNC43OSAxMTQuNzkgMCAwIDEgMzggMTYuNSAxMTUuNTUgMTE1LjU1IDAgMCAxLTEyOC40NyAwIDExNC43OSAxMTQuNzkgMCAwIDEgMzgtMTYuNWwxNS43NSAxNS43NWgyMXoiIHN0eWxlPSJmaWxsOiMwRDIwNEE7Ii8+PHBhdGggZD0ibTE0Ni40IDE5Ni4xNC0xNy40IDE3LjQ0LTEuMTcgMS4xN2gtMjQuMzRsLTEuMTgtMS4xNy0xNy40My0xNy40NGMxLjQ5LTAuNDEgMy0wLjc5IDQuNTEtMS4xNGw0LjY3LTEgMTIuNzQgMTIuNzRoMTcuNjlsMTIuNzMtMTIuNzQgNC42NyAxYzEuNTIgMC4zNSAzIDAuNzMgNC41MSAxLjE0eiIgc3R5bGU9ImZpbGw6IzAwZmZkZjsiLz48cGF0aCBkPSJtNjkuODM0IDMzLjgyNmMtOC4yMDAxLTAuMDYyNi0xNi40NDQgMi42NzUzLTIzLjE1MiA3LjcwMzgtOC41Mjk4IDYuOTg5OS0xMi4xNTkgMTkuNjEtMTIuMzI5IDMyLjY4LTAuMjA0MSAxNS40NzYgMS42MDkyIDM0Ljc1MiAxLjc0NjQgNTEuOTE1IDAuMTA0MTQgMTMuMDQ3IDAuNTM0ODUgMjUuOTg0LTIuOTE5NyAzMy45OTUtMi40OTk0IDUuODEtOS4wOTU1IDkuNjAwNi0xNi4xOTYgMTIuMzExIDcuOTU5OSAyLjgzMDEgMjUuMDA5IDIuODA5NCAzMy41OCAxLjUzOTMgMTAuOC0xLjU5IDE3LjIzOC02LjUyOTQgMTcuMTU5LTIyLjY5OS0wLjA5MTEtMTUuOTMtMS4zODk0LTI5LjIzLTEuNTU5LTQ1LjgzLTAuMzIwOC0xMS45ODMtMS41NjktMjQuMjkxIDQuOTc3NC0zMy45ODcgNC4yMTM5LTYuMTI2NSAxMC40NTItMTAuNTIxIDE3LjExNi0xMy41ODggMy45MjkyLTEuODU3NSA4LjAzODQtMy4zMDgzIDEyLjI2My00LjMyOTctNi44NzE4LTEzLjU3NC0xOC43MzItMTkuNjE4LTMwLjY4Ny0xOS43MDl6IiBzdHlsZT0iZmlsbDpub25lOyIvPjxwYXRoIGQ9Im05MC44IDc2LjI0NmMxMS45MTgtMTcuMTI1IDMxLjk5Ni0yMy4yMTggNDkuNzQzLTE3LjQ4OCAxMS44MSAzLjk0OTYgMjAuNjkyIDEzLjM4OSAyMi4zMTMgMjguMjM3IDAuNTEwNTEgNi4yMDk4IDAuNjM0MTMgMTIuNDQ1IDAuMzcwMDcgMTguNjctMC4yMzk3MyAxMS4yLTAuNzI5NDYgMjMuODItMS4wOTk1IDM0LjA4LTAuODIwMDUgMjIuNDMgMC4wNTkzIDM1LjEgMjQuNTg5IDM2LjMgOC41NjM1IDAuMzIxMjIgMTcuMTM3LTAuMjI4NDUgMjUuNTktMS42NDA1aC0wLjAxOThjLTEwLjc0LTMuMzc5OS0xNy45OC0xNS42MDktMTkuMy0yNi4yODktMS4yOS0xMC40MS0wLjYwOTgtMjMuNDMtMC43ODk4LTM4LjA5MS0wLjE3MDEtMTQuOTYgMS4wMzk4LTI5LjgxOSAwLjI4MDA4LTQyLjA4OS0xLjQxNC0yMi43NzctMTQuOTQ3LTM4LjUwNS0zNC4xMjYtNDUuMTUyLTI3LjgxMy03LjM1LTUxLjA4MyAwLjA5MS02MS42NzIgMTcuMzQzLTUuNDY5OCA4LjkxMTItNy43NDEzIDIwLjA3LTUuODc4OCAzNi4xMjF6IiBzdHlsZT0iZmlsbDojOWMwMDkyOyIvPjxwYXRoIGQ9Im03MC45NTkgOTQuOTg1aDM1LjAzMWMyLjQwODYgMWUtNSA0LjM2MTIgMS45NTIzIDQuMzYxMiA0LjM2MDZsLTIuNTg2NCAxNy41MTFjLTAuMzUxNSAyLjM3OTktMS43MjE4IDQuMzYwNi0zLjg0NTcgNC4zNjA2aC0zMC45Yy0yLjEyMzktMWUtNSAtMy44NDU3LTEuOTUyMy0zLjg0NTctNC4zNjA2bC0yLjU4NjQtMTcuNTExYzFlLTUgLTIuNDA4MiAxLjk1MjYtNC4zNjA2IDQuMzYxMi00LjM2MDZ6IiBzdHlsZT0iZmlsbDojMDAwO3N0cm9rZS1saW5lY2FwOnJvdW5kO3N0cm9rZS1saW5lam9pbjpyb3VuZDtzdHJva2Utd2lkdGg6My4wMDQ1cHg7c3Ryb2tlOiMwMDA7Ii8+PHBhdGggZD0ibTE2MC4wNSA5NC45ODVoLTM1LjAzMWMtMi40MDg2IDFlLTUgLTQuMzYxMiAxLjk1MjMtNC4zNjEyIDQuMzYwNmwyLjU4NjQgMTcuNTExYzAuMzUxNDkgMi4zNzk5IDEuNzIxOCA0LjM2MDYgMy44NDU3IDQuMzYwNmgzMC45YzIuMTIzOS0xZS01IDMuODQ1Ny0xLjk1MjMgMy44NDU3LTQuMzYwNmwyLjU4NjQtMTcuNTExYy0xZS01IC0yLjQwODItMS45NTI2LTQuMzYwNi00LjM2MTItNC4zNjA2eiIgc3R5bGU9ImZpbGw6IzAwMDtzdHJva2UtbGluZWNhcDpyb3VuZDtzdHJva2UtbGluZWpvaW46cm91bmQ7c3Ryb2tlLXdpZHRoOjMuMDA0NXB4O3N0cm9rZTojMDAwOyIvPjxwYXRoIGQ9Im05MC42MDcgMTAyLjM1YTQuNjMzNyA0LjYzMzIgMCAxIDAgNC42ODkyIDQuNjMzNyA0LjYzMzcgNC42MzMyIDAgMCAwLTQuNjg5Mi00LjYzMzd6bTQ5LjcyIDBhNC42MzM3IDQuNjMzMiAwIDEgMCA0LjY0NDQgNC42MzM3IDQuNjMzNyA0LjYzMzIgMCAwIDAtNC42NDQ0LTQuNjMzN3oiIHN0eWxlPSJmaWxsOiMwMDA7Ii8+PHBhdGggZD0ibTcwLjY2IDk0Ljk4NWgtMTEuNzc1IiBzdHlsZT0iZmlsbDpub25lO3N0cm9rZS1saW5lY2FwOnJvdW5kO3N0cm9rZS1saW5lam9pbjpyb3VuZDtzdHJva2Utd2lkdGg6My4wMDQ1cHg7c3Ryb2tlOiMwMDA7Ii8+PHBhdGggZD0ibTE3Mi4xMyA5NC45ODVoLTE5LjQ4NCIgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2UtbGluZWNhcDpyb3VuZDtzdHJva2UtbGluZWpvaW46cm91bmQ7c3Ryb2tlLXdpZHRoOjMuMDA0NXB4O3N0cm9rZTojMDAwOyIvPjxwYXRoIGQ9Im0xMDkuMzIgMTA2LjJjNC4yMDQ1LTIuNDI3IDkuMzAzNi0xLjkxMyAxMi4zNTMtMC4wMjU4IiBzdHlsZT0iZmlsbDpub25lO3N0cm9rZS1saW5lY2FwOnJvdW5kO3N0cm9rZS1saW5lam9pbjpyb3VuZDtzdHJva2Utd2lkdGg6My4wMDQ1cHg7c3Ryb2tlOiMwMDA7Ii8+PHBhdGggZD0ibTE0OC4zMyAxMDkuNzktNS43NjI2LTguMjMyNCIgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2UtbGluZWNhcDpyb3VuZDtzdHJva2UtbGluZWpvaW46cm91bmQ7c3Ryb2tlLXdpZHRoOjQ7c3Ryb2tlOiNmZmY7Ii8+PHBhdGggZD0ibTE1Ni4yNyAxMDUtMi40MDMtMy40MzI4IiBzdHlsZT0iZmlsbDpub25lO3N0cm9rZS1saW5lY2FwOnJvdW5kO3N0cm9rZS1saW5lam9pbjpyb3VuZDtzdHJva2Utd2lkdGg6NDtzdHJva2U6I2ZmZjsiLz48cGF0aCBkPSJtODIuNzQ4IDExNC4zNC04Ljk0ODktMTIuNzg0IiBzdHlsZT0iZmlsbDpub25lO3N0cm9rZS1saW5lY2FwOnJvdW5kO3N0cm9rZS1saW5lam9pbjpyb3VuZDtzdHJva2Utd2lkdGg6NDtzdHJva2U6I2ZmZjsiLz48cGF0aCBkPSJtOTEuNDA4IDEwOS43OS01Ljc2MjYtOC4yMzI0IiBzdHlsZT0iZmlsbDpub25lO3N0cm9rZS1saW5lY2FwOnJvdW5kO3N0cm9rZS1saW5lam9pbjpyb3VuZDtzdHJva2Utd2lkdGg6NDtzdHJva2U6I2ZmZjsiLz48cGF0aCBkPSJtOTcuMDYgMTQ0LjU5YTIwLjE1IDIwLjE1IDAgMCAwIDM2Ljg4IDQuNTN6IiBzdHlsZT0iZmlsbDojZmZmO3N0cm9rZS1saW5lY2FwOnJvdW5kO3N0cm9rZS1saW5lam9pbjpyb3VuZDtzdHJva2Utd2lkdGg6Mi45OTk5cHg7c3Ryb2tlOiMwMDA7Ii8+PC9zdmc+","created":"2024-11-25T08:51:00.890Z","checkpoint":"2024-11-25T08:51:00.891Z"},"blockAddress":"xWErLHHms6xP/SVdb9MJRry2VSEbkgu6ZfnLnMjSkt4IyuWeG0oZgupNX6ve90JjxohW0oVGFeI1xos41mUhEDfSM0Xsc3n1VejASQzQeaJyt7pq5I94TyxC829lw0UGlhF74OkXYGeQ66ahmH9N3yiWcATht3CSoebsxzIplt6Shat9oCE65aGYTvIloUBk7+VTMoKvX/vBMZd01LeOeOu9TUFmyOGsRBjReOu0rDg4ffdi335oI+EjHTEjx7zG3cWLCu8ozLbbx16QE+hIEJ6ebDYhMMW8/0YPNHsR+8g2lT+IyF8tnjEocjtBvwjgd5pN0BY6FRFOpHSknA+ovRQ1zk90LAES8MuY6ZlSMKwA98UoLfU+2dSYK5+7SB4iPykTHoVe51DahHaE8LZ5HOkWWtTrUF8lzXERmfo8xyRX6tjcqQG59yzjgBGqGhc2Q3AyEwlqjYARGCS7ZLJEU7ROP/HShOAT7uwttkv9OCa0jhIEkivrf0DkTFCYE12a5sh7ASbTjMiBITAaUe/WN3RvBS91lCe17B1ypnZKgAtypk7CxLQpOEkO8f111yCblasNziQs2V7wbnfFx5Yp+ZpoGMPeEwNpgOWwSGttZEkSA1zR/OmYvXDb/L6IYM1MnIAdjaNpD4siYhUJp0DaI3+GLTsr1keJYyDr',
        },
        "blockAddress": {
            "identifier": "did:ethr:0x07e4:0x035b737f93ef1a74b7fd32b62b4e313876722957ca3c705588cc3c883bf2fb568c",
            "address": "0x45C6ff6AF1Ec4E5D15668351B12A6C630a053e16",
            "privateKey": "0x2721a1f0de1656df452fa83238350d56b44403f2f02a59e840e854b61010c632",
            "publicKey": "0x035b737f93ef1a74b7fd32b62b4e313876722957ca3c705588cc3c883bf2fb568c",
            "mnemonic": {
                "phrase": "trigger happy matter office zoo chicken conduct borrow civil refuse addict lunar",
                "path": "m/44'/60'/0'/0/0",
                "locale": "en",
                "password": ""
            }
        },
        "securityConfig": {"algorithm": {"name": "CIPHER_TYPE_AES_GCM_256", "iv": "PWPhFzsftCklcfgc"}}
    }
    return identify


class Mnemonic:
    __slots__ = ("phrase", "path", "locale", "password")

    def __init__(self, phrase: str, path: str, locale: str, password: str):
        self.phrase = phrase
        self.path = path
        self.locale = locale
        self.password = password


def delete(args, option):
    print("start delete")
    print(f"namespace_id={args.namespace_id}")
    print(f"hash={args.hash}")
    print(f"proxy={option.proxy}")
    delete_client = AssetProvider(option=option)
    response: asset_pb2.DeleteAssetResponse = delete_client.delete(args.namespace_id, args.hash)
    print(f"delete success. code={response.body.status.code}")


def main():
    args, parser = arg_parse()
    identify_data = get_identify()["blockAddress"]

    # 创建 BlockAddress 实例
    block_address = BlockAddress()

    # 使用 ParseDict 填充数据
    ParseDict(identify_data, block_address)

    identity_file = args.identity_file
    if not os.path.exists(identity_file):
        raise Exception(f"identity_file not exists {identity_file}")

    identity: Identity = load(identity_file)
    block_address = decrypt_block_address(identity.blockAddress, identity.securityConfig.algorithm, args.password)
    print(f"block_address={block_address}")
    option = ProviderOption(
        proxy=get_proxy(),
        block_address=block_address
    )

    if args.command == "put":
        upload(args, option)
    elif args.command == "get":
        download(args, option)
    elif args.command == "delete":
        delete(args, option)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
