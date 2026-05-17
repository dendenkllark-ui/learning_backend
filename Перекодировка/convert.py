import os
from moviepy import VideoFileClip

# Определяем папку скрипта
script_dir = os.path.dirname(os.path.abspath(__file__))

print("Ищем видеофайлы в папке скрипта...")
mp4_files = [f for f in os.listdir(script_dir) if f.endswith('.mp4') and f != "gojo_fixed.mp4"]

if not mp4_files:
    print(f"[ОШИБКА] В папке {script_dir} нет MP4 файлов!")
    exit()

input_file = os.path.join(script_dir, mp4_files[0])
output_file = os.path.join(script_dir, "gojo_fixed.mp4")

try:
    print(f"Найдено видео: {mp4_files[0]}")
    print("Загружаем...")
    clip = VideoFileClip(input_file)
    
    # В новых версиях moviepy высота берется из clip.size[1]
    video_height = clip.size[1]
    
    if video_height > 1080:
        print(f"Уменьшаем разрешение с {video_height}p до 1080p...")
        clip = clip.resized(height=1080)
        
    print("Начинаем жесткую перекодировку в чистый H.264 (yuv420p)...")
    clip.write_videofile(
        output_file, 
        codec="libx264", 
        audio_codec="aac",
        ffmpeg_params=["-pix_fmt", "yuv420p"]
    )
    
    print(f"\n[УСПЕХ] Готово! Новый файл лежит там же: gojo_fixed.mp4")

except Exception as e:
    print(f"\n[ОШИБКА] Что-то пошло не так: {e}")