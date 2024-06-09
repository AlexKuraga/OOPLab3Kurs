import math
from typing import Callable

class PipePressure:
    def __init__(self, flow_rate: float, height: float, density: float, pressure: float, prev_pressure: float = 0):
        self.q = flow_rate
        self.h = height
        self.rho = density
        self.p = pressure
        self.p_n = prev_pressure

    def eq(self) -> float:
        return (9.81 * self.rho * self.q * self.h) / (self.p * 1000)

    def with_previous(self, f1: Callable[[], float]) -> float:
        print("Previous pressure")
        return (9.81 * self.rho * self.q * self.h) / (self.p_n * 1000 * f1())

    def calc(self, f1: Callable[[], float]) -> float:
        if self.p_n == 0:
            return self.eq()
        else:
            return self.with_previous(f1)

    def compute(self) -> float:
        return self.calc(self.eq)

if __name__ == "__main__":
    calc = PipePressure(12, 12, 3, 5, 12)
    print(calc.compute())