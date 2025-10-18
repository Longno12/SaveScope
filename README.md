# SaveScope

SaveScope is a simple Python tool for looking inside `.sav` game files to see what’s actually stored in them.  
It pulls out readable text, shows nearby byte data, and can guess possible numbers like integers or floats that might be linked to that text.

---

### Features
- Reads and analyzes any `.sav` file
- Extracts readable ASCII strings and nearby bytes
- Tries to detect integers and floats close to text data
- Saves everything into `game_analysis.txt`
- Works with just Python 3 — no extra installs needed

---

### How to Use
1. Download or clone this repo:
   ```bash
   git clone https://github.com/Longno12/SaveScope.git
   cd SaveScope
   ```
2. Make sure Python 3.8 or newer is installed.
3. Put your `.sav` file in the same folder as `Sav Decrypter.py`.
4. Run:
   ```bash
   python Sav Decrypter.py
   ```
5. Once it’s done, check the file called `game_analysis.txt` for the output.

---

### Example Output
```
Offset 0x00120A:
  String: hat_hat
  Before Bytes: 00 00 01 00 00
  After Bytes : 00 00 01 00 00 7f 3f 00 00
  Guess: int=1, float=1.000
------------------------------------------------------------
```

---

### Notes
This was made to inspect **Charlie Murder** save files, but it can work with pretty much any game that stores binary `.sav` data.  
It’s mainly meant for personal learning, testing, or curiosity — not for modifying or cheating in games.

---

### License
MIT License  

Copyright (c) 2025 Joe  

Permission is hereby granted, free of charge, to any person obtaining a copy  
of this software and associated documentation files (the "Software"), to deal  
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
copies of the Software, and to permit persons to whom the Software is  
furnished to do so, subject to the following conditions:  

The above copyright notice and this permission notice shall be included in  
all copies or substantial portions of the Software.  

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN  
THE SOFTWARE.
