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
