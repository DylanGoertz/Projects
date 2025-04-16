def main():

    CURRENT_RISE_RATE = 1.8  
    years = 25

    print("Year  Rise (in millimeters)")

    total_rise = 0
    for year in range(1, years + 1):
        rise_this_year = CURRENT_RISE_RATE * year
        total_rise += rise_this_year
        print(f"{year}:    {rise_this_year:.2f}")

    print(f"Total rise over {years} years: {total_rise:.2f}")

main()
