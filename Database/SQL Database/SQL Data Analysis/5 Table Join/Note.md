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

<br/><br/>

## 08. 다른 종류의 테이블 조인하기 II

### INNER JOIN
- OUTER JOIN과 달리 기준되는 테이블 없이, 두 테이블 모두 기준 컬럼에 일치하는 값이 있는 로우들만 연결됨
- 집합으로 차면 교집합

<br/><br/>

## 09. Foreign Key가 아닌 컬럼 기준으로 조인을 하기도 합니다.

조인을 할 때 보통 Foreign Key를 기준으로 하는 것은 맞지만, 그렇다고 꼭 Foreign Key만을 기준으로 해야하는 것은 아닙니다. 꼭 Foreign Key가 존재하지 않더라도 서로 같은 의미를 나타내는 컬럼들을 기준으로 조인하기도 하죠.  
이 경우 OUTER JOIN과 INNER JOIN의 결괏값 달라짐.  

<br/><br/>

## 10. Foreign Key와 조인 퀴즈

질문 1  
해설: 한 테이블의 컬럼 중에서 다른 테이블의 특정 row 하나를 식별할 수 있도록 해주는 컬럼은 foreign key입니다. 우리말로는 외래키라고도 합니다.  

질문 2  
해설: Foreign key를 갖고있고, 그것을 통해 다른 테이블을 참조해야하는 테이블을 자식 테이블, 참조당하는 테이블을 부모 테이블이라고 합니다.  

질문 3  
해설:  
두 테이블의 컬럼 간에 Foreign key 관계가 개념적으로 성립한다는 것과, Foreign key 관계가 실제로 설정되어있다는 것은 엄연히 다른 개념입니다.  
Foreign key 관계가 개념적으로 성립하더라도, Workbench 등의 프로그램으로 직접 Foreign key 설정을 해주지 않으면 자식 테이블에 이상한 row가 포함되는 것을 막을 수는 없습니다. 여기서 이상한 row라는 것은 'Foreign key 관계가 개념적으로 성립하는 자식 테이블의 컬럼에 부모 테이블의 관련 컬럼에 존재하지 않는 값이 있는 row'를 의미합니다.  
'개념적으로 성립' 한다는 것과 '실제로 그 관계를 DBMS로 설정'하는 것은 다르다는 사실, 꼭 기억하세요!

질문 4  
해설: 조인을 할 때는 일반적으로 Foreign key로 설정된 컬럼을 기준으로 할 때가 많습니다. 하지만 꼭 Foreign key가 설정된 경우에만 조인을 할 수 있는 것은 아닙니다. 꼭 Foreign key 관계가 설정되어있지 않더라도, 서로 다른 두 테이블의 컬럼이 같은 의미를 갖고 있으면, 조인을 해서 의미있는 결과를 얻어낼 수도 있습니다. 대신, 이때 두 컬럼의 데이터 타입은 같아야 합니다.  

질문 5  
해설:  
LEFT OUTER JOIN과 RIGHT OUTER JOIN을 보통, 묶어서 OUTER JOIN이라고 합니다. OUTER JOIN을 할 때는 항상 어느 테이블이 기준이 되는지 주의해야 합니다.  
INNER JOIN은 두 테이블 다 조인 기준을 만족하는 컬럼 값이 있는 row들만 보여줍니다.  

<br/><br/>

## 11. Foreign Key와 조인 실습

### 해설
일단 pizza_price_cost 테이블을 기준으로 sales 테이블을 LEFT OUTER JOIN하세요. 이때 기준 테이블의 id 컬럼과 sales 테이블의 menu_id 컬럼을 조인 기준으로 하면 되겠죠?

그 다음 COLEASE() 함수로 sales_volume 컬럼이 NULL이면 '판매량 정보 없음'이라고 표시하고 이 컬럼에는 AS로 '판매량'이라는 alias를 붙이세요.

