# Lorenz Attractor Simulation in Python

This repository contains a Python implementation of the Lorenz Attractor, a system of differential equations that exhibits chaotic behavior, famously used to model atmospheric convection. The code simulates the Lorenz system, plots the resulting trajectories, and includes unit tests to verify the correctness of the implementation.

## Features
- **Lorenz System Implementation**: Computes the derivatives of the Lorenz system based on its equations.
- **Simulation**: Simulates the Lorenz system over a specified number of steps, capturing the chaotic behavior of the system.
- **Plotting**: Visualizes the 3D trajectory of the Lorenz attractor using Matplotlib.
- **Unit Testing**: Includes unittests to verify the correctness of the Lorenz system's dynamics and its sensitivity to initial conditions.

## Lorenz System Equations
The Lorenz system is defined by three differential equations:

- dx/dt = sigma * (y - x)
- dy/dt = x * (rho - z) - y
- dz/dt = x * y - beta * z

Where:
- `sigma = 10`
- `rho = 28`
- `beta = 8/3`
