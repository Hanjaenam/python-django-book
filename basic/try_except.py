# try:
#   문장1
#   문장2
# except:
#   예외처리
# finally:
#   마지막에 항상 수행
  #위의 except 문은 except 뒤에 아무것도 쓰지 않았는데, 
  #이는 어떤 에러이든 발생하면 해당 except 블럭을 수행하라는 의미이다.
  #except 뒤에 "에러타입"을 적거나 "에러타입 as 에러변수"를 적을 수가 있는데, 
  #이는 특정한 타입의 에러가 발생했을 때만 해당 except 블럭을 실행하라는 뜻이다.


# def calc(values):
#     sum = None
#     # try...except...else
#     try:
#        sum = values[0] + values[1] + values[2]
#     except IndexError as err:
#         print('인덱스에러')
#     except Exception as err:
#         print(str(err))
#     else:
#         print('에러없음')
#     finally:
#         print(sum)
  # 첫번째는 IndexError가 발생했을 때만 그 블럭을 실행하며, 
  # 두번째는 일반적인 모든 Exception 이 발생했을 때 해당 블럭을 실행하라는 의미이다. 
  # 즉, 먼저 IndexError 인지 검사하고, 아니면 다음 except를 계속 순차적으로 
  # 체크하게 된다. except가 여러 개인 경우는 범위가 좁은 특별한 에러타입을 앞에 
  # 쓰고 보다 일반적인 에러타입을 뒤에 쓰게 된다.


# def calc(values):
#     sum = None
#     try:
#        sum = values[0] + values[1] + values[2]
#     except (IndexError, ValueError):
#         print('오류발생')
  # 만약 복수 Exception들이 동일한 except 블럭을 갖는다면, 
  # 위와 같이 이들 Expception들을 하나의 except 문에 묶어서 쓸 수도 있다.


# # pass 를 사용한 예
# try:
#    check()
# except FileExistsError:
#     pass
 
# # raise 를 사용한 예
# if total < 0:
#     raise Exception('Total Error')
  # 발생된 Exception을 그냥 무시하기 위해서는 보통 pass 문을 사용하며, 
  # 또한 개발자가 에러를 던지기 위해서는 raise문을 사용한다.
  # raise 뒤에 아무것도 없는 경우는 현재 Exception을 그대로 던지게 된다. 
  # 또한 raise 뒤에 특정한 에러타입과 에러메시지 (Optional)를 넣어 개발자가
  # 정의한 에러를 발생시킬 수 있다