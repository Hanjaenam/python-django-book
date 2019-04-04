# reference : http://pythonstudy.xyz/python/article/18-%ED%8C%A8%ED%82%A4%EC%A7%80
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

# str method
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