from flask import Flask, jsonify, request, render_template
from uuid import uuid4
from blockchain import BlockChain
from proof_of_work import Proof_of_work

# ノード生成
app = Flask(__name__)

# このノードのユニークアドレスを生成
node_identifire = str(uuid4()).replace('-', '')

# ブロックチェーンクラスをインスタンス化
blockchain = BlockChain()
poW = Proof_of_work()


@app.route('/')
def index():
    """
    Flaskのインデックスページテスト用
    """
    title = "ようこそ"
    message = "これはテスト用のインデックスページです"
    return render_template("index.html",
                           message=message,
                           title=title)


@app.route('/tr/new', methods=['POST'])
def new_transactions():
    """
    新しいトランザクションを追加する
    """
    values = request.get_json()

    # POSTされたデータに必要なデータがあるか確認する
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400

    # 新しいトランザクションを作る
    index = blockchain.new_transaction(values['sender'],
                                       values['recipient'],
                                       values['amount'])
    # レスポンスを生成する
    response = {'message': f'トランザクションはブロック {index} に追加されました'}
    return jsonify(response), 201


@app.route('/mining', methods=['GET'])
def mine():
    """
    新しいブロックを採掘する
    """
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    # プルーフオブワークで該当のプルーフを見つける
    proof = poW.algo(last_block)
    # プルーフ発見の報酬
    blockchain.new_transaction(
        sender="0",
        recipient=node_identifire,
        amount=1,
    )

    # チェーンに新しいブロックを加える
    block = blockchain.new_block(proof)

    response = {
        'message': '新しいブロックを採掘',
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': proof,
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200


@app.route('/chain', methods=['GET'])
def full_chain():
    """
    すべてのブロックチェーンを返す
    """
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }

# port6000でサーバーを起動する
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=5000)
