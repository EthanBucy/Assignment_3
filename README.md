Project Overview

This project implements a directed graph library in Python along with a parser
for loading edge data from the provided `sample_graph_data.txt` CSV file. The
graph supports breadth-first search (BFS) and depth-first search (DFS)
traversals that report the order in which vertices are visited.

Author

- Ethan Bucy

Running the Program

Execute `python3 -m starter.program` in the root terminal.
When prompted, enter the name of the starting vertex (Portland)

Assumptions and Design Decisions

- The sample data file always includes a header row and uses commas.
- Edge weights in the data file are numeric values that can be parsed as
  floating-point numbers.
- Graph vertices are uniquely identified by their string names from the input
  data.

DFS Traversal Output

DFS order: Portland -> Salem -> Eugene -> Corvallis -> Newport -> Tillamook -> Seaside -> Astoria -> Florence -> Coos_Bay -> Roseburg -> Medford -> Ashland -> Crater_Lake -> Bend -> Redmond -> Madras -> The_Dalles -> Hood_River -> Pendleton -> Ontario -> Burns

BFS Traversal Output

BFS order: Portland -> Salem -> Astoria -> Hood_River -> Newport -> Eugene -> Corvallis -> Seaside -> The_Dalles -> Tillamook -> Florence -> Bend -> Crater_Lake -> Roseburg -> Pendleton -> Madras -> Coos_Bay -> Redmond -> Burns -> Medford -> Ontario -> Ashland

