<<<<<<< HEAD:matplot/image_k10.py
import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7]

z=[ 0.57286113,  0.57163114,  0.57469759,  0.57781761,  0.58018418,  0.58162271, 0.58095828]
z2=[ 0.6140767,   0.61907172,  0.6293858,   0.63139441,  0.63431809,  0.6320679, 0.62832845]
z3=[ 0.64615727,  0.65480931,  0.6615764,   0.66289516,  0.66309922,  0.66471204,  0.66523512]
#z4=[ 0.64496665,  0.64086654,  0.63510031,  0.62024854,  0.60202204,0.58365142,  0.57074511]
Z4 = [ 0.64710449, 0.63563118, 0.63460148, 0.61817749, 0.59829672, 0.57901452, 0.56837194]
group_labels=[8,16,32,64,128,256,512]
#group_labels=x
plt.title('')
plt.xlabel('bits')
plt.ylabel('NDCG@10')

plt.plot(x,z,'b-^', label='ITQ')
plt.plot(x,z2,'r-+', label='ITSH')
plt.plot(x,z3,'y-x', label='TSH')
plt.plot(x,z4,'g-D',label='binMF')

plt.xticks(x,group_labels,rotation=0)
plt.legend(loc='upper center', bbox_to_anchor=(1.2,1),ncol=2,shadow=False)
plt.show()
=======
import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7]

z=[ 0.57286113,  0.57163114,  0.57469759,  0.57781761,  0.58018418,  0.58162271, 0.58095828]
z2=[ 0.6140767,   0.61907172,  0.6293858,   0.63139441,  0.63431809,  0.6320679, 0.62832845]
z3=[ 0.64615727,  0.65480931,  0.6615764,   0.66289516,  0.66309922,  0.66471204,  0.66523512]
z4=[ 0.64710449, 0.63563118, 0.63460148, 0.61817749, 0.59829672, 0.57901452, 0.56837194]
group_labels=[8,16,32,64,128,256,512]
#group_labels=x
plt.title('')
plt.xlabel('bits')
plt.ylabel('NDCG@10')

plt.plot(x,z,'b-^', label='ITQ')
plt.plot(x,z2,'r-+', label='ITSH')
plt.plot(x,z3,'y-x', label='UTSH')
plt.plot(x,z4,'g-D',label='binMF')

plt.xticks(x,group_labels,rotation=0)
plt.legend()
plt.show()
>>>>>>> 85d42eb5e021611d984a0cf78d54407d42a81e7f:code/matplot/image_k10.py