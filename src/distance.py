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
    return 0.0 if information in actuel else 1.0


def distance_mois(information: int, actuel: list[int] | None) -> float:
    if not actuel:
        return 0.0
    return 1.0 if information in actuel else 0.0


def find_closer(bird: dict, list_birds: list[Bird]) -> list[Bird]:
    nb_modif = len(bird.keys())
    res: list[float] = [0.0] * len(list_birds)

    for i, real in enumerate(list_birds):
        for key in bird.keys():
            match key:
                case "Taille":
                    if bird["Taille"] == "":
                        continue
                    res[i] += distance_list_int_or_int(
                        float(bird["Taille"]), real["Taille"]
                    )
                case "Envergure":
                    if bird["Envergure"] == "":
                        continue
                    res[i] += distance_list_int_or_int(
                        float(bird["Envergure"]), real["Envergure"]
                    )
                case "Poids":
                    if bird["Poids"] == "":
                        continue
                    res[i] += distance_list_int_or_int(
                        float(bird["Poids"]), real["Poids"]
                    )
                case "Couleurs_principales":
                    res[i] += distance_list_str(
                        bird["Couleurs_principales"], real["Couleurs_principales"]
                    )
                case "Bec":
                    res[i] += distance_str(bird["Bec"], real["Bec"])
                case "Couleur_bec":
                    res[i] += distance_list_str(
                        bird["Couleur_bec"], real["Couleur_bec"]
                    )
                case "Mois_observation":
                    res[i] += distance_mois(
                        bird["Mois_observation"], real["Periode_d_abscence"]
                    )
                case "Pattes":
                    res[i] += distance_str(bird["Pattes"], real["Pattes"])
                case "Couleur_pattes":
                    res[i] += distance_list_str(
                        bird["Couleur_pattes"], real["Couleur_pattes"]
                    )
                case "Regime_alimentaire":
                    res[i] += distance_list_str(
                        bird["Regime_alimentaire"], real["Regime_alimentaire"]
                    )
    for e in res:
        e /= nb_modif
    for i, e in enumerate(res):
        list_birds[i]["score"] = e

    # Trier par distance croissante (plus proche = plus petit score)
    id_res: list[int] = sorted(range(len(res)), key=lambda i: res[i])[:5]
    return [list_birds[i] for i in id_res]


"""
def find_closer(bird: dict, list_birds: list[Bird]) -> list[Bird]:
    res: list[float] = [0.0] * len(list_birds)
    nb_modif = len(bird.keys())
    for i, real in enumerate(list_birds):
        for key in bird.keys():
            match key:
                case "Taille":
                    res[i] += distance_list_int_or_int(
                        float(bird["Taille"]), real["Taille"]
                    )
                case "Envergure":
                    res[i] += distance_list_int_or_int(
                        float(bird["Envergure"]), real["Envergure"]
                    )
                case "Poids":
                    res[i] += distance_list_int_or_int(
                        float(bird["Poids"]), real["Poids"]
                    )
                case "Couleurs_principales":
                    res[i] += distance_str(
                        bird["Couleurs_principales"], real["Couleurs_principales"]
                    )
                case "Couleur_bec":
                    res[i] += distance_str(bird["Couleur_bec"], real["Couleur_bec"])
                case "Mois_observation":
                    res[i] += distance_mois(
                        bird["Mois_observation"], real["Periode_d_abscence"]
                    )
                case "Couleur_pattes":
                    res[i] += distance_str(
                        bird["Couleur_pattes"], real["Couleur_pattes"]
                    )

    id_res: list[int] = sorted(range(len(res)), key=lambda i: res[i], reverse=True)[:5]
    return [list_birds[i] for i in id_res]
"""
