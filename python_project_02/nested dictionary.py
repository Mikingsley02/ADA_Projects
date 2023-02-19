# Creating a nested dictionary for students with three tracks
ada_program = {
    "frontend_dev": {
        "stud_name": list(set(["Amaka disappoint", "Pretty cynthia", "Nedu japan"])),
        "stud_score": [70, 80, 90]
    },
    "backend_dev": {
        "stud_name": list(set(["jon bellion", "john doe", "john bellcat"])),
        "stud_score": [50, 60, 65]
    },
    "data": {
        "stud_name": list(set(["ada ada", "doja cat", "dog catcher", "bitrus beetroot", "beja rat", "pyhon ezege"])),
        "stud_score": [40, 100, 50, 75, 95, 85]
    }
}

#the scores for each student in each track
for track_name, track_data in ada_program.items():
    for i, student_name in enumerate(track_data["stud_name"]):
        track_data["stud_score"] [i]

# Printing the scores
print("The top students are:")
for track_name, track_data in ada_program.items():
    sorted_indexes = sorted(range(len(track_data["stud_name"])), key=lambda i: track_data["stud_score"][i], reverse=True)
    top_students = [
        f"{track_data['stud_name'][i]} with score of {track_data['stud_score'][i]} for {track_name} track"
        for i in sorted_indexes[:3]
    ]
    print(", ".join(top_students) + ".")
