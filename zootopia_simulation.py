from datetime import date
import stack
class ZootopiaTask:
    def __init__(self, discription: str, duedata=None):
        self.__discription = discription
        self.__duedata = duedata

    def __str__(self):
        return (f'Описание задачи: {self.__discription}\n'
                f'Срок выполнения: до {self.__duedata}')

st1 = stack.ZootopiaTasksStack()
t1 = ZootopiaTask('Строительство новых дорог', date(2025, 9, 1))
t2 = ZootopiaTask('Улучшение общественного транспорта', date(2026, 5, 14))
t3 = ZootopiaTask('Проведение культурных мероприятий', date(2024, 11, 28))
st1.push(t1)
print(st1.peek(), "\n", "*" * 20)
st1.push(t2)
print(st1.peek(), "\n", "*" * 20)
st1.push(t3)
print(st1.peek(), "\n", "*" * 20)
print(f'Количество активных задач: {st1.count()}', "\n", "*" * 20)
print(f'Задача удалена:\n{st1.pop()}', "\n", "*" * 20)
print(f'Количество активных задач: {st1.count()}', "\n", "*" * 20)