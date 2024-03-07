#!/usr/bin/env python
# coding: utf-8

# In[1]:


def col_name(col_number):
    col_name = ""
    while col_number > 0:
        col_number -= 1  # 나머지가 0일 때 몫을 줄이기 위해 1을 빼줌
        pre_number = col_number % 26  # 26으로 나눈 나머지 pre_number
        
        # 아스키코드 활용해 알파벳 할당
        col_name = chr(65 + pre_number) + col_name
        
        col_number //= 26  # col_number를 26으로 나눈 몫이 다시 col_number이 됨

    return col_name

# 사용자로부터 숫자 입력 받기
number = int(input("숫자를 입력하세요: "))

# 입력된 숫자에 대응되는 스프레드시트 컬럼 출력
result = col_name(number)
print(f"{number}에 대응되는 스프레드시트 컬럼: {result}")


# In[ ]:




