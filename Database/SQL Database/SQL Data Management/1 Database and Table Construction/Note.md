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
