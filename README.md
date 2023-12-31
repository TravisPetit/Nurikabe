# Nurikabe

_DEG-3-SHP3*_ is the following decision problem:


**INPUT**: A subgrid graph G = (V, E) with deg(v) ≤ 3 for all v in V and s ≠ t in V such that deg(s) = deg(t) = 1, and the degree of t's neighbor is 2.


**QUESTION**: Is there an s-t Hamiltonian path in G?


_DEG-3-SHP3*_ is **NP** complete. There exists a reduction of the form _DEG-3-SHP3*_ ≤ _IPC Nurikabe_. The latter is a planning domain from the IPC-2018 (see http://editor.planning.domains/).
This project provides a parser that takes arbitrary _DEG-3-SHP3*_ instances and returns the corresponding _IPC Nurikabe_ layout.

# Usage
``python3 main.py -fname filename.txt [-v][-b][-e][-T][-Tp]``
