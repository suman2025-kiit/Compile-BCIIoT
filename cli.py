import sys
from datetime import datetime, timezone
from pathlib import Path

from .compiler import compile_source
from .verkle import VerkleCommitment, sha256
from .blockchain import PermissionedBlockchain
from .scheduler import default_peers, schedule_tasks, execute_tasks


def main():
    if len(sys.argv) < 2:
        print("Usage: python -m compile_bciiot.cli examples/sample_program.ciiot")
        raise SystemExit(1)

    source_path = Path(sys.argv[1])
    source = source_path.read_text(encoding="utf-8")

    print("Compile-BCIIoT Secure Compilation Pipeline")

    result = compile_source(source)
    print("Tokens generated")
    print("AST generated")
    print("Semantic analysis passed")
    print("IR generated")
    print("Dependency graph constructed")
    print("Optimized IR generated")
    print("Executable tasks generated")

    artifacts = {
        "tokens": result["tokens"],
        "ast": result["ast"],
        "ir": result["ir"],
        "optimized_ir": result["optimized_ir"],
        "executable": result["executable"],
        "metadata": {
            "compiler_id": "compiler-node-1",
            "version": "1.0",
            "timestamp": datetime.now(timezone.utc).isoformat(),
        },
    }

    commitment = VerkleCommitment(artifacts)
    verkle_root = commitment.get_root()
    print("Artifacts committed using Verkle-style root")

    blockchain = PermissionedBlockchain()
    tx = {
        "tx_id": sha256({"root": verkle_root, "time": artifacts["metadata"]["timestamp"]})[:16],
        "verkle_root": verkle_root,
        "executable_hash": sha256(result["executable"]),
        "compiler_id": "compiler-node-1",
        "version": "1.0",
        "timestamp": artifacts["metadata"]["timestamp"],
    }
    blockchain.append_block([tx])
    print("Blockchain transaction appended")

    chain_root = blockchain.get_latest_verkle_root()
    if chain_root != verkle_root:
        raise RuntimeError("Executable verification failed.")
    print("Executable verified successfully")

    peers = default_peers()
    mapping = schedule_tasks(result["executable"], peers)
    certificates = execute_tasks(result["executable"], mapping)
    print("Distributed tasks executed")

    blockchain.append_block(certificates)
    print("Runtime certificates stored")

    if not blockchain.verify_chain():
        raise RuntimeError("Final blockchain audit failed.")
    print("Final blockchain audit successful")

    print("\nVerkle Root:", verkle_root)
    print("Task Mapping:", mapping)
    print("Runtime Certificates:", certificates)


if __name__ == "__main__":
    main()
