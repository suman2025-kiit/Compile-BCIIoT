from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Task:
    name: str
    cpu: int
    mem: int
    sec: int


@dataclass
class PeerDevice:
    device_id: str
    cpu: int
    mem: int
    bandwidth: int
    security: int


@dataclass
class CompilationTransaction:
    tx_id: str
    verkle_root: str
    executable_hash: str
    compiler_id: str
    version: str
    timestamp: str


@dataclass
class RuntimeCertificate:
    certificate_id: str
    task_name: str
    peer_id: str
    output_hash: str
    status: str
    timestamp: str
