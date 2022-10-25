2022.08.11

카카오페이에서 데이터 분석가로 활동하고 계시는 성균관대학교 의상학과 11학번 선배님의 온라인 클래스를 들었다.  
관심있던 웹개발 직무 외에 데이터 분석가 직무에 대한 많은 이야기를 들을 수 있었다.  
가장 인상깊은 것은 정말 열심히 사신다는 것.  
SQL 쿼리 관련 엄청난 노력을 통해 기본기를 갖추고 현장에서 매일 새벽까지 일하면서 쌓은 내공을 엿볼 수 있었다.  
네카라쿠배 가는 게 절대로 절대로 내가 생각한 것만큼 쉽지 않다고 느껴졌다.  
열심히 준비해서 꿈을 이룰 수 있게 되면 좋겠다.  
화이팅!!  


2022.10.25
```python
makers = []
first_products = []
revised_products = []

def teach(n):
    for i in range(n+1):
        makers.append(i)
    return makers

def first_production(makers):
    for maker in makers:
        first_products.append(100-20*maker)
    return first_products

def revised_production(products):
    for i in range(len(makers)):
        revised_products.append(first_products[i]-10*makers[len(makers)-i-1])
    return revised_products

def simulation(n):
    global makers
    makers = []
    global first_products
    first_products = []
    global revised_products
    revised_products = []
    print(teach(n))
    print(first_production(makers))
    print(revised_production(first_products))
    print(sum(revised_products))
    print()
    
for i in range(6):
    simulation(i)
```
자료해석과상황판단 중간고사 대체과제로 PAST 문제 풀고 있었는데, 알고리즘 같은 문제 나와서 검산 위해 코딩해봤다.  
그런데 오랜만에 파이썬으로 코드 짜서 그런지 너무 지저분하게 짰고 별로 마음에 안 든다.  
코딩 꾸준히 열심히 해야지.  
화이팅!
