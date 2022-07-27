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

def makeExtensionMap(dir):
   retMap = {'noext':[]}
   extList = []

   #omit diretories
   file_list = [f for f in os.listdir(dir) if os.path.isfile(f)]

   # Populate the extension map
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
            
def main():
   ext_map = {}

   # Get the list of extensions in the current directory
   dir = os.getcwd()
   ext_map = makeExtensionMap(dir) 

   # Walk over the extension map to create the diretory 
   createDirs(dir, list(ext_map.keys()))

   # Move the files to respective directories
   moveFiles(dir, ext_map)

if __name__=="__main__":
    main()