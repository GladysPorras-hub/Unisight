"""Central settings: palette, paths, section names. Edit here, not in the pages."""
from pathlib import Path

ROOT = Path(__file__).parent
DATA = ROOT / "data"
ASSETS = ROOT / "assets"

# Official palette: academic crimson, vivid coral orange, deep slate blue, smoke white, soft sand pink
CRIMSON, CORAL, SLATE, BONE, SAND = "#C5192D", "#FF3A21", "#1E293B", "#F8FAFC", "#FEE2E2"

SECTIONS = [
    "SDG 4 – Quality Education",
    "SDG 5 – Gender Equality",
    "Projections 2050",
    "Wireframes / What If?",
    "Take Action",
    "Who We Are",
]
