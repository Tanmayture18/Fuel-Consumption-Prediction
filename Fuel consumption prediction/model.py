import pandas as pd
import numpy as np
import pickle

if __name__=='__main__':
    df=pd.read_csv('auto-mpg.csv')
    df.drop(['car name','horsepower'],axis=1,inplace=True)
    X=df.drop('mpg',axis=1)
    y=df.mpg
    from sklearn.model_selection import train_test_split
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
    from sklearn.preprocessing import StandardScaler
    sc=StandardScaler()
    X_train=sc.fit_transform(X_train)
    X_test=sc.fit_transform(X_test)
    from sklearn.ensemble import RandomForestRegressor
    rr=RandomForestRegressor()
    rr.fit(X_train,y_train)
    file=open('model.pk1','wb')
    pickle.dump(rr,file)   
    file.close()
