[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/BhpP2ldf)
# Skinner Teaching Machine - Starter Code

COMP 395: AI and Learning Technologies

## Overview

This Flask application implements a teaching machine based on B.F. Skinner's programmed instruction principles (1958):

1. **Small steps** - Content broken into small "frames"
2. **Active responding** - Learner must produce an answer
3. **Immediate feedback** - Instant confirmation of correctness
4. **Self-pacing** - Learner controls the speed
5. **Low error rate** - Frames designed for high success

## Setup Instructions

### 1. Create and activate a conda environment

```bash
conda create -n flask-env python=3.11
conda activate flask-env
```

### 2. Install dependencies

```bash
pip install flask
```

Or use the requirements file:

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
python app.py
```

### 4. Open in browser

Navigate to: http://127.0.0.1:5000/

### 5. Stop the server

Press `Ctrl+C` in the terminal.

## Your Task

1. **Edit `frames.py`** - Replace the example frames with your own topic
   - Minimum 5 frames
   - Follow Skinner's principles
   - Be consistent with your frame structure

2. **Test thoroughly** - Make sure all frames work correctly

3. **Optional extensions** - See ideas in the code comments

## File Structure

```
skinner_starter/
├── app.py              # Main Flask application
├── frames.py           # Your frame definitions (EDIT THIS!)
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── templates/
    ├── base.html      # Shared layout and styles
    ├── index.html     # Welcome page
    ├── frame.html     # Frame display
    ├── feedback.html  # Answer feedback
    └── complete.html  # Final results
```

## Extension Ideas

- **Hints system** - Add hints to frames and a "Show Hint" button
- **Multiple answers** - Accept multiple correct answers per frame
- **Retry on incorrect** - Don't advance until correct (Skinner's original design)
- **Branching** - Add remedial frames for incorrect answers
- **Timing** - Track how long each frame takes
- **Persistence** - Save results to a JSON file or database

## Theory Connection

This implementation demonstrates **behaviorist** learning theory:
- Learning as behavior change through reinforcement
- Immediate feedback strengthens correct responses
- Small steps minimize errors (negative experiences)

Consider: How does this differ from **constructivist** approaches (Piaget, Papert)?

## Troubleshooting

**"Address already in use"**
- Another process is using port 5000
- Either stop that process or change the port: `app.run(port=5001)`

**"ModuleNotFoundError: No module named 'flask'"**
- Make sure your conda environment is activated
- Run `pip install flask`

**Changes not appearing**
- Flask's debug mode should auto-reload
- Try stopping and restarting the server
