from PIL import Image
import imagehash
import os
import numpy as np

class DuplicateRemover:
    def __init__(self,dirname,hash_size = 8):
        self.dirname = dirname
        self.hash_size = hash_size
            
    def find_similar(self,location,similarity=80):
        dup=[]
        fnames = os.listdir(self.dirname)
        fnames.remove(location.split('\\')[-1])
        for file in fnames:
            if(not(file.endswith(('.jpg','.png','.jpeg')))):
                fnames.remove(file)
        print(fnames)
        threshold = 1 - similarity/100
        diff_limit = int(threshold*(self.hash_size**2))
        with Image.open(location) as img:
            hash1 = imagehash.average_hash(img, self.hash_size).hash
        
        # print("Finding Similar Images to {} Now!\n".format(location))
        for image in fnames:
            with Image.open(os.path.join(self.dirname,image)) as img:
                hash2 = imagehash.average_hash(img, self.hash_size).hash
                
                if np.count_nonzero(hash1 != hash2) <= diff_limit:
                    dup.append(os.path.join(self.dirname,image))
        return dup
                    
                    
                    
                
        
            
