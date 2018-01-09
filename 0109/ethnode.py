import requests
import json

class Eth_json_rpc:
    def __init__(self):
        self.url="http://127.0.0.1:8545"
        self.headers = {'content-type': 'application/json'}
        self.payload = {
            "jsonrpc": "2.0",
            "method": "",
            "params": [],
            "id": 0
        }

    def eth_protocolVersion(self):
        """
        Returns the current ethereum protocol version.
        """
        self.payload["method"] = "eth_protocolVersion"
        self.payload["id"] = 67
        response = requests.post(self.url, data=json.dumps(self.payload), headers=self.headers).json()
        result = int(response["result"], 16)
        print("Protocol Version: %d" % result)

    def eth_syncing(self):
        """
        Returns an object with data about the sync status or false.
        """
        self.payload["method"] = "eth_syncing"
        self.payload["id"] = 1
        response = requests.post(self.url, data=json.dumps(self.payload), headers=self.headers).json()
        startingblock = int(response["result"]["startingBlock"], 16)
        highestblock = int(response["result"]["highestBlock"], 16)
        currentblock = int(response["result"]["currentBlock"], 16)
        knownstates = int(response["result"]["knownStates"], 16)
        pulledstates = int(response["result"]["pulledStates"], 16)
        print("StartingBlock: %d" % startingblock)
        print("HighestBlock: %d" % highestblock)
        print("CurrentBlock: %d" % currentblock)
        print("KnownStates: %d" % knownstates)
        print("PulledStates: %d" % pulledstates)

    def eth_getBalance(self,addr):
        """
        謎
        """
        self.payload["params"] = [addr, "latest"]
        self.payload["id"] = 0
        response = requests.post(self.url, data=json.dumps(self.payload), headers=self.headers).json()
        print("--eth_getBalance---")
        print(response)

if __name__ == "__main__":
    eth = Eth_json_rpc()
    eth.eth_protocolVersion()
    eth.eth_syncing()
    eth.eth_getBalance("address")
