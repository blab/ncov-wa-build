# About

This repository analyzes viral genomes from Washington State using [Nextstrain](https://nextstrain.org/). This is a copy of the [original Nextstrain ncov](https://github.com/nextstrain/ncov/) repository that has been modified for Washington-specific builds. These modifications draw heavily from work by John Huddleston in the [SPHERES augur build](https://github.com/nextstrain/spheres-augur-build).

# Usage
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
3. In this window click on "nextmeta" to download the file nextstrain_metadata.tsv.bz2. This should be decompressed and saved as data/metadata.tsv.
4. Then, in this window click on "nextfasta" to download the file nextstrain_sequences.fasta.bz2. This should be decompressed and saved as data/sequences.fasta.
For more details, see "Contextualizing your data" at [this guide](https://nextstrain.github.io/ncov/data-prep).

Run the workflow:
```
snakemake --profile wa_profiles/wa-external/
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
