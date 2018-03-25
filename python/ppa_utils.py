def verbose_print (string, verbose_level=2, verbose_setting=2):
  ''' Print the string with formatting if verbose_level
  is more than the verbose_setting assigned to the statement
  Lower the verbose_setting, 
      Args:
      string: the string to be printed
      verbose_level: current verbose level requested
      verbose_setting: Fixed verbosity level of the statement
  '''
  if verbose_level >= verbose_setting:
    if verbose_setting == 0:
        print ('\033[91m [ERROR]: ' + string + '\033[0m') # Always printed 
    elif verbose_setting == 1: 
        print ('\033[93m [WARNING]: ' + string + '\033[0m') # verbosity_level should be atleast 1
    elif verbose_setting == 2:
        print ('\033[92m [INFO]: ' + string + '\033[0m') # verbosity_level should be atleast 2
    else: 
          print ('\033[94m [INFO]: ' + string + '\033[0m') # helps to print extremly verbose info
