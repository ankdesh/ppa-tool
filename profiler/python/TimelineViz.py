import numpy as np

from bokeh.models import ColumnDataSource, DataRange1d, Plot, LinearAxis, Grid, Legend
from bokeh.plotting import figure
from bokeh.models.glyphs import Quad
from bokeh.io import curdoc, show, output_file
from bokeh.models.ranges import FactorRange
from bokeh.palettes import viridis

def create(listEvntsName, evntStartTime, evntEndTime, title, plot_height=100, plot_width = 900,
                      tools=None, colorPallete=None):
    ''' Creates Timeline Visualization '''
    
    numEvnts = len(listEvntsName)
    
    if colorPallete == None:
        colorPallete = viridis(numEvnts)
    
    assert numEvnts == len(evntStartTime), 'Num of events do not match'
    assert numEvnts == len(evntEndTime), 'Num of events do not match'
    

    xdr = DataRange1d()
    ydr = DataRange1d()
    
    plot = figure(title=title, x_range=xdr, y_range=ydr, plot_width=plot_width, plot_height=plot_height,
                  h_symmetry=False, v_symmetry=False, min_border=0)
    
    glyphs = []
    for i in range(numEvnts):
        source = ColumnDataSource(dict(
            left=evntStartTime[i],
            right=evntEndTime[i],
            top = [i+1] * len(evntStartTime[i]),
            bottom = [i] * len(evntStartTime[i])
        ))
        
        glyph = plot.quad(left="left", right="right", top="top", bottom="bottom",fill_color=colorPallete[i],
                          source=source)
        glyphs.append(glyph)
    
    legend_items = [(listEvntsName[i],[glyphs[i]]) for i in range(numEvnts)]
    legend = Legend(items=legend_items, location=(30, 0))
   
    plot.add_layout(legend, 'right')
    xaxis = LinearAxis() 
    plot.add_layout(Grid(dimension=0, ticker=xaxis.ticker))
    
    return plot


if __name__=='__main__':
    output_file('testTimelineViz.html', title = 'TimelineViz', mode = 'inline')

    #Generate events
    listEvntsName = ['EvntType1', 'EvntType2', 'EvnType3']
    x = np.linspace(1,9,9,dtype='int')
    evntStartTime = np.array([x**2, x**2 + 2, x**2 + 5])
    evntEndTime = evntStartTime + np.random.randint(1,5,(3,9))
    
    plot = create(listEvntsName, evntStartTime, evntEndTime, 'TimelineViz')
    show(plot)
