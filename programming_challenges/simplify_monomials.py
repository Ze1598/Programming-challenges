def simplify(poly):
    # Strings with characters for stripping
    digits = '0123456789'
    letters = 'abcdefghijklmnopqrstuvwxyz+-'
    # String to hold the simplified monomials
    simple_list = []

    # Separate the positive and negative monomials present in the input string.
    # Split at the plus sign.
    pos = [mon for mon in poly.split('+') if mon[0] != '-']
    neg = [mon for mon in poly.split('+') if mon[0] == '-']
    # Since positives and negatives will end up completely separated, remove 
    # the negative sign from the first negative monomial if it exists
    if neg:
        neg[0] = neg[0].replace('-', '')

    # Loop through the first positives list, and if any of the monomials can\
    # be split at '-' signs, it means there are negative monomials mixed in.\
    # Add split positives to the positives list and negatives to the negative\
    # list.
    # Do not forget to remove the split monomial from the positives list.
    # Create a temporary positive list so that the positive monomials list does\
    # not contain the strings with mixed monomials.
    pos_ = []
    for mon in pos:
        if len(mon.split('-')) > 1:
            split_neg = mon.split('-')
            pos_.append(split_neg[0])
            neg += [i for i in split_neg[1:]]
        else:
            pos_.append(mon)

    # Sort the monomials in both lists (both the monomials and the\
    # lists themselves)
    # At this point, the monomials have no signs but are separated\
    # between positive and negative
    pos = sorted([''.join(sorted(mon)) for mon in pos_])
    neg = sorted([''.join(sorted(mon)) for mon in neg])

    # Create a dictionary for all the different positive monomials and its\
    # corresponding total numerical value
    # Negative monomials are not involved in this part
    pos_vals = {}
    for mon in pos:
        mon_coeff = int(mon.strip(letters)) if mon.strip(letters) else 1
        mon_lit = mon.strip(digits)
        if mon_lit not in pos_vals:
            pos_vals[mon_lit] = mon_coeff
        else:
            pos_vals[mon_lit] += mon_coeff
    
    # Repeat the previous process for the negative monomials
    # Positive monomials are not involved in this part
    neg_vals = {}
    for mon in neg:
        mon_coeff = int(mon.strip(letters)) if mon.strip(letters) else 1
        mon_lit = mon.strip(digits)
        if mon_lit not in neg_vals:
            neg_vals[mon_lit] = mon_coeff
        else:
            neg_vals[mon_lit] += mon_coeff

    # At this point, the monomials still don't have signs assigned, they\
    # are only separated between positives and negatives

    # First loop through the positive monomials and subtract the\
    # corresponding negative monomials
    for mon in pos_vals:
        if mon in neg_vals:
            pos_vals[mon] -= neg_vals[mon]
            # Since this is a common monomial, delete it from the\
            # negative dictionary to avoid redundant looping
            del neg_vals[mon]
        # Only add this monomial to the simplified polynomial if its\
        # coefficient is not 0
        if pos_vals[mon]:
            # If the coefficient is 1, then it does need to be written\
            # in the final polynomial, just the literal part
            if pos_vals[mon] == 1:
                simple_list.append('+' + mon)
            else:
                simple_list.append('+' + str(pos_vals[mon]) + mon)
    
    for mon in neg_vals:
        # If the coefficient is 1, then only the literal part will\
        # appear in the final polynomial
        if neg_vals[mon] == 1:
            simple_list.append('-' + mon)
        else:
            simple_list.append('-' + str(neg_vals[mon]) + mon)

    # Sorted by length
    # simple_list = ''.join(sorted(simple_list, key=lambda x: len(x)))
    # Sorted by lexicographical order
    # simple_list = ''.join(sorted(simple_list, key=lambda x: (len(x.strip('+-'+digits)), x.strip('-+'))))
    simple_list = ''.join(sorted(simple_list, key=lambda x: (len(x.strip('+-'+digits)), x.strip('-+'+digits))))
    
    # Remove leading '+' sign if it's the case
    if simple_list:
        if simple_list[0] == '+':
            return simple_list[1:]
        else:
            return simple_list

polies = ['2xy-yx', 'dc+dcba', '-a+5ab+3a-c-2a', 'a+ca-ab', '-y+x', '-ab+b+4ac+4a']
results = ['xy', 'cd+abcd', '-c+5ab', 'a-ab+ac', 'x-y', '4a+b-ab+4ac']

for i in range(len(polies)):
    print('Polynomial:', polies[i])
    print('Simplified string:', simplify(polies[i]))
    print('Expected result:', results[i])
    print()