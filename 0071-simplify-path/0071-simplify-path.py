class Solution:
    def simplifyPath(self, path: str) -> str:
        canonical_path = ""
        canonical_list = []
        path_list = path.split('/')
        for i in path_list:
            if i == "" or i == ".":
                continue
            elif i == "..":
                if len( canonical_list) >0:
                    canonical_list.pop(-1)
            else:
                canonical_list.append(i)
        if len(canonical_list) == 0:
            return "/"
        else :
            while len(canonical_list) != 0:
                canonical_path = "/" + canonical_list.pop(-1) + canonical_path
        return canonical_path
            

 
                
        
        