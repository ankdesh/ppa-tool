from bokeh.models.widgets import Panel, Tabs
from bokeh.io import output_file, show
from bokeh.plotting import figure
import GraphViz, MultiLevelPerfViz, TimelineViz
import networkx as nx
import numpy as np
from bokeh.embed import file_html
from bokeh.resources import INLINE


G=nx.complete_graph(8)

# Tab 1 
plot = GraphViz.create(G, 'Complete Graph(8)', layout_prog='dot', tools="wheel_zoom,box_zoom,save,reset")
tab1 = Panel(child=plot, title="Graph")

# Tab 2
networks = ['VGG','Inception', 'Resnet']
confs = ['conf1','conf2','conf3','conf4','conf5','conf6','conf7']
data = np.random.randint(low = 1, high = 1000, size=(len(networks), len(confs)))
plot = MultiLevelPerfViz.create(networks, confs, data, "Perf. for multiple runs", "Cycles(in Millions)",
                                          tools= "wheel_zoom,box_zoom,save,reset")
tab2 = Panel(child=plot, title="MultiLevel")

# Tab3
listEvntsName = ['EvntType1', 'EvntType2', 'EvnType3']
x = np.linspace(1,9,9,dtype='int')
evntStartTime = np.array([x**2, x**2 + 2, x**2 + 5])
evntEndTime = evntStartTime + np.random.randint(1,5,(3,9))

plot = TimelineViz.create(listEvntsName, evntStartTime, evntEndTime, 'TimelineViz')
tab3 = Panel(child=plot, title="Timeline")

tabs = Tabs(tabs=[ tab1, tab2, tab3 ])

html = file_html(tabs, INLINE, "TimelinePlot").encode('utf-8').strip()

with open('multipleTabs.html','wb') as f:
    f.write(html)
