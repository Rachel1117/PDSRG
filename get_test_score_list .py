import os
import numpy as np
import pandas as pd

os.getcwd() 
def Get_Test_Score_List (FDD,DD_mat,i):
  drug_num = FDD.shape[0]
  n_pos = 0
  list_pos = 0
  attr_pos1= 0
  n_pos=0
  pd.options.display.float_format = lambda x : '{:.0f}'.format(x) if round(x,0) == x else '{:,.10f}'.format(x)
  attr0=pd.DataFrame(np.zeros(shape=(int(drug_num*(drug_num-1)/2),1))) 
  for m in range(1,drug_num) :
    for n in range(m) :
      attr0.loc[n_pos,0] = FDD[m,n]
      n_pos = n_pos + 1
  attr1=pd.DataFrame(np.zeros(shape=(int(drug_num*(drug_num-1)/2),2))) 
  for m in range(1,drug_num+1) :
    for n in range(0,m-1) :
      attr1.loc[attr_pos1,0] = int(m-1)
      attr1.loc[attr_pos1,1] = int(n)
      attr_pos1 = attr_pos1+1
  attr2=pd.DataFrame(np.zeros(shape=(int(drug_num*(drug_num-1)/2),1))) 
  for m in range(1,drug_num) :
    for n in range(m) :
      attr2.loc[list_pos,0] = DD_mat[m,n]
      list_pos = list_pos + 1
  attr=pd.concat([attr0,attr1,attr2],axis=1,ignore_index=True)
  attr=attr.rename(columns = {0:'prob',1:'r',2:'c',3:'obs'}) 

  return (attr)