# About

This repository analyzes viral genomes from Washington State using [Nextstrain](https://nextstrain.org/). This is a copy of the [original Nextstrain ncov](https://github.com/nextstrain/ncov/) repository that has been modified for Washington-specific builds. These modifications draw heavily from work by John Huddleston in the [SPHERES augur build](https://github.com/nextstrain/spheres-augur-build).

# Usage
Clone this repository.
`git clone https://github.com/blab/ncov-wa-build.git
cd ncov-wa-build/`

Modify build definitions, as needed, in `wa_profile/builds.yaml`. Run the workflow.
`snakemake --profile wa_profile/`

View the resulting builds with auspice from a local machine.
`auspice view`
