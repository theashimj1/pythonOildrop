import math

print("Insert all values on S.I unit")

viscosity = 0.000018205

rho_oil = 917

rho_air = 1.205

distance_bet_plates = 0.014

Voltage = 540

time_to_move_down = float(input('Time taken by particle to drop in absence of electric field (Sec) = '))

print("---" * 20)

time_to_move_up = float(input("Time taken by particle to move up in presence of electric field (Sec) = "))

up_velocity = 2e-3 / time_to_move_up

down_velocity = 2e-3 / time_to_move_down

b = 8.2e-3

P = 1.01e5

m = 2 * 9.8 * (rho_oil - rho_air)

c = 9 * viscosity * down_velocity

radius_before_correction = math.sqrt(c / m)

i = (1 + (b / (P * radius_before_correction)))

eff_viscosity = viscosity * (1 / i)

x = (9 * eff_viscosity * down_velocity) / (2 * 9.8 * rho_oil)

radius_corrected = math.sqrt((4.059e-8 ** 2) + x) - 1.059e-8

front = ((up_velocity / down_velocity) + 1)

weight = (4 / 3) * math.pi * (radius_corrected ** 3) * (rho_oil - rho_air) * 9.8

Electric_field = Voltage / distance_bet_plates

charge = front * (weight / Electric_field)

N = charge / 1.6e-19

print("---" * 10)

print("---------------------------RESULT--------------------------")

velocity_fall = f"Velocity of falling drop = {str(down_velocity)} m/s"
velocity_rise = f"Velocity of rising drop  = {str(up_velocity)} m/s "

print(velocity_fall)

print(velocity_rise)

print("---" * 10)

radius1 = f" Radius of particle before viscosity correction, a =  {str(radius_before_correction)} m"
print(" ")
radius2 = f" Radius of particle after viscosity correction, r =  {str(radius_corrected)} m"

print(radius1)

print(radius2)

print("---" * 10)

weight = f" Apparent weight of the particle , W = {str(weight)} kg"
print(weight)

field = f" The electric field applied between the plates , E = {str(Electric_field)} V/m"
print(field)

print("---" * 10)

charge = f" The charge on the particle is ,q = {str(charge)} Coulomb "
print(charge)

print("-------" * 10)

print(" Number of electrons , N , = " + str(N))

const = '''
                      where,
                         b = 8.2e3 Pa , is constant
                         
                         g = 9.8 m/s^2 , acceleration due to gravity
                         
                         P = 1.081e5 Pa , is atmospheric pressure
                          
                         Viscosity of air at 20 degree celsius = 0.000018205kg/m-s
                         
                         Density of the Oilve oil at 20 degree celsius = 917 kg/m^3
                         
                         Density of the air at 20 degree celsius = 1.205 kg/m^3
                         
                         Distance between two plates = 1.4 cm = 0.014 m
                         
                         Applied voltage = 540 V
'''

print(const)
