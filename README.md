# 8mbcom
Little and simple Python script that executes FFmpeg command for compressing video to under 8MB

Usually needs FFmpeg for works. Built for break Discord non-Nitro user upload limit. (Sometimes can't)

## Usage
 - On Windows, just drag your file into `DRAG.bat`.
 - Or run this `python 8mb.py YOUR_VIDEO_NAME_OR_PATH_HOHO.mp4`

## Example Outputs
```
Compressing YOUR_VIDEO_NAME_OR_PATH_HOHO.mp4 . . . (9.8MB) | bitrate = 224k
(FFmpeg things ...)
Compressed YOUR_VIDEO_NAME_OR_PATH_HOHO.mp4 -> YOUR_VIDEO_NAME_OR_PATH_HOHO.mp4 ! (1.5MB, 0.15% of an original)
Compressed file size is less than 8MB.
```
