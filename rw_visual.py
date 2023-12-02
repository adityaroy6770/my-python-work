import matplotlib.pyplot as plt
from random_walk import RandomWalk
#make a random walk
while True:
	
    rw=RandomWalk(50000)
    rw.fill_walk()
#plot the points in the walk
    plt.style.use('classic')
    fig,ax=plt.subplots(figsize=(15,9),dpi=128)
    point_numbers=range(rw.num_points)
    ax.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=1)
    ax.scatter(rw.x_values,rw.y_values,s=15)
    #emphasize the first and last points
    ax.scatter(0,0,c='green',edgecolor='none',s=100)
    ax.scatter(rw.x_values[-1],rw.y_values[-1],c='Red',edgecolor='none',s=100)
    #cleaning up the axis
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    plt.show()
    keep_running=input("make another walk? (yes/no)")
    if keep_running=='no':
	    break
