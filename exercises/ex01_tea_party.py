"""Let's plan a tea party!"""

__author__: str = "730466316"


def main_planner(guests: int) -> None:
    """Entrypoint of function."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Calculate how many tea bags are needed."""
    return people * 2


def treats(people: int) -> int:
    """Calculates how many treats are needed."""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculates the cost of tea bags and treats."""
    return ((tea_count) * 0.5) + ((treat_count) * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending?")))
