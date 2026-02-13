# Lemon 🍋
Lemon is a free, lightweight and fast python library to detect toxicity, insult, sexuality, threat, neutrality from text. It utilizes machine learning to do so.
# Installation
```py
pip install lemonify
```
**NOTE FOR WINDOWS USER:**
This library uses a small compiled extension on Windows (sdist install).
So you must install Microsoft Visual C++ Build Tools first.
1. Download and install:
    https://visualstudio.microsoft.com/visual-cpp-build-tools/
2. During setup, select:
   "Desktop development with C++"
3. Then run:
```py
python -m pip install --upgrade pip setuptools wheel
pip install lemonify
```
# Example usage
```py
from lemonify import lemon
print(lemon("you are stupid"))
```
# Response example
```py
{'toxicity': 1.0, 'insult': 1.0, 'sexuality': 0.0, 'threat': 0.0, 'neutrality': 0.0}
```
**Note that the value of emotions are in floating points between 0 and 1**
# Made with ♥️ by [Blaze](https://discord.com/users/1238444724386533417)
# Feel free to DM me on discord if there's any issues:>
# PyPi url
https://pypi.org/project/lemonify/
