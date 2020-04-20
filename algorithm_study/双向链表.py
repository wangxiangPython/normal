
class Node(object):
    def __init__(self,elem):
        self.elem = elem
        self.next = None
        self.prev = None

class DoubleLinkList(object):
    #双向链表  __init__  is_empty  length   travel  通单向链表

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
        print('')

    def add(self,item):
        node = Node(item)
        if self.__head is None:
            self.__head = node
        else:
            node.next = self.__head
            node.next.prev =  node
            self.__head = node

    def append(self,item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next !=None:
                cur = cur.next

            cur.next = node
            node.prev = cur

    def insert(self,pos,item):
        node = Node(item)
        if pos<=0:
            self.add(item)
        elif pos>(self.length()-1):
            self.append(item)
        else:
            cur = self.__head
            count = 0
            while count<pos:
                count+=1
                cur = cur.next
            #第一种插入顺序
            # node.next = cur
            # node.prev = cur.prev
            # cur.prev.next = node
            # cur.prev = node

            #第二种插入顺序
            node.next = cur
            node.prev = cur.prev
            cur.prev = node
            cur.prev.next = node

    def remove(self,item):
        # node = Node(item)
        cur = self.__head
        while cur!=None:
            if cur.elem == item:
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.next:
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next
    def search(self,item):
        # node = Node(item)
        cur = self.__head
        while cur!=None:
            if cur.elem ==item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == '__main__':
    dll = DoubleLinkList()
    print(dll.is_empty())
    print(dll.length())
    dll.append(1)
    dll.travel()
    print(dll.is_empty())
    print(dll.length())

    dll.add('??')

    dll.insert(0, 20)
    dll.insert(1, 30)
    dll.insert(20, 30)
    # dll.append(1)
    # dll.append(2)
    # dll.append(3)
    dll.travel()

    dll.remove(20)
    dll.travel()
    print(dll.search(30))