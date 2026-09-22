BASE_EFFICIENCY = 2.8
PENALTY_PER_TON = 0.03
DIESEL_PRICE = 27.01
AVERAGE_SPEED = 65

def get_fuel_efficiency(weight):
    return BASE_EFFICIENCY - (weight * PENALTY_PER_TON)

def get_fuel(kilometers, weight):
    return kilometers / get_fuel_efficiency(weight)

def getFuelCost (kilometers, weight):
    return get_fuel(kilometers, weight) * DIESEL_PRICE

# Comentario