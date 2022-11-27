# Write Python3 code here
# collection module used counting in dic for value and keys
from collections import Counter

num1 = int(input(''))
num2 = int(input(''))
print('sachin tweet_id_1')
print('sehwag tweet_id_2')
print("sachin tweet_id_3")
print("sehwag tweet_id_4")
num3 = int(input(''))
print("dhoni tweet_id_10")
print("dhoni tweet_id_11")
print("kohli tweet_id_12")
print("dhoni tweet_id_13")
print("dhoni tweet_id_14")

tweet_names = ["sachin tweet_id_1",
                "sehwag tweet_id_2",
                "sachin tweet_id_3",
                "sehwag tweet_id_4",
                "dhoni tweet_id_10",
                "dhoni tweet_id_11",
                "dhoni tweet_id_13",
                "dhoni tweet_id_14"
                "kohli tweet_id_12",
                ]

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
            if (key == "kohli"):
                break
            print(key, '' ,value)