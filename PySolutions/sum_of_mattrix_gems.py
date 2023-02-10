
from test_utils.helper_functions import verify_output

def  print_matrix(mat):
    for i in mat:
        pstr = ""
        for j in i:
            pstr += str(j) +  " "

def valid_direction(arr,i,j):
    return i >= 0 and i < len(arr) and j <  len(arr[0])


def update_matrix(queue,parent,max_score,arr,current_point,next_point):
    current_parent = parent[current_point[0]][current_point[1]]
    if valid_direction(arr,next_point[0],next_point[1]) and current_parent != next_point:
        old_score = max_score[next_point[0]][next_point[1]]
        new_score  = arr[next_point[0]][next_point[1]]+max_score[current_point[0]][current_point[1]]
        if new_score > old_score:
            queue.append(next_point)
            parent[next_point[0]][next_point[1]] = (current_point[0],current_point[1])
            max_score[next_point[0]][next_point[1]]  = new_score

def path(arr):
    max_score = [[-999999 for i in arr[0]] for j in range(len(arr))]
    parent = [[(-1,-1) for i in arr[0]] for j in range(len(arr))]
    max_score[0][0] = arr[0][0]

    queue  = [(0,0)]
    while  queue :
        current_point =  queue.pop(0)
        up = (current_point[0]-1,current_point[1])
        update_matrix(queue,parent,max_score,arr,current_point,up)
        down  = (current_point[0]+1,current_point[1])
        update_matrix(queue,parent,max_score,arr,current_point,down)
        right  = (current_point[0],current_point[1]+1)
        update_matrix(queue,parent,max_score,arr,current_point,right)


    return max_score[-1][-1]


if __name__ == "__main__":
    verify_output(18, path([[2,2,2],[2,2,2],[2,2,2]]))
    verify_output(1, path([[1,-1,1],[-1,1,-1],[1,-1,1]]))
    verify_output(20, path([[2,2,2,2],[2,2,2,2],[2,2,2,2]]))
