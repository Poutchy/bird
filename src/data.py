from csv import DictReader
from pathlib import Path

from .model import Bird


def parse_int_range(value: str) -> int | tuple[int, int]:
    if "-" in value:
        a, b = value.split("-")
        return int(a), int(b)
    return int(value)


def parse_float_range(value: str) -> float | tuple[float, float]:
    if "-" in value:
        a, b = value.split("-")
        return float(a), float(b)
    return float(value)


def parse_list(value: str) -> list[str]:
    if not value:
        return []
    return value.split("/")


def parse_months(value: str) -> list[int]:
    if not value:
        return []
    return [int(v) for v in value.split("/") if v.isdigit()]


def normalize_row(row: dict[str, str]) -> Bird:
    return {
        "Nom": row["Nom"],
        "Nom_latin": row["Nom latin"],
        "Type": row["Type"],
        "Taille": parse_int_range(row["Taille"]),
        "Envergure": parse_int_range(row["Envergure"]),
        "Poids": parse_float_range(row["Poids"]),
        "Couleurs_principales": parse_list(row["Couleurs principales"]),
        "Bec": row["Bec"],
        "Couleur_bec": parse_list(row["Couleur bec"]),
        "Periode_d_abscence": parse_months(row["Periode d'abscence"]),
        "Pattes": row["Pattes"],
        "Couleur_pattes": parse_list(row["Couleur pattes"]),
        "Regime_alimentaire": parse_list(row["Régime alimentaire"]),
    }


def create_list_birds(filename: str) -> list[Bird]:
    bird_dict = []
    with open(Path(filename), encoding="utf_8") as csvfile:
        birdreader = DictReader(csvfile, delimiter=";")
        for line in birdreader:
            bird_dict.append(normalize_row(line))
    return bird_dict


def normalize_form_data(form_data: dict) -> dict:
    normalized = {}
    for key, value in form_data.items():
        if isinstance(value, list):
            # Pour les champs multi-choix, on garde la liste
            if key in [
                "Couleurs_principales",
                "Couleur_bec",
                "Couleur_pattes",
                "Regime_alimentaire",
            ]:
                normalized[key] = value
            # Pour les champs simples (texte, radio, select), on prend le premier élément
            else:
                normalized[key] = value[0] if value else None
        else:
            normalized[key] = value
    return normalized


if __name__ == "__main__":
    temp_bird_dict: list[Bird] = create_list_birds("./src/oiseaux_utf8.csv")
    for bird in temp_bird_dict:
        print(bird)
