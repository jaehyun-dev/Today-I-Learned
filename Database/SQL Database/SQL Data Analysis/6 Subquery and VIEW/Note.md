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

<br/><br/>

2023.03.06

## 09. 서브쿼리의 종류 총정리

### 1. 단일값을 리턴하는 서브쿼리
하나의 값, 즉, 단일값을 리턴하는 서브쿼리입니다. 단일값은 수학, 물리 분야에서 **스칼라(scalar)** 라고도 하는데요. 그래서 이런 서브쿼리를 **스칼라 서브쿼리**라고도 합니다. 이런 스칼라 서브쿼리는 SELECT 절에서 하나의 컬럼처럼, WHERE 절에서 **=, > 등의 조건 표현식과 비교하는 값으로** 쓸 수 있겠죠?

### 2. 하나의 column에 여러 row들이 있는 형태의 결과를 리턴하는 서브쿼리
하나의 column에, 여러 row가 있는 형태의 결과를 리턴하는 서브쿼리입니다. 이런 서브쿼리는 **IN, ANY(SOME), ALL** 등의 키워드와 함께 쓸 수 있다고 했던 거, 기억나시죠?

### 3. 하나의 테이블 형태의 결과(여러 column, 여러 row)를 리턴하는 서브쿼리
테이블 형태의 값을 리턴하는 서브쿼리입니다. 이런 서브쿼리로 일시적으로 탄생한 테이블을 **derived table**이라고 한다고 했죠?(Oracle에서는 inline view라고도 합니다) 이런 서브쿼리로 생겨난 derived table은 마치 원래 있던 테이블인 것처럼 사용하면 됩니다. 대신, **derived table에는 alias를 붙여줘야 한다는 규칙이 있습니다.**

<br/><br/>

2023.03.07

## 10. EXISTS, NOT EXISTS와 상관 서브쿼리

서브쿼리는  
- 비상관 서브쿼리
- 상관 서브쿼리

로 분류할 수 있음  

### 비상관 서브쿼리(Non-correlated Subquery)
- 그 자체만으로도 실행이 가능한 서브쿼리 
- 서브쿼리가 그것을 둘러싼 outer query와 별개로, 독립적으로 실행될 수 있음
```MySQL
SELECT * FROM item
    WHERE id IN (SELECT item_id FROM review GROUP BY item_id HAVING COUNT(*) >= 3);
```

### 상관 서브쿼리(Correlated Subquery)
- outer query와 상관 관계가 있는 서브쿼리
- 서브쿼리가 outer query에 적힌 테이블 이름 등과 상관 관계를 갖고 있어서 그 단독으로는 실행되지 못함
```MySQL
SELECT * FROM item
    WHERE EXISTS (SELECT * FROM review WHERE review.item_id = item.id);
```
- item 테이블 각 row의 id(item.id) 값과 같은 값을 item_id(review.item_id) 컬럼에 가진 review 테이블의 row(가/들이) 있는지 조회하여,
- 만약에 존재하면(EXISTS 하면)
- WHERE 절은 TRUE가 되고, 최종 조회 결과에 담김

<br/><br/>

2023.03.08

## 11. 서브쿼리 종합 퀴즈

질문 1  
해설: 한 테이블에서 어떤 특정 테이블에 연관된 row가 있는 것들만, 혹은 없는 것들만 추려낼 때는 상관 서브쿼리를 사용하고 그 앞에 EXISTS 또는 NOT EXISTS를 붙이면 됩니다.

질문 2  
해설: MySQL에서는 FROM 뒤에서 서브쿼리가 리턴하는 테이블을 derived table이라고 합니다. 참고로, Oracle이라는 DBMS에서는 이것을 inline view라고도 합니다.

질문 3  
해설: 하나의 단일 값을 스칼라라고 하는데요. 스칼라(scalar)라는 단어는 원래 물리, 수학 분야에서 쓰이는 단어입니다. 스칼라의 좀더 자세한 정의는 다음과 같습니다.  
\*스칼라 : 하나의 수치만으로 완전히 표시되는 양으로 벡터 등과 같은 방향의 구별이 없는 수량이다. 예를 들면, 질량, 밀도 따위를 나타내는 수이다.

<br/><br/>

2023.03.09

## 12. 서브쿼리 종합 실습

```MySQL
SELECT
    MAX(copang_report.price) AS max_price,
    AVG(copang_report.star) AS avg_star,
    COUNT(DISTINCT(copang_report.email)) AS distinct_email_count
FROM
    (SELECT price, star, email
    FROM
        member AS m INNER JOIN review AS r
        ON m.id = r.mem_id
        INNER JOIN item AS i
        ON r.item_id = i.id) AS copang_report;
```

<br/><br/>

2023.03.10

## 13. 서브쿼리 vs. 조인

- 어떤 경우 (상관) 서브쿼리를 통해 얻고자 하는 결과는 조인(join)만으로도 충분히 해결할 수 있음
- 둘 중 어느 것을 쓸지는 상황에 따라, 더 익숙하고 직관적으로 이해할 수 있는 것 선택
- 하지만 만약 테이블에 아주 많은 수의 row들이 있을 때는 두 가지 방법 간에 속도 차이가 날 수도 있음

