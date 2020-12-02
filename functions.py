from math import *

class Circle:
    def area():
        a = float(input('enter the value of r: '))
        b = 22/7
        c = a*a*b
        print(c)

    def circumference():
        a = float(input('enter the value of r: '))
        b = 22/7
        c = 2*b*a
        print(c)

    def diameter():
        a = float(input('enter the vlaue of radius: '))
        print(a*2)

    def radius():
        a = float(input('enter the value of a: '))
        b = 22/7
        print(sqrt(a/b))

class Cone:
    def base_area():
        a = float(input('enter the value of r: '))
        b = 22/7
        print(a*a*b)

    def height():
        a = float(input('enter the value r: '))
        b = float(input('enter the value of a: '))
        c = 22/7
        d = (b/(c*a))-a
        e = d*d
        f = a*a
        g = e-f
        print(sqrt(g))

    def lateral_surface():
        a = float(input('enter the value r: '))
        b = float(input('enter the value of h: '))
        c = 22/7
        d = a*c
        e = a*a
        f = b*b
        g = e+f
        h = sqrt(g)
        print(d*h)

    def radius():
        a = float(input('enter the value of a: '))
        b = float(input('enter the value of h: '))
        c = a*a
        d = b*b
        e = 22/7
        f = e*((e+d)+(2*a))
        g = sqrt(c/f)
        print(g)
    
    def slant_height():
        a = float(input('enter the value of r: '))
        b = float(input('enter the value of h: '))
        c = a*a
        d = b*b
        print(sqrt(c+d))

    def surface_area():
        a = float(input('enter the value of r: '))
        b = float(input('enter the value of h: '))
        c = 22/7
        d = a*a
        e = b*b
        f = sqrt(d+e)
        g = c*a
        h = a+f
        print(g*h)
    
    def volume():
        a = float(input('enter the value of r: '))
        b = float(input('enter the value of h: '))
        c = 22/7
        d = a*a
        e = 1/3
        print(c*d*b*e)

class Cube:
    def diagonal():
        a = float(inf('enter the value of a: ')) 
        b = sqrt(3)
        print(a*b)

    def edge():
        a = float(inf('enter the value of a: '))
        print(sqrt(a/6))

    def surface_area():
        a = float(input('enter the value of a: '))
        print(6*a*a)

    def volume():
        a = float(input('enter the value of a: '))
        print(a*a*a)

class Cylinder:
    def base_area():
        a = float(input('enter the value of r: '))
        b = 22/7
        print(a*a*b)

    def height():
        a = float(input('enter the value of a: '))
        b = float(input('enter the value of r: '))
        c = 22/7
        d = 2*c*b
        e = b/d
        print(e-b)

    def lateral_surface_area():
        a = float(input('enter the value of r: '))
        b = float(input('enter the value of h: '))
        c = 22/7
        print(2*c*a*b)

    def radius():
        a = float(input('enter the value of a: '))
        b = float(input('enter the value of h: '))
        c = 22/7
        d = b*b
        e = (2*a)/c
        f = (sqrt(d+e))/2
        g = b/2
        h = f-g
        print(h)

    def surface_area():
        a = float(input('enter the value of r: '))
        b = float(input('enter the value of a: '))
        c = 22/7
        d = a+b
        print(2*c*a*d)

    def volume():
        a = float(input('enter the value of r: '))
        b = float(input('enter the value of h: '))
        c = 2/7
        print(c*a*a*b)

class Ellipse:
    def area():
        a = float(input('enter the value of a: '))
        b = float(input('enter the value of b: '))
        c = 22/7
        print(a*b*c)
        
    def axis_a():
        a = float(input('enter the value of area: '))
        b = float(input('enter the value of axis b: '))
        c = 22/7
        d = b*c
        print(a/d)

    def axis_b():
        a = float(input('enter the value of area: '))
        b = float(input('enter the value of axis a: '))
        c = 22/7
        d = b*c
        print(a/d)

    def circumference():
        a = float(input('enter the value of axis a: '))
        b = float(input('enter the value of axis b: '))
        c = 22/7
        d = a+b
        e = (3*a)+b
        f = a+(3*b)
        g = 3*(a+b)
        h = sqrt(f*e)
        i = g-h
        j = c*i
        print(j)

class Equilateral_triangle:
    def area():
        a = float(input('enter the value of a: '))
        b = sqrt(3)
        c = a*a
        d = b/4
        print(c*d)

    def perimeter():
        a = float('enter the value of a: ')
        print(3*a)