### 모범 답안
```MySQL
SELECT p.name, 
       COALESCE(s.sales_volume, '판매량 정보 없음') AS '판매량'
FROM pizza_price_cost AS p LEFT OUTER JOIN sales AS s ON p.id = s.menu_id;
```

<br/><br/>

## 12. 결합 연산과 집합 연산

### (1) A ∩ B (INTERSECT 연산자 사용)
```MySQL
SELECT * FROM member_A
INTERSECT 
SELECT * FROM member_B
```

### (2) A - B (MINUS 연산자 또는 EXCEPT 연산자 사용)
```MySQL
SELECT * FROM member_A 
MINUS
SELECT * FROM member_B
```

### (3) B - A (MINUS 연산자 또는 EXCEPT 연산자 사용)
```MySQL
SELECT * FROM member_B
MINUS
SELECT * FROM member_A
```

### (4) A U B (UNION 연산자 사용)
```MySQL
SELECT * FROM member_A
UNION
SELECT * FROM member_B
```
INTERSECT, MINUS, UNION 중에서 MySQL에서는 버전 8.0 기준으로 UNION 연산자만 지원함(다른 DBMS인 오라클에서는 3가지 연산자 모두를 지원함)


<br/><br/>

2023.02.26

## 13. 같은 종류의 테이블 조인하기
같은 종류의 테이블인데 최신화가 된 경우, 기존 테이블에 있던 게 누락됐을 수도 있고, 없던 게 추가됐을 수도 있음

### LEFT OUTER JOIN
기존 테이블을 기준으로 삼기 때문에, 기존에 있었지만 새 테이블에 없는 로우 찾을 수 있음
```MySQL
SELECT
    old.id AS old_id,
    old.name AS old_name,
    new.id AS new_id,
    new.name AS new_name
FROM item AS old RIGHT OUTER JOIN item_new AS new
ON old.id = new.id;
```

### RIGHT OUTER JOIN
새 테이블을 기준으로 삼기 때문에, 기존에 없었지만 새 테이블에 생긴 로우 찾을 수 있음

### INNER JOIN
기존 테이블과 새 테이블 모두 존재하는 로우 찾을 수 있음

### UNION
양쪽의 모든 로우를 중복없이 한번씩 조회하여 볼 수 있음
```MySQL
SELECT * FROM item
UNION
SELECT * FROM item_new;
```

<br/><br/>

## 14. ON 대신 USING을 쓸 수도 있어요
```MySQL
SELECT
    old.id AS old_id,
    old.name AS old_name,
    new.id AS new_id,
    new.name AS new_name
FROM item AS old RIGHT OUTER JOIN item_new AS new
USING(id);
```
JOIN하려는 두 테이블에서 조인 조건으로 사용되는 컬럼들의 이름이 같으면 USING() 안에 컬럼 이름 써도 됨

<br/><br/>

## 15. UNION 더 알아보기

### 1. 서로 다른 종류의 테이블도, 조회하는 컬럼을 일치시키면 집합 연산이 가능합니다.
- SELECT 절 뒤의 * 부분을 두 테이블이 공통적으로 갖고 있는 컬럼 이름들로 바꿔주면 됩니다.
- 두 테이블의 원래 컬럼 구조가 달라도, 두 테이블이 공통적으로 갖고 있는 컬럼들만 조회한 경우에는 UNION 같은 집합 연산을 수행할 수 있다는 사실, 잘 기억하세요.
- 총 컬럼의 수와, 각 컬럼의 데이터 타입만 일치하면 UNION 연산이 가능합니다.

### 2. UNION 과 UNION ALL
- UNION ALL은 UNION처럼 두 테이블의 합집합을 보여준다는 점은 같습니다. 하지만 겹치는 것을 중복 제거하지 않고, 겹치는 것들을 그대로 둘다 보여준다는 차이점이 있죠.
- UNION 연산과 UNION ALL 연산은 둘다 합집합을 구하되, 전자는 중복을 제거해서 보여주고, 후자는 그런 작업없이 두 테이블을 합친 결과를 그대로 보여준다는 차이가 있습니다.

