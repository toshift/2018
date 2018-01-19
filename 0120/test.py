# coding:utf-8
from flask import Flask
from uuid import uuid4

current_transactions = {}
node_identifire = str(uuid4()).replace('-', '')


def new_transaction(sender, recipient, amount):
    """
    新しいトランザクションをリストに加える
    @ param sender: <str> 送信者のアドレス
    @ param recipient: <str> 受信者のアドレス
    @ param amount: <int> 量
    @ return <int> このトランザクションを含むブロックのアドレス
    """
    try:
        current_transactions = ({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
    except Exception as e:
        print(e)
    else:
        print(current_transactions)
        pass

app = Flask(__name__)


@app.route('/')
def index():
    return "Test"

if __name__ == "__main__":
    # app.run(host='0.0.0.0', port='6189')
    new_transaction(
        sender="0",
        recipient=node_identifire,
        amount=1,
    )
