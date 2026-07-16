from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

W, H = 1100, 620
img = Image.new("RGB", (W, H), "#0f172a")
d = ImageDraw.Draw(img)
try:
    font = ImageFont.truetype("malgun.ttf", 22)
    font_sm = ImageFont.truetype("malgun.ttf", 18)
    font_lg = ImageFont.truetype("malgun.ttf", 28)
except Exception:
    font = ImageFont.load_default()
    font_sm = font
    font_lg = font


def box(x, y, w, h, fill, outline, title, lines):
    d.rounded_rectangle([x, y, x + w, y + h], radius=16, fill=fill, outline=outline, width=3)
    d.text((x + 18, y + 16), title, fill="#f8fafc", font=font_lg)
    yy = y + 56
    for line in lines:
        d.text((x + 18, yy), line, fill="#e2e8f0", font=font_sm)
        yy += 28


box(
    60,
    120,
    320,
    200,
    "#14532d",
    "#4ade80",
    "Windows",
    ["연두 :8768", "win_yeondu_server.py", "agent.cmd -p --trust"],
)
box(
    720,
    120,
    320,
    200,
    "#1e3a5f",
    "#38bdf8",
    "Mac mini",
    ["연두 :8767", "yeondu_task_server.py", "agent -p --trust"],
)
box(
    340,
    400,
    420,
    140,
    "#3b0764",
    "#c084fc",
    "메아리 (Telegram)",
    ["요청 / 답변 요약만 표시", "초록·연두 접두어로 구분"],
)

d.line([(380, 200), (720, 200)], fill="#94a3b8", width=4)
d.polygon([(710, 190), (730, 200), (710, 210)], fill="#94a3b8")
d.polygon([(390, 190), (370, 200), (390, 210)], fill="#94a3b8")
d.text((470, 160), "POST /task  (LAN)", fill="#fbbf24", font=font)

d.line([(220, 320), (450, 400)], fill="#a78bfa", width=3)
d.line([(880, 320), (650, 400)], fill="#a78bfa", width=3)
d.text(
    (40, 40),
    "연두 채널 = Cursor Win↔Mac task (초록 Claude와 포트 분리)",
    fill="#f8fafc",
    font=font,
)

out1 = Path("assets/2026-07-17-윈도우-맥-연두-커서-채널/diagram.png")
out2 = Path("scratch/blog/assets/2026-07-17-윈도우-맥-연두-커서-채널/diagram.png")
out1.parent.mkdir(parents=True, exist_ok=True)
out2.parent.mkdir(parents=True, exist_ok=True)
img.save(out1)
img.save(out2)
print("saved", out1, out2)
