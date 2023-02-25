# 5 테이블 조인을 통한 깊이있는 데이터 분석

2023.02.23

## 01. 여러 테이블 추가하기

### 조인(join)
- 여러 테이블을 합쳐서 하나의 테이블인 것처럼 보는 것

### 새로운 테이블 추가
- CSV 파일을 테이블로 만든 뒤 id 컬럼을 Primary Key로, Auto Increment 설정
- 날짜 컬럼의 데이터 타입을 DATE로 변경

<br/><br/>

## 02. 테이블 간의 연결고리
- item: 의류 상품 정보
- item_new
- member: 회원 정보
- review: 별점, 댓글
- stock: 재고 수량 정보

item의 id 컬럼에 해당하는 값이 stock의 item_id 컬럼과 연결되어야 함  
다른 값이 들어가면 안 됨  
이를 방지하기 위해 설정을 해줄 필요가 있음

<br/><br/>

2023.02.24

## 03. Foreign Key의 개념

### Foreign Key(외래키)
- 다른 테이블의 특정 row를 식별할 수 있게 해주는 컬럼
- 주로 다른 테이블의 Primary Key를 참조할 때가 많음

- 참조하는 테이블을 자식 테이블,
- 참조되는 테이블을 부모 테이블이라고 함

<br/><br/>

## 04. Foreign Key 설정하기
- Foreign Key 이름 설정, Reference Table 설정, 참조하는 Column 설정, 참조되는 Column 설정
- Foreign Key 설정하면, 나중에 참조하는 컬럼에 참조되는 컬럼에 없는 이상한 값이 삽입되려고 할 때 MySQL이 에러를 발생시켜줌

<br/><br/>

2023.02.25

## 05. 다른 종류의 테이블 조인하기 I

### JOIN
- 연결하다, 합치다
- 여러 테이블을 합쳐서 하나로 보이게 만드는 것
```MySQL
SELECT
    item.id,
    item.name,
    stock.item_id,
    stock.inventory_count
FROM item LEFT OUTER JOIN stock
ON item.id = stock.item_id
```
#### LEFT OUTER JOIN
- 왼쪽의 item 테이블을 기준으로 해서 stock 테이블을 합치라는 뜻

#### ON
- 합칠 때 기준, item 테이블의 id 컬럼과 stock 테이블의 item_id 컬럼의 값을 비교해서 서로 값이 같은 로우끼리 가로 방향으로 연결하라는 뜻

왼쪽 테이블의 컬럼에 있는데 오른쪽 테이블 컬럼에 없는 값은 NULL로 처리되어 연결됨  

RIGHT OUTER JOIN 하면 오른쪽 테이블을 기준으로 합쳐짐

<br/><br/>

## 06. 조인할 때 테이블에 alias 붙이기
- 컬럼 뿐만 아니라 테이블에도 alias 붙일 수 있음  
- FROM '테이블' AS 'alias'(또는 FROM '테이블' 'alias')
- 다른 부분의 테이블 이름 전부 alias로 바꿔줘야 함

<br/><br/>

## 07. 컬럼의 alias와 테이블의 alias
- 컬럼의 경우 컬럼의 이름의 alias로 변환되어 보여지게 하기 위한 용도
- 테이블의 경우 SQL문의 길이를 줄여서 가독성을 높이기 위한 용도
