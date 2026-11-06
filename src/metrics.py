"""Scoring for probabilistic predictions."""

import math


def brier(probs, outcomes) -> float:
    pairs = list(zip(probs, outcomes))
    return sum((p - o) ** 2 for p, o in pairs) / len(pairs)


def log_loss(probs, outcomes, eps: float = 1e-15) -> float:
    pairs = list(zip(probs, outcomes))
    return -sum(
        o * math.log(max(p, eps)) + (1 - o) * math.log(max(1 - p, eps)) for p, o in pairs
    ) / len(pairs)
