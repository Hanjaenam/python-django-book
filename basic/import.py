import math
n = math.factorial(5)

# factorial 함수만 import
from math import factorial  
n = factorial(5) / factorial(3) 

# 여러 함수를 import
from math import (factorial,acos)
n = factorial(3) + acos(1)
 
 # 모든 함수를 import
from math import *
n = sqrt(5) + fabs(-12.5) 

# factorial() 함수를 f()로 사용 가능
from math import factorial as f
n = f(5) / f(3)

# 모듈 위치
  # import하면 모듈을 찾기 위해 다음과 같은 경로를 순서대로 검색
    # 1. 현재 디렉토리
    # 2. 환경변수 PYTHONPATH에 지정된 경로
    # 3. Python이 설치된 경로 및 그 밑의 라이브러리 경로

# 모듈 작성
  # mylib.py
def add(a, b):
  return a + b
def substract(a, b):
  return a - b
  # exec.py
from mylib import *
i = add(10,20)
i = substract(20,5)

# 파이썬 모듈 .py 파일은 import 하여 사용할 수 있을 뿐만 아니라,
# 해당 모듈 파일 안에 있는 스크립트 전체를 바로 실행할 수도 있다.
# 파이썬에서 하나의 모듈을 import 하여 사용할 때와 스크립트 전체를 실행할 때를
# 동시에 지원하기 위하여 흔히 관행적으로 모듈 안에서 __name__ 을 체크하곤 한다.
# 파이썬에서 모듈을 import해서 사용할 경우 그 모듈 안의 __name__ 은 해당 모듈의
# 이름이 되며, 모듈을 스크립트로 실행할 경우 그 모듈 안의 __name__ 은 "__main__" 이 된다.
# 예를 들어, run.py이라는 모듈을 import 하여 사용할 경우 __name__ 은 run.py가 되며,
# "python3.5 run.py"와 같이 인터프리터로 스크립트를 바로 실행할 때
# __name__ 은 __main__ 이 된다.
# from mylib import * 일 경우 mylib.py내부에서 __name__은 "__main__"이 아니라 그 모듈의 이름이 되는 것.
