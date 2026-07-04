# Compile-BCIIoT
A Distributed and Secure Compilation Scheme in Cognitive-IIoT Network using Blockchain and Context-Free-Grammar 
# Compile-BCIIoT

**Compile-BCIIoT** is a research-oriented prototype for a distributed and secure compilation scheme in a Cognitive Industrial Internet of Things (C-IIoT) network using blockchain, context-free grammar, dependency graph optimization, and Verkle-style commitment verification.

This repository is designed as an executable proof-of-concept for the paper idea:

> Compile-BCIIoT: A Distributed and Secure Compilation Scheme in Cognitive-IIoT Network using Blockchain and Context-Free-Grammar

The prototype demonstrates the following pipeline:

1. Source program submission  
2. Lexical analysis  
3. Syntax analysis using a lightweight context-free grammar  
4. Semantic validation  
5. Intermediate representation generation  
6. Dependency graph construction  
7. IR optimization  
8. Executable task generation  
9. Compiler artifact hashing  
10. Verkle-style commitment root generation  
11. Blockchain transaction creation  
12. Verification at C-IIoT peer nodes  
13. Distributed execution  
14. Runtime certificate generation  
15. Final audit trail validation  

---

## Repository Structure

```text
Compile-BCIIoT-GitHub/
├── README.md
├── requirements.txt
├── LICENSE
├── .gitignore
├── pyproject.toml
├── src/
│   └── compile_bciiot/
│       ├── __init__.py
│       ├── cli.py
│       ├── compiler.py
│       ├── blockchain.py
│       ├── verkle.py
│       ├── scheduler.py
│       └── models.py
├── examples/
│   └── sample_program.ciiot
├── tests/
│   └── test_pipeline.py
└── .github/
    └── workflows/
        └── python-ci.yml
```

---

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Compile-BCIIoT.git
cd Compile-BCIIoT
```

### Step 2: Create a Python Virtual Environment

```bash
python -m venv venv
```

### Step 3: Activate the Environment

For Windows:

```bash
venv\Scripts\activate
```

For Linux or macOS:

```bash
source venv/bin/activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## How to Run

Run the full Compile-BCIIoT workflow using the example program:

```bash
python -m compile_bciiot.cli examples/sample_program.ciiot
```

Expected output:

```text
Compile-BCIIoT Secure Compilation Pipeline
Tokens generated
AST generated
Semantic analysis passed
IR generated
Dependency graph constructed
Optimized IR generated
Executable tasks generated
Artifacts committed using Verkle-style root
Blockchain transaction appended
Executable verified successfully
Distributed tasks executed
Runtime certificates stored
Final blockchain audit successful
```

---

## Example C-IIoT Source Program

```text
task temp_monitor cpu=2 mem=128 sec=4;
task vibration_check cpu=1 mem=64 sec=3;
task quality_scan cpu=3 mem=256 sec=5;
```

Each line defines one industrial task with CPU, memory, and security requirements.

---

## Core Modules

### 1. Compiler Module

File:

```text
src/compile_bciiot/compiler.py
```

Functions:

- `lexical_analysis()` converts source code into tokens.
- `syntax_analysis()` builds an AST.
- `semantic_analysis()` checks correctness.
- `generate_ir()` creates intermediate representation.
- `optimize_ir()` sorts and optimizes tasks.
- `generate_executable()` creates executable task units.

---

### 2. Verkle-style Commitment Module

File:

```text
src/compile_bciiot/verkle.py
```

This module simulates lightweight Verkle-style commitment generation. It hashes compiler artifacts and produces a compact root commitment for blockchain anchoring.

---

### 3. Blockchain Module

File:

```text
src/compile_bciiot/blockchain.py
```

This module implements a permissioned blockchain simulation with:

- genesis block creation
- compilation transaction storage
- runtime certificate storage
- chain integrity verification

---

### 4. Scheduler Module

File:

```text
src/compile_bciiot/scheduler.py
```

This module maps verified executable tasks to C-IIoT peer devices using CPU, memory, bandwidth, and security scores.

---

## Testing

Run all tests:

```bash
pytest
```

---

## GitHub Upload Steps

### Step 1: Create a New Repository

1. Go to GitHub.
2. Click **New Repository**.
3. Repository name: `Compile-BCIIoT`
4. Keep it public or private.
5. Do not initialize with README because this project already includes one.
6. Click **Create Repository**.

### Step 2: Initialize Git Locally

```bash
cd Compile-BCIIoT-GitHub
git init
git add .
git commit -m "Initial commit: Compile-BCIIoT secure compilation prototype"
```

### Step 3: Connect Local Folder to GitHub

Replace `YOUR-USERNAME` with your GitHub username:

```bash
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/Compile-BCIIoT.git
git push -u origin main
```

### Step 4: Verify Upload

Open:

```text
https://github.com/YOUR-USERNAME/Compile-BCIIoT
```

You should see the full code, README file, examples, and tests.

---

## Suggested GitHub Repository Description

```text
A blockchain-assisted distributed secure compilation framework for Cognitive-IIoT networks using context-free grammar, dependency graph optimization, Verkle-style commitments, and runtime audit certificates.
```

---

## Suggested Topics

Use these GitHub topics:

```text
blockchain
iiot
compiler-design
secure-compilation
edge-computing
verkle-tree
distributed-systems
cybersecurity
industry-5
python
```

---

## Citation

If this code is used in research, cite the associated Compile-BCIIoT manuscript.

---

## Disclaimer

This is a research prototype. It simulates blockchain and Verkle-style commitments for academic demonstration. For production use, replace the simulated blockchain with Hyperledger Fabric, Ethereum, or another permissioned blockchain platform, and replace the simplified Verkle simulation with a cryptographic vector commitment implementation.

