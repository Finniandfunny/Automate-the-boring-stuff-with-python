# Topic: List 
# Name : Comma code

# Function takes list and returns string 
def tum(a):
    #Declare an empty string
    st=""
    #Loop the list except the last item
    for i in a[:-1]:
        #Add the elements one by one upto the last and add comma between them
        st = st+i+", "
    #Add the 'and' before the last element
    st=st+"and "+a[-1]
    return st


l = ["apples","banana","tofu","cats"]
print(tum(l))
