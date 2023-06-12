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
