p = 2.1  # bar
m = 1030  # kg
g = 9.8  # meter per second squared
v = 18  # max velocity in meter per second ~65 km/hr
a = 1.46  # linear acceleration of the car
A = 2.8  # in meter square
C_d = 0.23
grade = 0.07  # 7% grade, world`s steepest road has grade of 40%


class power:
    def __init__(self):
        self.C_dr = -0.0000002636 * p ** 3 + 0.0000404822 * p ** 2 - 0.0020812137 * p + 0.0381150798
        self.C_sr = -0.0000001687 * p ** 3 + 0.0000255349 * p ** 2 - 0.001294484 * p + 0.0305104628

    def drag_force(self):  # calculates rolling resistance force
        return int((self.C_sr + 3.24 * self.C_dr * (v / 100) * 2.5) * m * g)

    def rolling_power(self):  # gives rolling power
        return self.drag_force() * v

    def power_to_accelerate(self):  # fives power to overcome acceleration
        return int(m * a * v)

    def drag_power(self):  # calculates air drag power
        return 0.5 * A * C_d * v ** 3  # considering still air

    def grade_power(self):  # calculates power to run height
        return m * a * v * grade

    def total_power(self):
        return (self.grade_power() + self.power_to_accelerate() + self.rolling_power() + self.drag_power()) / 1000

    def show(self):
        print('Power for to remain steady in watt:', int(self.rolling_power()) + int(self.drag_power()))  # watt
        print('Power to accelerate in watt:', self.power_to_accelerate())
        print('Power to overcome grade in watt:', self.grade_power())
        print('==' * 20)
        print(f'Total Power: {self.total_power()} watt')
        print(f'Total Power in horse-power: {self.total_power() / 746} hp')

    def energy_required(self):
        print(f'Energy required to run 5 hours, i.e. Approximately 325 km : {self.total_power() * 5} kwh')  # kilo
        # -watt-hr
        print(f'Amount of hydrogen needed is: {(self.total_power() * 5) / 33.6} kg')
        print(f'Volume of Hydrogen at 20 degree-Celsius and 700 bar: {self.volume()} litre')

    def volume(self):
        return (495 * ((self.total_power() * 5) / 33.6) * 293.15 * 0.08206) / 700


obj = power()
obj.show()
obj.energy_required()
