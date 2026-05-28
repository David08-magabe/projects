import statistics
def mean_median_mode(list):
    return statistics.mean(list), statistics.median(list), statistics.mode(list)
a,b,c=mean_median_mode([24,3,56,8,9,10])

print(f"mean is {a}\nmedian is {b}\nmedian is {c}")