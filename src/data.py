from csv import DictReader
from pathlib import Path
from typing import TypedDict


class Bird(TypedDict):
    Nom: str
    Nom_latin: str
    Type: str
    Taille: tuple[int, int] | int
    Envergure: tuple[int, int] | int
    Poids: tuple[float, float] | float
    Couleurs_principales: list[str]
    Bec: str
    Couleur_bec: list[str]
    Periode_d_abscence: list[int]
    Pattes: str
    Couleur_pattes: list[str]
    Régime_alimentaire: list[str]


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
        "Régime_alimentaire": parse_list(row["Régime alimentaire"]),
    }


temp_bird_dict: list[Bird] = []

with open(Path("src/oiseaux_utf8.csv"), encoding="utf_8") as csvfile:
    birdreader = DictReader(csvfile, delimiter=";")
    for line in birdreader:
        temp_bird_dict.append(normalize_row(line))
for line in temp_bird_dict:
    print(line)
