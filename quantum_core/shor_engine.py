"""
shor_engine.py — Lite demo-движок Алгоритма Шора для BotZaVOD Quantum Core.

Это НЕ настоящий квантовый алгоритм, а безопасная публичная версия:
- использует обычный Python (классическое факторизование);
- показывает структуру "движка" (инициализация, запуск, лог);
- в боевой версии внутренняя логика будет заменена на реальный core.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List


@dataclass
class ShorResult:
    number: int
    factors: List[int]
    steps: int
    mode: str = "lite-demo"


class ShorEngine:
    """Lite Shor-engine: классический факторизатор для публичного репо."""

    def __init__(self) -> None:
        self.name = "ShorEngineLite"
        self.version = "0.1.0"
        self.backend = "classical"

    def factor(self, n: int) -> ShorResult:
        """Очень простой перебор делителей, только для демо."""
        if n <= 1:
            return ShorResult(number=n, factors=[n], steps=0)

        factors: List[int] = []
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
        """Метаданные движка — удобно показывать в README/логах."""
        return {
            "engine": self.name,
            "version": self.version,
            "backend": self.backend,
            "mode": "public-lite",
        }


def run_shor_demo(n: int = 21) -> ShorResult:
    """
    Удобная обёртка: один вызов для тестов и примеров.

    Пример:
        from quantum_core import shor_engine
        result = shor_engine.run_shor_demo(33)
        print(result.factors)
    """
    engine = ShorEngine()
    return engine.factor(n)
  
