class ZootopiaTasksStack:

    class Node:
        def __init__(self, data):
            self.__data = data
            self.__prev = None

    def __init__(self):
        self.__top = None
        self.__size = 0

    def push(self, ZootopiaTask):
        """
        Добавляет новую задачу в колекцию
        :param ZootopiaTask: Объект класса ZootopiaTask
        :return: None
        """

        new_node = ZootopiaTasksStack.Node(ZootopiaTask)
        new_node.__prev = self.__top
        self.__top = new_node

        self.__size += 1
              
    def pop(self):
        pass

    def peek(self):
        pass

    def is_empty(self):
        pass

    def count(self):
        pass