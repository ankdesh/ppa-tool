import yaml
import os
from ppa_utils import verbose_print

def parseDB(filePath, verbose=1):
  ''' Parses Yaml file and returns dict 
      
      Args:
      filePath: Full path of DB File
      vebose: Verbosity level
      
      Return:
      dict of blocks and its parameters
  '''    
  assert os.path.exists(filePath), filePath + ' not found'
  
  ymlDict = yaml.load(open(filePath))
  
  # TODO Sanity Checks for Components
  
  verbose_print ('Parsed DB file: ' + filePath, verbose, 2)
  verbose_print ('Parse Dataset \n' + yaml.dump(ymlDict), verbose, 3)
      
  return ymlDict


if __name__=="__main__":
  parseDB('../sample_data/simple-1.yaml',verbose=3)

