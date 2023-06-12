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
