import pandas as pd

# Load the CSV from the downloaded file
df = pd.read_csv('timetable.csv')

# Format the data into Markdown for the README
table_md = df.to_markdown(index=False)

# Update the README file
with open("README.md", "r") as file:
    lines = file.readlines()

# Replace existing table or append
with open("README.md", "w") as file:
    in_table_section = False
    for line in lines:
        if line.strip() == "## 📅 Study Timetable":
            in_table_section = True
            file.write(line)
            file.write(table_md)
        elif in_table_section and line.strip().startswith("#"):
            in_table_section = False
            file.write(line)
        elif not in_table_section:
            file.write(line)
