def first_fit_decreasing(items, bin_capacity):
    # Sort items in descending order
    items.sort(reverse=True)
    
    # List to store the bins and their remaining capacity
    bins = []
    
    for item in items:
        # Try to place item in an existing bin
        placed = False
        for i in range(len(bins)):
            if bins[i] >= item:
                bins[i] -= item
                placed = True
                break
        
        # If item didn't fit in any existing bin, create a new bin
        if not placed:
            bins.append(bin_capacity - item)
    
    # Number of bins used
    num_bins = len(bins)
    return num_bins, bins

# Example usage
items = [3, 5, 1, 2]
bin_capacity = 8

num_bins, bins = first_fit_decreasing(items, bin_capacity)
print("Number of bins used:", num_bins)
print("Bins remaining capacities:", bins)
