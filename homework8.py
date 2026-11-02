# Homwwork 8

RESTAURANTS = [
    ("Mango Rice", 4.2, 25),
    ("Pad Thai House", 4.8, 40),
    ("Chicken Rice", 4.6, 15),
    ("Som Tam Corner", 4.6, 25),
    ("Boat Noodles", 4.8, 30),
]

def by_rating(r):
    # Highest rating first (-r[1]), if tied, faster time first (r[2])
    return (-r[1], r[2])

def by_time(r):
    # Fastest first (r[2]), if tied, higher rating first (-r[1])
    return (r[2], -r[1])

def main():
    choice = input("Sort by (rating/time): ").strip().lower()
    
    if choice == "rating":
        sorted_restaurants = sorted(RESTAURANTS, key=by_rating)
    elif choice == "time":
        sorted_restaurants = sorted(RESTAURANTS, key=by_time)
    else:
        print("Unknown option")
        return

    # Print the numbered list
    for i, (name, rating, minutes) in enumerate(sorted_restaurants, 1):
        print(f"{i}. {name}, {rating} stars, {minutes} min")

main()