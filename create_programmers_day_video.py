#!/usr/bin/env python3
"""
Programmer's Day Video Generator
Creates a short celebratory video for Programmer's Day (256th day of the year)
"""

import numpy as np
from PIL import Image, ImageDraw, ImageFont
import subprocess
import os

# Video settings
WIDTH = 1920
HEIGHT = 1080
FPS = 30
DURATION = 10  # seconds
TOTAL_FRAMES = FPS * DURATION

# Colors
BG_COLOR = (15, 23, 42)  # Dark blue
CODE_GREEN = (34, 197, 94)
ACCENT_BLUE = (59, 130, 246)
YELLOW = (250, 204, 21)
WHITE = (255, 255, 255)

def create_frame(frame_num):
    """Create a single frame of the video"""
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    progress = frame_num / TOTAL_FRAMES
    
    # Title animation (fade in and stay)
    if progress < 0.3:
        alpha = min(1.0, progress / 0.2)
    else:
        alpha = 1.0
    
    # Draw binary rain effect (Matrix-style)
    if progress > 0.1:
        for i in range(50):
            x = (i * 40 + frame_num * 5) % WIDTH
            y = ((frame_num * (3 + i % 5)) % (HEIGHT + 200)) - 200
            binary = str(frame_num % 2)
            color = tuple(int(c * 0.3) for c in CODE_GREEN)
            try:
                draw.text((x, y), binary, fill=color, font=None)
            except:
                pass
    
    # Main title
    if progress < 0.8:
        title_y = HEIGHT // 3
        
        # Draw "C ДНЁМ" (Happy)
        title1 = "С ДНЁМ"
        title_color = tuple(int(c * alpha) for c in YELLOW)
        draw.text((WIDTH // 2 - 200, title_y - 80), title1, fill=title_color, font=None)
        
        # Draw "ПРОГРАММИСТА!" (Programmer's Day!)
        title2 = "ПРОГРАММИСТА!"
        title_color = tuple(int(c * alpha) for c in CODE_GREEN)
        draw.text((WIDTH // 2 - 300, title_y), title2, fill=title_color, font=None)
        
        # Draw "256th day of the year"
        subtitle = "256-й день года"
        sub_color = tuple(int(c * alpha) for c in ACCENT_BLUE)
        draw.text((WIDTH // 2 - 180, title_y + 100), subtitle, fill=sub_color, font=None)
    
    # Animated code brackets
    if 0.3 < progress < 0.8:
        bracket_alpha = min(1.0, (progress - 0.3) / 0.1)
        bracket_offset = int(50 * (1 - bracket_alpha))
        
        left_bracket = "{"
        right_bracket = "}"
        bracket_color = tuple(int(c * bracket_alpha) for c in ACCENT_BLUE)
        
        draw.text((WIDTH // 2 - 400 - bracket_offset, HEIGHT // 2 - 50), 
                 left_bracket, fill=bracket_color, font=None)
        draw.text((WIDTH // 2 + 400 + bracket_offset, HEIGHT // 2 - 50), 
                 right_bracket, fill=bracket_color, font=None)
    
    # Git commit style message
    if progress > 0.5:
        commit_alpha = min(1.0, (progress - 0.5) / 0.2)
        commit_y = HEIGHT - 200
        
        commits = [
            "git commit -m 'Happy Programmer's Day!'",
            "// TODO: Celebrate with coffee ☕",
            "while(true) { code(); }",
        ]
        
        for i, commit in enumerate(commits):
            commit_color = tuple(int(c * commit_alpha) for c in CODE_GREEN)
            draw.text((100, commit_y + i * 40), commit, fill=commit_color, font=None)
    
    # Final message
    if progress > 0.8:
        final_alpha = min(1.0, (progress - 0.8) / 0.15)
        
        messages = [
            "Keep coding!",
            "Stay awesome!",
            "Debug responsibly 🐛",
        ]
        
        final_y = HEIGHT // 2 - 50
        for i, msg in enumerate(messages):
            msg_color = tuple(int(c * final_alpha) for c in WHITE)
            draw.text((WIDTH // 2 - 150, final_y + i * 50), msg, fill=msg_color, font=None)
    
    # Particle effects
    if progress > 0.6:
        for i in range(30):
            particle_progress = (progress - 0.6) / 0.4
            angle = (i * 12 + frame_num * 2) * np.pi / 180
            radius = 300 * particle_progress
            px = int(WIDTH // 2 + radius * np.cos(angle))
            py = int(HEIGHT // 2 + radius * np.sin(angle))
            
            if 0 <= px < WIDTH and 0 <= py < HEIGHT:
                particle_color = [CODE_GREEN, ACCENT_BLUE, YELLOW][i % 3]
                draw.ellipse([px-3, py-3, px+3, py+3], fill=particle_color)
    
    return img

def create_video():
    """Generate the complete video"""
    print("🎬 Creating Programmer's Day video...")
    
    # Create temp directory for frames
    os.makedirs('temp_frames', exist_ok=True)
    
    # Generate all frames
    print(f"📹 Generating {TOTAL_FRAMES} frames...")
    for i in range(TOTAL_FRAMES):
        if i % 30 == 0:
            print(f"  Frame {i}/{TOTAL_FRAMES}")
        
        frame = create_frame(i)
        frame.save(f'temp_frames/frame_{i:04d}.png')
    
    print("✅ All frames generated!")
    
    # Combine frames into video using ffmpeg
    print("🎞️  Encoding video with ffmpeg...")
    
    # Check if ffmpeg is available
    try:
        subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("⚠️  ffmpeg not found, installing...")
        subprocess.run(['apt-get', 'update', '-qq'], check=False)
        subprocess.run(['apt-get', 'install', '-y', '-qq', 'ffmpeg'], check=False)
    
    # Create video
    output_file = 'programmers_day_2026.mp4'
    cmd = [
        'ffmpeg', '-y',
        '-framerate', str(FPS),
        '-i', 'temp_frames/frame_%04d.png',
        '-c:v', 'libx264',
        '-preset', 'medium',
        '-crf', '23',
        '-pix_fmt', 'yuv420p',
        output_file
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"✨ Video created successfully: {output_file}")
        
        # Clean up temp frames
        print("🧹 Cleaning up temporary files...")
        for i in range(TOTAL_FRAMES):
            os.remove(f'temp_frames/frame_{i:04d}.png')
        os.rmdir('temp_frames')
        
        # Get file size
        size_mb = os.path.getsize(output_file) / (1024 * 1024)
        print(f"📊 File size: {size_mb:.2f} MB")
        print(f"⏱️  Duration: {DURATION} seconds @ {FPS} FPS")
    else:
        print(f"❌ Error creating video: {result.stderr}")
        return False
    
    return True

if __name__ == '__main__':
    print("=" * 60)
    print("  PROGRAMMER'S DAY VIDEO GENERATOR")
    print("  256th day of the year - September 13th")
    print("=" * 60)
    print()
    
    success = create_video()
    
    if success:
        print()
        print("🎉 Happy Programmer's Day! 🎉")
        print("🎊 С Днём Программиста! 🎊")
