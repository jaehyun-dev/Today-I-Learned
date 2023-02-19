# 4 데이터 분석 단계로 나아가기

2023.02.17

## 01. 데이터 특성 구하기

### COUNT
- row의 개수 구할 수 있음
```MySQL
SELECT COUNT(email) FROM member;
```
- email column을 기준으로 row가 몇 개 있는지  
- 이때, NULL은 개수에 포함되지 않음
```MySQL
SELECT COUNT(*) FROM member;
```
- 이렇게 하면 특정 column이 아니라 SELECT문에 의해 리턴되는 전체 로우 수 알려줌

### MAX, MIN
```MySQL
SELECT MAX(height) FROM member;
```
```MySQL
SELECT MIN(height) FROM member;
```
- 해당 column값 중 가장 큰값(MAX) 또는 작은값(MIN) 보여줌

### AVG
```MySQL
SELECT AVG(height) FROM member;
```
- 해당 column의 평균값 보여줌
- 평균을 계산할 때 NULL은 제외함

<br/><br/>

2023.02.18

## 02. 집계 함수와 산술 함수

### Aggregate Function(집계 함수)
- COUNT(개수), MAX(최댓값), MIN(최솟값), 평균값(AVG) 처럼 어떤 컬럼의 값들을 대상으로 원하는 특징을 구해주는 함수를 Aggregate Function, 집계 함수라고 함.
- SUM(합), STD(표준편차) 함수 등도 있음

### Mathematical Function(산술 함수)
- 산술 연산을 해주는 함수
- ABS(절댓값)
- SQRT(제곱근)
- CEIL(올림)
- FLOOR(내림)
- ROUND(반올림)

### 집계 함수와 산술 함수의 차이
1. 집계 함수는 특정 컬럼의 여러 row의 값들을 동시에 고려해서 실행되는 함수
2. 산술 함수는 특정 컬럼의 각 row의 값마다 실행되는 함수

<br/><br/>

## 03. NULL을 다루는 방법

### NULL값 다루기
특정 컬럼에 NULL이 있는 row를 추출하기
```MySQL
SELECT * FROM member WHERE address IS NULL;
```

특정 컬럼 값이 NULL이 아닌 row만 보려면
```MySQL
SELECT * FROM member WHERE address IS NOT NULL;
```
값이 들어있는 row들만 출력됨  

이처럼 NULL값 제외하려면 IS NOT NULL 쓰면 됨

### COALESCE
- 개발자가 아닌 다른 직군 사람들이 NULL의 의미를 이해하지 못할 수 있으니, NULL을 다른 단어로 바꿔줘야 할 수도 있음
- NULL을 다른 단어로 바꾸는 여러 방법이 있는데 그 중 하나는 COALESCE(합치다)
```MySQL
SELECT
    COALESCE(height, '####')
FROM member;
```
COALESCE에는 2개의 인자가 들어가는데, 첫 번째 인자는 그 값을 살펴보고, NULL이 아니면 그대로, NULL이라면 두 번째 인자를 출력

<br/><br/>

## 04. NULL에 관해 알아야하는 사실
### 1. IS NULL 과 = NULL은 다릅니다.
- IS NULL을 = NULL로 적는 경우가 있는데, NULL은 어떤 값이 아니기 때문에 등호로 비교할 수 없음  
- IS NULL이라는 키워드가 존재하는 이유  
- = NULL로 적으면 모든 row가 TRUE가 될 수 없기 때문에 아무 row도 출력되지 않음
- != NULL, <> NULL 등도 IS NOT NULL로 적어야 함

### 2. NULL에는 어떤 연산을 해도 결국 NULL이다.

<br/><br/>

## 05. 이상한 값을 제외하고 싶다면?
- 데이터의 특성 값을 구할 때는 기존 데이터 중에서 이상한 값들은 제외하고 구해야 함  
- 예를 들어 음수 나이, 100살이 넘어가는 나이 등은 BETWEEN A AND B를 이용해 제외하고 원하는 범위 안에서 계산할 수 있음
- WHERE address LIKE '%호' 를 이용해 '~호'로 끝나지 않는 주소를 걸러낼 수 있음

<br/><br/>

## 06. 데이터 분석 퀴즈

