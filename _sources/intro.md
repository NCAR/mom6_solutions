# Welcome to the OMWG diagnostics

Collection of notebooks and scripts used to diagnose MOM6 solutions conducted with CESM.

## Creating diagnostics for a single simulation

```
create_cesm_diagnostic.py -h

usage: create_cesm_diagnostic.py [-h] [--cimeroot CIMEROOT] [-sd START_DATE] [-ed END_DATE] [-p PROJ_CODE] [-ce CONDA_ENV] [-cl CLUSTER] [-debug]
                                 caseroot shortname

Create a new case to be processed using mom6_tools.

positional arguments:
  caseroot              Path to the CASEROOT
  shortname             A short name descring the experiment

optional arguments:
  -h, --help            show this help message and exit
  --cimeroot CIMEROOT   Path to the CIME root used in this experiment. Default is /glade/work/gmarques/cesm.sandboxes/cesm2_3_beta08/cime/
  -sd START_DATE, --start_date START_DATE
                        Start year to compute averages. Default 0038-01-01
  -ed END_DATE, --end_date END_DATE
                        End year to compute averages. Default 0059-01-01
  -p PROJ_CODE, --proj_code PROJ_CODE
                        Project code. Default NCGD0011
  -ce CONDA_ENV, --conda_env CONDA_ENV
                        Conda env to be used for running the scripts. Default dev2
  -cl CLUSTER, --cluster CLUSTER
                        Name of the cluster to run the scripts via batch jobs. Default casper, but cheyenne is also supported.
  -debug                Add priting statements for debugging purposes
```

Example:
```
create_cesm_diagnostic.py path-to-caseroot ctrl_zstar --cimeroot path-to-cimeroot -sd 0031-01-01 -ed 0061-12-31 -ce dev2 -cl casper
```

## Creating diagnostics for multiple simulations

**TODO**

The current approach is to create file **diag_config.yml** by hand. Please check file [diag_config.yml](https://github.com/NCAR/mom6_solutions/blob/main/diag_config.yml) contained in this repository as an example.

## Building a Jupyter Book

```
jb build notebooks
```

### Contributing

Would you like to include a new diagnostic? If so, here clone this repository, create your own branch

"git checkout -b name_of_your_branch",

then send us pull request.


```{tableofcontents}
```
