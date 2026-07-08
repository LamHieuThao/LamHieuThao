import re
from pathlib import Path

root = Path(r"g:\Tiến độ thực tập\Workshop_AWS-main")
content = root / "content"
static_images = root / "static" / "images"

pattern = re.compile(r"(?:/images/|/static/images/)([^)\s\"'?]+)")
used = set()

for p in content.rglob("*"):
    if p.suffix in {".md", ".html"}:
        text = p.read_text(encoding="utf-8", errors="ignore")
        for m in pattern.findall(text):
            used.add(m.split("?")[0].replace("\\", "/"))

all_files = []
for p in static_images.rglob("*"):
    if p.is_file():
        all_files.append(p.relative_to(static_images).as_posix())

workshop = sorted(f for f in all_files if f.startswith("5-Workshop"))
to_delete = sorted(f for f in all_files if f.startswith("5-Workshop") or f not in used)

out = root / "_image_audit.txt"
with open(out, "w", encoding="utf-8") as f:
    f.write(f"USED ({len(used)}):\n")
    for x in sorted(used):
        f.write(x + "\n")
    f.write(f"\nTO DELETE ({len(to_delete)}):\n")
    for x in to_delete:
        f.write(x + "\n")
    f.write(f"\nKEEP ({len(all_files) - len(to_delete)}):\n")
    for x in sorted(set(all_files) - set(to_delete)):
        f.write(x + "\n")

print("used", len(used))
print("all", len(all_files))
print("delete", len(to_delete))
print("keep", len(all_files) - len(to_delete))
