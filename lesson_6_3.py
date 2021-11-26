class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

data = Position("Иван", "Иванов", "Врач-терапевт", 150000, 40000)
print(f"Имя: {data.name}")
print(f"Фамилия: {data.surname}")
print(f"Должность: {data.position}")
print(f"Доход: {data._income}")
print(f"Полное имя: {data.get_full_name()}")
print(f"Суммарный доход: {data.get_total_income()}")
