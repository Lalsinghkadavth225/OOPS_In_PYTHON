
from functools import reduce
x=[1,2,3,4,4,5,6,7,8]
evens_list=list(filter(lambda n : n%2==0,x))
# print(evens_list)
double=list(map(lambda r: r*2, evens_list))
print(double)

add_two_ele=reduce(lambda a,b:a+b,double)

print(add_two_ele)