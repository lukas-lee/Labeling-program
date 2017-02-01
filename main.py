import os, sys
import shutil
import numpy as np
import tarfile
from PIL import Image

import scipy.io
#

def split_valid():
    valid_file = open('valid_list.txt','w')
    with open('train_list.txt','r+') as f:
        train_list = f.readlines()
        print(len(train_list))


        with open('target_list_n.txt','r') as f:
            target_list = f.readlines()
            
        
            with open('newfile.txt','w') as f:    
               

                for i in range( len(train_list)):
                    for j in range(len(target_list)):  
                         if (train_list[i][1:9] == target_list[j].split('n')[1][0:9][0:-1]):    #01440764
                                
                            data=target_list[j].split('n')[0]
                            f.write(train_list[i].split(' ')[0])
                            f.write(' ')
                            f.write(data) 
                            f.write('\n')
                            
split_valid()



