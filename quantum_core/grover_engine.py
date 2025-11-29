"""
grover_engine.py — Lite demo-движок Алгоритма Гровера для BotZaVOD Quantum Core.

Задача: показать структуру поискового движка без реального квантового backend'а.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Any, List, Dict, Callable
import random


@dataclass
class GroverResult:
    space_size: int
    target_index: int
    attempts: int
    found: bool
    mode: str = "lite-demo"


class GroverEngine:
    """Lite Grover-engine: имитация поиска по пространству состояний."""

    def __init__(self) -> None:
        self.name = "GroverEngineLite"
        self.version = "0.1.0"
        self.backend = "classical"

    def search(
        self,
        space: List[Any],
        oracle: Callable[[Any], bool],
        max_attempts: int = 64,
    ) -> GroverResult:
        """
        Имитируем «квантовый» поиск случайными попытками.

        space  — список элементов
        oracle — функция, которая говорит, является ли элемент целью
        """
        indices = list(range(len(space)))
        random.shuffle(indices)

        attempts = 0
        target_index = -1
        found = False

        for idx in indices[:max_attempts]:
            attempts += 1
            if oracle(space[idx]):
                target_index = idx
                found = True
                break

        return GroverResult(
            space_size=len(space),
            target_index=target_index,
            attempts=attempts,
            found=found,
        )

    def info(self) -> Dict[str, str]:
        return {
            "engine": self.name,
            "version": self.version,
            "backend": self.backend,
            "mode": "public-lite",
        }


def run_grover_demo() -> GroverResult:
    """Пример: ищем число 42 в массиве случайных чисел."""
    space = [random.randint(0, 100) for _ in range(64)]
    target = 42

    def oracle(x: int) -> bool:
        return x == target

    engine = GroverEngine()
    return engine.search(space, oracle)
  
