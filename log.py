import os
from datetime import datetime

today = datetime.now().strftime("%B %d, %Y")
time_now = datetime.now().strftime("%I:%M %p")

print("\n--- 🌐 Web Daily Log Generator ---")
focus = input("1. What was your primary focus today? ")
completed = input("2. What is one key task you completed? ")
learned = input("3. What is one new thing you learned? ")
rating_str = input("4. How was your day (1 to 5)? ")

try:
    rating = max(1, min(5, int(rating_str)))
except:
    rating = 5

stars = "⭐" * rating
percent = rating * 20

# 1. Save to JOURNAL.md as backup
md_entry = f"\n## Log: {today} ({time_now})\n* **Focus:** {focus}\n* **Completed:** {completed}\n* **Learned:** {learned}\n* **Rating:** {stars} ({rating}/5)\n---\n"
with open("JOURNAL.md", "a") as f:
    f.write(md_entry)

# 2. Create HTML card with graphics
card_html = f"""
        <!-- NEW_ENTRY -->
        <div class="card">
            <div class="card-header">
                <span class="date">📅 {today} • {time_now}</span>
                <span class="stars">{stars}</span>
            </div>
            <div class="card-body">
                <p><strong>🎯 Primary Focus:</strong> {focus}</p>
                <p><strong>✅ Completed:</strong> {completed}</p>
                <p><strong>💡 Learned:</strong> {learned}</p>
            </div>
            <div class="progress-label">Day Energy / Rating ({percent}%)</div>
            <div class="progress-bg">
                <div class="progress-bar" style="width: {percent}%;"></div>
            </div>
        </div>"""

html_file = "index.html"

# Base website template if index.html doesn't exist yet
if not os.path.exists(html_file):
    base_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chandana's Daily Log</title>
    <style>
        body {
            background: linear-gradient(135deg, #0f172a, #1e1b4b);
            color: #f8fafc;
            font-family: 'Segoe UI', Roboto, sans-serif;
            margin: 0;
            padding: 20px;
            min-height: 100vh;
        }
        .container {
            max-width: 650px;
            margin: 0 auto;
        }
        header {
            text-align: center;
            padding: 35px 20px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 20px;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.4);
        }
        h1 {
            margin: 0;
            font-size: 2rem;
            background: linear-gradient(90deg, #38bdf8, #c084fc);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        header p {
            color: #94a3b8;
            margin-top: 8px;
            font-size: 0.95rem;
        }
        .card {
            background: rgba(30, 41, 59, 0.75);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            padding: 22px;
            margin-bottom: 20px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
            transition: transform 0.2s ease, border-color 0.2s ease;
        }
        .card:hover {
            transform: translateY(-4px);
            border-color: #38bdf8;
        }
        .card-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            padding-bottom: 12px;
            margin-bottom: 15px;
        }
        .date {
            color: #38bdf8;
            font-weight: 600;
            font-size: 0.9rem;
        }
        .card-body p {
            margin: 12px 0;
            line-height: 1.5;
            color: #e2e8f0;
        }
        .progress-label {
            font-size: 0.75rem;
            color: #94a3b8;
            margin-top: 15px;
            margin-bottom: 6px;
        }
        .progress-bg {
            background: rgba(255, 255, 255, 0.1);
            height: 8px;
            border-radius: 4px;
            overflow: hidden;
        }
        .progress-bar {
            background: linear-gradient(90deg, #38bdf8, #818cf8, #c084fc);
            height: 100%;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🚀 Chandana's Daily Log</h1>
            <p>Automated Developer Journal • Built from Android</p>
        </header>
        <div id="entries">
        <!-- NEW_ENTRY -->
        </div>
    </div>
</body>
</html>"""
    with open(html_file, "w") as f:
        f.write(base_html)

# Insert the new card at the top of the website
with open(html_file, "r") as f:
    content = f.read()

updated_content = content.replace("<!-- NEW_ENTRY -->", card_html, 1)

with open(html_file, "w") as f:
    f.write(updated_content)

print("\n✨ Success! Graphic card added to index.html and JOURNAL.md!")
