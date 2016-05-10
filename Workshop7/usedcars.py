from car import Car

def main():
    bus = Car(180, "Bus")
    bus.drive(30)
    print(bus)

    limo = Car(100,"Limo")
    limo.add_fuel(20)
    limo.drive(115)
    print(limo)

main()