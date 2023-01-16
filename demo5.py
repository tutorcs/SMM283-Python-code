https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
from __future__ import print_function
##START
print("0123456789012345678901234567")
print("No#".ljust(5), "Trader".ljust(20), "CAP".rjust(3))
print("1".ljust(5), "Ryan Bonds".ljust(20), "45M".rjust(3))
print("2".ljust(5), "Barry Safe".ljust(20), "70M".rjust(3))
print("3".ljust(5), "Vera Silver".ljust(20), "80M".rjust(3))

print("\n\n")

print("0123456789012345678901234567")
print("{0:<5s}{1:<20s}{2:>3s}".format("No#", "Trader", "CAP"))
print("{0:<5s}{1:<20s}{2:>3s}".format("1", "Ryan Bonds", "45M"))
print("{0:<5s}{1:<20s}{2:>3s}".format("2", "Barry Safe", "70M"))
print("{0:<5s}{1:<20s}{2:>3s}".format("3", "Vera Silver", "80M"))


print("\n\n")

print("0123456789012345678901234567")
##using legacy C formatting...
print("%-5s%-20s%3s" % ("No#", "Trader", "CAP"))
print("%-5s%-20s%3s" % ("1", "Ryan Bonds", "45M"))
print("%-5s%-20s%3s" % ("2", "Barry Safe", "70M"))
print("%-5s%-20s%3s" % ("3", "Vera Silver", "80M"))
##END
