Data_list = []
with open ('Data_set_1_2.txt' , 'r') as f:
    n = 0
    for line in f:
        n += 1
        if n == 1:
            continue
        elif n == 10 or n == 100:
            Data_list.append (float(line[len(str(n)):len(str(n))+4]))
        else:
            Data_list.append (float(line[len(str(n))+1:len(str(n))+6]))
    #Data_list.remove('')
#print (Data_list)
#for i in Data_list:
    #print (type (i))
N = len (Data_list)
Data_list.sort()
quant_lev = float(input('Введите уровень квантиля  '))
Sum_Data = 0
Disp_Data = 0
Dist_Func_Dict = {}

quant_res = Data_list [round ((N-1) * quant_lev)]
k = 0

for i in Data_list:
    Sum_Data = Sum_Data + i
    k += 1
    Dist_Func_Dict [k/N] = i
Av_Data = Sum_Data / N
for j in Data_list:
    Disp_Data = Disp_Data + (j - Av_Data)**2
Disp_Data_res = Disp_Data / N

#print (Disp_Data_res, Av_Data, quant_res)
#print (Dist_Func_Dict)
x = list (Dist_Func_Dict.values())
y = list(Dist_Func_Dict.keys())

import matplotlib.pyplot as plt

#plt.plot (x,y)

fig, axs = plt.subplots(1, 2)
n_bins = int (input ('Количество столбцов гистограммы   '))
axs[0].hist(x, bins=n_bins)
axs[0].set_title('sepal length')
axs[1].hist(x, bins=n_bins)
axs[1].set_title('petal length')

plt.show()


#print (y, type (y))
