## Lecture 05 클래스/모듈/패키지/예외처리

#### 클래스

<u>*js와 다른점*</u>

1. 

   x **or** y ,x **and** y ,**not** x



<u>*파이썬 문법*</u>

1. 

   class name[(상속클래스이름)]:

   ​	num =0;

   ​	def _ _init__(**<u>self</u>**,name):  // 인스턴스 생성할때 자동으로 호출되는함수

   ​		self.name = name

   ​	def method(**<u>self</u>**,x,y):

   ​	def _ _del__(**<u>self</u>**):  // 인스턴스 소멸할때 자동으로 호출되는함수

   ​		self.name = undefined		

   **<u> 클래스 내에 함수는 첫번째 인자로 무조건 self를 받아야함</u>**

2. 

   인스턴스 말고 classname.method() 로 호출할 경우에는 꼭 self에 인스턴스를 넣어줘야함!

   인스턴스로  instance.method()  호출할경우에는  self 생략해도 가능

3. 

   연산자 오버로딩 : 연산자를 객체끼리 사용할수 있게 하는 기법

   

   ```python
   class teacher:
       def __init__(self,name):
           self.name = name;
       def __add__(self, other): ## 연산자 오버로딩
           print("%s 선생님은 %s 학생을 가르칩니다." % (self.name,other.name))
   
   class student:
       def __init__(self, name):
           self.name = name;
   
   teacher01 = teacher("김떙떙")
   student01 = student("안떙떙")
   
   teacher01 + student01 ## 연산자 오버로딩
   ```

