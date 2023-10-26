import numpy as np
import pandas as pd


def get_true(DD_mat):
    DD_mat=np.array(pd.read_csv("./DD_mat.csv", sep=',', header=None,index_col=False))
    TL(DD_mat,'true')
    # Get the id of the positive sample
    pos_id = []
    neg_id = []
    with open("D:/drug/data_true.csv") as file:
        content = file.readlines()[1:]
        for line in content:
            line = line.split(",")
            if int(float(line[-1].strip())) == 1:
                pos_id.append([int(float(line[1])), int(float(line[2]))])
            else:
                neg_id.append([int(float(line[1])), int(float(line[2]))])
        pos_id = np.array(pos_id)
        neg_id = np.array(neg_id)