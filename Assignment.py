import pandas as pd
import matplotlib as mt
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
import random

"""Provisional TB notifications by month or quarter

scale all plot figures
"""

mt.rc('figure', figsize=(20,10))

"""read the csv data and display parts"""

"""read the csv and display stats"""
pd.read_csv("TB_provisional_notifications_2023-03-02.csv")

"""assign the data to a pd.Dataframe variable df being a convenient naming convention"""
df=pd.read_csv("TB_provisional_notifications_2023-03-02.csv")

"""a statistical summary"""

"""summary statistics that give  a bigger picture of the data"""
df.describe()

"""line skew """
def skew():
    return np.random.randint(-100000,200,348)

def mline_arrays():
    """this function gives y axis and legend list of the multiline plot of monthly reports plotted against country index"""
    
    ylist=[]
    lblist=[]
    lup=1
    while (lup < 5 ):
        ylist.append(skew().astype(float)+(df[(f'm_0{lup}')].fillna(3000).to_numpy()))
        lblist.append(f'm_0{lup}')
        lup+=1
    """ while (lup < 13 ):
        ylist.append(skew().astype(float)+(df[(f'm_{lup}')].fillna(3000).to_numpy()))
        lblist.append(f'm_{lup}')
        lup+=1 """
    return (ylist),lblist
#mline_arrays()

"""a multiline chart

*   readabilty
*   variance


"""

#call y axis multi line functions
"""plotting the multi line function """
ylst,lblst=mline_arrays()
for m in range(0,(len(ylst))):
   plt.plot([x for x in range(0,348)], ylst[m], label=lblst[m] )
plt.legend()
plt.ylabel('provisional notifications')
plt.xlabel("country indices")
plt.title('tb provisional notifs multi_line')
plt.show()

"""a bar chart showing summations in quaters"""

x = ['q_1', 'q_2', 'q_3', 'q_4']
y = [np.sum(df[x[m]].fillna(0).to_numpy()) for m in range(0,4)]


# Create a bar chart with a custom color scheme
plt.bar(x, y, color=['#4C72B0', '#55A868', '#C44E52', '#8172B2'])

# Add labels and title
plt.xlabel('quarters')
plt.ylabel('report numbers')
plt.title('Bar Chart')

for i in range(len(x)):
    plt.text(i, y[i]+1, y[i], ha='center')

# Display the plot
plt.show()

"""concentric pie chart"""

"""comparing provisional notifications in the quaters vs the years"""
outer_labels = lblst
outer_sizes = [np.sum(df[lblst[m]].fillna(0).to_numpy()) for m in range(0,len(lblst))]
inner_labels = ['q_1', 'q_2', 'q_3', 'q_4']
inner_sizes = [np.sum(df[inner_labels[e]].fillna(0).to_numpy()) for e in range(0,4)]

# Create the outer pie chart
fig, ax = plt.subplots()
ax.pie(outer_sizes, labels=outer_labels, startangle=90, counterclock=False, wedgeprops=dict(width=0.4))
# Create the inner pie chart
ax.pie(inner_sizes,labels=inner_labels, radius=0.7, startangle=90, counterclock=False, wedgeprops=dict(width=0.4))
circle = plt.Circle((0, 0), 0.3, color='white')
ax.add_artist(circle)

# Add a title
plt.title('quater reports vs months')

# Display the plot
plt.show()