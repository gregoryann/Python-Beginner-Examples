def insertion_sort(items):
    # Split the list into sorted and unsorted
    # For each element in unsorted...
    counter = 0
    for i in range(1, len(items)):
        print(items)
        # Insert that element into the correct place in sorted by:
        # Store the element in a temp variable
        temp = items[i]
        # Shifting all larger sorted elements to the right by 1
        j = i
        while j > 0 and temp < items[j - 1]:
            counter += 1
            items[j] = items[j - 1]
            j -= 1
        # Insert the element after the first smaller elememnt
        items[j] = temp
        print(f"counter: {counter}")
    return items