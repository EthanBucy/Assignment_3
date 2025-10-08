# Assignment 3 Overview and Step-by-Step Plan

## Overview
This assignment focuses on building a directed graph library that conforms to the provided interfaces, parsing real-world data into that structure, and demonstrating both depth-first search (DFS) and breadth-first search (BFS) traversals. You will create concrete implementations for the graph, vertex, and edge abstractions, load edge data from a file, and then exercise traversal algorithms that report the visitation order. Deliverables include code, traversal outputs recorded in your README, and a tagged GitHub release.

## Step-by-Step Plan
1. **Repository Preparation**
   - Fork or clone the starter code into your own GitHub repository.
   - Add a README outlining project purpose, team members, and basic usage instructions.
   - Share repository access with the instructor (GitHub user `LucasCordova`).

2. **Familiarize Yourself with Interfaces**
   - Read `graph_interfaces.py` to understand required methods for `IGraph`, `IVertex`, and `IEdge`.
   - Note the behaviors you must support, such as tracking neighbors, visit status, and edge weights.

3. **Design Concrete Classes**
   - Sketch class diagrams or pseudocode for `Graph`, `Vertex`, and `Edge` in `graph_impl.py` that satisfy the interfaces.
   - Decide on internal data structures (e.g., adjacency maps, sets) for efficient lookups.

4. **Implement Graph Components**
   - Implement `Vertex` and `Edge` first, fulfilling property accessors and mutators.
   - Implement the `Graph` class methods for adding/removing vertices and edges, retrieving neighbors, and resetting visit states.
   - Write docstrings or comments explaining any non-obvious design decisions.

5. **Develop Data Parsing Logic**
   - Inspect `graph.txt` (or `sample_graph_data.txt` per assignment instructions) to understand its format.
   - Implement the `read_graph` function in `program.py` to open the file, parse lines, and populate your `Graph` instance.
   - Include error handling for missing files or malformed lines.

6. **Implement Traversal Algorithms**
   - Add `print_dfs` and `print_bfs` (or similarly named functions) in `program.py` that consume the graph and a start vertex.
   - For DFS, use recursion or an explicit stack while respecting directed edges.
   - For BFS, use a queue to explore vertices level by level.
   - Ensure both functions record or print the order of visited vertices.

7. **Test Traversals Manually**
   - Run the program, select various start vertices, and verify visitation sequences.
   - Compare results against expectations from the graph data to validate correctness.

8. **Document Traversal Output**
   - Capture sample DFS and BFS outputs and paste them into dedicated sections in your README as required.
   - Mention any assumptions (e.g., handling of duplicate edges or weights).

9. **Polish and Review**
   - Clean up code formatting and add comments where helpful.
   - Ensure the repository contains all required files, including the sample data and README updates.
   - Commit changes with descriptive messages throughout development.

10. **Submission Workflow**
    - Run final tests and create a release on GitHub (e.g., tag `v1.0`).
    - Publish the release, copy its URL, and submit it via Canvas before the deadline.

Following this plan will guide you from understanding the scaffold to delivering a complete, well-documented graph traversal project.
