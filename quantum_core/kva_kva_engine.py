"""
kva_kva_engine.py — Lite demo of the 'Kva-Kva' caching accelerator.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class KvaKvaStats:
    requests: int
    hits: int
    misses: int
    mode: str = "lite-demo"


class KvaKvaEngine:
    """Lite cache engine with simple hit/miss statistics."""

    def __init__(self):
        self.name = "KvaKvaEngineLite"
        self.version = "0.1.0"
        self._cache = {}
        self._hits = 0
        self._misses = 0

    def get_or_set(self, key: str, producer) -> Any:
        if key in self._cache:
            self._hits += 1
            return self._cache[key]

        self._misses += 1
        value = producer()
        self._cache[key] = value
        return value

    def stats(self) -> KvaKvaStats:
        return KvaKvaStats(
            requests=self._hits + self._misses,
            hits=self._hits,
            misses=self._misses,
        )


def run_kva_kva_demo() -> KvaKvaStats:
    engine = KvaKvaEngine()

    def make():
        return "heavy_result"

    engine.get_or_set("task", make)
    engine.get_or_set("task", make)
    engine.get_or_set("task", make)

    return engine.stats()
  
