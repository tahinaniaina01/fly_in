"""
Script pour supprimer l'arrière-plan d'une image.

Installation requise :
    pip install rembg pillow

Utilisation :
    python supprimer_arriere_plan.py chemin/vers/image.jpg
"""

import sys
from pathlib import Path
from rembg import remove
from PIL import Image


def supprimer_arriere_plan(chemin_entree: str, chemin_sortie: str = None) -> str:
    """
    Supprime l'arrière-plan d'une image et sauvegarde le résultat en PNG
    (avec transparence).

    Args:
        chemin_entree: chemin de l'image source
        chemin_sortie: chemin de l'image de sortie (optionnel)

    Returns:
        Le chemin du fichier généré.
    """
    chemin_entree = Path(chemin_entree)

    if not chemin_entree.exists():
        raise FileNotFoundError(f"Fichier introuvable : {chemin_entree}")

    if chemin_sortie is None:
        chemin_sortie = chemin_entree.with_name(
            chemin_entree.stem + "_sans_fond.png"
        )
    else:
        chemin_sortie = Path(chemin_sortie)

    # Ouverture de l'image d'origine
    with Image.open(chemin_entree) as image:
        # Suppression de l'arrière-plan (retourne une image avec canal alpha)
        resultat = remove(image)
        resultat.save(chemin_sortie)

    return str(chemin_sortie)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage : python supprimer_arriere_plan.py chemin/vers/image.jpg")
        sys.exit(1)

    entree = sys.argv[1]
    sortie = sys.argv[2] if len(sys.argv) > 2 else None

    try:
        resultat = supprimer_arriere_plan(entree, sortie)
        print(f"Image générée avec succès : {resultat}")
    except Exception as e:
        print(f"Erreur : {e}")
        sys.exit(1)