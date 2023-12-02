from plotly.graph_objs import Bar,Layout
from plotly import offline
from die import Die
#create a d6
die=Die()
#make some roles and see result in a list
results=[]
for roll_num in range(1000):
	result=die.roll()
	results.append(result)
#analyze the result
frequencies=[]
for value in range(1,die.num_sides+1):
	frequency=results.count(value)
	frequencies.append(frequency)
#visualize the results
x_values=list(range(1,die.num_sides+1))
data=[Bar(x=x_values,y=frequencies)]
x_axis_config={'title':'result'}
y_axis_config={'title':'frequency of results'}
my_layout=Layout(title='result of rolling one D6 1000 times',xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({'data':data,'layout':my_layout},filename='d6.html')
