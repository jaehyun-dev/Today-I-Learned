# 리스코프 치환 원칙

2023.05.04

## 01. 리스코프 치환 원칙 이해하기

### 리스코프 치환 원칙(Liskov Substitution Principle)
- 부모 클래스의 인스턴스를 사용하는 위치에 자식 클래스의 인스턴스를 대신 사용했을 때 코드가 원래 의도대로 작동해야 한다
- 자식 클래스의 인스턴스가 부모 클래스의 인스턴스가 행동하는 범위 내에서 행동해야 한다는 원칙
- 부모 클래스의 행동규약을 자식 클래스가 위반하지 말 것

자식 클래스가 오버라이딩을 잘못 하는 경우
1. 자식 클래스가 부모 클래스의 변수 타입을 바꾸거나 메소드의 파라미터 또는 리턴값의 타입 or 개수를 바꾸는 경우
2. 자식 클래스가 부모 클래스의 의도와 다르게 메소드를 오버라이딩 하는 경우 