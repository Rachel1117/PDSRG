import numpy as np
import pandas as pd

def get_train():
    # get the true value of DD
    DD = [line.strip().split("	") for line in open("D:/drug/data_drug/DD.txt").readlines()]
    # DD_train.txt
    for id in split_pos_id[i]:
        DD[int(id[0])][int(id[1])] = '0'
        DD[int(id[1])][int(id[0])] = '0'
    DD=pd.DataFrame(data=DD)
    DD.to_csv("D:/drug/DD_train_original/DD_{}.csv".format(i),sep=',',header=False,index=None)

    DD_mat = np.array(DD).astype(int)
    TL(DD_mat,'train')

    # read data
    content = open("./data_train.csv").readlines()
    file.close()

    # the positive samples are segmented
    x_pos_train = []
    x_pos_test = []
    x_neg_train_all = []
    x_neg_test = []
    for line in content[1:]:
        line = line.split(",")
        id_ = [int(float(id_)) for id_ in line[1:3]]
        if int(float(line[-1])) == 1:
            x_pos_train.append([float(i) for i in line[1:-1]])    
        elif id_ in split_pos_id[i]:
            x_pos_test.append([float(i) for i in line[1:-1]])
        elif id_ in split_neg_id[i]:
            x_neg_test.append([float(i) for i in line[1:-1]])
        else:
            x_neg_train_all.append([float(i) for i in line[1:-1]])
    x_pos_train = np.array(x_pos_train)
    x_pos_test = np.array(x_pos_test)
    x_pos_num = x_pos_train.shape[0]

    x_neg_test = np.array(x_neg_test)
    
    # calculation threshold
    thresholds = [sum([i ** 2 for i in sample[2:]]) for sample in x_neg_train_all]
    thresholds.sort(reverse=False)

    # select the negative samples of the training set that meet the requirements (those with the smallest eigenvalues from the origin)
    threshold = thresholds[x_pos_num]
    x_neg_train = []
    for sample in x_neg_train_all:
        distance = sum([i ** 2 for i in sample[2:]])
        if distance <= threshold:
            x_neg_train.append(sample)
    x_neg_train = np.array(x_neg_train)
    x_neg_test = np.array(x_neg_test)