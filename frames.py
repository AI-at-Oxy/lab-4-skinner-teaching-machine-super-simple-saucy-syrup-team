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
    # Frame 1: Ingredients #FIXME make it so that you can fill in two blanks or only one answer works for one and two
    {
        "prompt": "In Minecraft, we need two ingredients to make a compass. The first is _____.",
        "answers": ["iron ingots", "redstone dust"],
        "hint": "You can find either ingredient in a cave ...",
        "feedback_correct": "Correct! You need iron ingots.",
        "feedback_incorrect": "Not quite. You can find both of these ingredients in a cave."
    },
    # Frame 1.5: Ingredients 2
    {
        "prompt": "The second ingredient is _____.",
        "answers": ["iron ingots", "redstone dust"],
        "feedback_correct": "Correct! You need iron ingots and redstone dust.",
        "feedback_incorrect": "Not quite. You can find both of these ingredients in a cave."
    },

    """
    frame = {
    "prompt": "What keyword defines a function in Python?",
    "answer": "def",
    "answers": ["def"],  # List for multiple acceptable answers
    "hint": "It's a 3-letter word.",
    "feedback_correct": "Yes! 'def' is used to define functions.",
    "feedback_incorrect": "Not quite. We use 'def' to define functions.",
    "topic": "python-functions"
    }
    """
    
    # Frame 2: Number of Iron Ingots
    {
        "prompt": "You need _____ iron ingots.",
        "answer": "4",
        "feedback_correct": "Yes! You need 4 iron ingots.",
        "feedback_incorrect": "Not quite. How many sides are in a square?"
    },
    
    # Frame 3: Smelting
    {
        "prompt": "To make iron ingots, you _____ the iron ore",
        "answer": "smelt",
        "feedback_correct": "Correct! You use a furnace to smelt iron ore.",
        "feedback_incorrect": "Not quite. How do change solid iron into liquid to reshape it?"
    },
    
    # Frame 4: Crafting Table
    {
        "prompt": "To build a compass you use a ___ table",
        "answer": "crafting",
        "feedback_correct": "Yes! A crafting table helps to make many items in Minecraft",
        "feedback_incorrect": "Not quite, another word for building is crafting ..."
    },
    
    # Frame 5: 3x3 Grid
    {
        "prompt": "When you open the crafting table, you access a ___ x3 grid",
        "answer": "3",
        "feedback_correct": "Correct! To craft, you arrange ingredients in a 3x3 grid to make many different items",
        "feedback_incorrect": "Not quite, the crafting table uses a perfect square grid ..."
    },

    # Frame 6: Placement of Redstone Dust
    {
        "prompt": "The ____ goes in the center of the iron ingots",
        "answer": "redstone dust",
        "feedback_correct": "Correct! The redstone dust goes in the middle of the iron ingots",
        "feedback_incorrect": "Not quite, what is the other ingredient in the compass?"
    },
    
    # Frame 7: + Shape
    {
        "prompt": "The 4 iron ingots are arranged in a ____ shape around the redstone dust",
        "answer": "+",
        "feedback_correct": "Correct! The iron ingots evenly surround the redstone dust on all four sides",
        "feedback_incorrect": "The iron ingots should be placed in the middle-top, middle-bottom, middle-left, and middle-right slots (forming a + shape)"
    },
    
    # Frame 8: Collection
    {
        "prompt": "To collect, you ____ the compass from the result slot to your inventory.",
        "answer": "drag",
        "feedback_correct": "Yes! You drag the compass into your inventory. Now you can use your newly crafted compass!",
        "feedback_incorrect": "Not quite, if you click and hold down your mouse while moving it, you do what? ..."
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
