scores = {"arjun": 85, "meera": 92, "rahul": 78, "anu": 95}

top_student = max(scores, key=scores.get)
top_score = scores[top_student]

print("Student with the maximum marks:")
print("Name :", top_student)
print("Score:", top_score)