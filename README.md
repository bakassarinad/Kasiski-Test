# Kasiski Test

References:

https://arxiv.org/pdf/1912.04519 (Analyzing the Kasiski Method Against Vigenere Cipher)

The steps for the Kasiski method are:

a. Find all the repeating cryptograms inside the
coded text (long messages contain repetitive
cryptograms).

b. Calculate the distance between repeating
cryptograms.

c. Calculate all the factors (divisors) of the
distance (the divisor factor expresses the
key length).

d. Determine the slices of the set of dividing
factors. The value that appears in the slice
represents the number that appears on all the
dividing factors of the distances. This value
may be the key length. This is because
repeated strings can appear overlapping
