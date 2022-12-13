SHUT UP genshin
===

![emergency_food](img/1743d764b8439f6f2a941ce34d8be254.jpg)

A simple script to skip annoying dialogues in Genshin Impact. Press hotkey and it works.
[stfugen.webm](https://user-images.githubusercontent.com/59962728/207316128-b0fdd3f2-ccc1-42aa-afc0-e067d3dd89ae.webm)

---

Installation
---

```shell
(venv) Admin@DESKTOP S:\...\shutupgenshin > pip install -r requirements.txt
```

Launch
---

Launch the console with administrator rights, cd in script directory and just launch.

```shell
(venv) Admin@DESKTOP S:\...\shutupgenshin > python shutupgenshin.py

[INIT] STFUgenshin started.
[INFO] Dont forget to configure resolution in settings.json.
```

Configuration
---

There are several options to customize, such as panel coordinates for auto-reply and start/pause button selection.

```json
{
    "x_coordinates": 1632,
    "y_coordinates": 800,
    "start_pause_key": "f12",
    "press_timer": 0.01
}
```
