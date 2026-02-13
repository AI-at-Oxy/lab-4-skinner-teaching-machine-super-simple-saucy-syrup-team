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
    # Frame 1: Ingredients: Iron
    {
        "prompt": "In Minecraft, we need two ingredients to craft a compass. One is _____ ingots.",
        "answers": ["iron", "Iron", "IRON"],
        "hint": "This is one of the most common metals on Earth!",
        "feedback_correct": "Correct! You need iron ingots and one more ingredient.",
        "feedback_incorrect": "Not quite. You need iron ingots and one more ingredient."
    },
    # Frame 1.5: Ingredients: Redstone
    {
        "prompt": "The second ingredient is _____ dust.",
        "answers": ["redstone", "Redstone", "REDSTONE", "red stone", "Red stone", "Red Stone", "RED STONE"],
        "hint": "it's red ...",
        "feedback_correct": "Correct! You need iron ingots and redstone dust.",
        "feedback_incorrect": "Not quite. You need iron ingots and redstone dust"
    },
    
    # Frame 2: Number of Iron Ingots
    {
        "prompt": "Let's talk numbers ... You need _____ iron ingots.",
        "answers": ["4", "four", "Four", "FOUR", "IV"], # never forget roman numerals
        "hint": "It is an even number ...",
        "feedback_correct": "Yes! You need 4 iron ingots.",
        "feedback_incorrect": "Not quite. You need 4 iron ingots to make a compass."
    },
    
    # Frame 3: Smelting
    {
        "prompt": "To make iron ingots, you _____ the iron ore",
        "answer": "smelt",
        "hint": "This is the process of extracting a metal from its ore by melting it ... it is also the past tense of 'smell'",
        "feedback_correct": "Correct! You use a furnace to smelt iron ore.",
        "feedback_incorrect": "Not quite. You use a furnace to smelt iron ore."
    },
    
    # Frame 4: Crafting Table
    {
        "prompt": "To build a compass you use a _____ table",
        "answer": "crafting",
        "hint": "Another word for building is ... (its also in the name Minecraft!)",
        "feedback_correct": "Yes! A crafting table helps to make many items in Minecraft",
        "feedback_incorrect": "Not quite, A crafting table helps to make many items in Minecraft."
    },
    
    # Frame 5: 3x3 Grid
    {
        "prompt": "When you open the crafting table, you access a _____ x3 grid",
        "answer": "3",
        "hint": "The crafting table uses a perfect square grid ...",
        "feedback_correct": "Correct! To craft, you arrange ingredients in a 3x3 grid to make many different items.",
        "feedback_incorrect": "Not quite, to craft, you arrange ingredients in a 3x3 grid to make many different items."
    },

    # Frame 6: Placement of Redstone Dust
    {
        "prompt": "The _____ goes in the center of the iron ingots",
        "answer": "redstone dust",
        "hint": "Remember, the ingredients used to craft a compass are iron ingots and a type of dust ...",
        "feedback_correct": "Correct! The redstone dust goes in the middle of the iron ingots.",
        "feedback_incorrect": "Not quite, the redstone dust goes in the middle of the iron ingots."
    },
    
    # Frame 7: + Shape
    {
        "prompt": "The 4 iron ingots are arranged in a ____ shape around the redstone dust",
        "answers": ["+", "plus", "cross"],
        "hint": "To add, you use the _____ sign (also known as a cross)...",
        "feedback_correct": "Correct! The iron ingots evenly surround the redstone dust on all four sides",
        "feedback_incorrect": "Not quite, the iron ingots should be placed in the middle-top, middle-bottom, middle-left, and middle-right slots (forming a + shape)"
    },
    
    # Frame 8: Collection
    {
        "prompt": "To collect, you _____ the compass from the result slot to your inventory.",
        "answer": "drag",
        "hint": "If you click and hold down your mouse while moving it, you do what? ...",
        "feedback_correct": "Yes! You drag the compass into your inventory. Now you can use your newly crafted compass!",
        "feedback_incorrect": "Not quite, you drag the compass into your inventory. Now you can use your newly crafted compass!"
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
