# AIM: Implement a fxn that converts a spreadsheet column ID (i.e, "A", "B",...,"Z", "AA", etc) to the corresponding integer.
# "A" = 1, "AA"= 27, 27th column.
# Note: key insight is to think of the column IDs as base 26 integers.
# A = 1, B = 2, C = 3,..., Z = 26
# Example:
#                A A
#                 |
# A * 26**(n-1) + A * 26**(n-n)
# 1 * 26**1 + 1 * 26**0 = 27.

# The Code
def spreadsheet_encode_column(col_str):
    num = 0
    count = len(col_str)-1
    for s in col_str:
        num +=  (ord(s) - ord('A') + 1) * 26**count
        count -= 1
    return num


print(spreadsheet_encode_column("ZZ"))
