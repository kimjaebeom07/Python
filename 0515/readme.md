# WEEK 8. 객체와 클래스

객체와 클래스는 객체 지향 프로그래밍의 핵심 개념입니다. 클래스는 객체를 생성하기 위한 설계도 역할을 하며 객체는 클래스를 바탕으로 만들어진 실제 데이터입니다.

객체 지향 프로그래밍을 활용하면 프로그램을 보다 구조적으로 설계할 수 있으며 복잡한 기능도 체계적으로 구현할 수 있습니다.

예를 들자면

```python
class Student:
    def __init__(self, name):
        self.name = name

student1 = Student("Kim")

print(student1.name)
```
