
# coding: utf-8

# In[54]:


import pandas as pd
import sys
import numpy as np
import math


# In[112]:


def num_zoom(min_num,max_num,x,row):
    max_num = int(max_num)
    min_num = int(min_num)
    try:
        x = float(x)
    except:
        print(row)
    #x       = int(x)
    return (x - min_num)/(max_num - min_num)*1.0


# In[113]:


df = pd.DataFrame(pd.read_csv('data/train_1w.csv'))


# In[114]:


df = df.fillna('0')
#df = df.sample(frac=1)
#csv总行数
num = len(df) - 1


# In[128]:


def make_lst(file_path,start,end):
    with open(file_path, 'w') as f:
        for row in range(start,end):
            row_str     = str(row) + "\t" + str(4) + "\t" + str(5) + "\t" + str(1069) +"\t" + str(500) + "\t"
            coordinate  = str(df.iloc[row]['coordinate'])

            if ";" in coordinate:
                coordinates = coordinate.split(";")
                for val in coordinates:
                    if len(val) == 0:
                        continue
                    areas = val.split("_")
                    row_str += str(0) + "\t"
                    i = 0
                    for area in areas:
                        if  i % 2 == 0 :
                            row_str += str(num_zoom(0,1069,area,row)) + "\t"
                        else:
                            row_str += str(num_zoom(0,500,area,row)) + "\t"
                        i = i + 1
            elif coordinate:
                areas = coordinate.split("_")
                row_str += str(0) + "\t"
                i = 0
                for area in areas:
                    if i % 2 == 0 :
                        row_str += str(num_zoom(0,1069,area,row)) + "\t"
                    else:
                        row_str += str(num_zoom(0,500,area,row)) + "\t"
                    i = i + 1
            else:
                continue
            row_str += df.iloc[row]['name'] + "\r\n"
            f.write(row_str)
    f.close()


# In[129]:


make_lst('./image_val.lst',0,2000)


# In[130]:


make_lst('./image_train.lst',2000,num-2000)


# 

# In[ ]:




