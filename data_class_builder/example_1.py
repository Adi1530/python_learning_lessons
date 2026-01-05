# usual approach boiler plate template

# class Coordinate:
# 	def __init__(self,x,y):
# 		self.x=x
# 		self.y=y
#
# position = Coordinate(3,5)

# Using namedtuple
#
# from collections import namedtuple as nt
#
# Coordinate = nt("Coordinate",['x','y'])
# position = Coordinate(5,10)
# print(position)
# print(position == Coordinate(5,10))

# Using NamedTuple
#
# from typing import NamedTuple
#
# Coordinate = NamedTuple('Coordinate' , [('X',int) , ('Y' , int)])
# print(issubclass(Coordinate,tuple))
# position = Coordinate(4,5)
# print(position)

# from dataclasses import dataclass
#
# @dataclass
# class Coordinate:
# 	x : float
# 	y : float
#
# position = Coordinate(4.5 , 6.7)
# print(position)
#

# frozen condition in decorator
#
# from dataclasses import dataclass
#
# @dataclass(frozen=True)
# class Coordinate :
# 	X : float
# 	Y : float
#
# position = Coordinate(5,10)
# position.Y=15 # throws frozen instance error


