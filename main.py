def largest(a):
    if sum(a)==0:
        return '0'
    for i in range(len(a)):
        a[i]=str(a[i])
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[j]+a[i]>a[i]+a[j]:
                a[i],a[j]=a[j],a[i]
    return ''.join(a)
a=list(map(int,input().split()))
print(largest(a))
