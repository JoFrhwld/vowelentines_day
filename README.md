# Vowelentine's Day

This will hopefully be a shiny app that will MFA align and FAVE-extract vowels for an interactive "Vowelentines Day" event.

## Setup


1. Clone this repository, or create a new RStudio project from "Version control" and paste the git repo url in.
2.  Miniconda must be installed (<https://docs.conda.io/en/latest/miniconda.html>)

    -   I *highly* recommend running `conda config --set auto_activate_base false` after installation.

3. In the R console, run `renv::restore()`and anwer yes to all questions

### Setup Fallback

If the steps above dont work, especially if you get errors about architecture (`incompatible architecture (have 'arm64', need 'x86_64'))`)
try the following:

1. Delete the `renv/` directory and the `renv.lock` and `environment.yml` files.
2. Restart R (it will print a warning about there being no `renv/activate.R` file)
3. Run `config.R`

## Use

Open the `index.qmd` file, and click "Run Document"
