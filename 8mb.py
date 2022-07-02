import sys
import os
import subprocess

def size_format(n) :
    for u in ["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB"]:
        if abs(n) < 1024.0 :
            return f"{n:3.1f}{u}"
        n /= 1024.0
    return f"{n:.1f}YB"

target_8mb = 8192
file_path = sys.argv[1]
filename, ext = os.path.splitext(file_path)

duration = float(subprocess.check_output(
    [
        "ffprobe",
        "-v", "error",
        "-show_entries",
        "format=duration",
        "-of",
        "default=noprint_wrappers=1:nokey=1",
        file_path
    ]
).decode(sys.stdout.encoding))

realfilename = os.path.basename(file_path)
bitrate = target_8mb / duration
original_filestats = os.stat(file_path)
outputpath = filename + "_c" + ext
realoutputfilename = os.path.basename(outputpath)

print(
    f"Compressing {realfilename} . . .",
    f"({size_format(original_filestats.st_size)}) | bitrate = {int(bitrate)}k"
)

#####################

subprocess.call(
    [
        'ffmpeg',
        "-y",
        "-loglevel",
        "error",
        "-hide_banner",
        "-i",
        file_path,
        '-b', str(bitrate) + "k",
        outputpath
    ]
    ,shell=True
)

#####################

final_filestats = os.stat(outputpath)
percent = final_filestats.st_size / original_filestats.st_size
if percent < 1 :
    percent = f"\033[92m{percent:.2f}%\033[0m"
else :
    percent = f"\033[91m{percent:.2f}%\033[0m"

print(
    f"Compressed {realfilename} -> {realoutputfilename} !",
    f"({size_format(final_filestats.st_size)}, {percent} of an original)"
)

if final_filestats.st_size >= target_8mb * 1024 :
    print('\033[91mCompressed file size doesn\'t less than 8MB !\033[0m')
else :
    print('\033[92mCompressed file size is less than 8MB.\033[0m')

input()