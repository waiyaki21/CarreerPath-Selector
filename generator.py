import pandas as pd
from collections import defaultdict
from pathlib import Path

# ==========================
# CONFIG
# ==========================
INPUT_EXCEL = "C:/Users/Kelvin Waiyaki/Desktop/SCHOOL DOCS/SENIOR SELECTION/information/ALL_ALL_FILTERED.xlsx" 
OUTPUT_FILE = "C:/Users/Kelvin Waiyaki/Desktop/SCHOOL DOCS/SENIOR SELECTION/information/raw_data_map.py"

# ==========================
# READ EXCEL
# ==========================
df = pd.read_excel(INPUT_EXCEL)

# Normalize column names just in case
df.columns = [c.strip().lower() for c in df.columns]

required_cols = {
    "code",
    "track",
    "subject 1",
    "subject 2",
    "subject 3",
}

missing = required_cols - set(df.columns)
if missing:
    raise ValueError(f"Missing columns: {missing}")

# ==========================
# GROUP BY TRACK
# ==========================
grouped = defaultdict(list)

for _, row in df.iterrows():
    track = str(row["track"]).strip().upper()

    subjects = [
        str(row["subject 1"]).strip(),
        str(row["subject 2"]).strip(),
        str(row["subject 3"]).strip(),
    ]

    code = str(row["code"]).strip()

    grouped[track].append({
        "subjects": subjects,
        "code": code,
    })

# ==========================
# BUILD raw_data_map STRING
# ==========================
lines = []
lines.append("raw_data_map = {\n")

for track, entries in grouped.items():
    lines.append(f'    "{track}": """\n')

    for entry in entries:
        subject_line = ",".join(entry["subjects"])
        lines.append(f"{subject_line}\n")
        lines.append(f"Code: {entry['code']} | Track: {track}\n")

    lines.append('""",\n')

lines.append("}\n")

# ==========================
# WRITE OUTPUT
# ==========================
Path(OUTPUT_FILE).write_text("".join(lines), encoding="utf-8")

print(f"✅ raw_data_map written to {OUTPUT_FILE}")
