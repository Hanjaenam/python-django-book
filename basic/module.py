# 먼저 import문을 보면 import문은 모듈을 import 하는 것이므로,
# 패키지내 모듈을 import하기 위해서는 "import 패키지명.모듈명"과 같이
# 패키지명을 앞에 붙여 사용한다. 아래 예제에서 보면, bill.py 모듈을
# import 하기 위해 "import models.account.bill" 와 같이 전체 패키지명을
# 함께 표시하였음을 볼 수 있다. 또한 모듈내 함수를 사용하기 위하여
# models.account.bill.charge()와 같이 패키지명과 모듈명도 함께 써 주어야 한다.
  # 모듈 import 
  # import 패키지.모듈
import models.account.bill
models.account.bill.charge(1, 50)

# from 뒤에 패키지명 models.account을 사용하였고, import 다음 모듈명 bill을 사용하였다.
# 이 방식은 해당 모듈 내의 모든 함수를 사용할 수 있는데,
# bill.charge()와 같이 모듈명.함수명()으로 함수를 호출한다.
# 만약 패키지 모듈 내의 특정 함수만 import하여 사용하고 싶다면, 
# "from 패키지명.모듈명 import 함수명" 과 같이 from 에 "패키지명.모듈명"을 적고
# import 뒤에 함수명을 적는다.
  # 모듈안의 모든 함수 import
  # from 패키지명 import 모듈명
from models.account import bill
bill.charge(1, 50) 
  # 특정 함수만 import
  # from 패키지명.모듈명 import 함수명
from models.account.bill import charge
charge(1, 50)

# __init__
  # 패키지에는 __init__.py 라는 특별한 파일이 있는데,
  # 이 파일은 기본적으로 그 폴더가 일반 폴더가 아닌 패키지임을 표시하기 위해 
  # 사용될 뿐만 아니라, 패키지를 초기화하는 파이썬 코드를 넣을 수 있다. 
  # 버젼 3.3 이상에서는 이 파일이 없어도 패키지로 사용할 수 있지만, 
  # 호환성을 위해 두는 것이 좋다

  # __init__.py 파일에서 중요한 변수로 __all__ 이라는 리스트 변수가 있는데, 
  # 이 변수는 "from 패키지명 import *" 문을 사용할 때, 
  # 그 패키지 내에서 import 가능한 모듈들의 리스트를 담고 있다. 
  # 즉, __all__ 에 없는 모듈은 import 되지 않고 에러가 발생한다.

  # 아래 예제는 __init__.py 파일 안에 bill 모듈을 허락한 후, 
  # from ... import * 를 사용하여 해당 패지키로부터 허락된 모든 모듈을 import 한 후
  # bill.charge() 함수를 사용하는 예이다.
  
    # __init__.py 파일의 내용
__all__ = ['bill']
    # 패지키내 모든 모듈 import
    # from 패키지명 import *
from models.account import *
bill.charge(1, 50)

# 그 밖의 특별한 메서드들

# 객체가 소멸될 때 실행되는 소멸자 __del__
# 두 개의 객체를 더하는 __add__
# 두 개의 객체를 빼는 __sub__
# 두 개의 객체를 비교하는 __cmp__
# 문자열로 객체를 표현할 때 사용하는 __str__

# Dog 클래스는 Animal 클래스로부터 파생된 파생클래스
class Animal:
    def __init__(self, name):
        self.name = name
    def move(self):
        print("move")
    def speak(self):
        pass
 
class Dog (Animal):
    def speak(self):
        print("bark")
 
class Duck (Animal):
    def speak(self):
        print("quack")

animals = [Dog('doggy'), Duck('duck')]
 
for a in animals:
    a.speak()     # bark, quack
    print(a.name) # doggy, duck