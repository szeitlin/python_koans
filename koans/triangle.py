#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.


# triangle(a, b, c) analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    '''
    if a==b==c, 'equilateral'

    :param a:
    :param b:
    :param c:
    :return:
    '''
    sides = [a, b, c]

    #test for exceptions
    if 0 in sides:
        raise TriangleError

     #sides must actually form a triangle (triangle inequality theorem: c < a + b)
    sides.sort()
    if sides[2] > (sides[0]+ sides[1]):
        raise TriangleError

    #sides must be positive in length
    if any([x<0 for x in sides]):
        raise TriangleError

    sides_set = set(sides)

    if len(sides_set) == 1:
        return 'equilateral'

    else:
        if len(sides_set) == 2:
            return 'isosceles'
        else:
            return 'scalene'


class TriangleError(StandardError):
    pass


# triangle(1,2,3)
# triangle(2,2,2)
