def m(npt):
 lspeed = 299792458
 e = npt*lspeed**2
 return e
def main():
 npt = int(input('Mass in kilograms:'))
 e = m(npt)
 print(f'The equivalent energy is {e} Joules.')
print = main()