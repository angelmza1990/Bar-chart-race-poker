import bar_chart_race as bcr
import pandas as pd


df = pd.read_csv("campeones.csv")
# replace empty values with 0
df.fillna(0.0, inplace=True)

# create the bar chart race
bcr.bar_chart_race(
    df=df.set_index('Fecha'),
    #steps_per_period=80,
    orientation='h',
    sort='desc',
    n_bars=20,
    fixed_order=False,
    filename='campeones.gif',
    fig_kwargs={'facecolor': '#F8FAFF'},
    bar_label_font={'size': 10},
    tick_label_font={'size': 8},
    bar_kwargs={'alpha': 0.7, 'lw': 0.5},
    title={'label': 'Campeones TatoPoker', 'size': 16, 'weight': 'bold', 'pad': 20}
)