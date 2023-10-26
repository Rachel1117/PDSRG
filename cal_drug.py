import numpy as np

def Cal_ge_geSet(SGG, RGD):
    gene_num = RGD.shape[0]
    drug_num = RGD.shape[1]
    S_ge_geSet =np.zeros(shape=(gene_num,drug_num)) 
    for i in range(gene_num):
        for j in range(drug_num):
            a=SGG[i]
            b=RGD[:,j]
            c=np.zeros(shape=(SGG.shape[1],1))
            for m in range(len(a)):
                if a[m] !=0 and b[m]!=0:
                    c[m]=1
            #print(np.multiply(SGG[1],c))
            S_ge_geSet[i,j] = np.max(np.multiply(SGG[i],c.T))
    return(S_ge_geSet)

def Cal_drug_tar(S_ge_geSet,RGD):
    drug_num = S_ge_geSet.shape[1]
    SDT = np.identity(drug_num)
    for i in range(drug_num):
        for j in range(drug_num):
            a=[]
            for m in range(len(RGD[:,i])):
                if RGD[m,i]==1:
                    a.append(1) 
            c=np.sum(a)
            b=[]  
            for n in range(len(RGD[:,j])):
                if RGD[n,j]==1:
                    b.append(1)
            d=np.sum(b)
            if(c+d)!=0:
                SDT[i,j] = (np.sum(np.multiply(S_ge_geSet[:,i].T,RGD[:,j]))+np.sum(np.multiply(S_ge_geSet[:,j].T,RGD[:,i])))/(c+d)
    return(SDT)