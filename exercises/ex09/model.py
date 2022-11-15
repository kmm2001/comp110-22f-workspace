"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730314205"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, other: Point) -> float:
        """Returns the distance between the Point object the method was called on and some other Point object passed in as a parameter."""
        d: float = sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        return d


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction
    
    def tick(self) -> None:
        """Update to the next state/time."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()
    # Part 1) Define a method named `tick` with no parameters.
    # Its purpose is to reassign the object's location attribute
    # the result of adding the self object's location with its
    # direction. Hint: Look at the add method.

    def contract_disease(self) -> None:
        """Assign the INFECTED constant you defined above to the sickness attribute of the Cell object the method is called on."""
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool:
        """Return True when the cells sickness attribute is equal to VULNERABLE and False otherwise."""
        vulnerability: bool = True
        if self.sickness == constants.VULNERABLE:
            vulnerability = True
        else:
            vulnerability = False
        return vulnerability

    def is_infected(self) -> bool:
        """Return True when the cells sickness attribute is equal to INFECTED and False otherwise."""
        infectedness: bool = True
        if self.sickness >= constants.INFECTED:
            infectedness = True
        else:
            infectedness = False
        return infectedness

    def color(self) -> str:
        """It should return gray if the Cell is vulnerable, and red if the Cell is infected."""
        colors: str = ""
        if self.is_vulnerable():
            colors = "gray"
        elif self.is_infected():
            colors = "red"
        elif self.is_immune():
            colors = "green"
        return colors

    def contact_with(self, cell: Cell) -> None:
        """When two Cell objects make contact."""
        if cell.is_vulnerable() and self.is_infected():
            cell.contract_disease()
        if cell.is_infected() and self.is_vulnerable():
            self.contract_disease()

    def immunize(self) -> None:
        """Assigns the constant IMMUNE to the sickness attribute of the Cell."""
        self.sickness = constants.IMMUNE
    
    def is_immune(self) -> bool:
        """Returns True when the Cell objects sickness attribute is equal to the IMMUNE constant."""
        value: bool
        if constants.IMMUNE == self.sickness:
            value = True
        else:
            value = False
        return value


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, number_infected: int, immune_start: int = 0):
        """Initialize the cells with random locations and directions."""
        self.population = []
        if number_infected >= cells or number_infected <= 0:
            raise ValueError("Some number of the Cell objects must begin infected.")
        if immune_start >= cells or immune_start < 0:
            raise ValueError("Immune start out of bounds.")
        for i in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            if i < number_infected:
                cell.contract_disease()
            elif i >= number_infected and i < number_infected + immune_start:
                cell.immunize()
            self.population.append(cell)

    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def check_contacts(self) -> None:
        """Compare the distance between every two Cell object location attributes in the population."""
        for i in range(0, len(self.population)):
            for j in range(i + 1, len(self.population)):
                x: Cell = self.population[i]
                y: Cell = self.population[j]
                if x.location.distance(y.location) < constants.CELL_RADIUS:
                    x.contact_with(y)
                
    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        for cell in self.population:
            if cell.is_infected():
                return False
        return True