#!/bin/python


from pandas import read_csv
import pandas as pd
import numpy as np



file1 = 'sample_data.csv'
file2 = 'sample_data2.csv'
file3 = 'sample_data3.csv'

elements_file1 = pd.read_csv( file1 )['name'].tolist()
elements_file2 = pd.read_csv( file2 )['name'].tolist()
elements_file3 = pd.read_csv( file3 )['name'].tolist()

#print (elements_file1)


tetha = list(set(elements_file1 + elements_file2 + elements_file3))
#print( tetha )



n_tetha = len(tetha)
#print( n_tetha)

F = [elements_file1, elements_file2, elements_file3]

print(F)

list_file = [file1, file2, file3]
#print(list_file)

#y[len(F)][n_tetha]
y = []



for i in range(len(tetha)): 
    for j in range(len(F)):
        found = False
        for k in range(len(F[j])): 
            if F[j][k] == tetha[i] : 
                # y.append([list_file[j],tetha[i],1])
                y.append([list_file[j], tetha[i], 1])
                found = True
                break

        if found == False :
            # y.append([list_file[j],tetha[i],0])		
            y.append([list_file[j], tetha[i], 0])


for items in y:
   
    
    print(items[0], items[1], items[2])
y = [] 	



import matplotlib.pyplot as plt #enables the use matplotlib that enables us to plot
import numpy as np

import matplotlib as mpl
tetha = list(set(elements_file1 + elements_file2 + elements_file3))

objects =  ['one', 'two', 'three', 'four', 'five'] #data (elements of tetha (names of the different files).)


performance= [3, 3, 3, 2, 1]#data #number of times each corresponding names in the different files occurs.
#colors = [7,9,2,5,6] ths is meant to give different shades of color to the different points on the scatter plot.
plt.scatter(objects, performance, s=30)#creates a scatter plot with objects on x axis and perfomance on y axis s=size of scattter plots

'''cbar = plt.colorbar() 
#normally this should create a colorbar but it doesnt because of my matplotlib not updated.
#or some other problem

cbar.set_label('Distribution')'''

plt.style.use('seaborn') # its one of the numerous plot styles in which the scatter plots are presented



plt.tight_layout # creates an automatic pattern to our plots.
plt.show() #enables the scatter plot to show





