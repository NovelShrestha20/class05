#different
"""
Random Presentation Scheduler
--------------------------------------
You:
  1. Enter a list of names.
  2. Enter a list of topics.
The program:
  - Randomly assigns each person a topic.
  - Randomly assigns a day for each presentation.
  - Uses default days: Monday to Friday
"""

import random

# 1️⃣ Get names
names = []
print("Enter the names of presenters (type 'done' to finish):")
while True:
    name = input("Name: ").strip()
    if name.lower() == 'done':
        break
    if name:
        names.append(name)

# 2️⃣ Get topics
topics = []
print("\nEnter presentation topics (type 'done' to finish):")
while True:
    topic = input("Topic: ").strip()
    if topic.lower() == 'done':
        break
    if topic:
        topics.append(topic)

# 3️⃣ Check input
if not names or not topics:
    print("\n⚠️ Please enter at least one name and one topic. Try again.")
    quit()

# 4️⃣ Default list of days
default_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Shuffle everything for randomness
random.shuffle(names)
random.shuffle(topics)
random.shuffle(default_days)

# 5️⃣ Assign presentations
print("\n📅 Presentation Schedule 📅\n")

for i in range(len(names)):
    person = names[i]
    topic = topics[i % len(topics)]  # If fewer topics than people, reuse
    day = default_days[i % len(default_days)]  # Reuse days if needed

    print(f"{person} will present on \"{topic}\" on {day}.")

# 6️⃣ Pause (optional)
input("\nPress Enter to finish.")





"""source chat gpt"""