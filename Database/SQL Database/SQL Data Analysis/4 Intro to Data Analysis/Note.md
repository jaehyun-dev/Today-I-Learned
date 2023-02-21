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

<br/><br/>

2023.02.20

## 13. 고유값만 보기
### DISTINCT()
컬럼의 로우들에 다양한 값이 있는데 중복 없이 고윳값만 보여줌
```MySQL
SELECT DISTINCT(gender) FROM member;
```

### SUBSTRING
- 문자열의 입루를 추출하는 함수
```MySQL
SELECT DISTINCT(SUBSTRING(address, 1, 2)) FROM member;
```
- address 컬럼에 있는 값에서 가장 첫 번째 문자부터 시작해서 총 두 개의 문자를 추출하라는 뜻

<br/><br/>

## 14. 문자열 관련 함수들
### 1. LENGTH() 함수
- 문자열의 길이를 구해줌

### 2. UPPER(), LOWER() 함수
- 문자열을 모두 대문자 또는 소문자로 바꿔서 보여줌

### 3. LPAD(), RPAD() 함수
- LEFT(또는 RIGHT) + PADDING(채우기라는 뜻)의 줄임말
```MySQL
SELECT emal, LPAD(age, 10, '0') FROM member;
```
- age 왼쪽에 0을 10개 붙여라
- 문자열에 숫자 넣으면 자동으로 문자열로 형 변환 됨

### 4. TRIM(), LTRIM(), RTRIM() 함수
- 문자열의 왼쪽, 오른쪽 공백(스페이스)을 제거하는 함수


<br/><br/>

## 15. 그루핑해서 보기 I
```MySQL
SELECT
    gender,
    COUNT(*),
    AVG(height),
    MIN(weight)
FROM member
GROUP BY gender;
```
특정 칼럼을 기준으로 그루핑을 하면, 처음에는 DISTINCT 함수처럼 고윳값만 보이지만, 사실 해당 그룹으로 묶인 row가 안에 다 들어가있는 상황.  
그루핑을 한 후 집계함수 등을 쓰면 그룹별로 특성을 파악할 수 있음

<br/><br/>

## 16. 그루핑해서 보기 II
```MySQL
SELECT
    SUBSTRING(address, 1, 2) AS region,
    gender,
    COUNT(*)
FROM member
Group BY
    SUBSTRING(address, 1, 2),    
    gender;
```
컬럼을 가공하여 원하는 적절한 그루핑 가능함  
그루핑 기준을 여러 개 사용할 수 있고, 세분화된 그루핑이 가능함

<br/><br/>

## 17. 그루핑해서 보기 III
### HAVING
```MySQL
SELECT
    SUBSTRING(address, 1, 2) AS region,
    gender,
    COUNT(*)
FROM member
Group BY
    SUBSTRING(address, 1, 2),    
    gender
HAVING region = '서울';
```
- 지역을 '서울'로 가지고 있는 그룹만 보여주기
- HAVING 뒤에 조건을 추가하여 원하는 그룹만 볼 수 있음

### WHERE과 HAVING의 차이점
- WHERE: 테이블에서 맨 처음 로우들을 조회할 때 조건을 설정하기 위한 구문
- HAVING: 이미 조회된 로우들을 다시 그루핑하여 생성된 그룹들 중에서 다시 필터링을 할 때 쓰는 구문

### 특정 그룹을 제외하고 싶으면
```MySQL
HAVING region IS NOT NULL
```
과 같이 쓸 수 있음

#### 그루핑 후 정렬하면 더 깔끔하게 볼 수 있음

<br/><br/>

2023.02.21

## 18. GROUP BY를 쓸 때 지켜야하는 규칙

SELECT 절에는  
1. GROUP BY 뒤에서 사용한 컬럼들 또는
2. COUNT(), MAX() 등과 같은 집계 함수만  

쓸 수 있음  

즉,  
1. GROUP BY 절 뒤에 쓴 컬럼 이름들만, SELECT 절 뒤에도 쓸 수 있다.
2. 대신 SELECT 절 뒤에서 집계 함수에 그 외의 컬럼 이름을 인자로 넣는 것은 허용된다.

<br/><br/>

## 19. 그루핑해서 보기 퀴즈

질문 1  
해설: 특정 컬럼에 존재하는 고유한 값들을 보려면 해당 컬럼 이름 앞에 DISTINCT를 붙여주면 됩니다. DISTINCT는 '고유한' 이라는 뜻을 갖는 영어 단어입니다. 외우기 쉽죠?

질문 2  
해설: 문자열의 공백을 제거하는 함수에는 LTRIM()(왼쪽 공백 제거), RTRIM()(오른쪽 공백 제거), TRIM()(양쪽 공백 제거)이 있습니다.

질문 3  
해설: GROUP BY 뒤에는 그루핑 기준으로 사용할 컬럼들의 이름을 여러 개 적어줄 수 있습니다. 큰 덩어리로 그루핑하고 싶으면 그루핑 기준을 조금만 적어주고, 아주 상세한 수준까지 그루핑하고 싶다면 많이 적어주면 되겠죠?

질문 4  
해설: GROUP BY로 그루핑을 하고 난 후, 생성된 그룹들 중에서 특정 그룹들만 선별하려면 HAVING 절을 사용해야 합니다. 간혹, 이 HAVING 절과 WHERE 절을 혼동하시는 분들이 있는데요.  
WHERE 절은 SELECT 문에서 맨 처음에 row들을 필터링 할 때 쓰이고, 그 후로 그루핑까지 거친 후에야 HAVING 절에서 그 그룹들을 필터링하는 겁니다.

질문 5  
해설: FROM - WHERE - GROUP BY - HAVING - SELECT - ORDER BY - LIMIT  
SELECT 문 안의 각 절이 실행되는 순서는 그것의 작성 순서와는 다릅니다. 각 절의 실행 순서를 모르는 상태에서는 SQL 문이 조금만 길어지고 복잡해져도 혼동하기 쉽습니다. 각 절의 실행 순서를 정확하게 숙지하고 SQL 문을 본다면 그 의미가 자연스럽게 잘 이해될 겁니다.
