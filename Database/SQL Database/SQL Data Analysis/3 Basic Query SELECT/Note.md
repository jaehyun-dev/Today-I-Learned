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

<br/><br/>

2023.02.16

## 10. 데이터 조회 퀴즈

질문 1  
SELECT 문에서 특정 row를 선별해서 조회할 때는 WHERE 절을 사용한다는 사실, 꼭 기억하세요!

질문 2  
특정 구간을 조건으로 걸고 싶을 때는, BETWEEN a AND b(a부터 b까지) 구문을 사용하면 됩니다.

질문 3  
LIKE를 사용해서 문자열 패턴이 매칭되는 컬럼의 값을 가진 row들을 조회하려고 한다면, %(임의의 길이를 가진 문자열), \_(한 자리의 문자)의 의미를 잘 기억하셔야 합니다.

질문 4  
조건을 걸 때 OR이 너무 많아질 때는 혹시 그 대신에 IN을 사용할 수 있지는 않을지 고민해보세요.

질문 5  
Unix Timestamp는 1970년 1월 1일을 기준으로 특정 날짜, 시간까지 경과된 초로 그 날짜, 시간을 나타내는 표현법입니다. 유닉스 계열의 운영체제에서 시간을 나타나기 위해 주로 사용되는 Unix TImestamp는 데이터베이스 뿐만 아니라 그 자체로도 IT 분야에서 중요한 개념입니다. 만약 Unix Timestamp로 보이는 값을 만나면 MySQL에서는 FROM_UNIXTIME(Unix Timestamp 값) 함수를 써서 사람이 해석할 수 있는 형식의 날짜, 시간으로 변환할 수 있다는 사실을 기억하세요.

질문 6  
WHERE 절에서 AND가 OR보다 더 먼저 실행된다는 사실을 잘 기억하세요. 그리고 되도록이면 먼저 실행되기를 원하는 조건은 괄호로 묶는 것이 좋습니다.

<br/><br/>

## 11. 데이터 조회 실습
```MySQL
SELECT * 
FROM member 
WHERE (age BETWEEN 20 AND 29) AND (MONTH(sign_up_day) = 7);
```

<br/><br/>

## 12. 문자열 패턴 매칭 조건을 사용할 때 주의할 점
### 1. 이스케이핑(escaping) 문제
- 원래 특정 의미('임의의 길이를 가진 문자열')를 나타내던 문자(%)를 그 특정 의미가 아니라, 일반적인 문자처럼 취급하는 행위를 이스케이핑(escaping)이라고 함  
- 어떤 문자가 그것에 부여된 특정한 의미, 기능으로 해석되는 게 아니라 그냥 단순한 문자 하나로 해석되도록 하는 것을 이스케이핑이라고 함  
- 앞에 역슬래쉬(백슬래쉬, backslash) 기호(\)를 붙여 표현식이 아닌 문자로 해석할 수 있음

### 2. 대소문자 구분 문제
- 테이블에 적용된 기본 설정에서 Table collation 항목이 utf8mb4_0900_ai_ci로 설정되어 있으면 대소문자 구분되지 않음
- ci는 case-insensitive의 약자로 문자열이 동일한지 확인할 때, 대소문자를 구별하지 않겠다는 뜻
- LIKE와 표현식 사이에 BINARY를 입력하면 대소문자 구분할 수 있음(알파벳은 같지만 0과 1이 정확히 일치하지 않음)

<br/><br/>

## 13. 데이터 정렬해서 보기
### 정렬
- 'row들을', '특정 컬럼을 기준으로', '순서대로 출력'하는 것
- SELECT ~~ ORDER BY column_name;
- 기본적으로 작은 순서대로 오름차순
- MySQL은 NULL을 가장 작은 값으로 처리
- ORDER BY column_name ASC; ascending의 약자, 오름차순. 생략 가능
- ORDER BY column_name DESC; descending의 약자, 내림차순
- WHERE이 먼저 나오고 그 다음 ORDER가 나와야 함
- 콤마로 구분해서 여러 column을 기준으로 정렬할 수도 있음
- 이름을 먼저 쓴 컬럼을 우선으로 해서 정렬이 차례대로 수행됨

