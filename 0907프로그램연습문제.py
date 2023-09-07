#!/usr/bin/env python
# coding: utf-8

# In[2]:


#주어진 금액
money = int(input("금액을 정수로 입력하세요.: ")) 

#1만원권 갯수 계산
ten_thousand = money//10000

#나머지 금액
remainder = money % 10000

print(f"저축한 금액은 {money}입니다.")
print(f"이 금액의 1만원권은 {ten_thousand}입니다.")
print(f"1만원권을 제외한 나머지 금액은 {remainder}입니다.")


# In[6]:


base = int(input("밑변의 길이를 정수로 입력하세요.: "))
height = int(input("높이의 길이를 정수로 입력하세요.: "))
area = base * height * 0.5
print(f"넓이는 {area}입니다.")


# In[13]:


#투입한 돈
money = int(input("투입할 돈의 값을 정수로 입력하세요.: "))

#물건 값
price = int(input("물건의 값을 정수로 입력하세요.: "))

#거슴름 돈
remainder = money - price
print(f"거스름 돈은 {remainder}입니다.")

#500원 동전
coin500 = remainder//500
print(f"거스름 돈의 500원 동전은 {coin500}입니다.")

#100원 동전
coin100 = remainder//100
print(f"거스름 돈의 100원 동전은 {coin100}입니다.")

#500원 동전과 100원 동전 동시에 거스름 돈으로 준다.
x = remainder % 500 // 100
print(f"거스름 돈의 500원 동전은 {coin500}이고, 나머지 100원 동전은{x}입니다.")


# In[15]:


#국어 점수
ko = int(input("국어 점수를 입력하세요.: "))

#영어 점수
en = int(input("영어 점수를 입력하세요.: "))

#수학 점수
ma = int(input("수학 점수를 입력하세요.: "))

#과목별 점수
print("====================================================")
print(f"국어 점수: {ko}, 영어 점수: {en}, 수학 점수: {ma}")
print("====================================================")

#총점
total = ko + en + ma
print(f"총점은 {total}입니다.")

#평균
average = (ko + en + ma)/3
print(f"평균은 {average}입니다.")


# In[17]:


#이름
name = input("이름을 입력하세요: ")
#키
tall = int(input("키를 정수로 입력하세요."))
#몸무게
weight = int(input("몸무게를 정수로 입력하세요."))
#BMI
BMI = weight / ((tall/100)**2)

print(f"{name}님의 키는 {tall}이며, 몸무게는 {weight}입니다.\n BMI지수는 {BMI}입니다.")


# In[19]:


#이름
name = input("이름을 입력하세요.: ")

#주민등록번호
id = input("주민등록번호를 -없이 입력하세요.: ")

#몇년생
birth = id[:2]
print(f"{name}님은 {birth}년생 입니다.")

#성별숫자
gender = id[6]
print(f"{name}님의 성별숫자는 {gender}입니다.")


# In[ ]:




