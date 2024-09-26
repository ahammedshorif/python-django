#define dictionary (dict)
student1 ={"Rahi": 100, "shorif":33, "emo": 69}
# calculate average scores
avg = sum(student1.values())/len(student1)


# calculate min and max scores
min_score = min(student1.values())
max_score = max(student1.values())

#print the all scores

print("Average fo student scores: ",avg)
print("Min score: ",min_score)
print("Max score: ",max_score)