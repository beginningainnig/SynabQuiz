#!/usr/bin/env python
# coding: utf-8

# In[4]:


digits_kor = ["", "일", "이", "삼", "사", "오", "육", "칠", "팔", "구"] #한글 숫자 리스트 
units_kor = ["천", "백", "십", ""] #천백십단위 한글 단위 리스트
units = {3: '조 ', 7: '억 ', 11: '만 '} #특정 자릿수에 할당되는 한글 단위 딕셔너리
def num_to_korean(num_str):
    # 쉼표 제거 및 '원' 제거
    num_str = num_str[:-1].replace(",", "")
    
    # 문자열을 정수로 변환
    num = int(num_str, 10)
    
    # 범위 체크
    if not (1 <= num <= 100000000000000):
        return "이체범위를 벗어났습니다"
    
    # 16자리로 맞추기
    num_str = num_str.rjust(16, '0')
    
    # 결과를 저장할 리스트
    korean_buffer = []
    
    # 숫자 문자열을 순회하면서 처리
    for idx, ch in enumerate(num_str):
        digit = int(ch, 10)
        
        # 현재 자릿수에 대한 한글 표현 추가
        if digit > 0:
            korean_buffer.append(digits_kor[digit] + units_kor[idx % 4])
            
        # 특정 자릿수에 대한 한글 표현 추가
        if (idx in units) and int(num_str[idx - 3:idx + 1], 10) > 0:
            korean_buffer.append(units[idx])
    
    # 최종 결과 문자열 생성
    korean_str = "".join(korean_buffer).strip().replace("일천", "천").replace("일백", "백").replace("일십", "십") + "원"
    
    # 일만, 십일만, 백일만, 천일만 중복된 표현 수정
    if ("십일만" not in korean_str) and ("백일만" not in korean_str) and ("천일만" not in korean_str):
        korean_str = korean_str.replace("일만", "만")
        
    return korean_str

amounts = ["1원", "4원", "8원", "9원", "10원",
"17원", "79원", "80원", "95원", "205원",
"809원", "851원", "878원", "2,000원", "2,800원",
"7,008원", "8,174원", "9,718원", "45,150원", "50,000원",
"69,700원", "382,915원", "431,409원", "921,500원", "5,003,052원",
"5,039,670원", "6,835,623원", "8,000,000원", "10,000,003원", "35,100,000원",
"39,997,777원", "90,021,015원", "93,275,690원", "403,197,000원",
"459,176,461원", "730,080,000원", "999,999,000원", "6,887,000,000원",
"7,000,020,000원", "7,700,000,500원", "7,848,761,270원", "38,048,620,625원",
"57,000,000,000원", "74,778,562,249원", "97,417,165,814원", "101,000,120,000원",
"343,000,000,000원", "458,807,907,862원", "872,818,015,000원", "6,278,000,015,000원",
"7,991,000,844,000원", "9,000,400,000,675원", "22,018,914,675,100원",
"78,196,000,000,000원", "85,000,904,224,858원", "95,000,000,404,918원"]

total_score = 0

for amount in amounts:
    kr_str = read_num(amount)
    num_words = len(kr_str.split())
    num_chars = len(kr_str.replace(" ", ""))
    total_score += (num_words * num_chars)

print(total_score)

