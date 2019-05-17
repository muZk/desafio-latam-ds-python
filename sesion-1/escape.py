import sys

if len(sys.argv) > 2:
    gravity = float(sys.argv[1])
    radius = float(sys.argv[2])
    escape_velocity = (2 * gravity * radius * 1000) ** (0.5)
    print(escape_velocity)
