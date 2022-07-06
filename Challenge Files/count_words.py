from collections import Counter
from prettytable import PrettyTable


def count_words(filepath):
    with open(filepath, "r") as f:
        contents = f.readlines()

    strn = "".join([x.strip().lower() for x in contents if len(x) > 1])
    # Chose to convert to lowercase so E and e would count as the same character
    word_list = strn.split()
    num = 0
    top20 = Counter(word_list).most_common(20)
    print(f"-- 📖 Reading file {filepath} --")
    print(f"Total Words: {len(word_list)}")
    print("Top 20 Most Frequent Words:")
    myTable = PrettyTable(["Ranking", "Word", "Frequency"])
    for top in top20:
        num += 1
        myTable.add_row([f"#{num}", top[0], top[1]])
    print(myTable)


count_words("pride_and_prej_first_chapter.txt")


"""
GIVEN SOLUTION
"""
# import re
# import collections

# def count_words(path):
#     with open(path, encoding='utf-8') as file:
#         all_words = re.findall(r"[0-9a-zA-Z-]+", file.read())
#         all_words = [word.upper() for word in all_words]
#         print(all_words)
#         print("\nTotal Words:", len(all_words))
#
#         word_counts = collections.Counter(all_words)
#
#         print("\nTop 20 Words:")
#         for word in word_counts.most_common(20):
#             print(word[0], '\t', word[1])

# count_words("pride_and_prej_first_chapter.txt")


### REFLECTION ###
# Solution quite similar once again
# Point of improvement is maybe the selection of words as we had differing results when calculating the frequencies
# The solution given would remove all contracted words which is an interesting distinctions
