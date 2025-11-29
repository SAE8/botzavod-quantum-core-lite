"""
dolce_engine.py — Lite demo of the custom 'Dolce' optimization engine.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, Dict, List
import random


@dataclass
class DolceStep:
    iteration: int
    value: float
    temperature: float


@dataclass
class DolceResult:
    best_value: float
    history: List[DolceStep]
    mode: str = "lite-demo"


class DolceEngine:
    """Lite optimization engine similar to soft simulated annealing."""

    def __init__(self):
        self.name = "DolceEngineLite"
        self.version = "0.1.0"

    def optimize(
        self,
        objective: Callable[[float], float],
        start: float = 0.0,
        steps: int = 50,
    ) -> DolceResult:

        value = start
        best_value = objective(value)
        history = []

        for i in range(steps):
            temperature = max(0.01, 1.0 - i / steps)
            proposal = value + random.uniform(-1, 1) * temperature
            score = objective(proposal)

            if score < best_value or random.random() < temperature * 0.3:
                value = proposal
                best_value = min(best_value, score)

            history.append(DolceStep(i, value, temperature))

        return DolceResult(best_value=best_value, history=history)

    def info(self) -> Dict[str, str]:
        return {"engine": self.name, "version": self.version, "mode": "public-lite"}


def run_dolce_demo() -> DolceResult:
    def obj(x):
        return x * x

    engine = DolceEngine()
    return engine.optimize(obj, start=3.0)
  
