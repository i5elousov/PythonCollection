from datetime import datetime
import stack
class ZootopiaTask:
    def __init__(self, discription: str, duedata=None):
        self.__discription = discription
        self.__duedata = duedata

    def __str__(self):
        return (f'Описание задачи: {self.__discription}\n'
                f'Срок выполнения: до {self.__duedata}')
