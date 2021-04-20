# Based on script by Trevor Bedford in Seattle Flu Augur build: https://github.com/seattleflu/augur-build/blob/master/scripts/generate_coloring_tsne.py

import argparse
import pandas as pd
from sklearn.manifold import TSNE

def mapping(coor, label):
    #creates dictionary mapping of lat/long based on a label (i.e region, country, etc.)
    cfile = pd.read_csv(coor, header = None, sep = '\t')
    location_dict = {}
    for row in cfile.index:
        if cfile.iloc[row,0] == label:
            location_dict[cfile.iloc[row,1]] = {'latitude': cfile.iloc[row,2], 'longitude': cfile.iloc[row,3]}

    location_df = pd.DataFrame.from_dict(location_dict, orient = 'index')
    location_df.index.name = label
    lat_long_df = location_df.values[:,0:2]
    return lat_long_df, location_df

def tsne_ranking(lat_long_df, location_df, label):
    #creates a ranking of t-SNE
    lat_long_transformed = TSNE(n_components=1).fit_transform(lat_long_df)
    lat_long_transformed_df = pd.DataFrame(lat_long_transformed, columns=['1d_loc'])
    lat_long_transformed_df[label] = location_df.index
    lat_long_transformed_df["rank"] = lat_long_transformed_df['1d_loc'].rank()
    lat_long_sorted = lat_long_transformed_df.sort_values(by ="rank")
    return lat_long_sorted

def color_assignment(lat_long_sorted, output_fname, label):
    #Evenly assigns a color on the Nextstrain 36 color scale
    color_scale = ["#511EA8", "#4928B4", "#4334BF", "#4041C7", "#3F50CC", "#3F5ED0", "#416CCE", "#4379CD", "#4784C7", "#4B8FC1", "#5098B9", "#56A0AF", "#5CA7A4", "#63AC99", "#6BB18E", "#73B583", "#7CB878", "#86BB6E", "#90BC65", "#9ABD5C", "#A4BE56", "#AFBD4F", "#B9BC4A", "#C2BA46", "#CCB742", "#D3B240", "#DAAC3D", "#DFA43B", "#E39B39", "#E68F36", "#E68234", "#E67431", "#E4632E", "#E1512A", "#DF4027", "#DC2F24"]
    counter = 0
    if len(lat_long_sorted['rank']) >= 36:
        jump = 1
    else:
        jump = 36/len(lat_long_sorted['rank'])
    color_boundary = lat_long_sorted['rank'].max()/36
    for index, row in lat_long_sorted.iterrows():
        if int(row['rank']%color_boundary) != 0:
            lat_long_sorted.loc[index,'color'] = color_scale[int(counter)]
        elif int(row['rank']%color_boundary) == 0:
            lat_long_sorted.loc[index,'color'] = color_scale[int(counter)]
            counter = counter + jump
            print(counter)

    #subsets dataframe to only include location and color and prints to tsv
    lat_long_sorted['geo'] = 'location'
    final_colors_df = lat_long_sorted[['geo', label, 'color']]
    final_colors_df.to_csv(output_fname, sep='\t', index = False, mode = 'a', header = False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Assigns coloring for census tract using 1D- t-SNE",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument('--coordinates', type=str, required=True, help="tsv file containing lat/long coordinates and cooresponding region")
    parser.add_argument('--label', type=str, required=True, help= "geographic entity of interest like region, country or location")
    parser.add_argument('--output', type=str, required=True, help="name of output file for colors.tsv")

    args = parser.parse_args()

#makes Dataframe mapping of lat_longs file
coor_mapping, original_df = mapping(args.coordinates, args.label)

#runs PCA on lat/long and order ranks PC1
tsne_rank = tsne_ranking(coor_mapping, original_df, args.label)

#equally distributes colors among the census tracks and outputs a color TSV file
color_assignment(tsne_rank, args.output, args.label)
