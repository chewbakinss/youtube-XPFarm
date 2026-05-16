# youtube-XPFarm
Youtube live chat xp farming !!(not viable on streams with superchat)!!

---
### I'm too lazy to keep #1 on youtube streams XP system most of the time, so here's my bot to help your ego thrive and not move a finger🫩

It took me a few streams to **"crack"** the secret formula of youtube XP system, and still there are questions about the algorithm. In a nutshell:
- Youtube gives out **75xp** every hour starting from your first message in chat.
- It is distributed equally between first **3 messages** in said hour.
- Every message after depletion of **hourly XP** is not awarded.
- Xp that haven't been "activated" are **wasted** and your **cap resets to 75** after said hour.

#### There is some counter-intuitive decision work being done in case multiple users end up with the same amount of XP.

_You would think that the **most logical way of deciding who's higher on leaderboards** should be the one who got to said xp first, or at least in alphabetical order so it's logical..._

**But no, here's a screenshot from a test(the #3 got to 150xp first and is higher alphabetically)**
<img width="435" height="299" alt="image" src="https://github.com/user-attachments/assets/519a264b-46ba-43e7-89ae-f07fd63cece0" />

### So, at the end of the day, it's not a complex bot in any way, you just need to hop on stream early and start farming.

The bot starts sending messages every hour in bunches of 3 taking slowmode settins in account.

_CMD based customisable automation is to be added(sry, I'm a noob)_

---
## Later this'll be automated, but for now you need to kickstart the process because of the chrome anti-automation security.

### 1 - Open chrome through cmd with:
```bash
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9223 --user-data-dir="C:\Users\YOUR_USER\AppData\Local\Google\Chrome\User Data Bot"
```

You should get into your chrome profile, but if not(and I kinda expect it not to) - go on youtube.com and log in
<img width="1110" height="610" alt="GitTut1" src="https://github.com/user-attachments/assets/19e7c246-5311-496d-934d-da247f98eeef" />

### **!IMPORTANT! Do not close this window, you should run the code with said window being open**

---
### 2 - Paste the main.py code in vscode, run "pip install playwright" and "install playwright" in venv terminal.
Then you should go to the stream you want to farm xp on and copy the chat popout link
<img width="418" height="502" alt="GitTut3" src="https://github.com/user-attachments/assets/7ac2a990-3dad-489b-9ffe-60dadc9d4405" />

---
### 3 - You're all set, run the program(the output will be "Messaxe {x}", which will just print out their order, customize it if needed)
<img width="800" height="450" alt="0516-ezgif com-video-to-gif-converter" src="https://github.com/user-attachments/assets/f25d353c-1165-4ffa-830b-c88fd244e416" />

---
_that's my first git... kinda nervous👉👈_
