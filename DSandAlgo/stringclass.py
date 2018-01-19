#strings are immutable so we have o(n^2) while doing the following:
letters=''
for c in document:
    if c.isalpha():
        letters += c

#this can be reduced to linear time o(n) by doing the following:
temp=[]  #This is an empty list
for c in document:
    if c.isalpha():
        temp.append(c)
letters=''.join(temp)  # we are joining list to a string


#further improvement can also be done by using list comprehension
letters=''.join(c for c in document if c.isalpha())
