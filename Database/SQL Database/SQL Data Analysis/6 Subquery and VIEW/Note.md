# 6 서브쿼리와 뷰를 활용한 유연한 데이터 분석

2023.02.27

## 01. 서브쿼리란?

### 서브쿼리
- SQL문 안에 '부품'처럼 들어가는 SELECT문

```MySQL
SELECT i.id, i.name, AVG(star) AS avg_star
FROM item AS i LEFT OUTER JOIN review AS r
ON r.item_id = i.id
GROUP BY i.id, i.name
HAVING avg_star < (SELECT AVG(star) FROM review)
ORDER BY avg_star DESC;
```
이 쿼리문 안에서
```MySQL
(SELECT AVG(star) FROM review)
```
이 부분이 서브 쿼리

<br/><br/>

2023.02.28

## 02. SELECT 절에 있는 서브쿼리
```MySQL
SELECT
    id, 
    name, 
    price, 
    (SELECT MAX(price) FROM item) AS max_price
FROM copang_main.item;
```
```MySQL
    (SELECT MAX(price) FROM item)
```
이 부분이 SELECT 절에 쓰인 서브쿼리. item 테이블 중 가장 비싼 상품의 가격을 보여줌.

<br/><br/>

2023.03.01

## 03. WHERE 절에 있는 서브쿼리 I
```MySQL
SELECT
    id, 
    name, 
    price
FROM copang_main.item
WHERE price > (SELECT MAX(price) FROM item);
```
```MySQL
              (SELECT MAX(price) FROM item)
```
이 부분이 WHERE 절에 쓰인 서브쿼리. item 테이블 중 가장 비싼 상품의 가격을 보여줌.

<br/><br/>

2023.03.02

## 04. WHERE 절에 있는 서브쿼리 II

- 서브쿼리에 값 하나를 리턴하는 경우만 있는 것은 아님
```MySQL
SELECT * FROM item
WHERE id IN
(
SELECT item_id
FROM review
GROUP BY item_id HAVING COUNT(*) >= 3
);
```
review 테이블에서, 리뷰가 3개 이상인 로우들을 SELECT 한 다음, 해당 목록에 있는 id를 item 테이블에서 SELECT 하여 보여주는 것

<br/><br/>

2023.03.03

## 05. ANY(SOME), ALL

### 1. ANY의 의미(+SOME)
- ANY가 WHERE 절에서 사용될 때는, 서브쿼리의 결과에 있는 각 row의 값들 중 하나라도 조건을 만족하는 경우가 있으면 TRUE를 리턴한다는 뜻입니다.  
- SOME도 서브쿼리의 결과에 있는 각 row의 값들 중 하나라도 조건을 만족하면 TRUE를 리턴합니다.
```MySQL
SELECT * FROM FOR_TEST.codeit_theater
    WHERE view_count > ANY(SELECT view_count FROM FOR_TEST.codeit_theater WHERE category = 'ACTION')
        AND category != 'ACTION'
```
view_count가 ACTION 카테고리에 있는 영화들의 view_count 중 어느 하나보다 더 높으면서 카테고리가 ACTION이 아닌 영화를 보여줌

### 2. ALL의 의미
- ALL은 모든 경우에 대해서 해당 조건이 성립해야 TRUE를 리턴합니다.
```MySQL
SELECT * FROM FOR_TEST.codeit_theater
    WHERE view_count > ALL(SELECT view_count FROM FOR_TEST.codeit_theater WHERE category = 'ACTION')
        AND category != 'ACTION'
```
view_count가 ACTION 카테고리에 있는 모든 영화들의 view_count보다 더 높으면서 카테고리가 ACTION이 아닌 영화를 보여줌

<br/><br/>

2023.03.04

## 06. 서브쿼리 기초 퀴즈

질문 1  
해설: 다른 SQL 문의 일부로 쓰이는 SELECT 문을 서브쿼리라고 합니다. 이때 전체 SQL 문을 outer query, 서브쿼리를 inner query라고도 합니다.

질문 2  
해설: SELECT 절에서 서브쿼리를 사용하는 방법을 묻는 문제입니다. 평균값을 구하는 집계 함수는 AVG() 죠?

질문 3  
해설:  
서브쿼리와 LIMIT을 함께 사용하는 응용 문제입니다.
정답을 넣고 완성한 서브쿼리는 다음과 같은데요.
```MySQL
SELECT SUBSTRING(address, 1, 2) 
FROM member 
GROUP BY SUBSTRING(address, 1, 2) 
ORDER BY COUNT(*) DESC 
LIMIT 1;
```
이 서브쿼리는
1. 주요 지역별로 회원들을 그루핑한 후에,
2. 그룹들을 각 그룹당 row 개수대로 내림차순 정렬하고,
3. 그 중에서도 1등만 추립니다.

그럼 회원들이 가장 많이 살고 있는 주요 지역 이름을 알 수 있겠죠?
이 전체 SQL 문을 Workbench에서 직접 실행해보시고, 어떤 주요 지역의 회원들이 조회되는지 확인해보세요.

전체 SQL 문 :
```MySQL
SELECT * 
FROM member 
WHERE SUBSTRING(address, 1, 2) =
    (
        SELECT SUBSTRING(address, 1, 2) 
        FROM member 
        GROUP BY SUBSTRING(address, 1, 2) 
        ORDER BY COUNT(*) DESC 
        LIMIT 1
    );
```

<br/><br/>

## 07. 서브쿼리 기초 실습
### 해설
```MySQL
SELECT * 
FROM review 
WHERE item_id IN 
     (
      SELECT id 
      FROM item 
      WHERE registration_date < '2018-12-31'
     );
```
지금 정답에 있는 서브쿼리는 아래와 같이 실행됩니다.

![a](https://user-images.githubusercontent.com/71001479/222886664-6355698e-cdd4-431c-ac63-c5c7f2c7a550.png)

실행 결과를 보니 하나의 컬럼에 여러 row 형식인 결과를 리턴하죠?  
그러니까 정답의 전체 SQL 문은 아래 코드와 같은 의미라고 생각하시면 됩니다.
```MySQL
SELECT * 
FROM review 
WHERE item_id IN (1, 3);
```

<br/><br/>

2023.03.05

## 08. FROM 절에 있는 서브쿼리

- 서브쿼리로 컬럼 하나가 아니라 테이블 형태로 여러 컬럼과 여러 로우를 뽑아낼 수 있는데, 이걸 derived table이라고 함  
- derived table은 반드시 alias를 붙여줘야 함
```MySQL
SELECT
    AVG(review_count),
    MAX(review_count),
    MIN(review_count)
FROM
(SELECT
    SUBSTRING(address, 1, 2) AS region,
    COUNT(*) AS review_count
FROM review AS r LEFT OUTER JOIN member AS m
ON r.mem_id = m.id
GROUP BY SUBSTRING(address, 1, 2)
HAVING region IS NOT NULL
    AND region != '안드') AS review_count_summary;
```
