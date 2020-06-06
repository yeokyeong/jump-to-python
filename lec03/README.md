## Lecture 03 제어문

#### 연산자

<u>*js와 다른점*</u>

1. 

   x **or** y ,x **and** y ,**not** x

  2.

 	  elseif 대신 **elif**

3. 

   while ,if 조건 넣을때 괄호 사용 x

   While num != 4 : 

   ...

4. 

   num**++** 문법 작동 x



<u>*파이썬만의 문법*</u>

1. 

   x **in** [리스트, 튜플, 문자열]

   x **not in** [리스트, 튜플, 문자열]

2. 

   아무런 동작하고 싶지 않을때

   if(true):

   ​	**pass**	

3. 

   **for 변수 in [리스트,튜플, 문자열]:**

   ```python
   for (first,last) in [("one",1),("two",2),("three",3)]:
   ```

4. 

   range(1,11)  1~10까지 숫자 리스트 만들어주는 함수

5. 

   print(~~~,end =" ") 

   end =" " 는 줄바꿈 하지 않고 띄어쓰기만 

6. 

   리스트안에 제어문 가능

   [표현식 for 변수 in [리스트, 튜플, 문자열] if 조건] 

   중첩 for문도 사용가능

   리스트안에서 쓰이는 for 문에는 : 없음

   ```python
   result = [n*3 for n in list]
   result = [n*3 for n in list if n%2 ==0 ]
   ```

   