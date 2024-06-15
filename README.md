# Prey and Predator Simulation

## Overview
This project is a simulation of a predator-prey ecosystem, controlled by various statistical parameters. The key statistics include hunt success rate, flee success rate, and birth rate. The simulation aims to model the dynamic interactions between predators and prey over time.

## Features
- **Hunt Success Rate:** Probability that a predator successfully hunts a prey.
- **Flee Success Rate:** Probability that a prey successfully escapes a predator.
- **Birth Rate:** Rate at which new prey and predators are born.
- **Death Rate:** Determined by unsuccessful hunts for predators and successful hunts for prey.

## How It Works
- **Predators** attempt to hunt prey. Whether a hunt is successful is determined by the hunt success rate.
- **Prey** attempt to flee from predators. Whether a flee is successful is determined by the flee success rate.
- **Births** occur at a rate defined by the birth rate parameter for both predators and prey.
- **Deaths**:
  - Prey die if a predator successfully hunts them.
  - Predators die if they fail to hunt prey over a certain period, representing starvation.

## Parameters
- **Hunt Success Rate (`hunt_success`)**: Float between 0 and 1 representing the probability of a successful hunt.
- **Flee Success Rate (`flee_success`)**: Float between 0 and 1 representing the probability of a successful flee.
- **Birth Rate (`birth_rate`)**: Float between 0 and 1 representing the probability of reproduction in each time step.
- **Starvation Time (`starvation_time`)**: Integer representing the maximum number of time steps a predator can survive without hunting successfully.
