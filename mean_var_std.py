import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    arr1=np.array(list)
    arr=np.array(list).reshape(3,3)
    calculations={
        'mean':[arr.mean(axis=0).tolist(),arr.mean(axis=1).tolist(),arr1.mean()],
        'variance':[arr.var(axis=0).tolist(),arr.var(axis=1).tolist(),arr1.var()],
        'standard deviation':[arr.std(axis=0).tolist(),arr.std(axis=1).tolist(),arr1.std()],
        'max':[arr.max(axis=0).tolist(),arr.max(axis=1).tolist(),arr1.max()],
        'min':[arr.min(axis=0).tolist(),arr.min(axis=1).tolist(),arr1.min()],
        'sum':[arr.sum(axis=0).tolist(),arr.sum(axis=1).tolist(),arr1.sum()]
    }
    
    

    
    return calculations