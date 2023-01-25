class Node:
    """이진 탐색 트리 노드"""
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left_child = None
        self.right_child = None


# 노드 인스턴스 생성
node_0 = Node(5)
node_1 = Node(3)
node_2 = Node(7)

node_0.left_child = node_1
node_0.right_child = node_2

node_1.parent = node_0
node_2.parent = node_0

# 노드 뿐만이 아니라 이진 탐색 트리 자체도 클래스로 만들면 편하게 사용할 수 있음

class BinarySearchTree:
    """이진 탐색 트리 클래스"""
    def __init__(self):
        self.root = None


# 비어 있는 이진 탐색 트리 생성
bst = BinarySearchTree()

# 아직까지는 빈 이진 탐색 트리 생성만 했음
# 다음 레슨부터 데이터를 저장, 탐색, 삭제하는 방법 배울 것