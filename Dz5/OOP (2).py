class PipePressure:
    def __init__(self, flow_rate, height, density, pressure, prev_pressure=None):
        self.q = flow_rate
        self.h = height
        self.rho = density
        self.p = pressure
        self.p_n = prev_pressure

    def eq(self):
        return (9.81 * self.rho * self.q * self.h) / (self.p * 1000)

    def with_previous(self, f1):
        print("Previous pressure\n")
        return (9.81 * self.rho * self.q * self.h) / (self.p_n * 1000 * f1())

    def calc(self, f1):
        if self.p_n is None:
            return self.eq()
        else:
            return self.with_previous(f1)

    def compute(self):
        return self.calc(self.eq)


calc = PipePressure(12, 12, 3, 5, 12)
print(calc.compute())
