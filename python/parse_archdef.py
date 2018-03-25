import yaml
import os
from ppa_utils import verbose_print

def parseArchFile(filePath, verbose=1):
  ''' Parses Yaml file and returns component list 
      
      Args:
      filePath: Full path of Arch File
      vebose: Verbosity level
      
      Return:
      dict of Components and its Basic block conf 
  '''    
  assert os.path.exists(filePath), filePath + 'does not exist'

  archMap = yaml.load(open(filePath))
  
  # TODO Sanity Checks for Components
  
  verbose_print ('Parsed Arch file: ' + filePath, verbose, 2)
  verbose_print (yaml.dump(archMap), verbose, 3)
      
  return archMap

if __name__=="__main__":
  parseArchFile('../sample_data/simple-arch.yaml',verbose=3)
