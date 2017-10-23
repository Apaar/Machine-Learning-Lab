#Code:

import random
import sys

def calculate_means(cluster):
    means = []
    for k in cluster:
        sum_cluster = 0
        for p in k:
            sum_cluster+=p
        means.append(sum_cluster/len(k))
    return means
    
def generate_random(data,k):
    # 1. k initial "means" are randomly selected from the data set.
    l = random.sample(range(0, len(data)), k)
    #print(l) l has indices of k random numbers
    
    # 2. k clusters are created by associating every observation with the nearest mean.
    cluster = []
    for i in l:
        new_list = []
        new_list.append(data[i])
        cluster.append(new_list)
        
    return cluster  
    
def validate_cluster(cluster):
    cluster = sorted(cluster)
    for i in range(len(cluster)-1):
        if cluster[i] == cluster[i+1]:
            return False
    return True
    
    
def k_means(data, k):
    
    val = False
    while val == False:
        cluster = generate_random(data,k)
        val = validate_cluster(cluster)
    
    
    means = calculate_means(cluster)

    
    cluster_equal = False
    it = 0
    while not cluster_equal:
        it+=1
        prev_cluster = cluster
        cluster = []
        for i in range(k):
            cluster.append([])
        for num in range(len(data)):
                min_index = 0
                cur_min = sys.maxsize
                for mean_index in range(len(means)):
                    if abs(means[mean_index]-data[num]) < cur_min:
                        min_index = mean_index
                        cur_min = abs(means[mean_index]-data[num])
                cluster[min_index].append(data[num])
        
        means = calculate_means(cluster)
        print(prev_cluster)
        print(cluster)
        print()
        cluster_equal = sorted(prev_cluster)==sorted(cluster)
    print(it)
    print()
    return cluster



if __name__ == '__main__':
    Ages = [15,15,16,19,19,20,20,21,22,28,35,40,41,42,43,44,60,61,65]
    print(list(k_means(Ages, 10)))


