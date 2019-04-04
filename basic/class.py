# class
  # 클래스 정의 내의 pass문은 빈 동작 혹은 아직 구현되지 않았음을 의미하는 것으로 
  # 여기서는 빈 클래스를 의미한다.
class MyClass:
    pass

  # 파이썬에서 메서드는 크게 인스턴스 메서드(instance method), 
  # 정적 메서드(static method), 클래스 메서드(class method)가 있다.
  # 가장 흔히 쓰이는 인스턴스 메서드는 인스턴스 변수에 엑세스할 수 있도록 
  # 메서드의 첫번째 파라미터에 항상 객체 자신을 의미하는 "self"라는 파라미터를 갖는다.
  # 아래 예제에서 calcArea()가 인스턴스 메서드에 해당된다. 
  # 인스턴스 메서드는 여러 파라미터를 가질 수 있지만, 
  # 첫번째 파라미터는 항상 self 를 갖는다.
class Rectangle:
  # 클래스 변수 - static value
    # 클래스 정의에서 메서드 밖에 존재하는 변수를 클래스 변수(class variable)라 하는데,
    # 이는 해당 클래스를 사용하는 모두에게 공용으로 사용되는 변수이다.
    # 클래스 변수는 클래스 내외부에서 "클래스명.변수명" 으로 엑세스 할 수 있다.
    # 위의 예제에서 count는 클래스변수로서 "Rectangle.count"와 같이 엑세스할 수 있다.
  # 클래스 변수 - static value
  count = 0  # 클래스 변수 - static value

  # 초기자(initializer)
    # 클래스로부터 새 객체를 생성할 때마다 실행되는 특별한 메서드로 __init__() 이라는 메서드가 있는데, 
    # 이를 흔히 클래스 Initializer 라 부른다 (주: 파이썬에서 두개의 밑줄 (__) 시작하고 두개의 밑줄로 
    # 끝나는 레이블은 보통 특별한 의미를 갖는다). Initializer는 클래스로부터 객체를 만들 때, 
    # 인스턴스 변수를 초기화하거나 객체의 초기상태를 만들기 위한 문장들을 실행하는 곳이다
      # (주: Python의 Initializer는 C#/C++/Java 등에서 일컫는 생성자(Constructor)와 약간 다르다. 
      # Python에서 클래스 생성자(Constructor)는 실제 런타임 엔진 내부에서 실행되는데, 
      # 이 생성자(Constructor) 실행 도중 클래스 안에 Initializer가 있는지 체크하여 만약 있으면 
      # Initializer를 호출하여 객체의 변수 등을 초기화한다.).
  # 초기자(initializer)
  def __init__(self, width, height):
    # self.* : 인스턴스변수
      # 클래스 변수가 하나의 클래스에 하나만 존재하는 반면, 
      # 인스턴스 변수는 각 객체 인스턴스마다 별도로 존재한다. 
      # 클래스 정의에서 메서드 안에서 사용되면서 "self.변수명"처럼 사용되는 변수를 
      # 인스턴스 변수(instance variable)라 하는데, 이는 각 객체별로 서로 다른 값을 
      # 갖는 변수이다. 인스턴스 변수는 클래스 내부에서는 self.width 과 같이 "self." 
      # 을 사용하여 엑세스하고, 클래스 밖에서는 "객체변수.인스턴스변수"와 같이 엑세스 한다.
    # self.* : 인스턴스변수
    self.width = width
    self.height = height
    Rectangle.count += 1

  # 인스턴스 메서드
  def calcArea(self):
    area = self.width * self.height
    return area

  # 정적메서드
    # 인스턴스 메서드가 객체의 인스턴스 필드를 self를 통해 엑세스할 수 있는 반면,
    # 정적 메서드는 이러한 self 파라미터를 갖지 않고 인스턴스 변수에 엑세스할 수 없다.
    # 따라서, 정적 메서드는 보통 객체 필드와 독립적이지만 로직상 클래스내에 포함되는 메서드에 사용된다
  @staticmethod
  def isSquare(rectWidth, rectHeight):
      return rectWidth == rectHeight

  # 클래스 메서드
    # 클래스 메서드는 정적 메서드와 비슷한데, 객체 인스턴스를 의미하는 self 대신 cls 라는 클래스를 
    # 의미하는 파라미터를 전달받는다. 정적 메서드는 이러한 cls 파라미터를 전달받지 않는다. 
    # 클래스 메서드는 이렇게 전달받은 cls 파라미터를 통해 클래스 변수 등을 엑세스할 수 있다
  @classmethod
  def printCount(cls):
      print(cls.count)
# 클래스메서드 ? 정적메서드?
  # 일반적으로 인스턴스 데이타를 엑세스 할 필요가 없는 경우 클래스 메서드나 정적 메서드를 사용하는데,
  # 이때 보통 클래스 변수를 엑세스할 필요가 있을 때는 클래스 메서드를,
  # 이를 엑세스할 필요가 없을 때는 정적 메서드를 사용한다.


# 만약 특정 변수명이나 메서드를 private으로 만들어야 한다면 두개의 밑줄(__)을 
# 이름 앞에 붙이면 된다.
def __init__(self, width, height):
    self.width = width
    self.height = height
    # private 변수 __area
    self.__area = width * height
# test 해볼 것
# private 메서드
def __internalRun(self):
    pass