from collections import defaultdict,deque


class Solution:
    def __generate_adj_list(self,wordList):
        adj = defaultdict(list)
        for w in wordList:
            for i in range(len(w)):
                adj[w[:i]+'*'+w[i+1:]].append(w)
        return adj
                
    
    def bfs(self,adj,beginWord,endWord):
        
        q = deque([(beginWord,[beginWord])])
        visited = set([beginWord])
        ans = []
        
        found = False
        
        while q and not found:
            length = len(q)
            localVisited = set()
            for _ in range(length):
                w,path = q.popleft()
                for i in range(len(w)):
                    for neigh in adj[w[:i]+'*'+w[i+1:]]:
                    
                        if neigh == endWord:
                            ans.append(path+[neigh])
                            found = True
                        if neigh not in visited:
                            localVisited.add(neigh)
                            q.append((neigh,path+[neigh]))
            visited = visited.union(localVisited)
        return ans
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        if beginWord==endWord or endWord not in wordList:
            return []
        
        adj = self.__generate_adj_list(wordList+[beginWord])
       
        
        return self.bfs(adj,beginWord,endWord)
