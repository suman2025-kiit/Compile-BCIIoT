import hashlib
import json
from typing import Any, Dict, List


def sha256(data: Any) -> str:
    """Generate SHA-256 hash for any JSON-serializable object."""
    encoded = json.dumps(data, sort_keys=True).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


class VerkleCommitment:
    """
    Lightweight Verkle-style commitment simulator.

    This is not a production vector commitment implementation.
    It is a research-friendly approximation for showing compact artifact
    commitment and root verification.
    """

    def __init__(self, artifacts: Dict[str, Any]):
        self.artifacts = artifacts
        self.artifact_hashes = {name: sha256(value) for name, value in artifacts.items()}
        self.root = self._commit(list(self.artifact_hashes.values()))

    def _commit(self, hashes: List[str]) -> str:
        return sha256({"verkle_children": hashes})

    def get_root(self) -> str:
        return self.root

    def get_proof(self, artifact_name: str) -> Dict[str, Any]:
        if artifact_name not in self.artifact_hashes:
            raise KeyError(f"Artifact not found: {artifact_name}")
        return {
            "artifact": artifact_name,
            "artifact_hash": self.artifact_hashes[artifact_name],
            "root": self.root,
            "sibling_commitments": [
                h for name, h in self.artifact_hashes.items() if name != artifact_name
            ],
        }

    def verify(self, artifact_name: str, artifact_value: Any, proof: Dict[str, Any]) -> bool:
        local_hash = sha256(artifact_value)
        if local_hash != proof["artifact_hash"]:
            return False
        reconstructed = self._commit([self.artifact_hashes[name] for name in self.artifact_hashes])
        return reconstructed == proof["root"] == self.root
