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
