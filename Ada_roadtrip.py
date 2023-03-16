def Ada_roadtrip(vehicle_names, vehicle_ranges, vehicle_rental_prices, days_rental, total_distance, charging_cost):

    cheapest_car = ""
    cheapest_cost = float('inf')

    for i in range(len(vehicle_names)):
        rental_cost = vehicle_rental_prices[i] * days_rental
        charging_cost = total_distance / vehicle_ranges[i] * charging_cost
        total_cost = rental_cost + charging_cost
        vehicle_name = vehicle_names[i]

        if total_cost < cheapest_cost:
            cheapest_car = vehicle_names[i]
            cheapest_cost = total_cost

    print(f"The least expensive vehicle is the {cheapest_car} which will cost ${cheapest_cost:.2f} to take on the trip")

    #return cheapest_car, cheapest_cost

vehicle_names = ["Toyota Prius", "Leaf", "ID4"]
vehicle_ranges = [100, 200, 75]
vehicle_rental_prices = [50.00, 75.00, 100.00]
total_distance = 1000  # in km
days_rental = 3
charging_cost = 5  # $5/charge

Ada_roadtrip(vehicle_names, vehicle_ranges, vehicle_rental_prices, days_rental, total_distance, charging_cost)


