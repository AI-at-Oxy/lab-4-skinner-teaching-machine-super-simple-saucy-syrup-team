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
    "prompt": "The capital of France is _____.",
    "answer": "paris"
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
    # Frame 1: Introduction
    {
        "prompt": "In Minecraft, we need _____ and _____ to make a compass.",
        "answers": ["iron ingots", "redstone dust"],
        "feedback_correct": "Correct! You need iron ingots and redstone dust.",
        "feedback_incorrect": "Not quite. You can find both of these ingredients in a cave."
    },
    
    # Frame 2: Assignment operator
    {
        "prompt": "You need ___ iron ingots.",
        "answer": "4",
        "feedback_correct": "Yes! You need 4 iron ingots.",
        "feedback_incorrect": "Not quite. How many sides are in a square?"
    },
    
    # Frame 3: Simple assignment
    {
        "prompt": "To make iron ingots, you ___ the iron ore",
        "answer": "smelt",
        "feedback_correct": "Correct! You use a ",
        "feedback_incorrect": "Remember, we use = for assignment. So: x = 5"
    },
    
    # Frame 4: String variables
    {
        "prompt": "Text data in Python is called a _____.",
        "answer": "string",
        "feedback_correct": "Yes! Strings are sequences of characters (text).",
        "feedback_incorrect": "Text data is called a string."
    },
    
    # Frame 5: String syntax
    {
        "prompt": "Strings must be surrounded by _____ or double quotes.",
        "answer": "single",
        "feedback_correct": "Correct! Both 'hello' and \"hello\" are valid strings.",
        "feedback_incorrect": "Strings use single quotes or double quotes: 'hello' or \"hello\""
    },
    
    # Frame 6: Naming conventions
    {
        "prompt": "Variable names in Python cannot start with a _____.",
        "answer": "number",
        "feedback_correct": "Right! Variables can't start with numbers. 'var1' is ok, '1var' is not.",
        "feedback_incorrect": "Variable names cannot start with a number."
    },
    
    # Frame 7: Case sensitivity
    {
        "prompt": "In Python, 'Name' and 'name' are _____ variables. (same/different)",
        "answer": "different",
        "feedback_correct": "Correct! Python is case-sensitive.",
        "feedback_incorrect": "Python is case-sensitive, so Name and name are different."
    },
    
    # Frame 8: Print function
    {
        "prompt": "To display a variable's value, we use the _____ function.",
        "answer": "print",
        "feedback_correct": "Yes! print(x) displays the value of x.",
        "feedback_incorrect": "We use the print() function to display values."
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