<br/><br/>

2023.03.11

## 14. 서브쿼리의 중첩과 그 문제점

서브쿼리 안에 또다시 서브쿼리를 중첩해서 쓸 수 있음  
서브쿼리로 원하는 row나 테이블을 뽑아낸 다음, 그 안에서 또 필요한 조건을 나타낼 때  
그러나 가독성이나 직관성에 안 좋은 영향을 끼칠 수 있음  
해결하기 위한 방법은 VIEW

<br/><br/>

2023.03.12

## 15. 데이터 분석가의 자산, 뷰

서브쿼리를 중첩해서 사용했을 때 생길 수 있는 가독성 등의 문제를 해결할 수 있는 방법은 뷰(VIEW)

### 뷰(VIEW, 가상 테이블)
- 조인 등의 작업을 해서 만든 '결과 테이블'이 가상으로 저장된 형태
```MySQL
CREATE VIEW 'table name' AS
SELECT ...
```
SELECT 이하 서브쿼리문으로 조회된 테이블을 뷰로 만드는 SQL문  
뷰 쓰면 원래 있었던 테이블처럼 가상으로 테이블 만들어서 저장하기 때문에 중첩 서브쿼리 쓰는 대신 간단하게 표현할 수 있음

<br/><br/>

2023.03.13

## 16. 뷰에 관해 알아야할 사실

- 뷰는 테이블과 달리 데이터가 물리적으로 컴퓨터에 저장되어 있는 건 아님
- 뷰를 사용하면 DBMS가 뷰를 생성하는 SQL문을 재실행하는 방식으로 가상의 테이블을 만들어줌

### 뷰의 장점
#### 1. 사용자에게 높은 편의성을 제공
- 여러 테이블을 조인하는 SQL문을 매번 필요할 때마다 사용하는 대신 뷰로 저장해두고 필요할 때 재활용

#### 2. 각 직무별 데이터 수요에 알맞은, 다양한 구조의 데이터 분석 기반을 구축 가능
- 같은 테이블들이 존재하는 상황에서도, 직무에 따라, 상황에 따라, 필요로 하는 데이터의 종류와 그 구조가 사람마다 다를 수 있음
- 뷰를 사용하면 각자에게 적합한 구조로 데이터들을 준비해둘 수 있기 때문에 회사 입장에서도 기존의 테이블 구조를 건드리지 않고, 풍부한 데이터 분석 기반을 준비할 수 있게 됨

#### 3. 데이터 보안을 제공
- 원본 테이블에 민감한 개인정보 등이 담겨있는 경우, 해당 컬럼을 제외하고 나머지 컬럼을 담고 있는 VIEW를 만들어 데이터 분석가에게 전달 가능
- SQL문을 사용해 특정 로우들을 공개하지 않는 것도 가능
- 공개 가능한 정보만 있는 뷰를 만들고, 데이터 분석가가 원본 테이블에 직접적인 접근을 못하도록 DBMS 사용자별 권한 관리를 하고, 제공되는 뷰에만 접근할 수 있도록 하면 됨

<br/><br/>

2023.03.14

## 17. 뷰와 데이터 분석 실무 퀴즈

질문 1  
해설: 굳이 테이블 전체 데이터를 조회하지 않고, 테이블의 컬럼 구조만 간단하게 파악하려면 DESCRIBE '테이블 이름;을 실행하면 됩니다.

질문 2  
해설: 뷰를 쓰면 매번 복잡한 SQL 문을 작성할 필요가 없다는 장점(편의성), 테이블 내용을 보안이 필요한 column이나 row는 제외하고 외부로 제공할 수 있다는 장점(보안성)이 있습니다.

질문 3  
해설: CREATE VIEW '뷰 이름' AS SELECT 문;을 사용하면 뷰를 생성할 수 있습니다.

<br/><br/>

2023.03.14

## 18. 뷰와 데이터 분석 실무 실습

### 해설
(1) 컬럼 구조 살펴보기
```MySQL
DESCRIBE employee;
```
DESCRIBE로 일단 컬럼 구조만 간단히 살펴보면 됩니다. 물론, 그냥 SELECT * FROM employee;를 실행해서 살펴봐도 되지만, row 수가 많은 테이블인 경우에는 시간이 조금 걸릴 수도 있다는 점, 참고하세요.

(2) 뷰 생성하기
```MySQL
CREATE VIEW v_emp AS 
    SELECT id,
           name,
           age, 
           department, 
           phone_num, 
           hire_date 
    FROM employee;
```
CREATE VIEW 으로 뷰를 생성하면 됩니다. 이때 SELECT 문은 민감한 정보인 address(직원의 주소) 컬럼과 rating_grade(인사고과 점수) 컬럼을 제외한 컬럼들만 조회하는 내용으로 적으면 되겠죠?

(3) 만들어진 뷰 조회하기
```MySQL
SELECT * 
FROM v_emp;
```
뷰는 '가상 테이블'입니다. 이제 v_emp 라는 뷰를 마치 원래 있던 테이블인 것처럼 자유롭게 조회할 수 있습니다. 뷰가 잘 만들어졌는지 확인해보세요.
