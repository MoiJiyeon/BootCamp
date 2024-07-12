def count_ordered_pairs(input_string, target_sequence):
    count = 0
    current_count = [0] * len(target_sequence)

    for char in input_string:
        for i, target_char in enumerate(target_sequence):
            if char == target_char:
                if i == 0:
                    current_count[i] += 1
                else:
                    current_count[i] += current_count[i - 1]

    return current_count[-1]

# 테스트
input_string = 'GTPPCACZTPC
target_sequence = 'GTPC'

pairs_count = count_ordered_pairs(input_string, target_sequence)
print(f"순서쌍의 개수: {pairs_count}")
