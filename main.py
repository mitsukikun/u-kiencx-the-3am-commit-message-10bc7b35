import os

PREFIX = "fix: it works now, "
MIDDLE = "I don't know why, I don't want to know why, "
ENDING = "and if you touch it I will scream"
LINE = PREFIX + MIDDLE + ENDING

# Entry line must stay within 139 characters (competition limit).
MAX_CHARS = 139

if len(LINE) > MAX_CHARS:
    raise ValueError("line exceeds 139 characters")

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
