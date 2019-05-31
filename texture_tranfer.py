#everything is ok

import os
import shutil
import maya.cmds as cmds

class Active(object):
    def __init__(self):
        self.newPath = cmds.workspace (q =True ,rd=True )+ cmds.workspace (fileRuleEntry="sourceImages")

    def set_file(self):
        fileNameList = []        
        fileList = cmds.ls(type = "file")
        print fileList
        #fileList = cmds.ls(selection = True) 
        for files in fileList :
            filePath = cmds.getAttr(files +".fileTextureName")  
            fileName = os.path.basename(filePath)
            
            fileNameList.append(fileName)
 
        for i,fnl in enumerate(fileNameList,1):
            print (i,fnl)


    def copyfile_to_newpath(self):
        fileList = cmds.ls(type = "file")        
        
        for files in fileList :
            filePath = cmds.getAttr(files +".fileTextureName")  

            if filePath == self.newPath +'/'+ os.path.basename(filePath):
                print os.path.basename(filePath) + "  is same"
                continue

            shutil.copy(filePath,self.newPath)
            print "copy file ::"+ os.path.basename(filePath)

          
    def connected(self):
        fileList = cmds.ls(type = "file")
        for files in fileList :
            filePath = cmds.getAttr(files +".fileTextureName")   
            fileName= os.path.basename(filePath)
            FinalPath= os.path.join(self.newPath,fileName)
            cmds.setAttr((files +".fileTextureName"), FinalPath,type="string")
    
#inpath =C:/Users/pouse.napat/Documents/27_05_2019/OLD/sourceImages/pattern-512.png
#os.path.basename(inpath)= pattern-512.png 
#os.path.dirname(inpath) = C:/Users/pouse.napat/Documents/27_05_2019/OLD/sourceImages
#       