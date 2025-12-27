from sortedcontainers import SortedList

class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.available = defaultdict(SortedList) # Movie - > Price, Shop
        self.rented = SortedList() # Price, Shop, Movie
        self.movieShopPrice = {}

        for shop, movie, price in entries:
            self.available[movie].add((price, shop))
            self.movieShopPrice[(movie, shop)] = price
            

    def search(self, movie: int) -> List[int]:
        # Cheapest shops
        res = []

        i = 0
        while i < len(self.available[movie]) and i < 5:
            price, shop = self.available[movie][i]
            res.append(shop)
            i += 1
        return res
        

    def rent(self, shop: int, movie: int) -> None:
        price = self.movieShopPrice[(movie, shop)]

        self.available[movie].discard((price, shop))
        self.rented.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.movieShopPrice[(movie, shop)]

        self.rented.remove((price, shop, movie))
        self.available[movie].add((price, shop))

    def report(self) -> List[List[int]]:
        # Cheapest rented

        res = []
        i = 0
        while i < len(self.rented) and i < 5:
            price, shop, movie = self.rented[i]
            res.append([shop, movie])
            i += 1

        return res
        