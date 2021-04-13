## Toltec Website

This repository contains the files used to build [Toltec’s website](https://toltec-dev.org).
Please refer to the website or to the [main repository](https://github.com/toltec-dev/toltec) for information on how to install Toltec.

### Workflows

Commits pushed to the main branch of this repository will trigger a GitHub Workflow that builds the website and deploys it to the live server.
This workflow is also triggered by pushes to the main repository’s stable branch (to update the [bootstrap script](https://toltec-dev.org/bootstrap) to the latest stable version).

### Build Instructions

We use [Docutils](https://docutils.sourceforge.io/) to author and build the pages.
After cloning this repo, use the following commands to generate the web pages.
The build result will be located under the `build/` folder.

```console
$ virtualenv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ make
```
