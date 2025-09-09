import math
print("Detta program räknar ut din motors volym: ps håll dig till cm:")
radie = float(input("Skriv din motors första cylinder's radie:"))
cylinder =float(input("Hur hög är motorns första cylinder? "))
motortyp =float(input("Hur många cylindrar har din motor?"))

cylinder_volume = pow(radie, 2)
cylinder_volume2 = cylinder_volume * math.pi
cylinder_volume3 = cylinder_volume2 * cylinder
engine_volume = cylinder_volume3 * motortyp

print(f"Din motorvolym är: {engine_volume} cm^3")


