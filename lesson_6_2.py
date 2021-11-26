class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt(self):
        weight_sq_m_asph = 25
        thickness_asph = 5
        weight_kg_asph = self._length * self._width * weight_sq_m_asph * thickness_asph
        weight_t_asph = weight_kg_asph / 1000
        return f"Масса асфальта: {weight_kg_asph} кг, или {weight_t_asph} т"

l = float(input('Длина дороги: '))
w = float(input('Ширина дороги: '))
r = Road(l, w)
print(r.asphalt())
