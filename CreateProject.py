import os

# Base course folder
base_dir = "Python_AI_Course"

# Subfolders
folders = [
    "JupyterNotebooks",
    "Assignments",
    "Programs",
    "Materials"
]

# Chapters for Jupyter notebooks
chapters = [
    "Chapter 1 - Introduction to Python and AI",
    "Chapter 2 - Python Basics - Data Types, Operators, and Control Structures",
    "Chapter 3 - Functions, Scope, and Recursion",
    "Chapter 4 - Data Structures in Python",
    "Chapter 5 - File Handling, Exceptions, and Modules",
    "Chapter 6 - Object-Oriented Programming in Python",
    "Chapter 7 - Data Manipulation with NumPy and Pandas",
    "Chapter 8 - Data Visualization with Matplotlib and Seaborn",
    "Chapter 9 - Introduction to Machine Learning",
    "Chapter 10 - Supervised Learning - Regression and Classification",
    "Chapter 11 - Unsupervised Learning",
    "Chapter 12 - Introduction to Deep Learning",
    "Chapter 13 - Natural Language Processing Basics",
    "Chapter 14 - Final Project and Deployment Basics",
]

# Create base directory
os.makedirs(base_dir, exist_ok=True)

# Create subdirectories
for folder in folders:
    path = os.path.join(base_dir, folder)
    os.makedirs(path, exist_ok=True)

# Create chapter folders inside JupyterNotebooks
for chapter in chapters:
    path = os.path.join(base_dir, "JupyterNotebooks", chapter)
    os.makedirs(path, exist_ok=True)
    # Add empty notebook placeholder
    with open(os.path.join(path, f"{chapter}.ipynb"), "w") as f:
        f.write("{}")

# Create README.md
with open(os.path.join(base_dir, "README.md"), "w") as f:
    f.write("# Python + AI Course\n\n")
    f.write("This repository contains materials, notebooks, programs, and assignments for the Python + AI course.\n")

# Create .gitignore
with open(os.path.join(base_dir, ".gitignore"), "w") as f:
    f.write("__pycache__/\n")
    f.write("*.pyc\n")
    f.write(".ipynb_checkpoints/\n")
    f.write("env/\n")
    f.write(".DS_Store\n")

print(f"✅ Course folder structure created inside '{base_dir}'")
