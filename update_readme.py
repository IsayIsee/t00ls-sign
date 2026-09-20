import re
from datetime import date, datetime

README_PATH = "README.md"
PATTERN = re.compile(r"已稳定运行：(\d{4}-\d{2}-\d{2}) ~ \d{4}-\d{2}-\d{2}（\d+ *天）。")

def main():
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    match = PATTERN.search(content)
    if not match:
        print("未找到运行时间行,跳过更新")
        return

    start_str = match.group(1)
    start_date = datetime.strptime(start_str, "%Y-%m-%d").date()
    today = date.today()
    days = (today - start_date).days + 1

    new_line = f"已稳定运行：{start_str} ~ {today.isoformat()}（{days} 天）。"
    new_content = PATTERN.sub(new_line, content, count=1)

    if new_content != content:
        with open(README_PATH, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"README 已更新: {new_line}")
    else:
        print("内容无变化")

if __name__ == "__main__":
    main()
