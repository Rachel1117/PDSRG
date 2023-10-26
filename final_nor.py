import numpy as np

def row_nor(input):
  rows = input.shape[0]
  cols = input.shape[1]
  output=np.zeros(shape=(rows,cols))
  for i in range(rows) :
    s = sum(input[i])
    for j in range(cols) :
      if s==0:
        output[i,j]==0
      else:
        output[i,j] = input[i,j]/s
  return(output)

def col_nor(input):
  rows = input.shape[0]
  cols = input.shape[1] 
  output=np.zeros(shape=(rows,cols))
  for i in range(rows) :
    s = sum(input[:,i])
    for j in range(cols) :
      if s==0:
        output[i,j]==0
      else:
        output[i,j] = input[i,j]/s
  return(output)

def fix_no_zero(input):
  rows = input.shape[0]
  cols = input.shape[1]
  output=np.zeros(shape=(rows,cols))
  for i in range(rows) :
    for j in range(cols) :
      if input[i,j]==0 and i==j :
        output[i,j] = 0
      elif i==j :
        output[i,j] = input[i,j] ** (-0.5)
      else:
        output[i,j] = input[i,j]
  return(output)

def split_mat(input):
  rows = input.shape[0]
  cols = input.shape[1] 
  mid =  np.sum(input)
  output1 = np.zeros(shape=(rows,mid))
  output2 = np.zeros(shape=(mid,cols))
  start = 0
  for i in range(rows) :
    num = sum(input[i])
    if num != 0 :
      for j in range(start,start+num) :
        output1[i,j] = 1
      start = start + num

  start = 0
  for i in range(cols) :
    num = sum(input[:,i])
    if num != 0:
      for j in range(start,start+num) :
        output2[j,i] = 1
      start = start + num
  output=[output1,output2]
  return(output)
  
def final_nor(input1, input2):
  rows1 = input1.shape[0]
  cols2 = input2.shape[1]
  output = np.zeros(shape=(rows1,cols2))
  for i in range(rows1):
    for j in range(cols2):
      f1 = sum(input1[i]*input2[:,j])
      f2 = np.linalg.norm(input1[i,], axis=None)*np.linalg.norm(input2[:,j], axis=None)
      if f2!=0 :
        output[i,j] = f1/f2
      else :
        output[i,j] = 0
  return(output)