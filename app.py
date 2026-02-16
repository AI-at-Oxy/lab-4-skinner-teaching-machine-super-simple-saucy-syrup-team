"""
Skinner Teaching Machine - Flask Application
COMP 395: AI and Learning Technologies

This Flask app implements a simple teaching machine based on 
B.F. Skinner's programmed instruction principles:
1. Small steps (frames)
2. Active responding
3. Immediate feedback
4. Self-pacing
5. Low error rate

YOUR TASK: 
- Design your own frames in frames.py
- Optionally extend this app with hints, branching, etc.
"""

from flask import Flask, render_template, request, session, redirect, url_for
from frames import FRAMES

app = Flask(__name__)
app.secret_key = "change-this-to-a-secret-key"  # Change this in production!


@app.route("/")
def index():
    """
    Welcome page - resets progress and displays instructions.
    """
    # Initialize/reset session variables
    session["current_frame"] = 0
    session["score"] = 0
    session["attempts"] = 0
    
    return render_template("index.html", total_frames=len(FRAMES))


@app.route("/frame")
def show_frame():
    """
    Display the current frame to the student.
    If all frames are complete, redirect to completion page.
    """
    frame_idx = session.get("current_frame", 0)
    
    # Check if we've completed all frames
    if frame_idx >= len(FRAMES):
        return redirect(url_for("complete"))
    
    frame = FRAMES[frame_idx]
    
    return render_template(
        "frame.html",
        frame=frame,
        frame_num=frame_idx + 1,
        total=len(FRAMES)
    )

@app.route("/submit", methods=["POST"])
def submit_answer():
    frame_idx = session.get("current_frame", 0)
    frame = FRAMES[frame_idx]

    user_answer = request.form.get("answer", "").strip().lower()
    correct_answers = [a.lower() for a in frame["answer"]]

    # Track attempts
    attempts = session.get("attempts", 0)

    is_correct = user_answer in correct_answers

    if is_correct:
        session["score"] = session.get("score", 0) + 1
        session["current_frame"] = frame_idx + 1
        session["attempts"] = 0  # reset attempts
        feedback = frame.get("feedback_correct", "Correct!")
    else:
        attempts += 1
        session["attempts"] = attempts
        feedback = frame.get("feedback_incorrect", "Not quite.")

    return render_template(
        "attempts.html",
        is_correct=is_correct,
        feedback=feedback,
        frame=frame,
        attempts=attempts
    )

@app.route("/complete")
def complete():
    """
    Display final results after all frames are completed.
    """
    score = session.get("score", 0)
    total = len(FRAMES)
    percentage = round((score / total) * 100) if total > 0 else 0
    
    return render_template(
        "complete.html",
        score=score,
        total=total,
        percentage=percentage
    )


# =============================================================================
# EXTENSION IDEAS (uncomment and modify as needed)
# =============================================================================

# @app.route("/hint")
# def show_hint():
#     """Show a hint for the current frame (if available)."""
#     frame_idx = session.get("current_frame", 0)
#     frame = FRAMES[frame_idx]
#     hint = frame.get("hint", "No hint available for this frame.")
#     return render_template("hint.html", hint=hint, frame=frame)


# @app.route("/reset")
# def reset():
#     """Reset progress and start over."""
#     session.clear()
#     return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True, port=5050)
