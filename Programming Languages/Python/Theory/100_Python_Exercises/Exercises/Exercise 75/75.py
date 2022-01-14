#Plot the data in the file provided through the URL http://www.pythonhow.com/data/sampledata.txt
import pandas
import pylab as plt

data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data.plot(x='x', y='y', kind='scatter')
plt.show()

"""

from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

output_file("bokeh_plot.html")
data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
f = figure()
f.circle(x=data["x"], y=data["y"])

show(f)
"""
