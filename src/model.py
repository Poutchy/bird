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
    Regime_alimentaire: list[str]
    score: float
