# 1 데이터베이스와 테이블 구축

2023.05.29

## 01. 이번 토픽을 듣기 전에 해야할 일
- 'SQL로 하는 데이터 분석' 토픽 수강
- MySQL, MySQL Workbench 설치

<br/><br/>

## 02. 데이터베이스 생성하기
```SQL
CREATE DATABASE course_rating;
```
course_rating이라는 이름의 데이터베이스 생성

그런데 만약 같은 SQL문을 두 번 실행하면, 에러가 남  
같은 이름의 데이터베이스를 중복해서 생성할 수 없기 때문

```SQL
CREATE DATABASE IF NOT EXISTS course_rating;
```
IF NOT EXISTS: 만약 없다면 실행  
있을 경우 에러 대신 경고 표시  

```SQL
USE course_rating;
```
DBMS에서는 여러 개의 데이터베이스를 다룰 수 있음  
따라서 어느 데이터베이스에서 작업을 할지 지정해줘야 함  
USE 이용해서 지정해주거나, 왼쪽 네비게이터에서 데이터베이스 이름 더블클릭  
사용할 데이터베이스 지정 후에 테이블 생성할 수 있음  

<br/><br/>

## 03. 사용할 데이터베이스 지정히기
USE 사용하면 어느 데이터베이스 사용할 건지 지정할 수 있음  
SELECT문 쓸 때 어느 데이터베이스인지 앞에 이름 지정 안 하고 바로 테이블 이름부터 쓸 수 있음  
만약 USE 쓴 데이터베이스 외의 데이터베이스 조회하려면 (데이버테이스 이름).(테이블 이름)으로 조회할 수 있음  

<br/><br/>

## 04. 테이블 생성하기
MySQL 워크벤치에서 버튼을 이용하여 테이블 생성에 필요한 것 지정하고 Apply 버튼 누르면, 다음과 같은 SQL문이 생성됨  
```SQL
CREATE TABLE `course_rating`.`student` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(20) NULL,
  `student_number` INT NULL,
  `major` VARCHAR(15) NULL,
  `email` VARCHAR(50) NULL,
  `phone` VARCHAR(15) NULL,
  `admission_date` DATE NULL,
  PRIMARY KEY (`id`))
COMMENT = '		';
```  
이 SQL문 실행한 것과 같은 결과  

<br/><br/>

## 05. 컬럼의 데이터 타입에 관하여
- 각 컬럼에 적절한 데이터 타입(Data Type) 설정하는 것 중요함
- 저장 용량 효율적 활용, row 수 많아졌을 때 성능에 영향 미침

### 1. Numeric types(숫자형 타입)
#### (1) 정수형 타입
##### 1) TINYINT
- TINYINT SIGNED: -128 ~ 127
- TINYINT UNSIGNED: 0 ~ 255
- 생략하면 SIGNED가 붙은 것으로 자동 해석됨
##### 2) SMALLINT
- SMALLINT SIGNED: -32768 ~ 32767
- SMALLINT UNSIGNED: 0 ~ 65535
##### 3) MEDIUMINT
- MEDIUMINT SIGNED : -8388608 ~ 8388607
- MEDIUMINT UNSIGNED : 0 ~ 16777215
##### 4) INT
- INT SIGNED : -2147483648 ~ 2147483647
- INT UNSIGNED : 0 ~ 4294967295
##### 5) BIGINT
- BIGINT SIGNED : -9223372036854775808 ~ 9223372036854775807
- BIGINT UNSIGNED : 0 ~ 18446744073709551615
#### (2) 실수형 타입
##### 1) DECIMAL
- DECIMAL(M, D)의 형식으로 나타냄
- 여기서 M은 최대로 쓸 수 있는 전체 숫자의 자리수이고, D는 최대로 쓸 수 있는 소수점 뒤에 있는 자리의 수를 의미
- M은 최대 65, D는 30까지의 값을 가질 수 있음
- DECIMAL이라는 단어 대신 DEC, NUMERIC, FIXED를 써도 됨
##### 2) FLOAT
- -3.402823466E+38 ~ -1.175494351E-38, 0, 1.175494351E-38 ~ 3.402823466E+38 범위의 실수들을 나타낼 수 있는 데이터 타입
##### 3) DOUBLE
- -1.7976931348623157E+308 ~ -2.2250738585072014E-308, 0, 2.2250738585072014E-308 ~ 1.7976931348623157E+308 범위의 실수들을 나타낼 수 있는 데이터 타입
- FLOAT에 비해 범위도 넓고 정밀도도 더 높음

### 2. 날짜 및 시간 타입(Date and Time Types)
#### (1) DATE 
- 날짜를 저장하는 데이터 타입
- 날짜는 ’2020-03-26’ 이런 형식의 연, 월, 일 순으로 값을 나타냄
#### (2) DATETIME
- 날짜와 시간을 저장하는 데이터 타입
- ’2020-03-26 09:30:27’ 이런 식으로 연, 월, 일, 시, 분, 초를 나타냄
#### (3) TIMESTAMP
- 날짜와 시간을 저장하는 데이터 타입
- ’2020-03-26 09:30:27’ 이런 식으로 연, 월, 일, 시, 분, 초를 나타냄
- DATETIME과 다른 점은 타임 존(time_zone) 정보도 함께 저장함
#### (4) TIME 
- 시간을 나타내는 데이터 타입
- ’09:27:31’ 형식으로 ‘시:분:초’를 나타냄

