
# 🏓 Table Tennis Serve analyser (AI-Powered MVP)

A personal project to build an AI-powered tool that detects, analyzes, and classifies table tennis serves using computer vision. This is an MVP (Minimum Viable Product) built in spare time with minimal resources — ideal for enthusiasts, engineers, and sports tech learners.

---

## 🔍 Project Goals

- 🎯 Detect table tennis serve moments from video footage
- 🧠 Build a lightweight ML model to classify serve types (in future phases)
- 🎥 Use computer vision to locate and track the ball during serve motions
- 🧪 Collect data and iterate toward a smarter feedback tool

---

## ✅ MVP Scope

> Focused on **ball motion detection** — no AI model required initially.

- [x] Video input (match or training clip)
- [x] Detect small, fast-moving ball using motion + colour filters
- [x] Visualise and highlight potential serve moments
- [ ] Export data or highlight timestamps for serve events
- [ ] (Future) Classify types of serves with trained ML model

---

## 📁 Folder Structure

```
serve-analyser/
│
├── videos/               # Raw table tennis footage
├── outputs/              # Processed video clips
├── scripts/
│   └── ball_tracker.py   # Motion detection and ball highlighting
├── notebooks/            # (Later) Data exploration & model training
├── README.md             # This file
└── requirements.txt      # Dependencies
```

---

## ▶️ Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/your-username/serve-analyser.git
cd serve-analyser
```

### 2. Set up environment

```bash
pip install -r requirements.txt
```

### 3. Run the tracker

```bash
python scripts/ball_tracker.py
```

Make sure you have a video file in `videos/` and update the path in the script if needed.

---

## 🛠️ Tech Stack

- `Python 3.10+`
- `OpenCV`
- (Planned) `PyTorch` / `TensorFlow`
- `Streamlit` (for UI in future MVP phase)

---

## 🔮 Future Plans

- Train an AI model to classify serve types (e.g. backspin, sidespin)
- Add UI for users to upload videos and get feedback
- Use pose estimation (like MediaPipe or OpenPose)
- Build a web-based front-end for coaches and players

---

## 🤝 Contributing or Discussing

This is a passion project. If you have experience with:
- Computer vision
- Table tennis coaching
- Model deployment
Feel free to open an issue, suggest an idea, or reach out.

---

## 📬 Contact

If you're interested in collaborating or providing feedback, please reach out via GitHub or email.

---

**Note:** This project is for research, learning, and fun — it is not a commercial product.
