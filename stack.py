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
        """
        Удаляет последнюю задачу из коллекции и возвращает нам ее
        :return: Удаленная задача
        """

        if self.__size == 0:
            return None

        data = self.__top.__data
        self.__top = self.__top.__perv
        self.__size -= 1

        return data

    def peek(self):
        """
        Возвращает последнюю добаленную задачу из коллекции
        :return: Последняя внесенная задача в коллекцию
        """
        return self.__top.__data if self.__size != 0 else None

    def is_empty(self):
        """
        Проверка коллекции на пустоту
        :return: True - если коллекция пуста
                 False - если в коллекции есть задачи
        """
        return self.__top is not None

    def count(self):
        pass