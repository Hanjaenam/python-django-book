# list ( js - array )
  # indexing, slicing
a = ['ab', 10, False]
print(a[0], a[1], a[-1]) # -1 : last index
a = [1,3,5,7,9]
x = a[1:3]   # 3, 5
x = a[:2]    # 1, 3
x = a[3:]    # 7, 9
a.append(11) # 추가
a[1] = 11    # 변경
print(a)
del a[2]     # 삭제 2번째 인덱스 삭제 후 뒤 value 앞으로 하나씩
print(a)
a = [1,2]
b = [3,4,5]
  # merge, iterate
c = a + b    # 병합
d = a * 3
print(d)     #[1, 2, 1, 2, 1, 2]
  # etc
mylist = "this is a book that is a pencil".split() # default : ' '
i = mylist.index('book') # i=3
n = mylist.count('is') # 2
  # List Comprehension
list = [n ** 2 for n in range(10) if n % 3 == 0] # True이면 n에 할당된다.
print(list) # [0, 9, 36, 81]

# tuple
  # List와 다른 점은 Tuple은 새로운 요소를 추가하거나 갱신, 삭제하는 일을 할 수 없다.
  # 한 번 결정된 요소는 변경할 수 없는 Immutable 데이터 타입
t = ('ab', 10, False)
print(t)
  # 요소가 하나일 경우에는 요소 뒤에 콤마를 붙여 명시적으로 Tuple임을 표시해야 한다.
  # (123)일 경우 산술식의 괄호로 인식하여 타입이 정수가 된다.
t1 = (123)
print(t1) # int
t2 = (123, )
print(t2) # tuple
t = (1,5,10)
  # indexing, slicing
second = t[1]
last = t[-1]
s = t[1:2]
s = t[1:]
  # merge, iterate
a = (1, 2)
b = (3, 4, 5)
c = a + b
print(c)  # (1, 2, 3, 4, 5)
d = a * 3
print(d)  # (1, 2, 1, 2, 1, 2)
  # allocate
name = ("john", "kim")
print(name)
firstname, lastname = name
print(firstname, ",", lastname)

# dict ( js - Map )
  # key - value
  # Hash Table
  # key - 그 값을 변경할 수 없는 Immutable 타입이여야 한다 
  ##      key 는 중복이 될 수 없다.
  ##      (string, Tuple 사용가능, List 사용불가)
  # value - Immutable, Mutable 모두 가능
scores = {"a": 90, "b": 70, "c": 100}
v = scores["a"]
scores["a"] = 93
print(scores)
persons = [("a", 30), ("b", 40)]
print(persons)  # [('a', 30), ('b', 40)]
mydict = dict(persons)  # dict로 만들어준다.
print(mydict)   # {'a': 30, 'b': 40}
scores = dict(a=80, b=90, c=85)
print(scores["b"])  # 90
  # append, modify, delete, read
scores = {"a": 90, "b": 85, "c": 80}
scores["a"] = 30  # modify
scores["d"] = 20  # append
del scores["c"]   # delete
for key in scores:
  val = scores[key]
  print("%s : %d"%(key,val))  # key는 랜덤하게 리턴되는데, 이는 해시테이블의 속성
  #method
    # key
keys = scores.keys()
for k in keys:
  print(k)
    # value
values = scores.values()
for v in values:
  print(v)
    # list-tuple 로 변환
print(scores)          # scores : {"a": 30, "b": 85, "d": 30}
items = scores.items()
print(items)           # list-tuple : [("a", 30), ("b", 85), ("d", 30)]
    #update
persons = [("a", 10), ("b", 20), ("c", 30)]
mydict = dict(persons)
mydict.update({"a": 15, "b": 25}) # can update at one go
    # etc
v = scores.get('a')
v = scores.get('b')
if 'a' in scores:
  print('a exists')
scores.clear()

# set ( js - Set )
  # 중복이 없는 요소들로만 구성된 컬렉션
  # 만약 set을 정의할 때, 중복된 값을 입력하는 경우, set은 중복된 값을 한 번만 가지고 있게 된다.
myset = {1,1,3,5,5}
print(myset) # {1,3,5}
mylist = ["a","a","b","b","b"]
s = set(mylist)
print(s)
  # append, delete
myset = {1,3,5}
mtset.add(4)          # append one
myset.update({4,2,10})# append multiple
myset.remove(1)
my.set.clear()        # delete all
  # 집합 연산
a = {1, 3, 5}
b = {1, 2, 5}
i = a & b # 교집합
u = a | b # 합집합
d = a - b # 차집합
