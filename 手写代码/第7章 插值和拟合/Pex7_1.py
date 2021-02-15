def h(x,y,a):
    s=0.0
    for i in range(len(y)):
        t=y[i]
        for j in range(len(y)):
            if i!=j:
                t*=(a-x[j])/(x[i]-x[j])
        s +=t
    return s