# OpenNightLights
Collection of open tools and training materials for using Nighttime Lights in high resolution measures of sustainable development


# setup for using tutorial
this tutorial uses conda package manager
1. make sure conda is installed on your machine
2. clone this repo
3. from root directory of this repo (i.e. where this file is located),
create conda env using the existing `environment.yml` file,
from CLI: `conda env create --prefix ./venv -f environment.yml`



# for building and maintaining the site using Jupyter book:
- Make sure `onl/_config.yml` and `onl/_toc.yml` are updated to include all
files being published

To build from root directory:
`jupyter-book build onl`

You can view this build locally (it is not yet published) by opening `./_build/html/index.html`
in your browser. Execute `jupyter-book build onl` to refresh.

To publish book to Github pages or to update the published content, (from root directory):
`ghp-import -n -p -f onl/_build/html`

This will push content to the live link at: https://worldbank.github.io/OpenNightLights/welcome.html

Shield: [![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg