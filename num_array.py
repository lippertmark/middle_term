import copy


class NumArray:
    class Node:
        def __init__(self, next=None, prev=None, val=None, sign=1):
            self.next = next
            self.prev = prev
            self.val = val
            if sign == None:
                if self.val < 0:
                    self.sign = -1
                else:
                    self.sign = 1
            else:
                self.sign = sign

        def __add__(self, other):
            if isinstance(other, NumArray.Node):
                return self.val * self.sign + other.val * other.sign

        def __str__(self):
            return str(self.val)

    def __init__(self, number=0):
        if number < 0:
            self.sign = -1
            number = -number
        else:
            self.sign = 1
        self.head = NumArray.Node(sign=self.sign)
        self.tail = NumArray.Node(sign=self.sign)

        curr = None
        self.tail = NumArray.Node(val=number % 10, sign=self.sign)
        curr = self.tail
        number //= 10
        while number > 0:
            new_node = NumArray.Node(next=curr, val=number % 10, sign=self.sign)
            curr.prev = new_node
            curr = new_node
            number //= 10
        self.head = curr

    def __neg__(self):
        new_num = copy.deepcopy(self)
        new_num.sign = new_num.sign * (-1)
        curr = new_num.head
        while curr.next != None:
            curr.sign = curr.sign * (-1)
            curr = curr.next
        curr.sign = curr.sign * (-1)
        return new_num

    def __add__(self, other):
        new_num = NumArray()
        curr_1 = self.tail
        curr_2 = other.tail
        new_num.tail.val = curr_1 + curr_2
        curr = new_num.tail
        ym = curr.val // 10
        curr.val %= 10
        null_node = NumArray.Node(val=0)
        while curr_1.prev != None or curr_2.prev != None:
            if curr_1.prev != None:
                curr_1 = curr_1.prev
            else:
                curr_1 = null_node
            if curr_2.prev != None:
                curr_2 = curr_2.prev
            else:
                curr_2 = null_node

            new_node = NumArray.Node(next=curr, val=curr_1 + curr_2 + ym)
            ym = curr.val // 10
            curr.val %= 10
            curr.prev = new_node
            curr = new_node
        if ym != 0:
            new_node = NumArray.Node(next=curr, val=ym)
            curr.prev = new_node
            curr = new_node
        new_num.head = curr
        return new_num

    def __sub__(self, other):
        return self + (-other)

    def __str__(self):
        s = ''
        if self.sign == -1:
            s = '-'
        curr = self.head
        while curr.next != None:
            s += str(curr)
            curr = curr.next
        s += str(curr)
        return s

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        flag = True
        if self.sign != other.sign:
            return False

        curr_1 = self.tail
        curr_2 = other.tail
        while curr_1.prev != None or curr_2.prev != None:
            if curr_1.prev == None:
                return False
            if curr_1.prev == None:
                return True


ch_1 = NumArray(123)
ch_2 = NumArray(23)
ch_2_neg = - ch_2
ch_4 = ch_1 - ch_2
print(ch_1)
print(ch_2)

print(ch_4)
