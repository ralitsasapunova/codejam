from math import gcd

def main():
    test_cases = int(input())

    for i in range(test_cases):
        input() # dont need n and length
        numbers = list(map(int, input().strip().split()))
        current_greatest_common_divisor = gcd(numbers[0], numbers[1])
        other_divisor = numbers[0] // current_greatest_common_divisor

        all_primes = set()
        all_primes.add(current_greatest_common_divisor)
        all_primes.add(other_divisor)

        pairs = list()
        pairs.append([other_divisor, current_greatest_common_divisor])

        for number in numbers[1:]:
            other_divisor = number // current_greatest_common_divisor
            all_primes.add(other_divisor)
            pairs.append([current_greatest_common_divisor, other_divisor])
            current_greatest_common_divisor = other_divisor

        prime_dict = {}
        for index, prime in enumerate(sorted(all_primes)):
            prime_dict[prime] = chr(65 + index)

        result = list()
        result.append(prime_dict[pairs[0][0]])

        for pair in pairs:
            result.append(prime_dict[pair[1]])

        print("".join(result))

if __name__ == '__main__':
    main()