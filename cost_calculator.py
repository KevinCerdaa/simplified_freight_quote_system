BASE_EFFICIENCY = 2.8
PENALTY_PER_TON = 0.03
DIESEL_PRICE = 27.01
AVERAGE_SPEED = 65
REFEER_CONSUME = 2.5
AVARAGE_MANEUVERS_COST = 6000

def get_fuel_efficiency(weight):
    return BASE_EFFICIENCY - (weight * PENALTY_PER_TON)

def get_fuel(kilometers, weight):
    return kilometers / get_fuel_efficiency(weight)

def get_fuel_cost (kilometers, weight):
    return get_fuel(kilometers, weight) * DIESEL_PRICE

def get_route_hours(kilometers):
    return kilometers / AVERAGE_SPEED

def get_refeer_cost(is_refeer, kilometers):
    if is_refeer: return REFEER_CONSUME * get_route_hours(kilometers) * DIESEL_PRICE
    else: return 0

def get_maneuvers_cost(needs_maneuvers):
    if needs_maneuvers: return AVARAGE_MANEUVERS_COST
    else: return 0

def get_insurance_cost(needs_insurance, charge_value):
    if needs_insurance: return charge_value * 0.008
    else: return 0

def get_total_cost(kilometers, weight, is_refeer, needs_maneuvers, needs_insurance, charge_value):
    operational_cost = get_fuel_cost(kilometers, weight) + get_refeer_cost(is_refeer, kilometers) + get_maneuvers_cost(needs_maneuvers) + get_insurance_cost(needs_insurance, charge_value)
    subtotal = operational_cost * 1.20
    taxes = subtotal * 0.16
    total = subtotal + taxes
    return {'kilometers': kilometers, 'fuel_cost': round(get_fuel_cost(kilometers, weight), 2), 'refeer_cost': round(get_refeer_cost(is_refeer, kilometers), 2), 'maneuvers_cost': round(get_maneuvers_cost(needs_maneuvers), 2), 'insurance_cost': round(get_insurance_cost(needs_insurance, charge_value), 2), 'operational_cost': round(operational_cost, 2), 'subtotal': round(subtotal, 2), 'taxes': round(taxes, 2), 'total': round(total, 2)}

print(get_total_cost(450, 18, True, True, True, 850000))