"""
shor_engine.py — Lite public demo of Shor's Algorithm engine for BotZaVOD Quantum Core.

This is NOT a real quantum implementation — only a safe classical demo:
- classical integer factorization;
- clean engine structure (init, run, metadata);
- serves as a placeholder for the private quantum backend.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import List, Dict


@dataclass
class ShorResult:
    number: int
    factors: List[int]
    steps: int
    mode: str = "lite-demo"


class ShorEngine:
    """Lite Shor Engine — classical factorization for public repository."""

    def __init__(self):
        self.name = "ShorEngineLite"
        self.version = "0.1.0"
        self.backend = "classical"

    def factor(self, n: int) -> ShorResult:
        """Very simple divisor search — demo only."""
        if n <= 1:
            return ShorResult(number=n, factors=[n], steps=0)

        factors = []
        d = 2
        steps = 0
        tmp = n

        while d * d <= tmp:
            while tmp % d == 0:
                factors.append(d)
                tmp //= d
            d += 1
            steps += 1

        if tmp > 1:
            factors.append(tmp)

        return ShorResult(number=n, factors=factors, steps=steps)

    def info(self) -> Dict[str, str]:
        return {
            "engine": self.name,
            "version": self.version,
            "backend": self.backend,
            "mode": "public-lite",
        }


def run_shor_demo(n: int = 21) -> ShorResult:
    """Convenience wrapper for quick testing."""
    engine = ShorEngine()
    return engine.factor(n)
    
