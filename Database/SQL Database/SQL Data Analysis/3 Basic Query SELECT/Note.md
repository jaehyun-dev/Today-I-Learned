# 3 데이터 조회로 기본 다지기

2023.02.13

## 01. 코드잇의 SQL 실행기 사용법!
- 코드잇 웹페이지 SQL 실행기를 사용할 때 데이터베이스 이름은 빼고 테이블 이름만 쓰기

<br/><br/>

## 02. 데이터 조회의 핵심, SELECT와 WHERE
### SELECT
- '테이블의 데이터를', '조회할 때' 사용하는 구문
```SQL
SELECT * FROM copang_main.member;
```

- \*는 모든 것 지칭. \* 대신 email, age, address 등 컬럼 이름 넣으면 해당 데이터만 보임  
- 즉 SELECT 바로 뒤에는 보고 싶은 컬럼의 이름들을 적어주는 위치
- From 다음에는 데이터를 조회하고 싶은 테이블의 이름을 써주는 위치
- 위 SQL문 해석해보면, copang_main 데이터베이스의 member 테이블에서 모든 컬럼 데이터를 보여달라는 뜻

### WHERE
- 특정 조건을 설정하는 구문
```SQL
SELECT * FROM copang_main.member WHERE email = 'taehos@hanmail.net';
```
- 특정 조건을 만족하는 로우들만 조회할 때 사용

<br/><br/>

## 03. SQL 작성 형식에 관한 이야기
1. SQL문 끝에는 항상 세미콜론(;)을 써줘야 함
2. SQL문 안에는 공백이나 개행 등을 자유롭게 넣을 수 있음(가독성 향상)
3. SQL문에서 예약어(SELECT, FROM 등)는 대문자로 쓰기(관례)
4. 데이터베이스 이름은 상황 따라 생략도 가능(USE로 데이터베이스 지정하고 생략 가능)

<br/><br/>

## 04. 조건을 나타내는 다양한 방법
- 부등호(<, >): 작거나 큰 범위 설정
- BETWEEN A AND B: A부터 B까지 범위 설정
- NOT: 뒤의 조건이 아닌 범위 설정
- DATE 형식의 데이터도 부등호, BETWEEN 사용하여 범위 설정할 수 있음

<br/><br/>

## 05. 문자열 패턴 매칭 조건
### LIKE, %
```SQL
SELECT * FROM member WHERE address LIKE '서울%';
```
- address 데이터의 문자열의 첫 부분이 '서울'로 시작하고 그 뒤에 임의의 길이를 가진 문자열 있는 모든 데이터 조회
- '%ABC%': 문자열 'ABC'가 포함된 모든 문자열

<br/><br/>

## 06. 그밖에 알아야할 조건 표현식
1. 같지 않음(!=, <>)
2. 이 중에 있는~ (IN(A, B, C))
3. 한 글자를 나타내는 _

<br/><br/>

## 07. DATE 데이터 타입 관련 함수
### 1. 연도, 월, 일 추출하기
YEAR, MONTH, DAYOFMONTH

### 2. 날짜 간의 차이 구하기
DATEDIFF(A, B)

오늘 날짜: CURDATE()

### 3. 날짜 더하기 뺴기
- DATE_ADD(A, INTERVAL 300 DAY)
- DATE_SUB(B, INTERVAL 250 DAY)

### 4. UNIX Timestamp 값
- 특정 날짜의 특정 시간을 1970년 1월 1일을 기준으로, 총 몇 초가 지났는지 나타낸 값
- UNIX_TIMESTAMP(A): A를 UNIX Timestamp 값으로 변환
- FROM_UNIXTIME(B): B를 일반적인 날짜 시간으로 변환

### 5. 기타
- 날짜, 시간 관련 데이터 타입 : https://dev.mysql.com/doc/refman/8.0/en/date-and-time-types.html
- 날짜, 시간 관련 함수 : https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html

<br/><br/>

2023.02.14

## 08. 여러 개의 조건 걸기
### AND
```SQL
SELECT * FROM member
WHERE gender = 'm'
    AND address LIKE '서울%'
    AND age BETWEEN 25 and 29;
```

### OR
```SQL
SELECT * FROM member
WHERE MONTH(sign_up_day) BETWEEM 3 AND 5
    OR MONTH(sign_up_day) BETWEEN 9 AND 11;
```

### AND OR
```SQL
SELECT * FROM member
WHERE (gender = 'm' AND height >= 180)
    OR (gender = 'f' AND height >= 170);
```
먼저 실행해야 할 부분은 괄호로 묶어주면 좋음

<br/><br/>

2023.02.15

## 09. 여러 조건을 걸 때 주의할 점
### 1. OR를 사용할 때의 주의사항
```MySQL
~ WHERE id = 1 OR id = 2
```
이렇게 적어야 하는데, 
```MySQL
~ WHERE id = 1 OR 2
```
이렇게 적으면 안 됨. 0 이외의 모든 숫자는 TRUE이기 때문에, 모든 row 출력됨

### 2. AND와 OR 간의 우선순위
AND가 OR보다 우선순위가 높음.  
그러나 괄호가 AND보다 우선순위가 높기 때문에, 먼저 실행되기를 원하는 조건을 괄호로 씌워주면 됨
