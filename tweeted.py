# Write Python3 code here
# collection module used counting in dic for value and keys
from collections import Counter
tweet_names = ["sachin tweet_id_1",
                "sehwag tweet_id_2",
                "sachin tweet_id_3",
                "sachin tweet_id_4"]

uniq_names = [pref_names.split()[0] for pref_names in tweet_names]

times = Counter(uniq_names)
repeat = times.values()

for element in set(repeat):
    dup1 = ([(key, value) for key, value in sorted(times.items()) if value == element])

    if len(dup1) > 1:
        for (key, value) in dup1:
            print(key, '' ,value)
    max_value = max(times.values())
    temp_max_result = [(key, value) for key, value in sorted(times.items()) if value == max_value]

    if temp_max_result != dup1:
        for (key, value) in temp_max_result:
            print(key, '' ,value)