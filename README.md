# ✨Image Processing - Karate Chop Kick

_This project is a simple image processing project that detects the movement of sticks in the Karate Chop Kick game._

<br>

# 🚀 Starting

_These instructions allow you to get a copy of the running project on your local machine._

## 📋 Pre-requisites
_You need to have a 3.X version of Python_

## 🔧 Installation

- Make a git clone or download it in zip
    ```bash
    git clone https://github.com/irania9O/image-processing-kaarate-chop-kick.git
    ```

- Get in the directory
    ```bash
    cd image-processing-kaarate-chop-kick
    ```

- Install from your terminal with pip requirements.txt:
    ```bash
    pip install -r requirements.txt
    ```

- Change **coordinates** at lines 21, 29, 31, 53 and 61 in `main.py` file to your coordinates:
    ```python
    # main.py
    ...
    21. x, y = (333,750) # coordinates of the first point
    29. image = np.array(ImageGrab.grab(bbox=(280,620,505,680))) # coordinates of the left side of the image
    31. image = np.array(ImageGrab.grab(bbox=(505,620,730,680))) # coordinates of the right side of the image
    53. x, y = (650,750) # coordinates of the right side of the image
    61. x, y = (333,750) # coordinates of the left side of the image
    ```

# 🧮 Run

```bash
python main.py
```
<br>

# 🖼️  Demo
<video src='./videos/demo.mp4'>

<!-- # 🖼️  Demo
<br>

![home](./videos/demo.mp4) -->