<br/><br/>

## 16. 서로 다른 3개의 테이블 조인하기
```MySQL
SELECT
    i.name, i.id,
    r.item_id, r.star, r.comment, r.mem_id,
    m.id, m.email
FROM
    item AS i LEFT OUTER JOIN review AS r
        ON r.item_id = i.id
    LEFT OUTER JOIN member AS m
        ON r.mem_id = m.id;
```
```MySQL
    item AS i LEFT OUTER JOIN review AS r
        ON r.item_id = i.id
```
이 부분이 먼저 JOIN되어 하나의 테이블로 합쳐지고, 그게 다시
```MySQL
    LEFT OUTER JOIN member AS m
        ON r.mem_id = m.id;
```
이 부분과 JOIN되어 세 테이블이 하나로 합쳐짐

<br/><br/>

## 17. 세 테이블의 조인 과정

### 1. 두 개의 테이블을 참조하는 review 테이블
- review 테이블은 member 테이블도 참조하고 있고, item 테이블도 참조하고 있음  
1. review(mem_id 컬럼) -> member(id 컬럼)
2. review(item_id 컬럼) -> item(id 컬럼)

리뷰 하나가 있을 때, 누가 남겼는지 알고 싶으면 mem_id 컬럼을 통해 member 테이블을 참조하고, 어떤 상품에 관한 리뷰인지 알고 싶으면 item_id 컬럼을 통해 item 테이블을 참조하면 됨

### 2. 1:1 관계 , 1:n 관계
- 하나의 상품에는 여러 개의 리뷰가 달릴 수 있는데, 이런 걸 1:n 관계라고 함
- 상품과 재고량과 같은 1:1 관계와 다르게, 1:n 중 1에 해당하는 테이블의 row는 조인 결과에서 여러 번 등장할 수 있음

<br/><br/>

## 18. 의미있는 데이터 추출하기 I
여성 회원들의 평균 평점이 높은 순으로 정렬하기
```MySQL
SELECT i.id, i.name, AVG(star)
FROM
    item AS i LEFT OUTER JOIN review AS r
        ON r.item_id = i.id
    LEFT OUTER JOIN member AS m
        ON r.mem_id = m.id
WHERE m.gender = 'f'
GROUP BY i.id, i.name
ORDER BY AVG(star) DESC;
```

<br/><br/>

## 19. 의미있는 데이터 추출하기 II
리뷰가 최소 2개 이상인 아이템만 추출, 같은 평점이면 리뷰 수 많은 순으로 정렬하여 조회
```MySQL
SELECT i.id, i.name, AVG(star), COUNT(*)
FROM
    item AS i LEFT OUTER JOIN review AS r
        ON r.item_id = i.id
    LEFT OUTER JOIN member AS m
        ON r.mem_id = m.id
WHERE m.gender = 'f'
GROUP BY i.id, i.name
HAVING COUNT(*) > 1
ORDER BY
    AVG(star) DESC,
    COUNT(*) DESC;
```

남성 회원에게 적용하고 싶으면, m.gender = 'm'으로만 바꾸면 됨  

평점이 가장 안 좋은 item_id 2번 아이템의 리뷰 조회
```MySQL
SELECT * FROM review WHERE item_id = 2;
```

<br/><br/>

## 20. 여러 테이블 조인하기 퀴즈

질문 1  
해설:  
집합 연산자에는 크게
- INTERSECT : 교집합
- MINUS(또는 EXCEPT) : 차집합
- UNION : 합집합

이 있습니다. 이 중에서 두 집합에 있는 모든 row를 합쳐서 하나로 보여주는 건 UNION 연산자였죠?

