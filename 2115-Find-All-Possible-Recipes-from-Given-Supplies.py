class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        neighbors = defaultdict(list)
        indegree = defaultdict(int)

        for i in range(len(ingredients)):
            for j in range(len(ingredients[i])):
                ingredient = ingredients[i][j]
                recipe = recipes[i]
                neighbors[ingredient].append(recipe)
                indegree[recipe] += 1

        # Kahn's Algo
        queue = deque()
        for supply in supplies:
            queue.append(supply)

        recipes = set(recipes)
        res = []
        while queue:
            curr = queue.popleft()
            if curr in recipes:
                res.append(curr)

            for nei in neighbors[curr]:
                indegree[nei] -= 1
                if not indegree[nei]:
                    queue.append(nei)

        return res