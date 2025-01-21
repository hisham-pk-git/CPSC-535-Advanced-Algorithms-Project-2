def trap_water(elevations):
    # Edge case: if the array is empty or has fewer than 3 elements, no water can be trapped
    if not elevations or len(elevations) < 3:
        return 0

    # Initialize pointers and max height trackers
    start = 0
    end = len(elevations) - 1
    left_max_height = 0
    right_max_height = 0
    total_trapped_water = 0

    # Iterate while the start pointer is less than the end pointer
    while start < end:
        # If the height at the start pointer is less than the height at the end pointer
        if elevations[start] < elevations[end]:
            
            if elevations[start] >= left_max_height:
                # set new left_max
                left_max_height = elevations[start] 
            else:
                # If the height at start is less than the left maximum, it can trap water
                total_trapped_water += left_max_height - elevations[start]
            # Move the start pointer inward
            start += 1
        else:
            
            if elevations[end] >= right_max_height:
                # set new right_max
                right_max_height = elevations[end]
            else:
                # If the height at end is less than the right maximum, it can trap water
                total_trapped_water += right_max_height - elevations[end]
            # Move the end pointer inward
            end -= 1

    return total_trapped_water


def main():
    # Authors: Hisham Panamthodi  Kajahussain, Kenny Le
    # Ask user for input
    try:
        # Input the elevation chart as space-separated integers
        heights = list(map(int, input("Enter the elevation chart (space-separated values): ").split()))

        # Calculate and print the total trapped water
        result = trap_water(heights)
        print(f"Total trapped water: {result} units")

    except ValueError:
        print("Invalid input. Please enter space-separated integers.")

# Run the program
if __name__ == "__main__":
    main()
