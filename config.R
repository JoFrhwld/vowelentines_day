renv::install("reticulate")
# per https://github.com/rstudio/renv/issues/993

reticulate::conda_create(
   envname="./renv/python/condaenvs/renv-python",
   packages = "montreal-forced-aligner"
   )

reticulate::use_condaenv(
  "./renv/python/condaenvs/renv-python", 
  required = TRUE
)

renv::use_python(
  python=reticulate::py_discover_config()$python, 
  type="conda"
)

# add git version manually
reticulate::py_install(
  "git+https://github.com/JoFrhwld/FAVE@feature/parselmouth-fix",
  pip = T
  )

## Update fave in environment.yml manually
renv::snapshot()
