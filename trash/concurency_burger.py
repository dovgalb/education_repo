from dataclasses import dataclass, field, InitVar


@dataclass(order=False)
class V3D:
    x: int
    y: int
    z: int = field(compare=False)
    calc_len: InitVar[bool] = True
    length: float = field(init=False, default=0)

    def __post_init__(self, calc_len: bool):
        if calc_len is True:
            self.length = (self.x * self.y * self.z) ** 0.5

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, V3D):
            raise TypeError(f"Can't compare V3D")
        return self.x == other.x and self.y == other.y and self.z == other.z


v = V3D(2, 4, 6, False)
v1 = V3D(2, 4, 3, True)
print(v == v1)
