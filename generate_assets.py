from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import math

OUT = Path('/home/ubuntu/tanishk-readme-redesign/assets')
OUT.mkdir(parents=True, exist_ok=True)

FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
FONT_BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
MONO = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'
MONO_BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf'


def f(path, size):
    return ImageFont.truetype(path, size)


def gradient(w, h, a, b):
    im = Image.new('RGB', (w, h), a)
    px = im.load()
    for y in range(h):
        t = y / max(1, h - 1)
        for x in range(w):
            u = x / max(1, w - 1)
            q = (t * 0.55 + u * 0.45)
            px[x, y] = tuple(int(a[i] * (1 - q) + b[i] * q) for i in range(3))
    return im


def text(draw, xy, value, font, fill, anchor=None):
    draw.text(xy, value, font=font, fill=fill, anchor=anchor)


def rounded(draw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def header():
    w, h = 1400, 360
    im = gradient(w, h, (2, 6, 23), (8, 47, 73))
    d = ImageDraw.Draw(im, 'RGBA')
    for x in range(0, w, 32):
        d.line((x, 0, x, h), fill=(125, 211, 252, 18), width=1)
    for y in range(0, h, 32):
        d.line((0, y, w, y), fill=(125, 211, 252, 18), width=1)
    d.ellipse((990, -230, 1450, 230), fill=(14, 165, 233, 18), outline=(56, 189, 248, 38), width=2)
    d.arc((0, 150, 1500, 520), 180, 355, fill=(56, 189, 248, 65), width=2)
    d.arc((0, 165, 1500, 535), 180, 355, fill=(125, 211, 252, 30), width=1)
    rounded(d, (72, 72, 262, 262), 32, (15, 23, 42, 255), (56, 189, 248, 180), 2)
    d.polygon([(116, 112), (218, 112), (218, 140), (183, 140), (183, 226), (151, 226), (151, 140), (116, 140)], fill=(56, 189, 248, 255))
    d.ellipse((216, 211, 230, 225), fill=(125, 211, 252, 255))
    d.line((101, 239, 232, 239), fill=(56, 189, 248, 90), width=2)
    text(d, (318, 104), 'TANISHK GUPTA / PROFILE README', f(MONO_BOLD, 17), (125, 211, 252, 255))
    text(d, (318, 164), 'Build systems.', f(FONT_BOLD, 54), (248, 250, 252, 255))
    text(d, (318, 226), 'Solve problems.', f(FONT_BOLD, 54), (248, 250, 252, 255))
    d.rounded_rectangle((322, 304, 334, 316), radius=2, fill=(14, 165, 233, 255))
    text(d, (350, 302), 'CSE @ MNNIT ALLAHABAD  ·  FULL STACK  ·  DSA / CP', f(MONO, 16), (203, 213, 225, 255))
    text(d, (1090, 213), '$ tanishk --status', f(MONO, 14), (125, 211, 252, 255))
    text(d, (1090, 239), 'building: full-stack', f(MONO, 14), (203, 213, 225, 255))
    text(d, (1090, 265), 'learning: systems + AI', f(MONO, 14), (203, 213, 225, 255))
    text(d, (1090, 291), 'status: shipping', f(MONO, 14), (56, 189, 248, 255))
    im.save(OUT / 'profile-header.png', optimize=True)


def studenthub():
    w, h = 1200, 460
    im = gradient(w, h, (7, 17, 31), (12, 41, 65))
    d = ImageDraw.Draw(im, 'RGBA')
    d.ellipse((920, -180, 1360, 260), fill=(14, 165, 233, 22))
    text(d, (54, 44), '01 / STUDENTHUB', f(MONO_BOLD, 15), (125, 211, 252, 255))
    text(d, (54, 78), 'Find the right resource faster.', f(FONT_BOLD, 28), (248, 250, 252, 255))
    text(d, (54, 112), 'Academic notes, PDFs, and previous-year papers — organized by context.', f(FONT, 15), (148, 163, 184, 255))
    rounded(d, (54, 166, 1146, 404), 16, (15, 23, 42, 255), (56, 189, 248, 70), 2)
    rounded(d, (54, 166, 262, 404), 16, (11, 33, 53, 255))
    text(d, (82, 194), 'WORKSPACE', f(MONO_BOLD, 12), (203, 213, 225, 255))
    text(d, (82, 232), 'Semester 04', f(FONT_BOLD, 16), (248, 250, 252, 255))
    text(d, (82, 268), 'Data Structures', f(FONT, 14), (125, 211, 252, 255))
    text(d, (82, 298), 'Operating Systems', f(FONT, 14), (148, 163, 184, 255))
    text(d, (82, 328), 'Computer Networks', f(FONT, 14), (148, 163, 184, 255))
    d.rounded_rectangle((82, 364, 174, 368), radius=2, fill=(14, 165, 233, 255))
    text(d, (304, 194), 'RECENT RESOURCES', f(MONO_BOLD, 12), (203, 213, 225, 255))
    for x, title, meta, foot in [(304, 'DSA Notes', 'PDF · 2.4 MB', 'uploaded by you'), (566, 'OS Papers', 'PDF · 1.1 MB', 'exam archive')]:
        rounded(d, (x, 228, x + 238, 368), 12, (19, 40, 59, 255), (56, 189, 248, 42), 1)
        rounded(d, (x + 22, 252, x + 56, 294), 6, (14, 165, 233, 45), (56, 189, 248, 130), 1)
        d.line((x + 33, 262, x + 46, 262), fill=(125, 211, 252, 255), width=2)
        d.line((x + 33, 272, x + 46, 272), fill=(125, 211, 252, 255), width=2)
        d.line((x + 33, 282, x + 42, 282), fill=(125, 211, 252, 255), width=2)
        text(d, (x + 74, 253), title, f(FONT_BOLD, 14), (248, 250, 252, 255))
        text(d, (x + 74, 277), meta, f(FONT, 12), (148, 163, 184, 255))
        text(d, (x + 22, 329), foot, f(MONO, 11), (125, 211, 252, 255))
    rounded(d, (828, 228, 1116, 368), 12, (19, 40, 59, 255), (56, 189, 248, 42), 1)
    text(d, (854, 253), 'STACK', f(MONO_BOLD, 11), (203, 213, 225, 255))
    text(d, (854, 286), 'Node.js · Express', f(FONT, 15), (248, 250, 252, 255))
    text(d, (854, 312), 'MongoDB · Cloudinary', f(FONT, 15), (248, 250, 252, 255))
    text(d, (854, 338), 'auth · ownership · validation', f(FONT, 13), (125, 211, 252, 255))
    im.save(OUT / 'studenthub.png', optimize=True)


def readmeforge():
    w, h = 1200, 460
    im = gradient(w, h, (11, 16, 32), (27, 23, 64))
    d = ImageDraw.Draw(im, 'RGBA')
    d.ellipse((920, -180, 1360, 260), fill=(167, 139, 250, 20))
    text(d, (54, 44), '02 / READMEFORGE', f(MONO_BOLD, 15), (196, 181, 253, 255))
    text(d, (54, 78), 'Documentation, with a live feedback loop.', f(FONT_BOLD, 28), (248, 250, 252, 255))
    text(d, (54, 112), 'Generate, preview, and copy a README without leaving the browser.', f(FONT, 15), (165, 180, 252, 255))
    rounded(d, (54, 166, 1146, 404), 16, (17, 24, 39, 255), (167, 139, 250, 70), 2)
    rounded(d, (54, 166, 532, 404), 16, (15, 23, 42, 255))
    text(d, (82, 194), 'INPUT / PROJECT MODE', f(MONO_BOLD, 11), (196, 181, 253, 255))
    rounded(d, (82, 224, 482, 258), 7, (24, 35, 56, 255), (56, 189, 248, 100), 1)
    text(d, (98, 234), 'owner / repository', f(MONO, 12), (203, 213, 225, 255))
    rounded(d, (82, 272, 274, 354), 9, (24, 35, 56, 255))
    text(d, (98, 292), 'PROJECT NAME', f(MONO, 10), (100, 116, 139, 255))
    text(d, (98, 317), 'ReadmeForge', f(FONT_BOLD, 15), (248, 250, 252, 255))
    rounded(d, (290, 272, 482, 354), 9, (24, 35, 56, 255))
    text(d, (306, 292), 'OUTPUT', f(MONO, 10), (100, 116, 139, 255))
    text(d, (306, 317), 'profile.md', f(FONT_BOLD, 15), (125, 211, 252, 255))
    d.rectangle((532, 166, 1146, 204), fill=(226, 232, 240, 255))
    d.ellipse((553, 180, 563, 190), fill=(167, 139, 250, 255))
    text(d, (578, 176), 'LIVE MARKDOWN PREVIEW', f(MONO, 11), (71, 85, 105, 255))
    d.rectangle((532, 204, 1146, 404), fill=(248, 250, 252, 255))
    text(d, (570, 226), 'ReadmeForge', f(FONT_BOLD, 20), (15, 23, 42, 255))
    d.rounded_rectangle((570, 256, 930, 266), radius=5, fill=(203, 213, 225, 255))
    d.rounded_rectangle((570, 278, 1042, 285), radius=3, fill=(226, 232, 240, 255))
    d.rounded_rectangle((570, 293, 988, 300), radius=3, fill=(226, 232, 240, 255))
    d.rounded_rectangle((570, 324, 688, 352), radius=7, fill=(56, 189, 248, 255))
    text(d, (593, 331), 'COPY MARKDOWN', f(MONO_BOLD, 10), (255, 255, 255, 255))
    im.save(OUT / 'readmeforge.png', optimize=True)


def portfolio():
    w, h = 1200, 460
    im = gradient(w, h, (5, 11, 23), (16, 36, 58))
    d = ImageDraw.Draw(im, 'RGBA')
    d.polygon([(720, 0), (1200, 0), (1200, 460), (720, 460), (860, 350), (900, 255), (850, 130)], fill=(14, 165, 233, 18))
    text(d, (54, 44), '03 / ADVANCED PORTFOLIO', f(MONO_BOLD, 15), (125, 211, 252, 255))
    text(d, (54, 82), 'Interfaces with a point of view.', f(FONT_BOLD, 36), (248, 250, 252, 255))
    text(d, (54, 126), 'Scroll-triggered movement, magnetic interactions, and resilient fallbacks.', f(FONT, 15), (148, 163, 184, 255))
    rounded(d, (54, 188, 1146, 390), 16, (11, 21, 36, 255), (56, 189, 248, 70), 2)
    rounded(d, (84, 218, 708, 358), 12, (15, 29, 48, 255))
    text(d, (116, 246), 'SELECTED WORK / 01', f(MONO_BOLD, 11), (100, 116, 139, 255))
    text(d, (116, 275), 'Digital experiences', f(FONT_BOLD, 30), (248, 250, 252, 255))
    d.rounded_rectangle((116, 320, 346, 328), radius=4, fill=(56, 189, 248, 255))
    d.rounded_rectangle((116, 340, 496, 346), radius=3, fill=(51, 65, 85, 255))
    d.rounded_rectangle((116, 352, 414, 358), radius=3, fill=(30, 58, 82, 255))
    rounded(d, (744, 218, 1116, 358), 12, (15, 29, 48, 255))
    text(d, (774, 246), 'MOTION SYSTEM', f(MONO_BOLD, 11), (125, 211, 252, 255))
    d.ellipse((780, 282, 808, 310), fill=(14, 165, 233, 55), outline=(56, 189, 248, 255), width=1)
    d.line((794, 282, 794, 310), fill=(125, 211, 252, 255), width=2)
    d.line((780, 296, 808, 296), fill=(125, 211, 252, 255), width=2)
    d.line((832, 296, 1048, 296), fill=(51, 65, 85, 255), width=2)
    d.ellipse((914, 290, 926, 302), fill=(125, 211, 252, 255))
    d.ellipse((1042, 290, 1054, 302), fill=(14, 165, 233, 255))
    text(d, (774, 326), 'GSAP · ScrollTrigger · fallback-first', f(FONT, 13), (203, 213, 225, 255))
    im.save(OUT / 'portfolio.png', optimize=True)


def portfolio_v1():
    w, h = 1200, 460
    im = gradient(w, h, (248, 250, 252), (224, 242, 254))
    d = ImageDraw.Draw(im, 'RGBA')
    text(d, (54, 44), '04 / PERSONAL PORTFOLIO', f(MONO_BOLD, 15), (3, 105, 161, 255))
    text(d, (54, 82), 'A clear home for the essentials.', f(FONT_BOLD, 30), (15, 23, 42, 255))
    text(d, (54, 118), 'Responsive structure first: profile, skills, work, and contact.', f(FONT, 15), (71, 85, 105, 255))
    rounded(d, (54, 174, 1146, 390), 16, (255, 255, 255, 255))
    rounded(d, (54, 174, 1146, 218), 16, (15, 46, 74, 255))
    d.ellipse((78, 190, 90, 202), fill=(56, 189, 248, 255))
    text(d, (106, 184), 'TANISHK GUPTA / PORTFOLIO', f(MONO, 12), (224, 242, 254, 255))
    text(d, (86, 245), 'Computer Science Student', f(FONT_BOLD, 23), (15, 23, 42, 255))
    text(d, (86, 276), 'MNNIT Allahabad · DSA · Web Development · ML', f(FONT, 14), (71, 85, 105, 255))
    d.rounded_rectangle((86, 318, 208, 348), radius=15, fill=(14, 165, 233, 255))
    text(d, (113, 325), 'VIEW MY WORK', f(MONO_BOLD, 10), (255, 255, 255, 255))
    rounded(d, (584, 248, 814, 352), 12, (241, 245, 249, 255))
    text(d, (610, 270), 'SKILLS', f(MONO_BOLD, 11), (3, 105, 161, 255))
    text(d, (610, 300), 'C++ · Python · JavaScript', f(FONT, 14), (15, 23, 42, 255))
    text(d, (610, 324), 'HTML · CSS · Git', f(FONT, 14), (15, 23, 42, 255))
    rounded(d, (840, 248, 1098, 352), 12, (241, 245, 249, 255))
    text(d, (866, 270), 'CONTACT', f(MONO_BOLD, 11), (3, 105, 161, 255))
    text(d, (866, 300), 'GitHub · LinkedIn', f(FONT, 14), (15, 23, 42, 255))
    text(d, (866, 324), 'Email · Coding profiles', f(FONT, 14), (15, 23, 42, 255))
    im.save(OUT / 'portfolio-v1.png', optimize=True)


if __name__ == '__main__':
    header()
    studenthub()
    readmeforge()
    portfolio()
    portfolio_v1()
