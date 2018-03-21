
class Node:
  def __init__(nodeName, parent, children, value):

    assert type(chidren) is list, 'children should be a list'

    self.parent = parent
    self.children = children
    self.value = value
    
    
