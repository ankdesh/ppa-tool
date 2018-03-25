import argparse
from parse_db import parseDB
from parse_archdef import parseArchFile
from ppa_utils import verbose_print
import ppa_tree
import itertools

def getTopNumber(dbData, archDefData, topModule, verbose):
  ''' Returns the value requested for top level module
    
    Arguments:
    dbData = Database data in dict format
    archDefData = List of all Modules
    topModule = Name of top level module to be evaluated
    verbose = Verbosity level
  '''

  allModulesName = list(archDefData.keys())

  assert topModule in allModulesName, topModule + ' not in the Arch files'

  # Create Root node
  rootNode = ppa_tree.Node(topModule,False)

  # Queue to hold nodes non-leaf to be yet expanded in the tree
  qNameToNode = [(topModule, rootNode)]

  while qNameToNode:
    verbose_print ('Current Q status: ' + str(qNameToNode), verbose, 3)
    moduleName, moduleNode = qNameToNode.pop(0)
    verbose_print ('Processing Node: ' + moduleName, verbose,3)
    verbose_print ('Current Q status: ' + str(qNameToNode), verbose,3)
    for childName,childVal in archDefData[moduleName].items():
      
      if childName in list(dbData.keys()):
        childArea = dbData[childName]['Area']  # TODO Make it generic for power
        verbose_print(childName + ' is basicblock. Adding as child to ' + moduleName, verbose, 2)
        
        # Create node for basic block
        childNode = ppa_tree.Node(moduleName + '.' + childName, True, childArea, childVal)
        moduleNode.addChild(childNode)

      elif childName in list(archDefData.keys()):
        verbose_print(childName + ' is a Module. Adding as child to ' + moduleName, verbose, 2)
        
        # Create node for basic block
        childNode = ppa_tree.Node(childName, False, None, childVal)
        moduleNode.addChild(childNode)
        qNameToNode.append((childName, childNode))

  #Update all values
  rootNode.updateTreeValue()

  # Dump tree 
  if verbose == 2:
    rootNode.dumpGraphPng(topModule, full = 0)
  if verbose == 3:
    rootNode.dumpGraphPng(topModule, full = 1)

  return rootNode.value    

def driver():

  #Parse Arguments
  parser = argparse.ArgumentParser()
  parser.add_argument('-d', action='store', dest='dbFilename',
                    help='Database filepath')

  parser.add_argument('-a', action='append', dest='archdefFilename',
                      default=[], help='One or more name of the arch description file',
                      )

  parser.add_argument('-m', action='append', dest='topModules',
                      default=[], help='Modules for which area to be reported')
  parser.add_argument('-v', action='store', dest='verbosity', type=int, 
                      default=2, help='Verbosity levels 0=Errors only, 1=Warnings, 2=Info Level 1, 3=Info Level 2')

  args = parser.parse_args()

  assert args.dbFilename != None, 'Provide a dbFilename using -d param'
  assert args.archdefFilename != [], 'Provide atleast one arch def filename using -a param'
  assert args.topModules != [], 'Provide atleast one top level module using argument -m'

  # Parse DB file
  dbData = parseDB(args.dbFilename,verbose = args.verbosity)

  # Parse Arch Def files
  archDefData = {}
  for fileName in args.archdefFilename:
    archDefData.update(parseArchFile(fileName, verbose = args.verbosity))

  for module in args.topModules:
    topNum = getTopNumber(dbData, archDefData, module,args.verbosity)
    print ('Total Area for component module ' + module + ' = ' + str(topNum))


if __name__ == '__main__':
  driver()
