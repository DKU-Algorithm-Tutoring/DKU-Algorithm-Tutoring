import heapq

N = int(input())
N_list = []
for i in range(N) :
    N_list[i] = input()
    N_list[i] = int(N_list[i])
heap = []
for i in range(N) :
    if N_list[i] == 0 :
        if heap is not None :
            heapq.heappop(heap)
            print(heap[0])
        else :
            print("0")