질문 2  
해설: 조인 조건은 보통 ON 뒤에 적는 게 일반적입니다. 하지만 기준이 되는 두 컬럼의 이름이 같을 경우 USING을 사용할 수도 있는데요. 혹시 USING이 쓰인 조인을 보더라도 당황하지 마세요.

질문 3  
해설: FROM 절에서 테이블에 alias를 붙였다면 이 alias로 각 테이블을 나타내야 합니다. 원래의 테이블 이름을 사용하면 오히려 에러가 납니다.

질문 4  
해설: UNION과 UNION ALL은 두 테이블을 합친다는 공통점은 있지만, 두 테이블의 중복 row를 제거하는지 여부에 따른 차이가 있습니다. 참고로, UNION은 중복 row를 제거하는 작업이 하나 더 추가되기 때문에 UNION ALL보다 실행완료까지의 시간이 미세하게나마 더 걸린다는 특징이 있습니다.

<br/><br/>

## 21. 여러 테이블 조인하기 실습

### 해설
(1) 일단 세 테이블을 이너 조인(INNER JOIN)하세요.
```MySQL
FROM review AS r INNER JOIN item AS i ON r.item_id = i.id
INNER JOIN member AS m ON r.mem_id = m.id
```
(2) 그리고 item 테이블의 gender 컬럼의 값이 u인 row들만 선별하세요.
```MySQL
WHERE i.gender = 'u'
```
(3) item 테이블의 registration_date 컬럼에서 연도를 추출해서 이것(상품 등록 연도)을 기준으로 row들을 그루핑하세요.
```MySQL
GROUP BY YEAR(i.registration_date)
```
(4) 각 그룹 내 row 개수가 10개 이상인 그룹들만 추리세요.
```MySQL
HAVING COUNT(*) >= 10
```
(5) 결과를 별점 평균값을 기준으로 내림차순 정렬하세요.
```MySQL
ORDER BY AVG(star) DESC;
```
(6) 컬럼은 총 세 개를 조회하세요.
1. 상품 등록 연도 컬럼('등록 연도'라는 alias를 붙이세요.)
2. 각 그룹 내 row의 개수('리뷰 개수'라는 alias를 붙이세요.)
3. 각 그룹별 별점 평균값('별점 평균값'이라는 alias를 붙이세요.)

```MySQL
SELECT YEAR(i.registration_date) AS '등록 연도', 
       COUNT(*) AS '리뷰 개수', 
       AVG(star) AS '별점 평균값'
```

별로 어렵지 않죠? 이 SQL 문을 실행한 결과는 다음과 같습니다.

![a](https://user-images.githubusercontent.com/71001479/221415715-a52e9181-a59d-4b9a-bc01-3c5e13f11728.png)

2019년도에 해당하는 그룹만 보이는군요. 아마 HAVING COUNT(\*) >= 10 절 때문인 것 같은데요. 이 부분을 제거하고 다시 실행해보면,

![b](https://user-images.githubusercontent.com/71001479/221415736-3bf7facc-95c2-4311-a528-4df9c62b6b58.png)

이렇게 2018년도 그룹도 볼 수 있습니다. 2018년에 등록된 상품에 비해, 2019년에 등록된 상품들의 총 리뷰 수가 좀더 많긴 하지만 별점 평균값은 조금 떨어졌네요. 리뷰 수가 많아졌다는 건 그만큼 판매량이 많아졌다는 뜻이라 좋은 의미지만, 대신 별점 평균값이 떨어지지 않도록 잘 관리해야겠네요.

### 모범 답안
```MySQL
SELECT YEAR(i.registration_date) AS '등록 연도', 
       COUNT(*) AS '리뷰 개수', 
       AVG(star) AS '별점 평균값'
FROM review AS r INNER JOIN item AS i ON r.item_id = i.id
INNER JOIN member AS m ON r.mem_id = m.id
WHERE i.gender = 'u'
GROUP BY YEAR(i.registration_date)
HAVING COUNT(*) >= 10
ORDER BY AVG(star) DESC;
```
