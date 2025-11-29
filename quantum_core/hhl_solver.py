"""
hhl_solver.py — Lite public demo of the HHL quantum linear solver.

This is a classical Gaussian elimination placeholder for the real HHL backend.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import List


@dataclass
class HHLResult:
    solution: List[float]
    mode: str = "lite-demo"


class HHLSolver:
    """Lite HHL Solver using classical elimination."""

    def __init__(self):
        self.name = "HHLSolverLite"
        self.version = "0.1.0"

    def solve(self, a: List[List[float]], b: List[float]) -> HHLResult:
        n = len(a)
        m = [row[:] + [b_i] for row, b_i in zip(a, b)]

        # forward elimination
        for i in range(n):
            pivot = m[i][i] or 1e-9
            for j in range(i, n + 1):
                m[i][j] /= pivot
            for k in range(i + 1, n):
                factor = m[k][i]
                for j in range(i, n + 1):
                    m[k][j] -= factor * m[i][j]

        # back substitution
        x = [0.0] * n
        for i in range(n - 1, -1, -1):
            x[i] = m[i][n] - sum(m[i][j] * x[j] for j in range(i + 1, n))

        return HHLResult(solution=x)


def run_hhl_demo() -> HHLResult:
    a = [
        [2.0, 1.0],
        [1.0, -1.0],
    ]
    b = [5.0, 1.0]
    solver = HHLSolver()
    return solver.solve(a, b)
  
