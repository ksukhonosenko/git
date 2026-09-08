# Programmer's Day Video 🎉

## About Programmer's Day

**Programmer's Day** (День программиста) is celebrated on the **256th day of the year**:
- In regular years: **September 13th**
- In leap years: **September 12th**

The number **256** was chosen because it's 2^8, the number of distinct values that can be represented with an 8-bit byte, a number well known to programmers.

## Generated Video

**File:** `programmers_day_2026.mp4`
- **Duration:** 10 seconds
- **Resolution:** 1920x1080 (Full HD)
- **Frame Rate:** 30 FPS
- **Size:** ~0.21 MB

## Video Features

The video includes several festive programming-themed elements:

1. **Matrix-style Binary Rain** - Animated falling binary digits
2. **Animated Title** - "С ДНЁМ ПРОГРАММИСТА!" (Happy Programmer's Day!) with fade-in effect
3. **Celebratory Messages:**
   - "256-й день года" (256th day of the year)
   - "Keep coding!"
   - "Stay awesome!"
   - "Debug responsibly 🐛"
4. **Code Snippets:**
   - Git commit messages
   - Programming jokes and comments
5. **Animated Brackets** - Sliding curly braces `{ }`
6. **Particle Effects** - Colorful particles radiating outward
7. **Programming Color Scheme** - Terminal green, blue accents, dark background

## How to Regenerate

To create the video again or modify it:

```bash
# Install dependencies
pip3 install -r requirements.txt

# Run the generator
python3 create_programmers_day_video.py
```

## Files Included

- `create_programmers_day_video.py` - Python script to generate the video
- `requirements.txt` - Python dependencies
- `programmers_day_2026.mp4` - The generated video file
- `PROGRAMMERS_DAY_README.md` - This documentation

## Technical Details

The video is generated using:
- **Python 3** - Main programming language
- **Pillow (PIL)** - Image generation and manipulation
- **NumPy** - Mathematical calculations for animations
- **FFmpeg** - Video encoding from image frames

Each frame is individually rendered with calculated animations, then combined into a smooth MP4 video.

---

**🎊 Happy Programmer's Day! / С Днём Программиста! 🎊**

*Remember: There are only 10 types of people in the world - those who understand binary and those who don't!*
