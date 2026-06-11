# 🎵 MP3 Player

A simple command-line MP3 player built with Python and Pygame. Browse your local music library and control playback right from the terminal.

---

## Features

- Lists all `.mp3` files from a local music folder
- Play any song by entering its number
- Playback controls: Pause, Resume, and Stop
- Lightweight — no GUI required

---

## Requirements

- Python 3.x
- [Pygame](https://www.pygame.org/)

---

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Subhankar-parashar/mp3-player.git
   cd mp3-player
   ```

2. **Install dependencies**
   ```bash
   pip install pygame
   ```

3. **Add your music**

   Create a folder named `Music01` in the project directory and place your `.mp3` files inside it:
   ```
   mp3-player/
   ├── Music01/
   │   ├── Lush Life.mp3
   │   ├── On the Floor.mp3
   │   └── ...
   └── player.py
   ```

---

## Usage

Run the script:

```bash
python player.py
```

You'll see a numbered list of your songs:

```
**** MP3 Player ****
My song list
1. Lush Life.mp3
2. On the Floor.mp3

Enter the song to play (or Q to quit):
```

Enter a number to play a song. Once playing, use these commands:

| Command | Action  |
|---------|---------|
| `P`     | Pause   |
| `R`     | Resume  |
| `S`     | Stop    |

Enter `Q` at the song selection menu to exit.

---

## Project Structure

```
mp3-player/
├── Music01/        # Place your .mp3 files here
├── player.py       # Main script
└── README.md
```

---
