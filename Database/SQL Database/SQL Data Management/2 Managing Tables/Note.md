# 2 테이블 다루기

2023.06.12

## 01. 컬럼 정보를 한 눈에 보여주는 DESCRIBE
```MySQL
DESCRIBE table_name;
```

DESCRIBE 뒤에 확인하고 싶은 테이블 이름을 쓰면 해당 테이블의 컬럼 구조, 각 컬럼의 데이터 타입, 속성을 볼 수 있음
- Field: 컬럼의 이름
- Type: 컬럼의 데이터 타입
- Null: 컬럼의 Null 속성 유무
- Key : Primary Key, Unique 속성 여부
- Default : 컬럼의 기본값
- Extra : AUTO_INCREMENT 등의 기타 속성

DESC로 줄여써도 됨

<br/><br/>

## 02. 컬럼 추가와 컬럼의 이름 변경
시간이 흐르면서 테이블에 저장해야 할 정보들이 조금씩 변하기 때문에 컬럼 구조는 바뀔 수 있음  

```MySQL
ALTER TABLE student ADD gender CHAR(1) NULL;
```
- ALTER TABLE: 테이블 변경하라
- ADD: 컬럼 추가하라

```MySQL
ALTER TABLE student 
    RENAME COLUMN student_number TO registration_number;
```
- RENAME COLUMN A to B: A 컬럼 이름을 B로 바꿔라

<br/><br/>

## 03. 컬럼 삭제와 컬럼의 데이터 타입 변경
#### 컬럼 삭제하기
```MySQL
ALTER TABLE student DROP admission_date;
```
- Drop column_name: 컬럼 삭제하라

#### 컬럼 데이터 타입 변경하기
```MySQL
ALTER TABLE student MODIFY major INT;
```
- Modify column_name data_type: column_name 컬럼의 데이터 타입을 data_type로 수정, 변경하라
- 컬럼 데이터 타입 변경하려면 먼저 변경하려는 데이터 타입의 값으로 컬럼 값들을 변경해줘야 함
- MySQL이 엄격하지 않은 편이라 가능

<br/><br/>

## 04. 혹시 UPDATE가 안되는 분이라면?
- MySQL Workbench에서 safe update mode 사용 중이면 모든 row의 특정 컬럼을 갱신하거나 WHERE절에 Primary Key가 사용되지 않은 UPDATE문이 실행되지 않음
- 설정에서 해제해주면 됨
- DBMS의 특정 모드가 어떻게 설정되어있느냐에 따라 같은 SQL문이라도 실행 결과가 달라질 수 있음

<br/><br/>

## 05. 컬럼 구조 변경 퀴즈

질문 1  
해설: 테이블의 현재 컬럼들에 관한 정보를 한 눈에 보려면 DESCRIBE(묘사하다) 문을 사용해야 합니다. 줄여서 DESC만 써도 됩니다.

질문 2  
해설: 테이블에 컬럼을 추가할 때는 ALTER TABLE `테이블 이름` ADD `새 컬럼 정보`; 형식의 SQL 문을 사용합니다. 이때 ADD 말고 ADD COLUMN이라고 써도 됩니다.

질문 3  
헤설: 테이블의 기존 컬럼의 이름을 변경할 때는 ALTER TABLE `테이블 이름` RENAME COLUMN `기존 이름` TO `새 이름`; 형식의 SQL 문을 사용해야 합니다. 

질문 4  
해설: 테이블의 기존 컬럼을 삭제할 때는 ALTER TABLE `테이블 이름` DROP COLUMN `컬럼 이름`; 형식의 SQL 문을 써야 합니다. 이때 DROP COLUMN에서 COLUMN은 생략해도 됩니다.

질문 5  
해설: 테이블의 기존 컬럼의 데이터 타입을 변경할 때는 ALTER TABLE `테이블 이름` MODIFY `새로 설정할 컬럼 정보`; 형식의 SQL 문을 실행하면 됩니다. 꼭 데이터 타입 뿐만 아니라 NOT NULL, AUTO INCREMENT 같은 컬럼의 속성을 변경할 때도 MODIFY를 사용하는데요. 속성을 변경하는 방법은 곧바로 이후 영상에서 배울 겁니다.

<br/><br/>

## 06. 컬럼 구조 변경 실습
```MySQL
ALTER TABLE shoes RENAME COLUMN name TO model;
ALTER TABLE shoes MODIFY size DOUBLE NOT NULL;
ALTER TABLE shoes DROP COLUMN brand;
ALTER TABLE shoes ADD stock INT NOT NULL;
```
