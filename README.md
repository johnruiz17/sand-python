## Sand

![sand-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/b29b1f24-12ce-4579-aca6-acda72b8ee4b)

## Description
This program simulates a two-dimensional world filled with sand particles. Users can interact with the sand by clicking and dragging to:

* Place sand particles
* Place rocks (immobile particles)
* Erase sand particles
* Erase a large area of sand particles
  
The simulation incorporates the following physics:

* Gravity: Sand particles fall downward until they hit another particle or the bottom of the world.
* Brownian motion: Sand particles experience a slight random side-to-side movement.
  
## Technologies Used
* Python 3
* Tkinter library: for creating the graphical user interface (GUI)
* Random library: for generating random numbers used in Brownian motion

  
## Installation
This program requires Python 3 to be installed on your system. You can download and install Python from the official website: https://www.python.org/downloads/   

## Usage
Open a terminal or command prompt and run the program by typing the following command:
```bash
python3 sand.py
```
You can optionally specify the size of the sand world and the size of each sand particle in pixels when running the program:

```bash
python3 sand.py [width] [height] [particle_size]
```

* width: The number of sand particles wide (default: 50)
* height: The number of sand particles tall (default: 50)
* particle_size: The size of each sand particle in pixels (default: 14)

