'''
Adds additional location info to metadata. Adds "Washington State" to location for all Washington samples without a location.
Flags are:
    --metadata
    --additional
    --output
'''

import argparse
import pandas as pd

def load_metadata(file):
    '''
    Loads metadata tsv as df.
    '''
    with open(file) as tfile:
        metadata = pd.read_csv(tfile, sep = '\t', index_col='strain')
    return metadata

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Makes JSON of iSNVs",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument('--metadata', type=str, required=True, help = 'metadata tsv')
    parser.add_argument('--additional', type=str, required=True, help = 'tsv with more metadata to add')
    parser.add_argument('--output', type=str, required=True, help = 'location of output tsv')
    args = parser.parse_args()

    # Load all metadata to merge
    metadata = load_metadata(args.metadata)
    additional = load_metadata(args.additional)

    # Merge metadata
    new = metadata.combine_first(additional)
    new.loc[(new.division == 'Washington') & (new.location.isna()), 'location'] = 'Washington State'

    # Save final df
    with open(args.output, 'w') as f:
        new.to_csv(f, sep = '\t')