질문 1  
해설: 특정 컬럼의 값들 중 최대값을 구해주는 집계 함수는 MAX() 함수입니다.

질문 2  
해설:  
집계 함수와 산술 함수는 함께 사용할 수도 있습니다. 위 문제의 답을 구하려면, AVG(price)의 결과값에 ROUND() 함수를 적용하면 해결하면 되겠죠?  
2번 보기는 각 price 값에 반올림을 적용하고, 그 반올림한 값들의 평균값을 구하는 것이기 때문에 오답입니다.

질문 3  
해설: NULL에는 어떤 연산을 해도 그 결과가 NULL입니다. 이 사실을 잘 기억하세요.

퀴즈 4  
해설: COALESCE() 함수를 사용하면 NULL을 다른 값으로 변환해서 표시할 수 있습니다.

<br/><br/>

## 07. 데이터 분석 실습
### 해설
일단 comment 컬럼이 NULL이 아닌 row들만 조회하고 그 row들의 개수, 그리고 그 row들의 별점의 평균값을 구해야 합니다. 별점 평균값을 반올림하려면 ROUND() 산술 함수를 사용하면 되겠죠?

### 모범 답안
```MySQL
SELECT COUNT(*),
       ROUND(AVG(star)) 
FROM review 
WHERE comment IS NOT NULL; 
```

<br/><br/>

2023.02.19

## 08. 컬럼끼리 계산하기
컬럼끼리 산술계산 할 수 있음
- +(더하기)
- -(뺴기)
- \*(곱하기)
- /(나누기)
- %(나머지 구하기)

```MySQL
SELECT email, height, weight, weight / ( (height/100) * (height/100) )
FROM member;
```

식 중에 하나라도 NULL이면 결괏값도 NULL로 표시됨

<br/><br/>

## 09. 컬럼에 alias 붙이기

### Alias(별명, 멸칭)
원래의 컬럼 이름을 다른 이름으로 교체하는 방법(alias 붙이기)
```MySQL
SELECT
    email,
    height AS 키,
    weight AS 몸무게,
    weight / ( (height/100) * (height/100) ) AS BMI
FROM member;
```
AS 안 쓰고 컬럼 이름 뒤에 스페이스 하나 띄우고 alias 써도 됨  
되도록이면 AS 쓰는 게 안 헷갈림

### CONCAT
concatenate(연결하다)의 줄임말  
```MySQL
SELECT
    email,
    CONCAT(height, 'cm', ', ', weight, 'kg') AS '키와 몸무게',
    weight / ( (height/100) * (height/100) ) AS BMI
FROM member;
```

<br/><br/>

## 10. 컬럼의 값 변환해서 보기

### CASE
```MySQL
SELECT ..., 

CASE
    WHEN ... THEN ___
    WHEN ... THEN ___
    ELSE ___
END

FROM member;
```
CASE도 하나의 컬럼이 됨

<br/><br/>

## 11. 컬럼 자유롭게 다루기 퀴즈

질문 1  
해설: 컬럼에 alias를 붙일 때는 '원래의 컬럼 이름'과, alias 사이에 AS 또는 스페이스를 써주면 됩니다.

질문 2  
해설:  
CASE() 함수는
```MySQL
CASE
    WHEN 조건1 THEN 해당 조건이 TRUE일 때 보여줄 값
    WHEN 조건2 THEN 해당 조건이 TRUE일 때 보여줄 값
    WHEN 조건3 THEN 해당 조건이 TRUE일 때 보여줄 값
    ELSE 그 밖의 모든 경우
END
```
의 형식으로 작성한다는 사실을 잘 기억하세요.

<br/><br/>

## 12. 컬럼 자유롭게 다루기 실습
```MySQL
SELECT name,
       price,
       price/cost,
       (CASE 
            WHEN price/cost >= 1 AND price/cost < 1.5 THEN 'C. 저효율 메뉴'
            WHEN price/cost >= 1.5 AND price/cost < 1.7 THEN 'B. 중효율 메뉴'
            WHEN price/cost >= 1.7 THEN 'A. 고효율 메뉴'
        END) AS efficiency
FROM pizza_price_cost
ORDER BY efficiency DESC, price ASC
LIMIT 6;
```
