import os
import sys

sys.path.append(os.path.abspath("./_ext"))

project = "Toltec"
copyright = "2021, The Toltec Contributors"
author = "The Toltec Contributors"

html_theme_path = ["_themes"]
html_static_path = ["_static"]
templates_path = ["_templates"]

html_title = "Toltec"
html_theme = "toltec"
master_doc = "sitemap"
html_sidebars = { "**": ["nav.html", "sidefooter.html"] }
html_permalinks_icon = "#"

extensions = [
    "sphinxcontrib.fulltoc",
    "bootstrap",
]
