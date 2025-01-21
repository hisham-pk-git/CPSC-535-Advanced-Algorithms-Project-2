def longest_string_chain(words):
    # Sort words by their length (ascending order)
    words.sort(key=len)
    
    # Dictionary to store the longest chain ending with each word
    chain_map = {}
    longest_chain = []

    for word in words:
        chain_map[word] = [word]  # Initialize the chain for the current word
        
        # Try removing each character to form a predecessor
        for i in range(len(word)):
            predecessor = word[:i] + word[i+1:]

            # If the predecessor exists in the dictionary, update the chain
            if predecessor in chain_map:
                current_chain = [word] + chain_map[predecessor]
                if len(current_chain) > len(chain_map[word]):
                    chain_map[word] = current_chain
        
        # Track the longest chain found so far
        if len(chain_map[word]) > len(longest_chain):
            longest_chain = chain_map[word]
    
    # If the longest chain has only one string, return an empty array
    return longest_chain if len(longest_chain) > 1 else []

def main():
    # Authors: Hisham Panamthodi  Kajahussain, Kenny Le
    # Input from the user
    print("Enter the strings separated by space:")
    user_input = input().strip()
    
    # Split the input into a list of strings
    strings = user_input.split()
    
    # Find the longest string chain
    result = longest_string_chain(strings)
    
    # Print the result
    if result:
        print("Longest String Chain:")
        print(result)
    else:
        print("No valid string chain found.")

if __name__ == "__main__":
    main()
