"""
Skinner Teaching Machine - Frame Definitions
COMP 395: AI and Learning Technologies

This file contains the instructional frames for your teaching machine.

=============================================================================
YOUR TASK:
=============================================================================
1. Choose a topic you want to teach (5-10 frames minimum)
2. Design your frame structure (see options below)
3. Write frames that follow Skinner's principles:
   - Small steps: Each frame teaches ONE small concept
   - Build sequentially: Later frames build on earlier ones
   - High success rate: Design for ~95% correct answers
   - Clear prompts: Unambiguous fill-in-the-blank or short answer

=============================================================================
FRAME STRUCTURE OPTIONS:
=============================================================================

OPTION A - Minimal:
frame = {
    "prompt": "You need ____ and _____ to craft a compass",
    "answer": "iron, iron ingot, redstone"
}

OPTION B - With feedback (RECOMMENDED):
frame = {
    "prompt": "The capital of France is _____.",
    "answer": "paris",
    "feedback_correct": "Correct! Paris is the capital of France.",
    "feedback_incorrect": "Not quite. The answer is Paris."
}

OPTION C - Rich (with hints and multiple answers):
frame = {
    "prompt": "What keyword defines a function in Python?",
    "answer": "def",
    "answers": ["def"],  # List for multiple acceptable answers
    "hint": "It's a 3-letter word.",
    "feedback_correct": "Yes! 'def' is used to define functions.",
    "feedback_incorrect": "Not quite. We use 'def' to define functions.",
    "topic": "python-functions"
}

Choose a structure and be CONSISTENT across all your frames!
=============================================================================
"""

# =============================================================================
# EXAMPLE FRAMES: Introduction to Python Variables
# Replace these with your own topic!
# =============================================================================

FRAMES = [
    {
        "prompt": "To craft a compass you need _____ and ________.",
        "answer": ["iron ingot and redstone", "redstone and iron ingot"],
        "feedback_correct": "Correct! You need iron ingots and redstone!",
        "feedback_incorrect": "Not quite. You can find both of them in a cave"
    },
    
    # Frame 2: Assignment operator
 {
    "prompt": "You need ___ iron ingots",
    "answer": ["4", "four", "Four", "FOUR"],
    "feedback_correct": "Yes! You need four iron ingots!",
    "feedback_too_high": "Not quite, you don't need that many.",
    "feedback_too_low": "Not quite, you need a few more."
},
    
    # Frame 3: Simple assignment
    {
        "prompt": "To make the iron ingots you ______ the iron",
        "answer": ["smelt", "Smelt", "SMELT"],
        "feedback_correct": "Correct! You have to smelt the iron!",
        "feedback_incorrect": "You have to use a furnace to do this!"
    },
    
    # Frame 4: String variables
    {
        "prompt": "To make a compass you need a ______ table",
        "answer": ["crafting", "Crafting", "CRAFTING"],
        "feedback_correct": "Yes! You need a crafting table!",
        "feedback_incorrect": "What's another word for make, or create?"
    },
    
    # Frame 5: String syntax
    {
        "prompt": "The ____ goes in the center spot of the crafting table",
        "answer": ["redstone", "REDSTONE"],
        "feedback_correct": "Correct!",
        "feedback_incorrect": "You need the other maerial"
    },
    
]

# =============================================================================
# TIPS FOR WRITING GOOD FRAMES:
# =============================================================================
# 
# 1. START EASY: First frames should be very simple
# 
# 2. ONE CONCEPT PER FRAME: Don't combine multiple ideas
# 
# 3. USE BLANKS STRATEGICALLY: 
#    "In Python, we use _____ to define a function."
#    Not: "What do we use to define a function in Python?"
# 
# 4. BUILD ON PREVIOUS FRAMES: Frame 5 can reference concepts from Frame 3
# 
# 5. ANTICIPATE ERRORS: Your feedback_incorrect should address common mistakes
# 
# 6. NORMALIZE ANSWERS: The app converts to lowercase and strips whitespace,
#    but consider if "=" and "equals" should both be accepted
#
# =============================================================================
