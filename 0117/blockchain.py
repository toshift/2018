# coding: utf-8
import hashlib
import json
from time import time

"""
・チェーンはトランザクションを収納
・新しいブロックはチェーンに加える
・ハッシュ : メッセージを特定するための暗号化技術
・トランザクション : データベース管理システム（または類似のシステム）内で実行される、分けることのできない一連の情報処理の単位
"""


class BlockChain(object):

    def __init__(self):
        # チェーン
        self.chain = []
        # トランザクション
        self.current_transactions = []
        # ジェネシスブロックの生成
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        """
        新しいブロックの生成、チェーンに加える
        @param previous_hash: <str> 前のブロックのハッシュ
        @param proof: <int> プルーフオブワークアルゴリズムから得られるプルーフ
        @return: <dict> 新しいブロック
        """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # 現在のトランザクションリストをリセット
        self.current_transactions = []

        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        新しいトランザクションをリストに加える
        @ param sender: <str> 送信者のアドレス
        @ param recipient: <str> 受信者のアドレス
        @ param amount: <int> 量
        @ return <int> このトランザクションを含むブロックのアドレス
        """
        self.current_transactions({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """
        ブロックをハッシュ化する
        @ param block: <dict> ブロック
        @ return <str>
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha224(block_string).hexdigest()

    @property
    def last_block(self):
        """
        チェーンの最後のブロックをリターンする
        """
        return self.chain[-1]
