# List
oldlist = [1, 2, 'A', False, 3]
newlist = [i*i for i in oldlist if type(i)==int]
print(newlist)
# 출력: [1, 4, 9]

# Set
oldlist = [1, 1, 2, 3, 3, 4]
newlist = {i*i for i in oldlist}
print(newlist)
# 출력 : {16, 1, 9, 4}

# Dict
id_name = {1: '박진수', 2: '강만진', 3: '홍수정'}
name_id = {val:key for key,val in id_name.items()}
print(name_id)
# 출력 : {'박진수': 1, '강만진': 2, '홍수정': 3}
def isodd(val):
  return val % 2 == 1
mydict = {x:x*x for x in range(101) if isodd(x)}
print(mydict)