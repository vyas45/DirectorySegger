'''
This script is going to run every once a while and seggregate the files
based on extension
.pdf -> ./pdfs/
.xxx -> ./xxx/

Todo:
====
1. Start with current directory
2. Add option for a specific directory
'''
import os
import shutil
import argparse

# Setup the class to handle the metadata for the utility
class DirSegger:
    def __init__(self, dir_name):
        self.dir = dir_name

def makeExtensionMap(dir):
   retMap = {'noext':[]}
   extList = []

   #omit diretories
   file_list = [f for f in os.listdir(dir) if os.path.isfile(dir + "/" + f)]
   print(file_list)

   # Populate the extension map
   # TODO: Find a better way to get extension on files
   for file in file_list:
      ext_split = file.split(".")
      # Add to the noext direcory
      if (len(ext_split) < 2):
          retMap['noext'].append(file)
          continue
      ext = ext_split[1]
      if ext in retMap:
          retMap[ext].append(file)
      else:
          retMap[ext] = [file]
    
   return (retMap)

# Create directory at path if not there already
def createDirs(path, dir_list):
    for name in dir_list:
        fqn = path + "/" + name
        if not os.path.isdir(fqn):
            os.mkdir(fqn)

# Move the files to the respective directories
def moveFiles(path, ext_map):
    for (dir_name, files) in ext_map.items():
        target_dir = str(path) + "/" + str(dir_name)
        # Move the files to the target dir
        for file in files:
            src = str(path) + "/" + str(file)
            dest = str(target_dir) + "/" + str(file)
            print(src, dest)
            shutil.move(src, dest)
            
def main(dir):
   ext_map = {}

   # Get the list of extensions in the current directory
   #dir = os.getcwd()
   print("Dir is : ", dir)
   ext_map = makeExtensionMap(dir) 

   print(ext_map)
   
   # Walk over the extension map to create the diretory 
   createDirs(dir, list(ext_map.keys()))

   # Move the files to respective directories
   moveFiles(dir, ext_map)

# Handle the init stuff
def init():
    parser = argparse.ArgumentParser( description='Descirbes the options for DirectorySegger')
    parser.add_argument("--dir", type=str, required=False, help='The directory which is getting cleaned')
    args = parser.parse_args()

    if args.dir:
        dir_name = args.dir
    else:
        dir_name = os.getcwd() 

    # Setup the class object
    dirSeg = DirSegger(dir_name)        
    return (dirSeg)

if __name__=="__main__":
    dirSeg = init()
    main(dirSeg.dir)