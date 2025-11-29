"""
yota_engine.py — Lite demo of the 'Yota' load-routing engine.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List


@dataclass
class RouteDecision:
    target: str
    score: float
    all_scores: Dict[str, float]
    mode: str = "lite-demo"


class YotaEngine:
    """Lite Yota Engine — chooses best compute channel based on load hints."""

    def __init__(self):
        self.name = "YotaEngineLite"
        self.version = "0.1.0"
        self.channels = ["cpu", "gpu", "quantum", "remote_node"]

    def route(self, load_hint: Dict[str, float]) -> RouteDecision:
        scores = {}

        for ch in self.channels:
            busy = load_hint.get(ch, 0.5)
            scores[ch] = 1.0 - busy  # lower load = higher score

        best = max(scores, key=scores.get)

        return RouteDecision(
            target=best,
            score=scores[best],
            all_scores=scores,
        )


def run_yota_demo() -> RouteDecision:
    engine = YotaEngine()
    load = {"cpu": 0.1, "gpu": 0.8, "quantum": 0.9, "remote_node": 0.4}
    return engine.route(load)
  
