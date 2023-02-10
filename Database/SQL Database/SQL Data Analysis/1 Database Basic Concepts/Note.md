# 1 데이터베이스 기본 개념

2023.02.09

## 01. 데이터베이스와 테이블

### 데이터베이스
- 일정한 체계 속에 저장된 데이터의 집합

### 테이블
- 데이터가 저장되는 단위
- 표 형태로 저장된 데이터의 집합

하나의 데이터베이스에 여러 개의 테이블이 존재할 수 있음

<br/><br/>

2023.02.10

## 02. 테이블의 row와 column
- row(행): 개체 하나를 나타내는 단위
- column(열): 개체가 가지는 속성 하나 하나를 나타내는 단위

<br/><br/>

## 03. DBMS와 SQL
### DBMS
- DataBase Management System(데이터베이스 관리 시스템)의 줄임말
- 데이터베이스를 관리하기 위해 사용하는 프로그램  
- Oracle, MariaDB, MySQL, SQLite, MS SQL Server 등이 있음

### SQL
- 모든 DBMS는 SQL이라는 언어로 명령을 내림  
- Structured Query Language의 약자
- 국제 표준 SQL이 있으나, DBMS마다 조금씩 다른 경우 있음(대부분의 기능에는 차이가 없음)

<br/><br/>

## 04. MySQL과 설치

### DBMS의 주요 구성 요소
- client(클라이언트 프로그램): 사용자가 server에 접속해서 원하는 데이터베이스 관련 작업을 할 수 있도록, SQL을 입력할 수 있는 화면 등을 제공하는 프로그램
- server(서버 프로그램): client로부터 SQL 문 등을 전달받아 데이터베이스 관련 작업을 직접 처리하는 프로그램
- 대부분의 DBMS가 이런 식으로 client를 통해 server에 접속하는 구조로 되어 있음
- DBMS를 사용한다는 것은, 실행되고 있는 server에 client를 이용해서 접속한 후, 원하는 명령을 내린다는 뜻

### MySQL
- 오픈 소스 소프트웨어
- 서버 프로그램: mysqld
- 클라이언트 프로그램: mysql
- MySQL Workbench: CLI 대신 GUI 환경으로 사용할 수 있게 해주는 프로그램
