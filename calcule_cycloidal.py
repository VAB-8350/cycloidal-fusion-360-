from math import pi

print('***Formula para cycloidal en fusion***\n')

R = input('inserte radio de rotor en mm:    ')
E = input('inserte exentricidad en mm:    ')
R_r = input('inserte radio de vastagos en mm:    ')
N = input('inserte cantidad de vastagos:    ')

try:
    R = float(R)
    E = float(E)
    R_r = float(R_r)
    N = int(N)

    EN = int(E) * int(N)

    X = "({R}*cos(t))-({R_r}*cos(t+atan(sin((1-{N})*t)/(({R}/{EN})-cos((1-{N})*t)))))-({E}*cos({N}*t))".format(R = R, R_r = R_r, N=N, EN=EN, E=E)

    Y = "(-{R}*sin(t))+({R_r}*sin(t+atan(sin((1-{N})*t)/(({R}/{EN})-cos((1-{N})*t)))))+({E}*sin({N}*t))".format(R = R, R_r = R_r, N=N, EN=EN, E=E)


    print("============================================================================================")
    print('ecuacion de X')
    print(X)
    print('ecuacion de Y')
    print(Y)
    print(pi*2)
    print("============================================================================================")

except:
    print('Los valores ingresados no son validos, ejecute nueva mente para corregirlos')