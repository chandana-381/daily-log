from datetime import datetime

today = datetime.now().strftime("%Y-%m-%d")
time_now = datetime.now().strftime("%I:%M %p")

print("\n--- Daily Log Entry Generator ---")
focus = input("1. What was your primary focus today? ")
completed = input("2. What is one key task you completed? ")
learned = input("3. What is one new thing you learned? ")
rating = input("4. How was your day (1 to 5)? ")

entry = f"""
## Log: {today} ({time_now})

* **Primary Focus:** {focus}
* **Completed:** {completed}
* **What I Learned:** {learned}
* **Day Rating:** {rating}/5

---
"""

with open("JOURNAL.md", "a") as file:
    file.write(entry)

print("\nSuccess! Entry saved to JOURNAL.md")
