# Vowelentine's Day

This will hopefully be a shiny app that will MFA align and FAVE-extract vowels for an interactive "Vowelentines Day" event.

## Setup

Ideally this will be a turn key operation. For now

1.  Miniconda must be installed (<https://docs.conda.io/en/latest/miniconda.html>)

    -   I *highly* recommend running `conda config --set auto_activate_base false` after installation.

2.  The x86_64 version of R must be installed

3.  Create a new RStudio project from Version Control

4.  Delete the `renv.lock` file

5.  Run `renv::init()`

6.  Run `renv::install("reticulate")`

7.  In the terminal, run

    ``` bash
    CONDA_SUBDIR=osx-64 conda create -p ./renv/python/condaenvs/renv-python montreal-forced-aligner -c conda-forge
    ```

8.  Run the remainder of `config.R`

## Use

Open the `index.qmd` file, and click "Run Document"