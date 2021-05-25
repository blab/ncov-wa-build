# About

This repository analyzes viral genomes from Washington State using [Nextstrain](https://nextstrain.org/). This is a copy of the [original Nextstrain ncov](https://github.com/nextstrain/ncov/) repository that has been modified for Washington-specific builds. These modifications draw heavily from work by John Huddleston in the [SPHERES augur build](https://github.com/nextstrain/spheres-augur-build).

# Usage
To run this workflow, the nextstrain toolkit will need to be installed. To install it, please follow the instructions [here](https://docs.nextstrain.org/en/latest/install-nextstrain.html).

Clone this repository.
```
git clone https://github.com/blab/ncov-wa-build.git
cd ncov-wa-build/
```

Modify build definitions, as needed, in `wa_profile/wa/builds.yaml`.

# If running externally

Download sequences from [GISAID](https://www.gisaid.org/). You will require a GISAID login to do so.
1. Log into GISAID's EpiCoV site
2. Click "Downloads" to bring up a modal window
3. In this window go to "Genomic Epidemiology / nextregions" and click "North America" this will download `ncov_north-america.tar.gz`. Decompress the tar file and and move the metadata file to `data/ncov_north-america.tsv` and move the sequences file to `data/ncov_north-america.fasta`. These sequences will serve as a the contextual dataset for the Washington sequences.
4. To download Washington sequences, go to "Genomic Epidemiology / Custom selection." Set location to "North America / USA / Washington" and check the "low coverage excl" and "collection date compl" boxes. Then select sequences from the past four months and download them. You may need to download multiple selections of sequences as you can only download a maximum of 5,000 sequences at a time using Custom selection. Decompress the tar file and move the metadata and sequences to the `data` folder. You will not need to remove the .xz compression from the files.

Currently, the workflow only expects one set of Washington metadata and sequences: `data/wa.metadata.tsv.xz` and `data/wa.sequences.fasta.xz`. If you download multiple selections, you will need to edit the inputs in `wa_profiles/wa-subsampled-background/subsampled-background-builds.yaml` to include all of your Washington sequence inputs.

To run the workflow on AWS using Nextstrain build, use the below command from inside the `ncov-wa-build` folder. Update memory and CPUs as you wish:
```
nextstrain build --detach --aws-batch --cpus 16 --memory 32gb . --profile wa_profiles/wa-subsampled-background/
```

# If Nextstrain team member
If running on Fred Hutch rhino cluster:
```
snakemake --profile wa_profiles/wa-rhino/
```

If running on aws-batch:
```
snakemake --profile wa_profiles/wa/
```
