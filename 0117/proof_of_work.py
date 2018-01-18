# coding: utf-8

import hashlib
import json


class Proof_of_work:
    """
    プルーフオブワークアルゴリズムのためのクラス
    """

    def algo(self, last_proof):
        """
        プルーフオブワークのアルゴリズム
        ハッシュ値検索の条件を加えて、そのハッシュ値が条件通りかどうかをチェックする
        """
        proof = 0
        while self.validation_proof(last_proof, proof) is False:
            proof += 1

    @staticmethod
    def validation_proof(last_proof, proof):
        """
        proofが正しいか確認する
        アルゴリズムの難易度はここで決まる
        @ param last_proof: <int> 前のproof
        @ param proof: <int> 現在のproof
        @ return <bool>
        """
        guess = f'{last_proof}{proof}'.encode()
        print(guess)
        guess_hash = hashlib.sha224(guess).hexdigest()
        print(guess_hash)

        return guess_hash[-1] == '0'

if __name__ == '__main__':
    pOw = Proof_of_work()
    pOw.algo(0)
