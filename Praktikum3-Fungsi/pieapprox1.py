import series
import userinput

n = userinput.get(3,10)
print(f"{n}-th approximation of pi is {series.pi_approx(n)}")
print(f"{n}-th approximation of e is {series.e_approx(n)}")