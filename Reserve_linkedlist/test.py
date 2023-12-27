import unittest
from reserve_linkedlist import  reverse_linked_list, print_linked_list
class TestReverseLinkedList(unittest.TestCase):

    def test_reverse_linked_list(self):

        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)

        reversed_head = reverse_linked_list(head)
        self.assertEqual(print_linked_list(reversed_head), [5, 4, 3, 2, 1])

if __name__ == '__main__':
    unittest.main()