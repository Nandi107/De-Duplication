import os
from DuplicateRemover import DuplicateRemover
def findandremoveduplicates(dirname):
    #dirname = dirname
    dr = DuplicateRemover(dirname)
    asd=os.listdir(dirname)
    for file in asd:
        if(file.endswith(('.jpg','.png','.jpeg'))):
            k=dr.find_similar(os.path.join(dirname,file),90)
            for i in k:
                os.remove(i)
                if i.split('\\')[-1] in asd:
                    asd.remove(i.split('\\')[-1])