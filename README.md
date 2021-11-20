## Toltec Website

_Please refer to [our website](https://toltec-dev.org) for information on how to install and use Toltec._

This repository contains the files used to build [Toltec’s website](https://toltec-dev.org).
We use [Sphinx](https://www.sphinx-doc.org/en/master/) to author and build the website.

### Structure

* The overall site structure is defined in [`src/sitemap.rst`](src/sitemap.rst). This file is used to generate the sidebar.
* The global site layout is defined in [`src/_themes/toltec/layout.html`](src/_themes/toltec/layout.html). In that folder, the stylesheet and global images can be found.
* Toltec-specific Sphinx extensions are defined under [`src/_ext`](src/_ext).

### Workflows

Commits pushed to the main branch of this repository will trigger a GitHub Workflow that builds the website and deploys it to the live server.
This workflow is also triggered by pushes to the main repository’s stable branch (to automatically update the [bootstrap script](https://toltec-dev.org/bootstrap) to the latest stable version).

### Build Instructions

After cloning this repo, use `make prod` to generate the website.
The build result will be located under the `dist/` folder.
You can also use `make dev` to start a live-reloading server, which is useful to see your changes rendered in real time.
