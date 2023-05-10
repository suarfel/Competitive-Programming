class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
    
        graph = defaultdict(list)
        in_coming =  defaultdict(int)
        
        for i in range(len(recipes)):
            for j in range(len(ingredients[i])):
                graph[ingredients[i][j]].append(recipes[i])
            in_coming[recipes[i]] = len(ingredients[i])
            
            
      
        
        queue = deque(supplies)
         
        ans  = []
        while queue:
            
            ingre = queue.popleft()
            
            for recipe in graph[ingre]:
                
                in_coming[recipe] -= 1
                if in_coming[recipe] == 0:
                    queue.append(recipe)
                    ans.append(recipe)
        return ans
        
        