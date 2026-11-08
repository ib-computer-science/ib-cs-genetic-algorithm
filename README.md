# IB CS genetic algorithm case study program (Python port)

A Python port of https://github.com/hurrja/ib-cs-tsp-ga: a genetic algorithm
that finds a solution to the travelling salesman problem (TSP). TSP data is
taken from the IBO CS genetic algorithm case study.

Supports:
- truncation, roulette wheel, and tournament selection
- PMX, OX and CX crossover
- city-switch mutation

The algorithm terminates when there is no improvement in the fittest
individual and no improvement in "median" fitness from the previous
generation.

## Usage

```
python3 main.py
```

All program data and parameters are coded in `main.py`. Change the
population size, number of elites, mutation rate, or swap in a different
`Selection`/`Crossover` implementation there to explore the algorithm's
behavior.

## Measure of fitness

Genetic algorithms maximize fitness. In TSP, route length is minimized, so
route length can not be used as a direct measure of fitness. In this
implementation, fitness is the *negative* of route length: maximizing it
minimizes route length, and the corresponding route length can be read
directly off a fitness value.

## Layout

- `distances.py` -- city list and the distance table
- `random_utils.py` -- small random-number helpers
- `population_utils.py` -- sorting a population by fitness, "median" fitness
- `selection.py` -- `Selection` base class and implementations
- `crossover.py` -- `Crossover` base class and implementations
- `mutation.py` -- `Mutation` base class and implementation
- `termination.py` -- `TerminationRule` base class and implementation
- `genetic_algorithm.py` -- `TSPGeneticAlgorithm`, the main loop
- `main.py` -- entry point wiring everything together

## License

Copyright (C) 2021 Jarmo Hurri, Askar Tuiushev, Gabriel Dearden and Diana
Ginzburg

This program is free software: you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option)
any later version. See `LICENSE.txt`.
