from collections import defaultdict, deque
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(set)
        recipes_s = set(recipes)
        in_degree = {c: 0 for c in recipes}
        for i in ingredients:
            for j in range(len(i)):
                in_degree[i[j]] = 0

        for i in range(len(recipes)):
            for j in range(len(ingredients[i])):
                if recipes[i] not in graph[ingredients[i][j]]:
                    graph[ingredients[i][j]].add(recipes[i])
                    in_degree[recipes[i]] += 1

        sources = deque([c for c in supplies])
        res = []
        while(sources):
            curr = sources.popleft()
            if curr in recipes_s:
                res.append(curr)

            for child in graph[curr]:
                in_degree[child] -=1
                if in_degree[child] == 0:
                    sources.append(child)

        return res