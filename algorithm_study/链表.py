class Node(object):
    # 构造函数
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkList(object):
    """单链表"""

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        return self.__head == None

    def length(self):
        # 游标，用来移动遍历节点
        cur = self.__head
        # count记录数量
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__head
        while cur != None:
            print(cur.elem, end=' ')
            cur = cur.next
        print('\n')

    def add(self, item):
        # 头插法
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        # 尾插法
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count < (pos - 1):
                pre = pre.next
                count += 1
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        cur = self.__head
        pre = None
        while cur!=None:
            if cur.elem == item:
                # if cur ==self.__head:
                if self.__head.elem==item:
                    self.__head=cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


# node = Node()

if __name__ == '__main__':
    s = SingleLinkList()
    print(s.is_empty())
    print(s.length())
    s.append(1)
    s.travel()
    print(s.is_empty())
    print(s.length())

    s.add('??')

    s.insert(0, 20)
    s.insert(1, 30)
    s.insert(20, 30)
    # s.append(1)
    # s.append(2)
    # s.append(3)
    s.travel()

    s.remove(20)
    s.travel()