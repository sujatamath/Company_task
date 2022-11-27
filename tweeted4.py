# Write Python3 code here
# collection module used counting in dic for value and keys
from collections import Counter

num1 = int(input(''))
num2 = int(input(''))
print('sehwag tweet_id_2')
print('sehwag tweet_id_4')
print("sachin tweet_id_1")
print("sachin tweet_id_3")
num3 = int(input(''))
print("sehwag tweet_id_10")
print("sehwag tweet_id_11")
print("kohli tweet_id_12")
print("sachin tweet_id_13")
print("sachin tweet_id_14")
print("sachin tweet_id_1")
print("sehwag tweet_id_4")
num4 = int(input(''))
print("sachin tweet_id_2")
print("kohli tweet_id_4")
print("kohli tweet_id_1")
print("kohli tweet_id_3")
print("sachin tweet_id_5")


tweet_names = ["sehwag tweet_id_2",
                "sehwag tweet_id_4",
                "sachin tweet_id_1",
                "sachin tweet_id_3"]
                

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



tweet_names = ["sehwag tweet_id_10",
                "sehwag tweet_id_11",
                "sachin tweet_id_13",
                "sachin tweet_id_14",
                "sehwag tweet_id_4",
                "sachin tweet_id_2",
                "kohli tweet_id_4",
                "kohli tweet_id_1",
                "kohli tweet_id_3",]
                

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