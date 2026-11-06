"""Elo rating model."""

K = 20
HOME_ADVANTAGE = 55  # pre-registered in writeup/methodology.md, Section 4
START_RATING = 1500


def expected(rating_a: float, rating_b: float) -> float:
    """Probability that A beats B."""
    return 1 / (1 + 10 ** ((rating_b - rating_a) / 400))


def update(rating_a: float, rating_b: float, score_a: float, k: float = K) -> tuple[float, float]:
    """Return new (rating_a, rating_b); score_a is 1 for a win, 0.5 tie, 0 loss."""
    delta = k * (score_a - expected(rating_a, rating_b))
    return rating_a + delta, rating_b - delta
