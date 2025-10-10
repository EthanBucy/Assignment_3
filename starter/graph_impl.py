"""Concrete graph data structure implementations."""

from __future__ import annotations

from typing import Dict, List

try:
    from starter.graph_interfaces import IEdge, IGraph, IVertex
except ModuleNotFoundError:  # Seems to only work with this try and except
    from graph_interfaces import IEdge, IGraph, IVertex


class Graph(IGraph):
    """A directed graph implementation backed by adjacency lists."""

    def __init__(self) -> None:
        self._vertices: Dict[str, Vertex] = {}
        self._edges: Dict[str, Edge] = {}

    def get_vertices(self) -> List[IVertex]:
        """Return all vertices in insertion order."""

        return list(self._vertices.values())

    def get_edges(self) -> List[IEdge]:
        """Return all edges currently in the graph."""

        return list(self._edges.values())

    def add_vertex(self, vertex: IVertex) -> None:
        """Add *vertex* to the graph if its name is not already present."""

        if not isinstance(vertex, Vertex):
            raise TypeError("Graph only supports Vertex instances")

        vertex_name = vertex.get_name()
        if vertex_name in self._vertices:
            return

        self._vertices[vertex_name] = vertex

    def remove_vertex(self, vertex_name: str) -> None:
        """Remove the vertex and any incident edges from the graph."""

        vertex = self._vertices.pop(vertex_name, None)
        if vertex is None:
            return

        # Remove outgoing edges
        for edge in list(vertex.get_edges()):
            self.remove_edge(edge.get_name())

        # Remove incoming edges
        for edge_name, edge in list(self._edges.items()):
            if edge.get_destination().get_name() == vertex_name:
                self.remove_edge(edge_name)

    def add_edge(self, edge: IEdge) -> None:
        """Add *edge* to the graph, attaching it to its source vertex."""

        if not isinstance(edge, Edge):
            raise TypeError("Graph only supports Edge instances")

        if edge.get_name() in self._edges:
            return

        source_vertex = edge.get_source()
        source_name = source_vertex.get_name()
        if source_name not in self._vertices:
            self.add_vertex(source_vertex)

        destination = edge.get_destination()
        if destination.get_name() not in self._vertices:
            self.add_vertex(destination)

        self._edges[edge.get_name()] = edge
        source_vertex.add_edge(edge)

    def remove_edge(self, edge_name: str) -> None:
        """Remove *edge_name* from the graph."""

        edge = self._edges.pop(edge_name, None)
        if edge is None:
            return

        source = edge.get_source()
        source.remove_edge(edge_name)

    def reset_visits(self) -> None:
        """Mark every vertex in the graph as unvisited."""

        for vertex in self._vertices.values():
            vertex.set_visited(False)


class Vertex(IVertex):
    """Vertex implementation storing outgoing edges and visit state."""

    def __init__(self, name: str) -> None:
        self._name: str = name
        self._edges: Dict[str, Edge] = {}
        self._visited: bool = False

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        self._name = name

    def add_edge(self, edge: IEdge) -> None:
        if not isinstance(edge, Edge):
            raise TypeError("Vertex only supports Edge instances")

        self._edges[edge.get_name()] = edge

    def remove_edge(self, edge_name: str) -> None:
        self._edges.pop(edge_name, None)

    def remove_edge_by_destination(self, destination_name: str) -> None:
        """Remove the edge whose destination vertex matches *destination_name*."""

        for edge_name, edge in list(self._edges.items()):
            if edge.get_destination().get_name() == destination_name:
                del self._edges[edge_name]

    def get_edges(self) -> List[IEdge]:
        return list(self._edges.values())

    def set_visited(self, visited: bool) -> None:
        self._visited = visited

    def is_visited(self) -> bool:
        return self._visited


class Edge(IEdge):
    """Directed edge representation with optional weight."""

    def __init__(self, name: str, source: Vertex, destination: Vertex, weight: float = 1.0) -> None:
        self._name: str = name
        self._source: Vertex = source
        self._destination: Vertex = destination
        self._weight: float = weight

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        self._name = name

    def get_destination(self) -> IVertex:
        return self._destination

    def get_weight(self) -> float:
        return self._weight

    def set_weight(self, weight: float) -> None:
        self._weight = weight

    def get_source(self) -> Vertex:
        """Return the vertex this edge originates from."""

        return self._source
