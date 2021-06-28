# About

This repository analyzes viral genomes from Washington State using [Nextstrain](https://nextstrain.org/).
This is a copy of the [original Nextstrain ncov](https://github.com/nextstrain/ncov/) repository that has been modified for Washington-specific builds.
These modifications draw heavily from work by John Huddleston in the [SPHERES augur build](https://github.com/nextstrain/spheres-augur-build).
The 1y, 4m, and 2m Washington builds are visible at: https://nextstrain.org/groups/blab/ncov/wa/1y, https://nextstrain.org/groups/blab/ncov/wa/4m, and https://nextstrain.org/groups/blab/ncov/wa/2m, respectively.

Trees are reconstructed from a set of focal sequences -- SARS-CoV-2 samples from Washington State collected during the past two months, four months, or year -- and contextual sequences -- other US and global SARS-CoV-2 samples chosen by genetic proximity to the focal dataset.
Contextual sequences can be selected from either two different datasets:
1. Sequences in [Nextstrain's North America SARS-CoV-2 build](https://nextstrain.org/ncov/north-america).
2. All sequences available on GISAID.

Trees built using either dataset reconstruct similar patterns of introductions and spread of SARS-CoV-2 in Washington State.
The location from which an introduction is inferred is more accurate with (2); however, using (2) requires downloading and aligning 1.7 million+ sequences from GISAID.
For most use cases, (1) is appropriate.

To run with (1), follow instructions for "Running with subsampled contextual dataset".
To run with (2), follow instructions for "Running with all GISAID contextual dataset".

# Installation

To run this workflow, the Nextstrain toolkit will need to be installed. To install it, please follow the instructions [here](https://docs.nextstrain.org/en/latest/install-nextstrain.html).

Clone this repository.
```
git clone https://github.com/blab/ncov-wa-build.git
cd ncov-wa-build/
```

# Running with subsampled contextual dataset

Download contextual sequences from [GISAID](https://www.gisaid.org/). You will require a GISAID login to do so.
1. Log into GISAID's EpiCoV site
2. Click "Downloads" to bring up a modal window
3. In this window go to "Genomic Epidemiology / nextregions" and click "North America". This will download `ncov_north-america.tar.gz`.
4. Move this file to the `data` directory.

Assemble Washington sequences. This can be done by filtering the entire FASTA & metadata files available from GISAID / EpiCoV / Downloads / Download packages to only Washington sequences. Alternatively, Washington sequences can be selected on GISAID using EpiCoV / Search. In the search box, set location to "North America / USA / Washington" and check the "low coverage excl" and "collection date compl" boxes. Then select sequences from the past four months and download them. Choose the "Input for augur build" option. You may need to download multiple selections of sequences as you can only download a maximum of 5,000 sequences at a time. Move downloaded tar files into `data` directory.

Currently, the workflow only expects one set of Washington metadata and sequences: `data/wa.metadata.tsv.xz` and `data/wa.sequences.fasta.xz`. You may need to update the inputs in `wa_profiles/wa-subsampled-background/subsampled-background-builds.yaml` to point to your focal Washington dataset. If metadata and sequences are bundled together in a single tar file, the input for both `metadata:` and `sequences:` can be that tar file. If you download multiple selections, you can add multiple Washington entries, e.g.
```
inputs:
  - name: washington1
    metadata: "data/wa1.tar.gz"
    sequences: "data/wa1.tar.gz"
  - name: washington2
    metadata: "data/wa2.tar.gz"
    sequences: "data/wa2.tar.gz"
  - name: contextual
    metadata: "data/ncov_north-america.tar.gz"
    sequences: "data/ncov_north-america.tar.gz"
```

Next, run the workflow on AWS using Nextstrain build using the below command from inside the `ncov-wa-build` folder. Update memory and CPUs as desired:
```
nextstrain build --detach --aws-batch --cpus 16 --memory 32gb . --profile wa_profiles/wa-subsampled-background/
```

# Running with all GISAID contextual dataset

## If running externally
Download sequences from [GISAID](https://www.gisaid.org/). You will require a GISAID login to do so.
1. Log into GISAID's EpiCoV site
2. Click "Downloads" to bring up a modal window
3. In this window, click "metadata" under "Download packages" to download the compressed metadata file. Please move this file to `data/metadata.tsv.tar.xz`. It does not need to be decompressed.
4. Then, in this window click on "FASTA" under "Download packages" to download the compressed sequences fasta. This should be decompressed and saved as `data/sequences.fasta.tar.xz`. It also does not need to be decompressed.

Run the workflow on AWS using Nextstrain build. Update memory and CPUs as desired:
```
nextstrain build --detach --aws-batch --cpus 16 --memory 32gb . --profile wa_profiles/wa-external/
```

## If Nextstrain team member
If running on Fred Hutch rhino cluster:
```
snakemake --profile wa_profiles/wa-rhino/
```

If running with AWS:
```
nextstrain build --detach --aws-batch --cpus 16 --memory 32gb . --profile wa_profiles/wa/
```
