import math
import numpy as np

def Original_hetesim(DG_mat, DD_mat, GG_mat,m_p):
  drug_num = DD_mat.shape[0]
  comp_mat1 = np.identity(drug_num)   
  comp_mat2 = np.identity(drug_num)    
  if len(m_p)%2==0:# judge divisible
    # print('even')
    # take the first element
    so = math.floor(len(m_p)/2)-1
    if so==0:
      comp_mat1 = row_nor(comp_mat1)   
      for j in range(1):
        if m_p[j:j+1]=='D' and m_p[j+1:j+2]=='D':
          temp = row_nor(DD_mat)
          #print(j+1)
        elif m_p[j:j+1]=='D' and m_p[j+1:j+2]=='G':
          temp = row_nor(DG_mat)
        elif m_p[j:j+1]=='G' and m_p[j+1:j+2]=='D':
          temp = row_nor(DG_mat.T)
        elif m_p[j:j+1]=='G' and m_p[j+1:j+2]=='G':
          temp = row_nor(GG_mat)
        comp_mat1 = np.dot(comp_mat1, temp) 

    else:
      comp_mat1 = row_nor(comp_mat1) 
      for j in range(so): 
        if m_p[j:j+1]=='D' and m_p[j+1:j+2]=='D':
          temp = row_nor(DD_mat)
          #print(j+1)
        elif m_p[j:j+1]=='D' and m_p[j+1:j+2]=='G':
          temp = row_nor(DG_mat)
        elif m_p[j:j+1]=='G' and m_p[j+1:j+2]=='D':
          temp = row_nor(DG_mat.T)
        elif m_p[j:j+1]=='G' and m_p[j+1:j+2]=='G':
          temp = row_nor(GG_mat)
        comp_mat1 = np.dot(comp_mat1, temp)  
      
    # take the first element after half
    st = int(len(m_p)/2)-1
    so = len(m_p)-2
    
    if st==0 and so==0:
      comp_mat2 = row_nor(comp_mat2)
      for j in range(1):
        if m_p[j+1:j+2]=='D' and m_p[j:j+1]=='D':
          temp = row_nor(DD_mat)
          #print(j+1)
        elif m_p[j+1:j+2]=='G' and m_p[j:j+1]=='D':
          temp = row_nor(DG_mat.T)
        elif m_p[j+1:j+2]=='D' and m_p[j:j+1]=='G':
          temp = row_nor(DG_mat)
        elif m_p[j+1:j+2]=='G' and m_p[j:j+1]=='G':
          temp = row_nor(GG_mat)
        comp_mat2 = np.dot(comp_mat2, temp)

    else:
        comp_mat2 = row_nor(comp_mat2)
        for j in range(so,st,-1):
          if m_p[j+1:j+2]=='D' and m_p[j:j+1]=='D':
            temp = row_nor(DD_mat)
            #print(j+1)
          elif m_p[j+1:j+2]=='G' and m_p[j:j+1]=='D':
            temp = row_nor(DG_mat.T)
          elif m_p[j+1:j+2]=='D' and m_p[j:j+1]=='G':
            temp = row_nor(DG_mat)
          elif m_p[j+1:j+2]=='G' and m_p[j:j+1]=='G':
            temp = row_nor(GG_mat)  
          comp_mat2 = np.dot(comp_mat2, temp) 

    
    # central position
    mid_pos = int(len(m_p)/2)-1

    if m_p[mid_pos:mid_pos+1]=='D' and m_p[mid_pos+1:mid_pos+2]=='D':
      AB = split_mat(DD_mat)     
    elif m_p[mid_pos:mid_pos+1]=='D' and m_p[mid_pos+1:mid_pos+2]=='G':
      AB = split_mat(DG_mat)
    elif m_p[mid_pos:mid_pos+1]=='G' and m_p[mid_pos+1:mid_pos+2]=='D':
      AB = split_mat(DG_mat.T)
    elif m_p[mid_pos:mid_pos+1]=='G' and m_p[mid_pos+1:mid_pos+2]=='G':
      AB = split_mat(GG_mat)
    
    A = AB[0]
    B = AB[1]
    
    #print(A.shape)
    #print(B.shape)
    
    comp_mat1 = row_nor(comp_mat1)
    A = row_nor(A)
    comp_mat1 = np.dot(comp_mat1,A)
    comp_mat2 = row_nor(comp_mat2)
    B = B.T
    B = row_nor(B)
    comp_mat2 = np.dot(comp_mat2,B)
    # print(comp_mat1.shape,comp_mat2.shape)
    drugsim_mat = final_nor(comp_mat1,comp_mat2.T)
    
  else:
    # print('odd')
    comp_mat1 = row_nor(comp_mat1)
    for j in range(math.floor(len(m_p)/2)):
      if m_p[j:j+1]=='D' and m_p[j+1:j+2]=='D':
        temp = row_nor(DD_mat)
        #print(1)
      elif m_p[j:j+1]=='D' and m_p[j+1:j+2]=='G':
        temp = row_nor(DG_mat)
        #print(2)
      elif m_p[j:j+1]=='G' and m_p[j+1:j+2]=='D':
        temp = row_nor(DG_mat.T)
        #print(3)
      elif m_p[j:j+1]=='G' and m_p[j+1:j+2]=='G':
        temp = row_nor(GG_mat)
        #print(4)
      comp_mat1 = np.dot(comp_mat1,temp)  
    #print(comp_mat1.shape)
    st = int(len(m_p)/2)-1
    so = len(m_p)-2

    comp_mat2 = row_nor(comp_mat2)
    for j in range(so,st,-1):
      if m_p[j:j+1]=='D' and m_p[j+1:j+2]=='D':
        temp = row_nor(DD_mat)
      elif m_p[j+1:j+2]=='G' and m_p[j:j+1]=='D':
        temp = row_nor(DG_mat.T)
      elif m_p[j+1:j+2]=='D' and m_p[j:j+1]=='G':
        temp = row_nor(DG_mat)
      elif m_p[j+1:j+2]=='G' and m_p[j:j+1]=='G':
        temp = row_nor(GG_mat)
      comp_mat2 = np.dot(comp_mat2, temp)
    #print(comp_mat1.shape,comp_mat2.shape)
    drugsim_mat = final_nor(comp_mat1,comp_mat2.T)
    #print(drugsim_mat.shape)
  return(drugsim_mat)