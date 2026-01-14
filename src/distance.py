from src.model import Bird


def distance_list_int_or_int(
    information: float, actuel: tuple[float, float] | float
) -> float:
    if isinstance(actuel, tuple):
        min_v, max_v = actuel
        if min_v <= information <= max_v:
            return 0.0

        dist = min(abs(information - min_v), abs(information - max_v))
        span = max_v - min_v
        return min(dist / span, 1.0) if span > 0 else 1.0
    if actuel == 0:
        return 1.0
    return min(abs(information - actuel) / actuel, 1.0)


def distance_list_str(information: list[str], actuel: list[str]) -> float:
    if not information and not actuel:
        return 0.0
    if not information or not actuel:
        return 1.0

    set_info = set(information)
    set_actuel = set(actuel)

    intersection = len(set_info & set_actuel)
    union = len(set_info | set_actuel)

    return 1.0 - (intersection / union)


def distance_str(information: str, actuel: list[str] | str) -> float:
    if isinstance(actuel, list):
        return 0.0 if information in actuel else 1.0
    return 0.0 if information == actuel else 1.0


def distance_mois(information: int, actuel: list[int] | None) -> float:
    if not actuel:
        return 0.0
    return 1.0 if information in actuel else 0.0


def find_closer(bird: dict, list_birds: list[Bird]) -> list[Bird]:
    return []
