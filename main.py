# WIP Testing V0.1
# Written by imgpslol

#!/usr/bin/env python3


# Simple CLI tool to download YouTube videos or audio using yt-dlp.
# Usage:
#   vgrab.py <url> -A   # Download audio
#   vgrab.py <url> -V   # Download video
#
# Dependencies:
#   - yt-dlp (install with: pip install yt-dlp)

import argparse
import subprocess

def download(url, mode):
    # Downloads the video or audio from the given URL using yt-dlp.
    command = ["yt-dlp"]
    
    if mode == "audio":
        # Extract audio and save as MP3
        command += ["-x", "--audio-format", "mp3"]
    elif mode == "video":
        # Download the best available video format
        command += ["-f", "best"]
    
    command.append(url)
    subprocess.run(command)

def main():
    # Parses command-line arguments and starts the download.
    parser = argparse.ArgumentParser(description="YouTube Video/Audio Downloader")
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument("-A", "--audio", action="store_true", help="Download as audio")
    parser.add_argument("-V", "--video", action="store_true", help="Download as video")
    
    args = parser.parse_args()
    
    if args.audio:
        download(args.url, "audio")
    elif args.video:
        download(args.url, "video")
    else:
        print("Please specify either -A (audio) or -V (video)")

if __name__ == "__main__":
    main()
