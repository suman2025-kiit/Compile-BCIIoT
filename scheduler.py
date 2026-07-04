from typing import Dict, List
from datetime import datetime, timezone
from .models import PeerDevice
from .verkle import sha256


def default_peers() -> List[PeerDevice]:
    return [
        PeerDevice("peer-1", cpu=4, mem=512, bandwidth=80, security=5),
        PeerDevice("peer-2", cpu=2, mem=256, bandwidth=60, security=4),
        PeerDevice("peer-3", cpu=8, mem=1024, bandwidth=100, security=5),
    ]


def score_peer(peer: PeerDevice) -> float:
    return 0.35 * peer.cpu + 0.25 * (peer.mem / 128) + 0.20 * (peer.bandwidth / 10) + 0.20 * peer.security


def schedule_tasks(executable: List[Dict[str, str]], peers: List[PeerDevice]) -> Dict[str, str]:
    """Assign tasks to the best available C-IIoT peer."""
    sorted_peers = sorted(peers, key=score_peer, reverse=True)
    mapping = {}
    for i, task in enumerate(executable):
        mapping[task["task"]] = sorted_peers[i % len(sorted_peers)].device_id
    return mapping


def execute_tasks(executable: List[Dict[str, str]], mapping: Dict[str, str]) -> List[Dict[str, str]]:
    """Simulate distributed execution and runtime certificate generation."""
    certificates = []
    for task in executable:
        peer_id = mapping[task["task"]]
        output = f"output::{task['bytecode']}::{peer_id}"
        cert = {
            "certificate_id": sha256({"task": task["task"], "peer": peer_id, "output": output})[:16],
            "task_name": task["task"],
            "peer_id": peer_id,
            "output_hash": sha256(output),
            "status": "SUCCESS",
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
        certificates.append(cert)
    return certificates
