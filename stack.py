class ZootopiaTasksStack:

    class Node:
        def __init__(self, data: any):
            self.data = data
            self.prev = None

    def __init__(self):
        self.__top = None
        self.__size = 0

    def push(self, zootopia_task: any) -> None:
        """
        Добавляет новую задачу в колекцию
        :param ZootopiaTask: Объект класса ZootopiaTask
        :return: None
        """

        new_node = ZootopiaTasksStack.Node(zootopia_task)
        new_node.prev = self.__top
        self.__top = new_node

        self.__size += 1

    def pop(self) -> None or any:
        """
        Удаляет последнюю задачу из коллекции и возвращает нам ее
        :return: Удаленная задача
        """

        if self.__size == 0:
            return None

        data = self.__top.data
        self.__top = self.__top.prev
        self.__size -= 1

        return data

    def peek(self) -> any:
        """
        Возвращает последнюю добаленную задачу из коллекции
        :return: Последняя внесенная задача в коллекцию
        """
        return self.__top.data if self.__size != 0 else None

    def is_empty(self) -> bool:
        """
        Проверка коллекции на пустоту
        :return: True - если коллекция пуста
                 False - если в коллекции есть задачи
        """
        return self.__top is not None

    def count(self) -> int:
        """
        Возвращает количство задач в коллекции
        :return: возвращает натуральное число
        """
        return self.__size