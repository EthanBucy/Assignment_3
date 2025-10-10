from __future__ import annotations

from collections import deque
from pathlib import Path
from typing import Deque, List, Optional

try:
    from starter.graph_impl import Edge, Graph, Vertex
    from starter.graph_interfaces import IGraph, IVertex
except ModuleNotFoundError:  # pragma: no cover - fallback when run as a script
    from graph_impl import Edge, Graph, Vertex
    from graph_interfaces import IGraph, IVertex


def read_graph(file_path: str) -> IGraph:
    """Read the graph from *file_path* and return a populated :class:`Graph`."""

    graph = Graph()
    vertices: dict[str, Vertex] = {}

    try:
        with open(file_path, "r", encoding="utf-8") as graph_file:
            # Skip header line
            next(graph_file)
            for line_number, line in enumerate(graph_file, start=2):
                stripped = line.strip()
                if not stripped:
                    continue

                parts = stripped.split(",")
                if len(parts) != 4:
                    raise ValueError(f"Line {line_number} malformed: {stripped}")

                source_name, destination_name, edge_label, weight_text = parts

                try:
                    weight = float(weight_text)
                except ValueError as exc:
                    raise ValueError(
                        f"Line {line_number} has invalid weight '{weight_text}'"
                    ) from exc

                source_vertex = vertices.setdefault(source_name, Vertex(source_name))
                destination_vertex = vertices.setdefault(
                    destination_name, Vertex(destination_name)
                )

                graph.add_vertex(source_vertex)
                graph.add_vertex(destination_vertex)

                edge_name = f"{source_name}->{destination_name}:{edge_label}"
                edge = Edge(edge_name, source_vertex, destination_vertex, weight)
                graph.add_edge(edge)

    except FileNotFoundError as exc:
        raise FileNotFoundError(f"Unable to open '{file_path}'") from exc

    return graph


def _visit(vertex: Vertex, order: List[str]) -> None:
    vertex.set_visited(True)
    order.append(vertex.get_name())


def print_dfs(graph: IGraph, start_vertex: IVertex) -> None:
    """Print the DFS traversal of the graph starting from *start_vertex*."""

    if not isinstance(graph, Graph) or not isinstance(start_vertex, Vertex):
        raise TypeError("DFS requires Graph and Vertex instances")

    graph.reset_visits()
    order: List[str] = []

    def dfs(current: Vertex) -> None:
        _visit(current, order)
        for edge in current.get_edges():
            neighbor = edge.get_destination()
            if isinstance(neighbor, Vertex) and not neighbor.is_visited():
                dfs(neighbor)

    dfs(start_vertex)
    print("DFS order:", " -> ".join(order))


def print_bfs(graph: IGraph, start_vertex: IVertex) -> None:
    """Print the BFS traversal of the graph starting from *start_vertex*."""

    if not isinstance(graph, Graph) or not isinstance(start_vertex, Vertex):
        raise TypeError("BFS requires Graph and Vertex instances")

    graph.reset_visits()
    order: List[str] = []
    queue: Deque[Vertex] = deque([start_vertex])
    start_vertex.set_visited(True)

    while queue:
        vertex = queue.popleft()
        order.append(vertex.get_name())

        for edge in vertex.get_edges():
            neighbor = edge.get_destination()
            if isinstance(neighbor, Vertex) and not neighbor.is_visited():
                neighbor.set_visited(True)
                queue.append(neighbor)

    print("BFS order:", " -> ".join(order))


def main() -> None:
    data_path = Path(__file__).with_name("sample_graph_data.txt")
    graph: IGraph = read_graph(str(data_path))
    start_vertex_name: str  = input("Enter the start vertex name: ")

    # Find the start vertex object
    start_vertex: Optional[IVertex]= next((v for v in graph.get_vertices() if v.get_name() == start_vertex_name), None)

    if start_vertex is None:
        print("Start vertex not found")
        return
    
    print_dfs(graph, start_vertex)
    print_bfs(graph, start_vertex)


if __name__ == "__main__":
    main()