class Solution:
  def remainingMethods(self, n: int, k: int, invocations: list[list[int]]) -> list[int]:
    graph = [[] for _ in range(n)]
    for u, v in invocations:
      graph[u].append(v)
      
    suspicious = set()
    stack = [k]
    suspicious.add(k)
    
    while stack:
      curr = stack.pop()
      for neighbor in graph[curr]:
        if neighbor not in suspicious:
          suspicious.add(neighbor)
          stack.append(neighbor)
              
    for u, v in invocations:
      if u not in suspicious and v in suspicious:
        return list(range(n))
        
    return [i for i in range(n) if i not in suspicious]