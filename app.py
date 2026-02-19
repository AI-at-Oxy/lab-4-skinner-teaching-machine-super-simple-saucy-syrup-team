import time  # <--- Added for timing feature
from flask import Flask, render_template, request, session, redirect, url_for
from frames import FRAMES

app = Flask(__name__)
app.secret_key = "change-this-to-a-secret-key" 

@app.route("/")
def index():
    """
    Welcome page - resets progress and displays instructions.
    """
    session["current_frame"] = 0
    session["score"] = 0
    session["attempts"] = {}
    session["timing_data"] = {}  # <--- Initialize timing storage
    
    return render_template("index.html", total_frames=len(FRAMES))


@app.route("/frame")
def show_frame():
    """
    Display the current frame and start the timer.
    """
    frame_idx = session.get("current_frame", 0)
    
    if frame_idx >= len(FRAMES):
        return redirect(url_for("complete"))
    
    # --- TIMING LOGIC START ---
    # Record the exact time the user was shown this frame
    session["start_time"] = time.time() 
    # --------------------------

    frame = FRAMES[frame_idx]
    
    if "attempts" not in session:
        session["attempts"] = {}
    
    frame_key = str(frame_idx)
    if frame_key not in session["attempts"]:
        session["attempts"][frame_key] = 0
    
    current_attempts = session["attempts"][frame_key]
    attempts_remaining = max(0, 3 - current_attempts)
    
    return render_template(
        "frame.html",
        frame=frame,
        frame_num=frame_idx + 1,
        total=len(FRAMES),
        current_attempts=current_attempts,
        attempts_remaining=attempts_remaining
    )


@app.route("/submit", methods=["POST"])
def submit_answer():
    """
    Process answer and record time taken for this attempt.
    """
    # --- TIMING LOGIC START ---
    # Calculate how long they spent on the frame before clicking submit
    end_time = time.time()
    start_time = session.get("start_time", end_time)
    duration = round(end_time - start_time, 2)
    # --------------------------

    frame_idx = session.get("current_frame", 0)
    frame = FRAMES[frame_idx]
    frame_key = str(frame_idx)

    # Store the timing data for this specific frame
    if "timing_data" not in session:
        session["timing_data"] = {}
    
    # We store times as a list in case they take multiple attempts
    if frame_key not in session["timing_data"]:
        session["timing_data"][frame_key] = []
    
    # Add this attempt's time to the list
    # (Using a temporary variable to ensure Flask notices the session change)
    timings = session["timing_data"]
    timings[frame_key].append(duration)
    session["timing_data"] = timings
    session.modified = True

    # Standard answer processing logic...
    if "attempts" not in session:
        session["attempts"] = {}
    if frame_key not in session["attempts"]:
        session["attempts"][frame_key] = 0
    
    user_answer = request.form.get("answer", "").strip()
    correct_answers = frame["answers"]
    is_correct = user_answer in correct_answers
    
    if not is_correct:
        session["attempts"][frame_key] += 1
    
    current_attempts = session["attempts"][frame_key]
    attempts_remaining = max(0, 3 - current_attempts)
    show_hint = attempts_remaining == 1
    show_answer = attempts_remaining == 0
    
    if is_correct:
        session["score"] = session.get("score", 0) + 1
        session["current_frame"] = frame_idx + 1
        feedback = frame.get("feedback_correct", "Correct! Well done.")
    else:
        feedback = frame.get("feedback_incorrect", "Not quite. Try again!")
    
    session.modified = True
    hint = frame.get("hint", "No hint available.")
    
    return render_template(
        "feedback.html",
        is_correct=is_correct,
        feedback=feedback,
        frame=frame,
        correct_answer=correct_answers[0],
        current_attempts=current_attempts,
        attempts_remaining=attempts_remaining,
        show_hint=show_hint,
        show_answer=show_answer,
        hint=hint,
        duration=duration # You can now show this on the feedback page!
    )


@app.route("/complete")
def complete():
    """
    Display results including timing data.
    """
    score = session.get("score", 0)
    total = len(FRAMES)
    percentage = round((score / total) * 100) if total > 0 else 0
    
    # Calculate total time spent across all frames
    timing_dict = session.get("timing_data", {})
    total_seconds = sum(sum(attempts) for attempts in timing_dict.values())
    
    return render_template(
        "complete.html",
        score=score,
        total=total,
        percentage=percentage,
        total_time=round(total_seconds, 2),
        all_timings=timing_dict # Passes the raw data if you want to list it
    )

if __name__ == "__main__":
    app.run(debug=True)