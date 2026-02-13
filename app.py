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
    """
    Process the student's answer:
    - Compare to correct answer (case-insensitive, stripped)
    - Update score and progress if correct
    - Display appropriate feedback
    """
    frame_idx = session.get("current_frame", 0)
    frame = FRAMES[frame_idx]
    
    # Get and normalize the user's answer
    user_answer = request.form.get("answer", "").strip() # multiple answers accounts for lowercase/uppercase already
    
    # Get and normalize the correct answer
    if "answers" in frame:
        correct_answer = frame["answer"]
        correct_answer_display = correct_answers[0]
    else:
        correct_answers = [frame["answer"]]
        correct_answer_display = frame["answer"]
    
    is_correct = user_answer in correct_answers
    
    # Check if correct
    is_correct = (user_answer == correct_answer)
    
    if is_correct:
        # Update score and advance to next frame
        session["score"] = session.get("score", 0) + 1
        session["current_frame"] = frame_idx + 1
    
    # Get feedback message (with fallback defaults)
    if is_correct:
        feedback = frame.get("feedback_correct", "Correct! Well done.")
    else:
        feedback = frame.get("feedback_incorrect", "Not quite. Try again!")
    
    return render_template(
        "feedback.html",
        is_correct=is_correct,
        feedback=feedback,
        frame=frame,
        correct_answer=correct_answer_display
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
    app.run(debug=True)