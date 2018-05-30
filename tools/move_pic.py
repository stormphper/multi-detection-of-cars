
# coding: utf-8

# In[2]:


import os
import shutil


# In[3]:


if not os.path.exists("validation"):
    os.mkdir("validation")


# In[4]:


if not os.path.exists("training"):
    os.mkdir("training")


# In[6]:


if not os.path.exists("image_val.lst"):
    print ("not has image_val.lst")
    exit()


# In[7]:


if not os.path.exists("image_train.lst"):
    print("not has image_train.lst")
    exit()


# In[14]:


for line in open("image_val.lst"):  
    line = line.split("\t")
    line_len = len(line)
    image_path = line[line_len - 1]
    image_path = image_path.strip()
    
    old_image = "./train/" + image_path
    
    if not os.path.exists(old_image):
        print (old_image)
        continue
    new_image = './validation/' + image_path
    shutil.copyfile(old_image,new_image)
    
    


# In[15]:


for line in open("image_train.lst"):  
    line = line.split("\t")
    line_len = len(line)
    image_path = line[line_len - 1]
    image_path = image_path.strip()
    
    old_image = "./train/" + image_path
    
    if not os.path.exists(old_image):
        print (old_image)
        continue
    new_image = './training/' + image_path
    shutil.copyfile(old_image,new_image)


# In[ ]:




