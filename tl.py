import numpy as np
import pandas as pd

def TL(DD_mat):
    
    DG_mat = np.array(pd.read_csv("./DG_mat.csv", sep=',', header=None,index_col=False))
    GG_mat = np.array(pd.read_csv("./GG_mat.csv", sep=',', header=None,index_col=False))
    DD_sim_ATC1 = np.array(pd.read_csv("./DD_sim_ATC1.csv", sep=',', header=None,index_col=False))
    DD_sim_ATC2 = np.array(pd.read_csv("./DD_sim_ATC2.csv", sep=',', header=None,index_col=False))
    DD_sim_ATC3 = np.array(pd.read_csv("./DD_sim_ATC3.csv", sep=',', header=None,index_col=False))
    DD_sim_chemical =np.array(pd.read_csv("./DD_sim_chemical.csv", sep=',', header=None,index_col=False))
    
    drug_num = DD_mat.shape[0]    

    SDD = Original_hetesim(DG_mat, DD_mat, GG_mat, m_p='DD')
    SDDD = Original_hetesim(DG_mat, DD_mat, GG_mat, m_p='DDD')
    SDGD = Original_hetesim(DG_mat, DD_mat, GG_mat, m_p='DGD')
    SDGDD = Original_hetesim(DG_mat, DD_mat, GG_mat, m_p='DGDD')
    SDGGD = Original_hetesim(DG_mat, DD_mat, GG_mat, m_p='DGGD')
    SDDDD = Original_hetesim(DG_mat, DD_mat, GG_mat, m_p='DDDD')
    SDDGD = Original_hetesim(DG_mat, DD_mat, GG_mat, m_p='DDGD')
    SDDDDD = Original_hetesim(DG_mat, DD_mat, GG_mat, m_p='DDDDD')
    SDDDGD = Original_hetesim(DG_mat, DD_mat, GG_mat, m_p='DDDGD')
    SDDGDD = Original_hetesim(DG_mat, DD_mat, GG_mat, m_p='DDGDD')
    SDDGGD = Original_hetesim(DG_mat, DD_mat, GG_mat, m_p='DDGGD')
    SDGDDD = Original_hetesim(DG_mat, DD_mat, GG_mat, m_p='DGDDD')
    SDGDGD = Original_hetesim(DG_mat, DD_mat, GG_mat, m_p='DGDGD')
    SDGGDD = Original_hetesim(DG_mat, DD_mat, GG_mat, m_p='DGGDD')
    SDGGGD = Original_hetesim(DG_mat, DD_mat, GG_mat, m_p='DGGGD')

    
    attr_num = 22

    attr = pd.DataFrame(np.zeros(shape=(int(drug_num*(drug_num-1)/2),int(attr_num))))
    pd.options.display.float_format = lambda x : '{:}'.format(x) if round(x,0) == x else '{:,.10f}'.format(x)
    attr_pos = 0
    for m in range(1,drug_num) :
        for n in range(0,m) :
            attr.loc[attr_pos,0] = DD_sim_ATC1[m,n]
            attr.loc[attr_pos,1] = DD_sim_ATC2[m,n]
            attr.loc[attr_pos,2] = DD_sim_ATC3[m,n]
            attr.loc[attr_pos,3] = DD_sim_chemical[m,n]

            attr.loc[attr_pos,4] = SDD[m,n]
            attr.loc[attr_pos,5] = 0.5*SDDD[m,n]
            attr.loc[attr_pos,6] = 0.5*SDGD[m,n] 

            attr.loc[attr_pos,7] = 0.33*SDGDD[m,n]
            attr.loc[attr_pos,8] = 0.33*SDGGD[m,n]
            attr.loc[attr_pos,9] = 0.33*SDDDD[m,n]
            attr.loc[attr_pos,10] = 0.33*SDDGD[m,n]
            
            attr.loc[attr_pos,11] = 0.25*SDDDDD[m,n]
            attr.loc[attr_pos,12] = 0.25*SDDDGD[m,n]
            attr.loc[attr_pos,13] = 0.25*SDDGDD[m,n] 
            attr.loc[attr_pos,14] = 0.25*SDDGGD[m,n] 
            attr.loc[attr_pos,15] = 0.25*SDGDDD[m,n] 
            attr.loc[attr_pos,16] = 0.25*SDGDGD[m,n] 
            attr.loc[attr_pos,17] = 0.25*SDGGDD[m,n] 
            attr.loc[attr_pos,18] = 0.25*SDGGGD[m,n] 
            attr.loc[attr_pos,21] = DD_mat[m,n]
            attr_pos = attr_pos+1

            #colnames(attr)[attr_num]  c("label")
    attr[19] = attr[[4,19]].mean(axis=1)
    attr[20] = attr[[4,19]].std(ddof=1,axis=1)
    
    attr_pos1= 0
    attr1=pd.DataFrame(np.zeros(shape=(int(drug_num*(drug_num-1)/2),2))) 
    for m in range(1,drug_num+1) :
        for n in range(0,m-1) :
            attr1.loc[attr_pos1,0] = int(m-1)
            attr1.loc[attr_pos1,1] = int(n)
            attr_pos1 = attr_pos1+1

    attr_pos2=0
    attr2=pd.DataFrame(np.zeros(shape=(int(drug_num*(drug_num-1)/2),1)))
    for i in range(1,int(drug_num*(drug_num-1)/2)+1) :
        attr2.loc[attr_pos2,0] =i
        attr_pos2 = attr_pos2+1        
    attr=pd.concat([attr2,attr1,attr],axis=1,ignore_index=True)
    attr=attr.rename(columns = {24:'label'}) 
    attr=attr.rename(columns = {1:'number1'}) 
    attr=attr.rename(columns = {2:'number2'}) 

    #print(attr)
    return attr