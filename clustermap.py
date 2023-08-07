import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Patch

# heatmap1_df = pd.read_excel("NISAR.xlsx", sheet_name = "Heatmap_1")

# DD_df = pd.read_excel("NISAR.xlsx", sheet_name = "DD")

# heatmap_DD_df = heatmap1_df.merge(DD_df, how = "inner", left_on = " S189_3275_uudd_dd", right_on = "Phosphosite" )

# heatmap_DD_df.to_csv("df2.csv")

# df1 = pd.read_csv("df1.csv")
# df2 = pd.read_csv("df2.csv")

# df = df1._append(df2)

# df.to_csv("final_heatmap1.csv")

def do(x):
    if 'Up' in x:
        return 1
    elif 'down' in x:
        return -1
    else:
        return 0

df = pd.read_excel('_CDK12_cutoff_expression.xlsx')

df["exp_val"] = df["expression"].apply(do)

pivot_table = pd.pivot_table(df, values = 'exp_val', index = 'exp_condition', columns = 'proteins', fill_value = 0)

size = (0.5*len(pivot_table.columns), 0.3*len(pivot_table.index))

cbar_ticks = [-1, 0, 1]

cluster_map = sns.clustermap(pivot_table, yticklabels=True, xticklabels = True, cmap = ['#00FF00', '#000000', '#FF0000'],figsize = size, cbar_kws={"ticks": cbar_ticks},cbar_pos=None)

# cluster_map.cax.set_visible(False)

cluster_map.ax_heatmap.set_xticklabels(cluster_map.ax_heatmap.get_xticklabels(), fontsize=13)

cluster_map.ax_heatmap.set_yticklabels(cluster_map.ax_heatmap.get_yticklabels(), fontsize=13)

legend_patches = [Patch(facecolor='#FF0000', label='up-regulation'),
                  Patch(facecolor='#000000', label='no-expression'),
                  Patch(facecolor='#00FF00', label='down-regulation')
                  ]

# plt.legend(handles=legend_patches, loc='upper left')

plt.legend(handles=legend_patches, title='Expressions', bbox_to_anchor=(0, 0.97), bbox_transform=plt.gcf().transFigure, loc='upper left', fontsize=23, title_fontsize=24)

plt.savefig("HeatMap1.png")


   
  
   
   
