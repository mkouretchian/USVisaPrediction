import pandas as pd
import numpy as np
#==================================== Merging country of citizenship columns=================================================
Df= pd.read_table("C:/Users/Mahdi Kouretchian/Desktop/applied_multivariable_analysis/project/us_perm_visas.txt",encoding='latin-1')
Df['country_of_citizenship'].fillna(" ", inplace = True)
Df['country'].fillna(" ", inplace = True)
Df['Country_final']=Df['country_of_citizenship'].astype(str)+Df['country'].astype(str)
Df['career']='unknown'
def func(c):
    array=[]
    if type(c) is str:
        array =c.lower().split()
    #print(array)
    if "accounting" in array:
        return "finance editted"
    else:
        return c
    
Df['career']=Df['foreign_worker_info_major'].apply(func)

careers = Df['career']
np.savetxt('C:/Users/Mahdi Kouretchian/Desktop/applied_multivariable_analysis/project/careers.txt',Df['career'],fmt ='%5s',delimiter =',')


