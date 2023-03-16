def Ada_roadtrip(vehicle_names, vehicle_ranges, vehicle_rental_prices):
    cheapest_car = ''
    cheapest_cost = float('inf')

    for i in range(len(vehicle_names)):
        rental_cost = vehicle_rental_prices[i] * rental_day
        total_charging_cost = total_distance / vehicle_ranges[i] * charging_cost
        total_cost = rental_cost + total_charging_cost

        if total_cost < cheapest_cost:
          cheapest_cost = total_cost
          cheapest_car = vehicle_names[i]

    print(f'"The least expensive vehicle is the {cheapest_car} which cost ${cheapest_cost:.2f} to take on trip"')


vehicle_names = ["Leaf"]
vehicle_ranges = [200]
vehicle_rental_prices = [75.00]
charging_cost = 5  # $5/charge
rental_day = 3
total_distance = 1000
Ada_roadtrip(vehicle_names, vehicle_ranges, vehicle_rental_prices)
