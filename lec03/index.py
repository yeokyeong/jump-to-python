money = 2000
card = 1
if money >=3000 or card:
    print("take taxi")
else:
    print("walk")
##
if "cooki"  not in ["latte","coffee","cake"]: pass
else: print("go there")

##
for i in ["one","two","three"]:
    print(i)
for (first,last) in [("one",1),("two",2),("three",3)]:
    print(first,last)

## 5명의 학생중 시험점수가 50점이 넘는학생 결과 출력
score = [40,30,20,60,90]
num = 0
for i in score:
    num=num+1
    if(i>=50): print("%d 학생은 통과입니다." % num)
    else:continue
## range 함수
sum = 0;
for i in range(1,11):
    sum = sum +i
print(sum)

for i in range(len(score)):
    if(score[i] >=50): print("%d 학생은 통과입니다." % (i+1))
    else:continue

##99단
for i in range(2,10):
    for j in range(1,10):
        print("%d X %d = %d" %(i ,j, (i*j)),end=" ")
    print(" ")

##리스트안에서 조건문 제어
list = [1,2,3,4,5]
result = []
for n in list:
 result.append(n*3)
print(result)

result = [n*3 for n in list]
print(result)

result = [n*3 for n in list if n%2 ==0 ]
print(result)

## 리스트안에서 99단
number =[i*j for i in range(2,9)
                for j in range(1,9)]
print(number)