<br/><br/>

## 14. 문자열 형 데이터 정렬
- 정렬 기준의 데이터 타입이 숫자형(INT 등)인 경우와 문자열형(TEXT 등)인 경우에 따라 정렬 결과 달라짐  
- 숫자: 19, 27, 120, 230(숫자 크기 비교함)
- 문자: 120, 19, 230, 27(맨앞에서부터 한 글자씩 비교함)
- CAST() 함수 사용하여 임시로 데이터 타입 바꿀 수 있음
- TEXT 타입 컬럼의 숫자값들을 숫자형 타입으로 보고 정렬하려면, ORDER BY CAST(data AS signed)와 같이 쓸 수 있음
- signed는 양수 음수 포함하는 정수, decimal은 실수
- 숫자를 문자처럼 비교하려면 char

<br/><br/>

## 15. 데이터 일부만 추려보기
- 쿼리문 마지막에 LIMIT a 추가하면 현재 조회된 로우들 중에서 a개만 추려서 보여달라는 뜻  
- LIMIT a, b: a번째 로우부터 시작해서 b개만 추려서 보여달라는 뜻
- row는 0번째부터 시작

<br/><br/>

## 16. 데이터 정렬 퀴즈

질문 1  
문자열 패턴이 일치하는지 비교하는 조건을 설정할 때는 이스케이핑에 유의해야 합니다. 이스케이핑을 하려면 역슬래쉬(\)를 해당 문자 앞에 써주면 된다는 사실, 잘 기억하세요!

질문 2  
문자열 비교를 할 때 대소문자 구분을 확실하게 하고 싶다면 문자열 패턴 표현식 앞에 BINARY라고 써주면 됩니다.

질문 3  
정렬을 할 때 오름차순은 ASC, 내림차순은 DESC로 나타냅니다. 그리고 더 먼저 적용되어야 하는 정렬 기준을, 더 앞에 적어줘야 합니다.

질문 4  
현재 보기의 각 키워드들은 FROM - WHERE - ORDER BY - LIMIT 순으로 써야합니다. 이런 순서는 SQL 문을 자주 쓰다보면 자연스럽게 익힐 수 있습니다.

질문 5  
CAST() 함수는 특정 데이터 타입의 컬럼에 저장된 값을, 일시적으로 다른 데이터 타입으로 변경할 수 있게 해주는 함수입니다. signed는 양과 음의 정수를 나타내는 데이터 타입입니다.

질문 6  
LIMIT은 row들 중 일부만을 추려서 보게 해주는 키워드로, ORDER BY와 함께 자주 사용됩니다.

질문 7  
LIMIT은 크게
1. LIMIT (row의 개수)
2. LIMIT (첫 번째 row를 기준으로 한 시작 Offset, row의 개수)

이 두 가지 사용 방식이 있습니다. 
이때 (2)에서 첫 번째 인자는,

가장 첫 번째 row가 0, 
두 번째 row가 1, 
세 번째 row가 2 ...

이라는 사실을 잘 기억하셔야 합니다.

<br/><br/>

## 17. 데이터 정렬 실습
```MySQL
SELECT * 
FROM review 
ORDER BY star ASC, registration_date DESC LIMIT 5;
```
또는
```MySQL
SELECT * 
FROM review 
ORDER BY star ASC, registration_date DESC LIMIT 0, 5;
```
ORDER BY star ASC, registration_date DESC 라고 써주면 별점 기준으로 오름차순, 그리고 같은 별점 안에서는 등록일자 기준으로 내림차순 정렬될 겁니다.

그리고 이렇게 정렬된 row들을 대상으로 LIMIT 5 또는 LIMIT 0, 5를 적용하면 문제의 답을 구할 수 있겠죠?
