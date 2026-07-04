import hashlib
import json
from datetime import datetime, timezone
from typing import Any, Dict, List


def hash_block(block: Dict[str, Any]) -> str:
    data = json.dumps(block, sort_keys=True).encode("utf-8")
    return hashlib.sha256(data).hexdigest()


class PermissionedBlockchain:
    """Small permissioned blockchain simulator for compilation audit."""

    def __init__(self):
        self.chain: List[Dict[str, Any]] = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis = {
            "index": 0,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "transactions": [],
            "previous_hash": "0" * 64,
        }
        genesis["block_hash"] = hash_block(genesis)
        self.chain.append(genesis)

    def append_block(self, transactions: List[Dict[str, Any]]) -> Dict[str, Any]:
        previous = self.chain[-1]
        block = {
            "index": len(self.chain),
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "transactions": transactions,
            "previous_hash": previous["block_hash"],
        }
        block["block_hash"] = hash_block(block)
        self.chain.append(block)
        return block

    def get_latest_verkle_root(self) -> str:
        for block in reversed(self.chain):
            for tx in reversed(block["transactions"]):
                if "verkle_root" in tx:
                    return tx["verkle_root"]
        raise LookupError("No Verkle root found on blockchain.")

    def verify_chain(self) -> bool:
        for i in range(1, len(self.chain)):
            if self.chain[i]["previous_hash"] != self.chain[i - 1]["block_hash"]:
                return False
            block_copy = dict(self.chain[i])
            block_hash = block_copy.pop("block_hash")
            if hash_block(block_copy) != block_hash:
                return False
        return True
