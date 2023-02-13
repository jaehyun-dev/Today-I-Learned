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