class Heptagon:
    def area():
        a = float(input('enter the value of a: '))
        b = 7/4
        c = 22/7
        d = c/7
        e = tan(d)
        f = a*a
        g = f/e
        print(b*g)

    def perimeter():
        a = float(input('enter the value of a: '))
        print(7*a)

    def side():
        a = float(input('enter the value of a: '))
        b = 22/7
        c = b/7
        d = tan(c)
        e = d/7
        f = 4*a
        g = e*f
        print(sqrt(g))

class Hexagion:
    def area():
        a = float(input('enter the value of a: '))
        b = sqrt(3)
        c = 3*b
        d = c/2
        e = a*a
        print(d*e)

    def perimeter():
        a = float(input('enter the value of a: '))
        print(6*a)

    def side():
        a = float(input('enter the value of a: '))
        b = sqrt(3)
        c = sqrt(b)
        d = (2/9)*a
        e = sqrt(d)
        print(c*e)

class Isoceles_triangle:
    def area():
        h = float(input('enter the value of h: '))
        b = float(input('enter the value of b: '))
        a = h*b
        print(a/2)

    def base():
        a = float(input('enter the value of a: '))
        b = float(input('enter the value of h: '))
        c = a/b
        print(2*c)

    def height():
        a = float(input('enter the value of a: '))
        b = float(input('enter the value of b: '))
        c = a/b
        print(2*c)

    def perimeter():
        a = float(input('enter the value of a: '))
        b = float(input('enter the value of b: '))
        c = 2*a
        print(c+b)

    def side():
        a = float(input('enter the value of a: '))
        b = float(input('enter the value of b: '))
        c = float(input('enter the value of gamma: ')
        d = sin(c)
        e = b*d
        f = a/e
        print(2*f)

class Ocatgon:
    def area():
        a = float(inf('enter the value of a: '))
        b = sqrt(2)
        c = 1+b
        print(2*c*a*a)

    def perimeter():
        a = float(inf('enter the value of a: '))
        print(8*a)

    def side():
        a = float(input('enter the value of a: '))
        b = sqrt(2) - 1
        c = a/2
        print(sqrt(b*c))

class Octahedron:
    def edge():
        a = float(input('enter the value of a: '))
        b = sqrt(sqrt(3))
        c = sqrt(a/18)
        print(b*c)

    def surface_area():
        a = fl(input('enter the value of a: '))
        b = sqrt(3)
        print(2*a*a*b)

    def volume():
        a = float(input('enter the value of a: '))
        b = sqrt(2)
        c = b*a*a*a
        print(c/3)

class Parallelogram:
    def area():
        a = float(input('enter the value of b: '))
        b = float(input('enter the value of h: '))
        print(a*b)

    def base():
        a = float(input('enter the value of a: '))
        b = float(input('enter the value of h: '))
        print(a/b)

    def height():
        a = float(input('enter the value of a: '))
        b = float(input('enter the value of b: '))
        print(a/b)

    def perimeter():
        a = float(input('enter the value of a: '))
        b = float(input('enter the value of b: '))
        c = a+b
        print(2*c)

    def side():
        a = float(input('enter the value of P: '))
        b = float(input('enter the value of known length: '))
        c = a/2
        print(c-2)
        
class Pentagon: 
    def area():
        a = float(input('enter the value of a: '))
        b = 1/4
        c = 2*sqrt(5)
        d = sqrt(5*(5+c))
        print(b*d*a*a)

    def diagonal():
        a = float(input('enter the value of a: '))
        b = sqrt(5)
        c = 1+b
        d = a/2
        print(c*d)

    def perimeter():
        a = float(input('enter the value of a: '))
        print(5*a)

    def side():
        a = float(input('enter the value of a: '))
        b = sqrt(5)
        c = b*b
        d = sqrt(a)
        e = 10+b
        f = c*d
        print(f/e)

class Pyramid:
    def base_area():
        a = float(input('enter the value of l: '))
        b = float(input('enter the value of w: '))
        print(a*b)

    def base_length():
        a = float(input('enter the value of a: '))
        b = float(input('enter the value of w: '))
        print(a/b)

    def base_width():
        a = float(input('enter the value of a: '))
        b = float(input('enter the value of l: '))
        print(a/b)

    def height():
        v = float(input('enter the value of v: '))
        w = float(input('enter the value of w: '))
        l = float(input('enter the value of h:'))
        a = 3*v
        b = w*l
        print(a/b)

    def lateral_surface():
        w = float(input('enter the value of w:'))
        l = float(input('enter the value of l:'))
        h = float(input('enter the value of h: '))
        a = (w/2)*(w/2)
        b = (l/2)*(l/2)
        c = h*h
        d = sqrt(a+c)
        e = sqrt(b+c)
        f = l*a
        g = w*e
        print(f+g)

    def surface_area():
        w = float(input('enter the value of w:'))
        l = float(input('enter the value of l:'))
        h = float(input('enter the value of h: '))
        a = (w/2)*(w/2)
        b = (l/2)*(l/2)
        c = h*h
        d = sqrt(a+c)
        e = sqrt(b+c)
        f = l*a
        g = w*e
        h = l*w
        print(f+g+h)

    def volume():
        l = float(input('enter the value of l: '))
        w = float(input('enter the value of w: '))
        h = float(input('enter the value of h: '))
        a = l*w*h
        print(a/3)

class Rectangle:
   def area():
        w = float(input('enter the value of l: '))
        b = float(input('enter the value of b: '))
        print(l*b)

    def diagonal():
        l = float(input('enter the value of l: '))
        b = float(input('enter the value of b: '))
        a = l*l
        c = b*b
        print(sqrt(a+b))

    def length():
        a = float(input('enter the value of a: '))
        b = float(input('enter the value of b: '))
        print(a/b)

    def perimeter():
        l = float(input('enter the value of l: '))
        b = float(input('enter the value of b: '))
        a = l+b
        print(2*a)

    def width():
        a = float(input('enter the value of a: '))
        b = float(input('enter the value of l: '))
        print(a/b)

class Cuboid:
    def diagonal():
        l = float(input('enter the value of l: '))
        b = float(input('enter the value of b: '))
        h = float(input('enter the value of h: '))
        x = l*l
        y = b*b
        z = h*h
        print(sqrt(x+y+z))

    def surface_area():
        l = float(input('enter the value of l: '))
        b = float(input('enter the value of b: '))
        h = float(input('enter the value of h: '))
        x = l*b
        y = b*h
        z = h*l
        a = x+y+z
        print(2*a)

    def volume():
        l = float(input('enter the value of l: '))
        b = float(input('enter the value of b: '))
        h = float(input('enter the value of h: '))
        print(l*b*h)

class Rhombus:
    def area():
        p = float(input('enter the value of p: '))
        q = float(input('enter the value of q: '))
        x = p*q
        p(x/2)

    def diagonal_p():
        a = float(input('enter the value of a: '))
        q = float(input('enter the value of q: '))
        x = a/q
        print(x/2)

    def diagonal_q():
        a = float(input('enter the value of a: '))
        q = float(input('enter the value of p: '))
        x = a/q
        print(x/2)

    def area():
        a = float(input('enter the value of a:'))
        print(4*a)

    def side():
        p = float(input('enter the value of p: '))
        q = float(input('enter the value of q: '))
        x = p*p
        y = q*q
        z = sqrt(x+y)
        p(z/2)

class Right_triangle():
    def area():
        a = float(input('enter the value of a: '))
        b = float(input('enter the value of b: '))
        x = a*b
        print(x/2)

    def base():
        c = float(input('enter the value of c: '))
        y = float(input('enter the value of y: '))
        x = cos(y)
        print(x*c)

    def gamma():
        a = float(input('enter the value of a: '))
        c = float(input('enter the value of c: '))
        x = a/c
        print(asin(x))

    def hyp():
        a = float(input('enter the value of a: '))
        b = float(input('enter the value of b: '))
        x = a*a
        y = b*b
        print(sqrt(x+y))

    def perimeter():
        a = float(input('enter the value of a: '))
        b = float(input('enter the value of b: '))
        c = float(input('enter the value of c: '))
        print(a+b+c)

    def side():
        c = float(input('enter the value of c: '))
        y = float(input('enter the value of y: '))
        x = sin(y)
        print(x*c)

class Sphere:
    def diameter():
        d = float(input('enter the value of r: '))
        print(2*d)

    def radius():
        a = float(input('enter the value of a: '))
        x = sqrt(a/pi)
        print(x/2)

    def surface_area():
        r = float(input('enter the value of r: '))
        print(4*pi*r*r)

    def volume():
        r = float(input('enter the value of r: '))
        a = 4*pi*r*r*r
        print(a/3)

class Square:
    def area():
        a = float(input('enter the value of a: '))
        print(a*a)

    def diagonal():
        a = float(input('enter the value of a: '))
        b = sqrt(2)
        print(a*b)

    def perimeter():
        a = float(input('enter the value of a: '))
        print(4*a)

    def side():
        a = float(input('enter the value of a: '))
        print(sqrt(a))

class Tetrahedron:
    def edge():
        a = float(input('enter the value of a: '))
        x = sqrt(a)
        y = sqrt(sqrt(y))
        print(x/y)

    def face_area():
        a =float(input('enter the value of a: '))
        x = sqrt(3)
        y = x/4
        print(y*a*a)

    def height():
        a = float(input('enter the value of a: '))
        x = sqrt(2/3)
        print(x*a)

    def surface_area():
        a = float(input('enter the value of a: '))
        x = sqrt(3)
        print(x*a*a)

    def volume():
        a = float(input('enter the value of a: '))
        b = sqrt(2)
        c = a*a*a
        d = 6*b
        print(c/d)

class Trapezoid:
    def area():
        a = float(input('enter the value of a: '))
        b = float(input('enter the value of b: '))
        h = float(input('enter the value of h: '))
        x = a+b
        y = h*x
        print(y/2)

    def base_a():
        a = float(input('enter the value of a: '))
        b = float(input('enter the value of b: '))
        h = float(input('enter the value of h: '))
        x = a/h 
        y = 2*x
        print(y-b)

    def base_b():
        a = float(input('enter the value of A: '))
        b = float(input('enter the value of a: '))
        h = float(input('enter the value of h: '))
        x = a/h 
        y = 2*x
        print(y-b)

    def height():
        aa = float(input('enter the value of A: '))
        a = float(input('enter the value of a: '))
        h = float(input('enter the value of b: '))
        x = 2*aa
        y = a+h
        print(x/y)

    def perimeter():
        a = float(input('enter the value of A: '))
        b = float(input('enter the value of a: '))
        c = float(input('enter the value of h: '))
        d = float(input('enter the value of A: '))
        print(a+b+c+d)

    def side_c:
        p = float(input('enter the value of p: '))
        a = float(input('enter the value of a: '))
        b = float(input('enter the value of b: '))
        c = float(input('enter the value of d: '))
        print(p-a-b-c)

    def side_d():
        p = float(input('enter the value of p: '))
        a = float(input('enter the value of a: '))
        b = float(input('enter the value of b: '))
        c = float(input('enter the value of c: '))
        print(p-a-b-c)

class Triangle:
    def area():
        h = float(input('enter the value of h: '))
        b = float(input('enter the value of b: '))
        x = h*b
        print(x/2)

    def base():
        a = float(input('enter the value of a: '))
        h = float(input('enter the value of h: '))
        x = a/h 
        print(2*x)

    def gamma():
        a = float(input('enter the value of A: '))
        b = float(input('enter the value of a: '))
        c = float(input('enter the value of b: '))
        d = b*c
        e = 2*a
        f = d*e
        print(asin(f))

    def height():
        a = float(input('enter the value of a: '))
        h = float(input('enter the value of b: '))
        x = a/h 
        print(2*x)

    def perimeter():
        a = float(input('enter the value of a: '))
        b = float(input('enter the value of b: '))
        h = float(input('enter the value of c: '))
        print(a+b+h)

    def side_a():
        a = float(input('enter the value of A: '))
        b = float(input('enter the value of b: '))
        c = float(input('enter the value of y: '))
        x = b*sin(c)
        y = 2*a
        print(x*y)

    def side_c():
        a = float(input('enter the value of P: '))
        b = float(input('enter the value of a: '))
        c = float(input('enter the value of b: '))
        print(p-a-b)

class Triangle_prism:
    def lateral_surface():
        a = float(input('enter the value of a: '))
        b = float(input('enter the value of b: '))
        c = float(input('enter the value of c: '))
        h = float(input('enter the value of h: '))
        x = a+b+c
        print(x*h)

    def surface_area():
        a = float(input('enter the value of a: '))
        b = float(input('enter the value of b: '))
        c = float(input('enter the value of c: '))
        h = float(input('enter the value of h: '))
        x = h*b
        y = a+b+c
        print(x*h*y)

    def volume():
        a = float(input('enter the value of a: '))
        b = float(input('enter the value of b: '))
        c = float(input('enter the value of c: '))
        h = float(input('enter the value of h: '))
        x = 1/4*h
        y = a*a
        z = b*b
        p = c*c
        q = y+z+p
        print(x*q)