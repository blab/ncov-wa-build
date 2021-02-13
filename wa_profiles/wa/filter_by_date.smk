ruleorder: proximity_score_filtered > proximity_score

def _get_latest_date(wildcards):
    return config["builds"][wildcards.build_name]["latest_date"]

rule latest_date:
    message:
        """
        Filter alignment for proximity score to only sequences within latest date.
        """
    input:
        alignment = "results/filtered.fasta",
        metadata = config["metadata"]
    output:
        alignment = "results/{build_name}/filtered_by_date.fasta"
    log:
        "logs/latest_date_{build_name}.txt"
    params:
        max_date = _get_latest_date,
    conda: config["conda_environment"]
    shell:
        """
        augur filter \
        --sequences {input.alignment} \
        --metadata {input.metadata} \
        --max-date {params.max_date} \
        --output {output.alignment} 2>&1 | tee {log}
        """

def _get_filtered_by_date(wildcards):
    if wildcards.build_name == "wa_mar20-jun20" or wildcards.build_name == "wa_jul20-oct20":
        return "results/{build_name}/filtered_by_date.fasta"
    else:
        return "results/filtered.fasta"

rule proximity_score_filtered:
    message:
        """
        determine priority for inclusion in as phylogenetic context by
        genetic similiarity to sequences in focal set for build '{wildcards.build_name}'.
        """
    input:
        alignment = _get_filtered_by_date,
        #alignment = "results/filtered.fasta",
        metadata = config["metadata"],
        reference = config["files"]["reference"],
        focal_alignment = "results/{build_name}/sample-{focus}.fasta"
    output:
        priorities = "results/{build_name}/proximity_{focus}.tsv"
    log:
        "logs/subsampling_priorities_{build_name}_{focus}.txt"
    resources:
        mem_mb = 4000
    conda: config["conda_environment"]
    shell:
        """
        python3 scripts/priorities.py --alignment {input.alignment} \
            --metadata {input.metadata} \
            --reference {input.reference} \
            --focal-alignment {input.focal_alignment} \
            --output {output.priorities} 2>&1 | tee {log}
        """
