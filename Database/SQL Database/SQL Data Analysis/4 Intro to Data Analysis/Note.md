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
