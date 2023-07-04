# GFS IMP 2023 Python Samples and Handouts

Python samples for school presentation in IMP 2023 (GFS) at [Gymnasium Plochingen](https://www.gymnasiumplochingen.de), Germany. 

## Pre-requisites

- Python 3.9 or higher recommended, older versions might work, too
- PyGame 2.0.1 or higher (setup instructions below)

### Installing PyGame

PyGame is a Python library that allows you to create games. 
It is not part of the standard Python library, so you need to install it separately.

To install PyGame, open a terminal and type:

```bash
pip install pygame
```

or use a Python package manager of your choice.


## Installation

Clone this repository to your computer or download it as a ZIP file.

## Running the samples

Each sample is located in a separate directory and can be run independently.

To run the samples, open a terminal, navigate to the directory of the sample you want to run and type:

```bash
  python sample_name.py
```

## List of samples

1. [Sample 1](01_sample/README.md)
   - PyGame skeleton that opens a window and shuts down when the window is closed.
2. [Sample 2](02_sample/README.md)
   - PyGame example rendering a static circle.
3. [Sample 3](03_sample/README.md)
   - PyGame example of a ball with uniform motion and bouncing off the edges of the screen.
4. [Sample 4](04_sample/README.md)
   - PyGame example of a ball under gravity and acceleration.
5. [Sample 5](05_sample/README.md)
   - PyGame example of controlling a ball with mouse, keyboard and joystick.
6. [Sample 6](06_sample/README.md)
   - PyGame example simulating the collision of balls
7. [Sample 7](07_sample/README.md)
    - PyGame example of a tileset and rendering tiles.
8. [Sample 8](08_sample/README.md)
    - PyGame where the player must avoid hitting other balls.

## Known issues

- Joystick controls are tested only with Competition Pro Extra USB Joystick. Other joysticks may work differently and code may need to be adapted.
- Sample 8: Edge cases of ball collisions are not handled on purpose. To keep the code simple, balls might overlap or get stuck in each other if e.g. collisions happen in corners or too many balls are on the screen.

## Further reading and sources

The internet is full of PyGame resources. Here are some links to get you started:

- [PyGame documentation](https://www.pygame.org/docs/)
- [PyGame tutorials](https://www.pygame.org/wiki/tutorials)
- [PyGame examples](https://www.pygame.org/tags/example)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/pygame)
- GitHub Copilot and GitHub Codepilot X

## How to contribute

General information about contributing to open source projects can be found in [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/).

If you are new to GitHub and want to contribute to this repository, please have a look at [Contributing to projects](https://docs.github.com/en/get-started/quickstart/contributing-to-projects).

As this repository is part of a school project it is not intended to be a full-fledged open source project. It is more of a playground for first steps with PyGame.

The more examples we have, the better. So if you have a PyGame example that you want to share, please feel free to contribute by forking this project and creating a pull request.


