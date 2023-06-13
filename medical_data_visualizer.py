import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = (df['weight']/(df['height']/100)**2)
df['overweight'] = np.where(df['overweight']>25,1,0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol']=np.where(df['cholesterol']>1,1,0)
df['gluc']=np.where(df['gluc']>1,1,0)
# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    
  
    df_cat = pd.melt(df, id_vars ='cardio',value_vars=['active','alco','cholesterol','gluc','overweight','smoke'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    
    

    # Draw the catplot with 'sns.catplot()'



    # Get the figure for the output
    sns.set_style("white")
    graph = sns.catplot(data=df_cat, x='variable', hue= 'value', kind='count', col='cardio',
                    aspect=2,palette='colorblind')
    graph.set(xlabel='variable', ylabel='total')
    fig = graph.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi'])
                           & (df['height'] >= (df['height'].quantile(0.025))) &
                           (df['height'] <= (df['height'].quantile(0.975))) &
                           (df['weight'] >= (df['weight'].quantile(0.025))) &
                           (df['weight'] <= (df['weight'].quantile(0.975)))]
    corr = df_heat.corr().round(1)

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(df.corr()))



    # Set up the matplotlib figure
    ticks = [-0.08,0.00,0.08,0.16,0.24]
    fig,ax = plt.subplots(1,1,figsize=(8,8))
    sns.set(font_scale=0.8)

    # Draw the heatmap with 'sns.heatmap()'
    
    sns.heatmap(corr,center = 0.0, vmax = 0.3, vmin= -0.15,
                  mask = mask, annot=True, square= True,robust =True, cbar_kws={'shrink':0.5, 'ticks': ticks},
                   linecolor= 'white',linewidths = 0.1 , annot_kws={'size': 10},ax=ax,fmt='.1f')



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