### 3. 문자열 타입(String type)
#### (1) CHAR
- 문자열을 나타내는 기본 타입으로 Character의 줄임말
- 괄호 안의 숫자는 문자를 최대 몇 자까지 저장할 수 있는지를 나타냄
- CHAR 타입의 괄호 안에는 0부터 255까지의 숫자를 적을 수 있음 
#### (2) VARCHAR
- 문자열의 최대 길이를 지정할 수 있는 문자열 타입
- 괄호 안에 최소 0부터 최대 65,535 ($2^{16}$ − 1)를 쓸 수 있음
- CHAR는 고정 길이 타입이고, VARCHAR는 가변 길이 타입
- 사실 VARCHAR라는 단어 자체가 Character Varing의 줄임말로 가변 문자열을 나타냄
- 저장 용량이 설정된 최대 길이에 맞게 고정되는 게 아니라 실제 저장된 값에 맞게 최적화됨
- 대신 VARCHAR 타입으로 값이 저장될 때는 해당 값의 사이즈를 나타내는 부분(1byte 또는 2byte)이 저장 용량에 추가됨
- 따라서 값의 길이가 크게 변하지 않을 컬럼에는 CHAR 타입을 사용하고, 길이가 들쑥날쑥할 컬럼에는 VARCHAR 타입을 쓰는 게 좋음
#### (3) TEXT
- 문자열을 저장하는 데이터 타입으로 최대 65535 자까지 저장할 수 있음
- 이외에도 16,777,215 ($2^{24}$ − 1) 자까지 저장할 수 있는 MEDIUMTEXT, 4,294,967,295($2^{32}$ − 1) 자까지 저장할 수 있는 LONGTEXT 타입이 있음

각 컬럼에 적합한 데이터 타입을 설정하기 위해서는 각 DBMS의 매뉴얼 페이지로 각 데이터 타입에 대해 정확하게 공부해야 함

<br/><br/>

2023.05.30

## 06. 코드잇의 SQL 실행기 사용법!
### ! SQL 실행기를 사용할 때의 주의사항
- 코드잇의 'SQL 실행기'는 사용자가 이미 하나의 데이터베이스를 선택했다고 가정한 상태에서 작동함 
- 따라서 테이블을 나타낼 때는, 테이블 이름만 적어야 하고, 데이터베이스 이름은 적으면 안 됨

<br/><br/>

## 07. CREATE TABLE문 설명
```SQL
CREATE TABLE `course_rating`.`student` (    # course_rating 데이터베이스에 student 테이블을 생성하라
  # 각 컬럼의 이름과 데이터 타입, 속성
  `id` INT NOT NULL AUTO_INCREMENT,    
  `name` VARCHAR(20) NULL,    # NULL은 생략 가능
  `student_number` INT NULL,
  `major` VARCHAR(15) NULL,
  `email` VARCHAR(50) NULL,
  `phone` VARCHAR(15) NULL,
  `admission_date` DATE NULL,
  PRIMARY KEY (`id`))    # id 컬럼을 Primary key로 지정. 이 줄 대신, 'id' 컬럼의 속성에 PRIMARY KEY 추가해도 됨 
COMMENT = '		';
```  

<br/><br/>

## 08. 백틱과 따옴표 이야기
SQL문 컬럼 이름에 \` 붙어있고, \`기호의 정식 명칭은 백틱(backtick)  
DBMS에서는 데이터베이스, 테이블, 컬럼 등과 같은 구성요소를 보통 object(객체)라고 하고, 이런 object에 붙여준 이름을 identifier(식별자)라고 함  
MySQL에서 백틱은 해당 단어가 identifier임을 나타내는 기호  
백틱을 쓰면 어느 단어가 사용자가 직접 이름을 지은 부분인지 확실하게 나타낼 수 있고, SQL 문법에 정해진 키워드로 이름을 지을 때는 백틱 필수  
작은따옴표, 큰따옴표는 문자열 값을 나타낼 때 사용

<br/><br/>

2023.06.04

## 09. 테이블에 row 추가하기 I
```SQL
INSERT INTO student
    (id, name, student_number, major, email, phone, admission_date)
    VALUES (1, '성태후', 20142947, '컴퓨터공학과',
        'taehos@naver.com', '010-7373-1234', '2014-03-12');
```
- student 테이블에 삽입하라
- 추가할 데이터의 컬럼
- 컬럼에 삽입할 값들

테이블에 정의된 모든 컬럼의 데이터를 삽입할 때에는, 컬럼 이름 쓰는 부분 생략해도 됨

<br/><br/>

## 10. 테이블에 row 추가하기 II
- row를 추가할 때, 컬럼 중 일부를 생략하고 삽입할 수 있음
- 삽입하지 않은 컬럼 값은 NULL로 추가됨
- primary key이면서 auto_increment 속성을 가지고 있는 id 컬럼은 값을 주지 않아도 자동으로 MySQL에서 이전 row보다 1 증가한 값으로 추가

<br/><br/>

2023.06.05

## 11. 데이터베이스와 테이블 생성 퀴즈

질문 1  
정답 : USE  
USE [데이터베이스 이름];은 해당 데이터베이스를 사용하겠다고 지정하는 SQL 문입니다. 이렇게 사용할 데이터베이스를 지정하고나면, 그 데이터베이스 안에 있는 테이블은 테이블 이름만으로도 가리킬 수 있게 됩니다. 

질문 2  
정답 : 2번  
테이블의 Primary Key는 반드시 NOT NULL 속성을 함께 가져야합니다. 그리고 보통 Primary Key는 정수형으로 설정하고 AUTO_INCREMENT 속성을 주는 게 일반적입니다. 참고로, AUTO_INCREMENT 속성은 정수형 데이터 타입의 컬럼에만 설정할 수 있습니다. 

질문 3  
정답 : 1번  
MySQL에서 SQL 문을 쓸 때 어떤 단어가 SQL 상의 키워드가 아닌 테이블 이름, 컬럼 이름 등이라는 것을 분명하게 나타내고 싶을 때는 백틱(backtick, \`)을 써주면 됩니다.
