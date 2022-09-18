import math

with open('language.txt','r') as f:
    
    a=f.read(1)
    print(a)


# li=[]
# l=[]
# for i in range(len(a)):
 
#     st=str(a[i])
#     stf=""
#     for i in st:
#         if  i=="\n":
#             continue
#         else:
#             stf+=i
#             li.append(i)
#     l.append(stf)
# s=[]
# t=[]
# special=[]
# for i in range(len(l)):
#     sub=""
#     left = 1

#     for j in l[i]:
     
#         if j!=" " and j!="(" and j!=")" and j!=":" :
#             sub+=j

            
#         else:
#             if j=="(" or j==")" or j==":":
#                 special.append(j)
#             if sub!='':
#                 t.append(sub)
#             sub=""

#             continue
#     if sub!='':
#         t.append(sub)
#     s.append(sub)


# print(l)
# print(li)
# print(t)
# print(special)

# d=[]
# for i in range(5):
#     d.append((i,i))

# print(d)


# a={
#     'a':'aron'
# }
# print(a['a'])

# # a=["my name is\n","aron shrestha\n","    print(name)"]
# # z=[]
# # for i in a:
    
# #     z.append(i.strip().split(' '))
# # print(z)
# a= "Aron"
# print(a[1])
# for i in range(len(a)):
#     print(a[i])
# a="ar"
# print(a[0:0])
# print(a[1])