import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from colour import Color
import os

path=os.getcwd()

file_name="/../../../../poses.txt"
file_name_grndtruth="/colmap_traj_sequence_6.txt"

file_name=path+file_name
file_name_grndtruth=path+file_name_grndtruth

with open(file_name, 'r') as reader:
    file=reader.readlines()

with open(file_name_grndtruth, 'r') as reader1:
    file_grndtruth=reader1.readlines()

l=len(file)
pos=np.zeros((l,3))
pos_x, pos_y, pos_z = [], [], []

l1=len(file_grndtruth)
pos_orig=np.zeros((l1,3))
pos_orig_x, pos_orig_y, pos_orig_z = [], [], []

for i,line in enumerate(file):
    line_list=line.split()
    pos[i]=np.array(line_list[1:4])
    pos_x.append(pos[i][0])
    pos_y.append(pos[i][1])
    pos_z.append(pos[i][2])

for j,line1 in enumerate(file_grndtruth):
    line_list1=line1.split()
    pos_orig[j]=np.array(line_list1[1:4])
    pos_orig_x.append(pos_orig[j][0])
    pos_orig_y.append(pos_orig[j][1])
    pos_orig_z.append(pos_orig[j][2])



fig = plt.figure()
ax = plt.axes(projection='3d')


ax.plot3D(pos_orig_x, pos_orig_y, pos_orig_z,label='Ground Truth' ,color='blue')
ax.plot3D(pos_x, pos_y, pos_z, label='ORBSlam Trajectory',color='red')


ax.legend()

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

