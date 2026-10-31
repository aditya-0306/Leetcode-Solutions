

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_map = {} # food -> [cuisine, rating]
        self.cuisine_map = defaultdict(SortedSet) # cuisine -> SortedSet of (-rating, food)
        
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_map[food] = [cuisine, rating]
            self.cuisine_map[cuisine].add((-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, old_rating = self.food_map[food]
        
        # Remove old entry from sorted set
        self.cuisine_map[cuisine].remove((-old_rating, food))
        # Add new entry
        self.cuisine_map[cuisine].add((-newRating, food))
        # Update food map
        self.food_map[food][1] = newRating

    def highestRated(self, cuisine: str) -> str:
        # The first element has the highest rating (most negative) and lexicographically smallest name
        return self.cuisine_map[cuisine][0][1]
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)