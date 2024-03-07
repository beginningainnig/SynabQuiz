#!/usr/bin/env python
# coding: utf-8

# In[1]:


def solve():
    A=[0, 0, 1, 8, 2, 2, 8, 9, 0, 3, 4, 0, 0]
    A.sort() #리스트 오름차순 정렬
    
    i = A.count(0) #0 몇개인 지 count => i개 (자리수)
    
    #리스트 길이보다 0 개수가 더 크면 -1 반환
    #0 이외의 숫자 중에서 최소 두 개의 숫자를 선택
    if len(A) < i+2 :
        return -1
    
    #0이 아닌 두 개 + 0의 개수만큼의 0 + 나머지 숫자 추출해 새로운 리스트 저장
    A = A[i:i+2] + [0]*i + A[i+2:]
    
    count=0 
    i=1    #초기화 
    
    
    #리스트 마지막 두 요소를 꺼내 더한 후 
    #자리수 i 업데이트 (*10)
    #count에 현재 자리수를 곱한 값을 더한다
    #count 반환
    while len(A) > 2:
        count+=(A.pop()+A.pop())*i
        i*=10
        
    count+=sum(A)*i
    return count

solve()

