# def

  # 함수내에서 i, mylist 값 변경
def f(i, mylist):
    i = i + 1
    mylist.append(0)
k = 10       
m = [1,2,3]  
f(k, m)      
print(k, m)  # 출력: 10 [1, 2, 3, 0]

  # default Parameter
def calc(i, j, factor = 1):
  return i * j * factor
result = calc(10, 20)
print(result)

  # Named Parameter
def report(name, age, score):
  print(name, score)
report(age=10, name="Kim", score=80)
#report(age=10, 'kim', score=80) # Error!

  # Variable length parameter
def total(*numbers):
  tot = 0
  for n in numbers:
      tot += n
  return tot
t = total(1,5,2,6)
print(t)

  # return
def calc2(*numbers):
  count = 0
  tot = 0
  for n in numbers:
      count += 1
      tot += n
  return count, tot
 
count, sum = calc2(1,5,2,6)  # (count, tot) 튜플을 리턴
print('return',count, sum)