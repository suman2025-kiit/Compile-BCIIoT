import re
from typing import Dict, List, Tuple
import networkx as nx
from .models import Task


TASK_PATTERN = re.compile(r"task\s+([A-Za-z_][A-Za-z0-9_]*)\s+cpu=(\d+)\s+mem=(\d+)\s+sec=(\d+)\s*;")


def lexical_analysis(source: str) -> List[str]:
    """Convert source code into lexical tokens."""
    token_pattern = r"[A-Za-z_][A-Za-z0-9_]*|\d+|=|;"
    return re.findall(token_pattern, source)


def syntax_analysis(source: str) -> List[Dict[str, int]]:
    """Parse the source code using a simple context-free task grammar."""
    ast = []
    lines = [line.strip() for line in source.splitlines() if line.strip()]
    for line in lines:
        match = TASK_PATTERN.fullmatch(line)
        if not match:
            raise SyntaxError(f"Invalid syntax: {line}")
        name, cpu, mem, sec = match.groups()
        ast.append({"type": "task", "name": name, "cpu": int(cpu), "mem": int(mem), "sec": int(sec)})
    return ast


def semantic_analysis(ast: List[Dict[str, int]]) -> bool:
    """Validate type, resource, and naming rules."""
    seen = set()
    for node in ast:
        if node["name"] in seen:
            raise ValueError(f"Duplicate task name: {node['name']}")
        seen.add(node["name"])

        if node["cpu"] <= 0 or node["mem"] <= 0 or node["sec"] <= 0:
            raise ValueError(f"Invalid resource values in task: {node['name']}")
    return True


def generate_ir(ast: List[Dict[str, int]]) -> List[Task]:
    """Generate intermediate representation from AST."""
    return [Task(name=n["name"], cpu=n["cpu"], mem=n["mem"], sec=n["sec"]) for n in ast]


def build_dependency_graph(ir: List[Task]) -> nx.DiGraph:
    """
    Build a dependency graph.

    For demonstration, tasks are connected sequentially. In a real compiler,
    this should be generated from data/control dependencies.
    """
    graph = nx.DiGraph()
    for task in ir:
        graph.add_node(task.name, task=task)

    for i in range(len(ir) - 1):
        graph.add_edge(ir[i].name, ir[i + 1].name)

    if not nx.is_directed_acyclic_graph(graph):
        raise ValueError("Dependency graph must be a DAG.")

    return graph


def optimize_ir(ir: List[Task], graph: nx.DiGraph) -> List[Task]:
    """Optimize IR using topological ordering and resource-cost sorting."""
    order = list(nx.topological_sort(graph))
    task_map = {task.name: task for task in ir}
    ordered_tasks = [task_map[name] for name in order]
    return sorted(ordered_tasks, key=lambda t: (t.cpu + t.mem / 128 + t.sec))


def generate_executable(optimized_ir: List[Task]) -> List[Dict[str, str]]:
    """Generate executable task units."""
    executable = []
    for task in optimized_ir:
        executable.append({
            "task": task.name,
            "bytecode": f"EXEC::{task.name}::CPU{task.cpu}::MEM{task.mem}::SEC{task.sec}"
        })
    return executable


def compile_source(source: str):
    """Run complete compiler pipeline."""
    tokens = lexical_analysis(source)
    ast = syntax_analysis(source)
    semantic_analysis(ast)
    ir = generate_ir(ast)
    graph = build_dependency_graph(ir)
    optimized_ir = optimize_ir(ir, graph)
    executable = generate_executable(optimized_ir)
    return {
        "tokens": tokens,
        "ast": ast,
        "ir": [task.__dict__ for task in ir],
        "optimized_ir": [task.__dict__ for task in optimized_ir],
        "executable": executable,
        "dependency_edges": list(graph.edges()),
    }
