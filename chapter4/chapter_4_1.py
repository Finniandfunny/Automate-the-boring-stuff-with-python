def tum(a):
    st=""
    for i in a[:-1]:
        st = st+i+", "
    st=st+"and "+a[-1]
    return st
l = ["apples","banana","tofu","cats"]
print(tum(l))
