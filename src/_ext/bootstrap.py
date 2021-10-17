"""
Download the latest bootstrap script as part of the build process.

This extension automatically fetches the latest bootstrap script from the
main GitHub repository, places it in the output directory, and injects its
checksum as an RST variable called 'bootstrap-hash'.
"""
from os import path
import hashlib
import os
import shutil
import urllib
from sphinx.util import logging


logger = logging.getLogger(__name__)


def setup(app):
    local = path.join(app.outdir, "bootstrap")
    os.makedirs(app.outdir, exist_ok=True)

    if not path.exists(local):
        # Download the bootstrap script from the main repository
        remote = "https://raw.githubusercontent.com/toltec-dev/toltec/stable/scripts/bootstrap/bootstrap"

        with urllib.request.urlopen(remote) as res, open(local, "wb") as out:
            shutil.copyfileobj(res, out)

        logger.info("Downloaded bootstrap script")

    # Compute the script checksum and inject it in the reST prolog
    checksum_obj = hashlib.sha256()

    with open(local, "rb") as out:
        for chunk in iter(lambda: out.read(4096), b""):
            checksum_obj.update(chunk)

    checksum = checksum_obj.hexdigest()
    old_prolog = app.config["rst_prolog"] or ""
    app.config["rst_prolog"] = old_prolog + \
        f".. |bootstrap-hash| replace:: {checksum}\n"
