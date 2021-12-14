def longestCommonPrefix(strs) -> str:
    prefix = strs[0]
    new_prefix = ""

    for word in strs[1:]:

        for let1, let2 in zip(prefix, word):
            if let1 == let2:
                new_prefix += let1
            else:
                break

        prefix = new_prefix
        new_prefix = ""

    return prefix


longestCommonPrefix(["dog","racecar","car"])