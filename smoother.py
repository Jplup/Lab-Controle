def linear(p1,p2,q):
    x=((1-q)*p1[0])+(q*p2[0])
    y=((1-q)*p1[1])+(q*p2[1])
    return [x,y]

def sampleDSignal(xs,ys,mul=1):
    dts=[]
    for i in range(len(xs)-1): dts.append(xs[i+1]-xs[i])
    dt=min(dts)/mul
    n=(xs[len(xs)-1]-xs[0])/dt
    p0=[xs[0],ys[0]]
    p1=[xs[1],ys[1]]
    t=xs[0]
    newXs=[]
    newYs=[]
    index=0
    dx=xs[1]-xs[0]
    for i in range(int(n)):
        if index+1==len(xs):
            break
        else:
            if t>=xs[index+1]:
                index+=1
                p0=[xs[index],ys[index]]
                p1=[xs[index+1],ys[index+1]]
                dx=p1[0]-p0[0]
        q=(t-p0[0])/dx
        newP=linear(p0,p1,q)
        newXs.append(newP[0])
        newYs.append(newP[1])
        t+=dt
    newXs.append(xs[len(xs)-1])
    newYs.append(ys[len(ys)-1])
    return newXs,newYs

printStuff=False

def smoothSignal(signal,samplerMul,nOfNeibours=1):
    xs,ys=sampleDSignal(signal[0],signal[1],samplerMul)
    newSig=[]
    if printStuff: print("nofnei:",nOfNeibours)
    if printStuff: input("Começar?")
    for i,y in enumerate(ys):
        mean=0
        count=0
        if printStuff: print("y:",y)
        if i==10:
            if printStuff: input("Parou")
        virtualNofNeibours=nOfNeibours
        if i<nOfNeibours: virtualNofNeibours=i
        if i>=len(ys)-nOfNeibours: virtualNofNeibours=len(ys)-i-1
        for minus in range(virtualNofNeibours):
            if printStuff: print("   minus:",minus)               
            mean+=ys[i-(minus+1)]
            count+=1
        for plus in range(virtualNofNeibours):
            if printStuff: print("   plus")
            mean+=ys[int(i+(plus+1))]
            count+=1
        mean+=y
        mean=mean/(count+1)
        if printStuff: print("mean:",mean,"count:",count+1,"\n\n")
        newSig.append(mean)
    newSig[0]=ys[0]
    return xs,newSig