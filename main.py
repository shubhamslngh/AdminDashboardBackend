def find_substring(input_str, k):
    n = len(input_str)
    min_length = n + 1
    min_substring = ""

    left = 0
    count_ones = 0

    for right in range(n):
        if input_str[right] == '1':
            count_ones += 1

        while count_ones == k:
            current_substring = input_str[left:right+1]
            current_length = right - left + 1

            if current_length < min_length or (current_length == min_length and current_substring < min_substring):
                min_length = current_length
                min_substring = current_substring

            if input_str[left] == '1':
                count_ones -= 1

            left += 1

    return min_substring

# Example usage
input_str = "10101"
k = 2
result = find_substring(input_str, k)
print(result)  # Output: "101"
