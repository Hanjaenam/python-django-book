# in
a = [1,2,3,4]
b = 3 in a
print(b)

# is
a = "ABC"
b = a
print(a is b) # 양쪽 Operand가 동일한 Object를 가리키는가

# formatting
p = "name: %s, age: %d"%("jaenam", 27)
print(p)

# type
s = 'abc'
type(s)
v = s[1]
type(s[1])
# Escape Sequence를 사용하지 않고 Raw String을 직접 사용한다는 것을 의미
path = r'c:\Temp\test.csv'
print(path)

# str library
s = ','.join(['ab', 'cd'])
print(s) # ab,cd
items = 'ab,cd,ef'.split(',')
print(items) # ['ab', 'cd', 'ef']
s = "name: {0}, age: {1}".format('jaenam', 27)
s = "name: {name}, age: {age}".format(name="jaenam", age=27)
area = [10, 20]
s = "width: {x[0]}, height: {x[1]}".format(x=area)
print(s)

# for
sum = 0
# range(3) stop
# range(3, 6) start, stop
# range(3, 6, 2) start, stop, step
for i in range(11):
  sum += i
print(i)
list = ['this', 'is', 'a', 'book']
for s in list:
  print(s)

# list
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
c = a + b    # 병합
d = a * 3
print(d)     #[1, 2, 1, 2, 1, 2]
mylist = "this is a book that is a pencil".split() # default : ' '
i = mylist.index('book') # i=3
n = mylist.count('is') # 2
# List Comprehension
list = [n ** 2 for n in range(10) if n % 3 == 0] # True이면 n에 할당된다.
print(list) # [0, 9, 36, 81]