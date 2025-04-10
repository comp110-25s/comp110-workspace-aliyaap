"""File to define River class."""

from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear


class River:
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        surviving_bears: list[Bear] = []
        surviving_fish: list[Fish] = []
        idx_bears: int = 0
        idx_fish: int = 0
        while idx_bears < len(self.bears):
            if self.bears[idx_bears].age < 5:
                surviving_bears.append(self.bears[idx_bears])
            idx_bears += 1
        self.bears = surviving_bears
        while idx_fish < len(self.fish):
            if self.fish[idx_fish].age < 3:
                surviving_fish.append(self.fish[idx_fish])
            idx_fish += 1
        self.fish = surviving_fish
        return None

    def bears_eating(self):
        if len(self.fish) <= 5:
            idx_fish: int = 0
            while idx_fish < 3:
                self.fish.pop(idx_fish)
            idx_fish += 1
        return None

    def check_hunger(self):
        idx_bears: int = 0
        hungry_bears: list[Bear] = []
        while idx_bears < len(self.bears):
            if self.bears[idx_bears].hunger_score < 0:
                hungry_bears.append(self.bears[idx_bears])
            idx_bears += 1
        self.bears = hungry_bears
        return None

    def repopulate_fish(self):
        fish_pairs: int = len(self.bears) // 2
        new_fish: int = fish_pairs * 4
        while new_fish > 0:
            self.fish.append(Fish())
            new_fish -= 1
        return None

    def repopulate_bears(self):
        bear_pairs: int = len(self.bears) // 2
        while bear_pairs > 0:
            self.bears.append(Bear())
            bear_pairs -= 1
        return None

    def view_river(self):

        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        count = 0
        while count < 7:
            self.one_river_day()
            count += 1
        return None

    def remove_fish(self, amount: int):

        idx_fish: int = 0
        while idx_fish <= amount:
            self.fish.pop(idx_fish)
        idx_fish += 1

        return None
