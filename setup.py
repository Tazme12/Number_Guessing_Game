from setuptools import setup, find_packages

setup(
    name="number_guessing_game",
    version="1.0.0",
    packages=find_packages(), 
    install_requires=[],  # No external dependencies needed
    entry_points={  
        "console_scripts": [
            "number-guessing-game=number_guessing_game.main:main" 
        ]
    },
    author="Cameron Thornton",
    author_email="camthornton.07@gmail.com",
    description="A simple CLI based number guessing game",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Tazme12/Number_Guessing_Game",  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)