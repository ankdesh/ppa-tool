from pprint import pprint, pformat
from ppa_utils import verbose_print

class Node:
  ''' Node represents a node in the expression tree for 
      recursively calculating top level Value
  '''
  
  def __init__(self, name, isLeaf, valuePerInstance = None, numInstances = None):

    ''' 
      Attributes:
      name : Name for the component
      children: list of children nodes
      if Leaf: Boolean to indicate if this is basic block node
      value: value of the parameter to be calculated
      valuePerInstance: Value of each instance of node (e.g. area of BB)
      numInstance: number of instances of the block
    '''

    self.name = name
    self.children = []
    self.isLeaf = isLeaf
    self.valuePerInstance = valuePerInstance
    self.numInstances = numInstances
    self.value = None

    if self.valuePerInstance != None and self.numInstances != None:
      self.value = self.valuePerInstance * self.numInstances


  def addChild(self, child):
    ''' Adds a single node a child
    '''
    
    assert type(child) is Node, 'Child should be a valid Node'
    assert not self.isLeaf, 'Attaching child to leaf node'
    self.children.append(child)


  def addChildren (self, children):
    ''' Adds a list of Nodes as children
    '''
    
    assert type(children) is list, 'children should be a list'
    assert not self.isLeaf, 'Attaching children to leaf node'
    self.children = self.children + children


  def updateTreeValue(self):
    ''' Traverse the tree in post order, 
        update the values for each node in tree
    '''
 
    #self.printNode() 
    for child in self.children:
      print ('>>' + child.name)
      child.updateTreeValue()
      
    childVals = [x.value for x in self.children]

    print ('>>>> ' + str(childVals))
    #for i, val in enumerate(childVals):
    #  assert val != None, self.children[i].name + ' not complete '

    self.value = sum(childVals)

  def printNode(self):
    ''' Prints the Node info with all attributes
    '''

    verbose_print (pformat(self.__dict__) + '\n', 2, 2)


  def printNodeName(self):
    ''' Prints the Node Name
    '''

    verbose_print (self.name, 2, 2)


  def printTreePreorder(self, full = 0):
    ''' Print entire tree rooted at this node
        in preorder fasion

        Args:
        full: 0 prints only node names
              1 prints full node info
    '''
   
    if full == 0: 
      self.printNodeName()
    else:
      self.printNode()

    for child in self.children:
      child.printTreePreorder(full)
    

if __name__ == "__main__":
  node0 = Node("Node0", False)
  node00 = Node("Node00", True, 2, 3)
  node01 = Node("Node01", False)
  node010 = Node("Node010", True, 4, 5)
  node011 = Node("Node011", True, 6, 7)

  node0.addChildren([node00, node01])
  node01.addChild(node010)
  node01.addChild(node011)

  #node0.printNodeName()

  node0.printTreePreorder(1)

  print ('Calulating Tree values...')
  node0.updateTreeValue()

  node0.printTreePreorder(1)
