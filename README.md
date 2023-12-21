# Raspberry Pi Gesture-Controlled LED System

## Project Overview

This project is a gesture-controlled LED system that uses a Raspberry Pi, a WS2812B LED strip, and a camera to detect hand gestures and change the LED colors accordingly. The system is controlled via a mobile app that communicates with a Rust API running on the Raspberry Pi. The Rust API manages the gesture recognition python process and communicates with the LED controller (also written in python) to change the LED colors.

- **LED Controller (Python):** Controls the LED strip.
- **Gesture Recognition (Python + OpenCV):** Detects hand gestures and changes LED colors.
- **Rust API (Rust):** Manages gesture recognition via HTTP endpoints.
- **Mobile App (React Native + Expo):** Interface to control the system.

## Project Description

1. **LED Controller:**
   - *Requirements:* Python, WS2812B LED strip, Raspberry Pi.
   - *Usage:* `python led_controller.py`
  
2. **Gesture Recognition:**
   - *Requirements:* Python, OpenCV, camera.
   - *Usage:* `python gesture_recognition.py`

3. **Rust API:**
   - *Requirements:* Rust, Raspberry Pi.
   - *Build:* `cargo build --target your_target_directory`
   - *Run:* `./your_executable`
  
4. **Mobile App:**
   - *Requirements:* Node.js, npm, Expo CLI.
   - *Start:* `cd mobile-app && expo start`

## Features

- LED control based on hand gestures.
- Rust API for gesture recognition initiation and termination.
- Mobile app interface for user-friendly control.

## Hardware Requirements

- Raspberry Pi.
- WS2812B LED strip.
- Camera for gesture recognition.

## Software Requirements

- Python.
- Rust.
- Node.js.
- Expo CLI.
- OpenCV.


## Contributing

This is a solo project, and contributions are not currently accepted. However, you are welcome to fork the repository and use it as a starting point for your own gesture-controlled led projects.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

If you have any questions or inquiries, feel free to reach out to me at [nahjaybattieste@gmail.com](mailto:nahjaybattieste@gmail.com).
