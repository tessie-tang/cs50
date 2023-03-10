import csv
import sys
import copy

def main():
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        return 1


    file = open(sys.argv[1])
    reader = csv.DictReader(file)
    names = reader.fieldnames[1:]

    dna_dict = {}
    with open(sys.argv[2]) as file:
        r = csv.reader(file)
        dna = r.__next__()[0]

    for n in names:
        dna_dict[n] = str((longest_match(dna, n)))

    result = False
    for row in reader:
        cpy = copy.copy(row)
        cpy.pop('name')
        if cpy == dna_dict:
            print(row['name'])
            result = True

    if result == False:
        print("No match")

def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
