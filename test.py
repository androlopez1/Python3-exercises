##def solution(A):
##    pass
##    N = len(A)
##    for p in range (0,N):
##        suma = 0;
##        sumados = 0;
##        for i in range(0,len(A)):
##            if i < p:
##                suma = suma + A[i]
##            elif i > p:
##                sumados = sumados + A[i]
##
##        if suma == sumados:
##            print (int(p))
##            break
##    
##A = [-1,3,-4,5,1,-6,2,1];
##solution(A);

##import math
##def solution (A):
##    N = len(A)
##    half = math.ceil(N/2)
##    A.sort
##    candidate = A[half]
##    count  = 0
##    for i in A:
##         if i == candidate:
##            count = count + 1
##    if count > half:
##        print (candidate)
##
##A = [3,3,3,50,3,3,8,3,3,3]
##solution(A)

##def solution(A):
##    N = len(A)
##    B = sorted(A)
##    count = 0
##    for i in range(0,N):
##        if A[i] == B[i]:
##            count = count + 1
##    different = N - count
##    if different > 2:        
##        print (1==2)
##    else:
##        print (1==1)
##        
##
##A = [1,3,3,4,7]
##solution(A)
   

##def solution(A, D):
##    pass
##    A.sort()
##    N = len(A)
##    stones = (N // D)
##    
##    if D <= N:
##        count = 0
##        for i in A:
##            
##            if i >= 0:
##                count = count + 1
##                if count == stones:
##                    print (i)
##                    break
##        if count < stones:
##            print(-1)
##
##    elif D > N:
##        print(0)
##                
###For answer i:
##D = 3
##A = [1, -1, 0, 2, 3, 5]
##solution (A,D)
###For answer -1:
##D = 2
##A = [1,-1,-1,-1,-1,-1,-1]
##solution(A,D)
###For answer 0:
##D = 8
##A = [1,-1,-1,-1,-1,-1,-1]
##solution(A,D)


##class Tree:
##
##    def _init_(self):
##        self.r = None
##        self.l = None
##        
##    
##
##def solution(T):
##    if T.l == None and T.r == None:
##        return 0
##    elif T.l == None:
##        return 1 + solution(T.r)
##    elif T.r == None:
##         return 1 + solution(T.l)
##    else:
##         return 1 + max(solution(T.l), solution(T.r))
##


##def  findNumber(arr, k):
##    for i in arr:
##        count = 0
##        if i == k:
##            count = 1
##            break;
##        else:
##            count = 0
##            
##    if count == 1:
##        return ('YES')
##    else:
##        return ('NO')
##
##arr = [5,1,2,3,4,5,1]
##k = 6
##
##findNumber(arr,k)



####
##def  oddNumbers(l, r):
##    for i in range(l+1,r+1):
##        if i%2 != 0:
##            return (i)
##
##oddNumbers(2,5)

##import urllib.request
##import json
##
##def  getMovieTitles(substr):
##        try:
##            url = "https://jsonmock.hackerrank.com/api/movies/search/?Title="+substr
##            resp = urllib.request.urlopen(url).read()
##            data = json.loads(resp)
##            print (data)
##        except urllib.error.HTTPError as e:
##            print("ERROR: ", e.read())
##        try:
##            url = "https://jsonmock.hackerrank.com/api/movies/search/?Title="+substr
##            resp = urllib.request.urlopen(url).read()
##            data = json.loads(resp)
##            print (data)
##        except urllib.error.HTTPError as e:
##            print("ERROR: ", e.read())
##        
##
##
##getMovieTitles('spiderman')
##


##def  decode(encoded):
##    encode = encoded.encode(encoding='')

##
##
##class Solution:
##    # @param start, a string
##    # @param end, a string
##    # @param dict, a set of string
##    # @return an integer
##    def findLadders(self, start, end, dict):
##        dict.add(start)
##        dict.add(end)
##        
##        result, cur, visited, found, trace = [], [start], set([start]), False, {word: [] for word in dict}  
##
##        while cur and not found:
##            for word in cur:
##                visited.add(word)
##                
##            next = set()
##            for word in cur:
##                for i in xrange(len(word)):
##                    for j in 'abcdefghijklmnopqrstuvwxyz':
##                        candidate = word[:i] + j + word[i + 1:]
##                        if candidate not in visited and candidate in dict:
##                            if candidate == end:
##                                found = True
##                            next.add(candidate)
##                            trace[candidate].append(word)
##            cur = next
##            
##        if found:
##            self.backtrack(result, trace, [], end)
##        
##        return result
##    
##    def backtrack(self, result, trace, path, word):
##        if not trace[word]:
##            result.append([word] + path)
##        else:
##            for prev in trace[word]:
##                self.backtrack(result, trace, [word] + path, prev)
##    
##print (Solution().findLadders("hit", "cog", set(["hot","dot","dog","lot","log"])))


##A=[[1,2,1,2,1,2],[3,4,3,4,3,4],[1,2,1,2,1,2],[3,4,3,4,3,4]]
##rows=len(A)
##columns=len(A[1])
##p=A[2][3]
##for p,k in range(0,rows):
##    for q,l in range(0,columns):
##        if A[(k+p)%N][]




##def lastLetters(word):
##    lastnum = word[len(word)-1]
##    last2num = word[len(word)-2]
##    print (lastnum, last2num)
##lastLetters('apple')
##



p = int(input().strip())
array =[]
pos = -1;
for a0 in range(p):
   n = int(input().strip())
   array.insert(a0,n)
print(array)
##    pos=pos+1
##    n = int(input().strip())












































    


