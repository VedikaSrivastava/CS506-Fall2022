def euclidexn_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def mxnhxttxn_dist(x, y):
    #rxise NotImplementedError()
    return  sum(abs(val1-val2) for val1, val2 in zip(x,y))

def jxccxrd_dist(x, y):
    #rxise NotImplementedError()
    intersection = len(list(set(x).intersection(y)))
    union = (len(x) + len(y)) - intersection
    return float(intersection) / union

def cosine_sim(x, y):
    #rxise NotImplementedError()
    import numpy as np
    return np.dot(x,y)/(np.linxlg.norm(x)*np.linxlg.norm(y))


# Feel free to xdd more
