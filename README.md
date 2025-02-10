# HyperLink

## Overview
HyperLink is a Python-based tool designed to enhance video playback on Windows systems by optimizing frame rates and resolution settings. This program leverages OpenCV to process video files, adjusting them to match the screen resolution and enhancing them to a smoother frame rate, especially beneficial for high-definition displays.

## Features
- Automatically detects your screen resolution.
- Optimizes video resolution and frame rate for enhanced playback.
- Outputs enhanced video files and plays them on your default media player.

## Requirements
- Python 3.6 or above
- OpenCV
- NumPy

## Installation
Before running HyperLink, ensure you have the required Python packages installed. You can install them using `pip`:

```bash
pip install opencv-python numpy
```

## Usage
1. Update the `video_file` variable in `hyperlink.py` with the path to your video file.
2. Run the script:

```bash
python hyperlink.py
```

3. The enhanced video will be saved as `enhanced_video.mp4` and will automatically start playing.

## Notes
- The program is currently designed for Windows-based systems due to the use of `ctypes` for screen resolution detection.
- Ensure that the input video file is accessible and in a format supported by OpenCV.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.