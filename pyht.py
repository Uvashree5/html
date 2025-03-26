import os
from datetime import datetime

# Ensure the output directory exists
os.makedirs("output", exist_ok=True)

# HTML content
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GitHub Actions HTML</title>
</head>
<body>
    <h1>Hello from GitHub Actions!</h1>
    <p>Generated on {datetime.now()}</p>
</body>
</html>
"""

# Write to the file
with open("output/index.html", "w") as file:
    file.write(html_content)

print("HTML file created successfully.")
