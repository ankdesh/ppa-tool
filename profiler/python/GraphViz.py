import networkx as nx

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval, Rect
from bokeh.palettes import viridis

def create(G, title, plot_height=500, layout_prog='dot', tools=None, colorPallete=None):
    '''Creates bokeh figure for Graph with given nodes and attributes
    G = networkX graph
    title = Graph Title
    plot_height = height of plot (default = 500)
    layout_prog = Layout program from Graphviz (default = dot)
    tools = Set of tools to display along with plot (Defalt = All Bokeh tools)
    colorPallette = a list of colors to use for Nodes (Default = sample from viridis)'''

    #Nodes and edges
    node_indices = list(G.nodes)
    edge_start = [x[0] for x in G.edges]
    edge_end = [x[1] for x in G.edges]
    
    #Assign location using layout program
    pos = nx.nx_pydot.graphviz_layout(G, prog=layout_prog)
    x_coords = [x[0] for x in pos.values()]
    y_coords = [x[1] for x in pos.values()]
  
    plot = figure(title="Graph Layout Demonstration", 
              x_range=(min(x_coords)-10,max(x_coords)+10), y_range=(min(y_coords)-10,max(y_coords)+10),
              tools=tools, plot_height=plot_height)

    graph = GraphRenderer()

    graph.node_renderer.data_source.data = dict(
        index=node_indices,
        fill_color = viridis(len(node_indices)))
    graph.node_renderer.glyph = Rect(height=10, width=10, fill_color="fill_color")

    graph.edge_renderer.data_source.data = dict(
        start=edge_start,
        end=edge_end)

    graph_layout = pos
    graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)
    
    plot.renderers.append(graph)
    
    return plot

if __name__=='__main__':
    output_file('testGraphViz.html', title = 'GraphViz', mode = 'inline')
    
    G=nx.complete_graph(8)

    plot = create(G, 'Complete Graph(8)', layout_prog='dot', tools="wheel_zoom,box_zoom,save,reset")

    show(plot)
