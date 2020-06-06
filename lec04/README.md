1. ## Lecture 03 제어문

   #### 함수

   <u>*js와 공통점*</u>

   1. 

      def sum(x,y=5)

      > y 초기값 설정 
      >
      > but def sum(x,y=5,z)  >> 오류남
      >
      > 초기값을 설정한 인자가 중간에 오면 오류 인자 생략할경우 문제 생길수있음
      >
      > 초기값 설정할 인자는 꼭 뒤쪽에 위치시킬것
      >
      > 

      

   

   <u>*파이썬만의 문법*</u>

   1. 

      **def** sum(x,y)**:**

      

   2. 

      **global** a 

      함수 내외에서 사용가능 , 권장하지 않음

      

#### 입출력

​	<u>*파이썬 문법*</u>

1. ​	

   intput()

   

2. 

   print()

   '+' 연산자 하지 않아도 string 붙일수있음

   ',' 연산자로 띄어쓰기 표현 가능

   입력인자 end 로 한줄 표현 가능

   `print("hello""world") ## helloworld 출력`

   `print("hello","world") ## hello world 출력`

   

3. 

​	f = open("파일명","파일 열기 모드")

​	open("파일.txt","w") 

​		a = 파일마지막에 추가

​		r = 읽기모드



4. 

​	f.close()



5. 

​	f.write(data)



6. 외부파일 읽어 사용할수 있도록 하는 함수

​	**readline()**

​	**readlines()**  << list를 반환

​	**read()** <<  내용 전체를 string 으로 반환



7. file open , close 한번에 처리

   with()

   ```python
   with open("foo.txt","w") as f:
       f.write("hello")
   ```

   





