import vrep
import time
import matplotlib.pyplot as python_plot
import math
import sys

vrep.simxFinish(-1)
clientID = vrep.simxStart('127.0.0.1', 20001, True, True, 5000, 5)
vrep.simxSynchronous(clientID, True)

if clientID != -1:

    print('Connected with VREP')
    print("")

    FuerzaX1 = []
    FuerzaY1 = []
    FuerzaZ1 = []

    FuerzaX2 = []
    FuerzaY2 = []
    FuerzaZ2 = []

    FuerzaX10 = []
    FuerzaY10 = []
    FuerzaZ10 = []

    FuerzaX20 = []
    FuerzaY20 = []
    FuerzaZ20 = []

    FuerzaX11 = []
    FuerzaY11 = []
    FuerzaZ11 = []

    FuerzaX21 = []
    FuerzaY21 = []
    FuerzaZ21 = []

    t = []
    t0 = time.time()

    while (vrep.simxGetConnectionId(clientID)) == 1:

        res1, retInts1, infovent, retStrings1, retBuffer1 = vrep.simxCallScriptFunction(clientID,
                                                                                             "modulo_body_visible",
                                                                                             vrep.sim_scripttype_childscript,
                                                                                             "info_ventosas", [], [], [],
                                                                                             bytearray(),
                                                                                             vrep.simx_opmode_blocking)
        if (infovent == [] or (time.time()-t0) > 20):
            break
        vrep.simxSynchronousTrigger(clientID)

        print(infovent)

        # Suction pad 1
        FuerzaX1.append(infovent[0])
        FuerzaY1.append(math.sqrt(infovent[1]*infovent[1] + infovent[0]*infovent[0]))
        FuerzaZ1.append(infovent[2])

        # Suction pad 2
        FuerzaX2.append(infovent[3])
        FuerzaY2.append(math.sqrt(infovent[4] * infovent[4] + infovent[3] * infovent[3]))
        FuerzaZ2.append(infovent[5])

        # Suction pad 3
        FuerzaX10.append(infovent[6])
        FuerzaY10.append(math.sqrt(infovent[7] * infovent[7] + infovent[6] * infovent[6]))
        FuerzaZ10.append(infovent[8])

        # Suction pad 4
        FuerzaX20.append(infovent[9])
        FuerzaY20.append(math.sqrt(infovent[10]*infovent[10] + infovent[9]*infovent[9]))
        FuerzaZ20.append(infovent[11])

        # Suction pad 5
        FuerzaX11.append(infovent[12])
        FuerzaY11.append(math.sqrt(infovent[13]*infovent[13] + infovent[12]*infovent[12]))
        FuerzaZ11.append(infovent[14])

        # Suction pad 6
        FuerzaX21.append(infovent[15])
        FuerzaY21.append(math.sqrt(infovent[16] * infovent[16] + infovent[15] * infovent[15]))
        FuerzaZ21.append(infovent[17])

        vrep.simxSynchronousTrigger(clientID)
        t.append(time.time()-t0)


    # Plot the data suction pad 1
    python_plot.figure(1)

    python_plot.plot(t, FuerzaZ1, 'b-', label='Fuerza Normal')
    python_plot.plot(t, FuerzaY1, 'r-', label='Fuerza Cortante')
    #python_plot.plot(t, FuerzaZ1, 'b-', label='FuerzaZ')

    python_plot.legend()
    python_plot.xlabel('Tiempo (s)')
    python_plot.ylabel('Fuerza (N)')
    python_plot.title('Fuerza ventosa 1')

    python_plot.grid(True)
    python_plot.show()




    # Plot the data suction pad 2
    python_plot.figure(1)

    python_plot.plot(t, FuerzaZ2, 'b-', label='Fuerza Normal')
    python_plot.plot(t, FuerzaY2, 'r-', label='Fuerza Cortante')
    # python_plot.plot(t, FuerzaZ1, 'b-', label='FuerzaZ')

    python_plot.legend()
    python_plot.xlabel('Tiempo (s)')
    python_plot.ylabel('Fuerza (N)')
    python_plot.title('Fuerza ventosa 2')

    python_plot.grid(True)
    python_plot.show()




    # Plot the data suction pad 3
    python_plot.figure(1)

    python_plot.plot(t, FuerzaZ10, 'b-', label='Fuerza Normal')
    python_plot.plot(t, FuerzaY10, 'r-', label='Fuerza Cortante')
    # python_plot.plot(t, FuerzaZ1, 'b-', label='FuerzaZ')

    python_plot.legend()
    python_plot.xlabel('Tiempo (s)')
    python_plot.ylabel('Fuerza (N)')
    python_plot.title('Fuerza ventosa 3')

    python_plot.grid(True)
    python_plot.show()




    # Plot the data suction pad 4
    python_plot.figure(1)

    python_plot.plot(t, FuerzaZ20, 'b-', label='Fuerza Normal')
    python_plot.plot(t, FuerzaY20, 'r-', label='Fuerza Cortante')
    #python_plot.plot(t, FuerzaZ10, 'b-', label='FuerzaZ')

    python_plot.legend()
    python_plot.xlabel('Tiempo (s)')
    python_plot.ylabel('Fuerza (N)')
    python_plot.title('Fuerza ventosa 4')

    python_plot.grid(True)
    python_plot.show()




    # Plot the data suction pad 5
    python_plot.figure(1)

    python_plot.plot(t, FuerzaZ11, 'b-', label='Fuerza Normal')
    python_plot.plot(t, FuerzaY11, 'r-', label='Fuerza Cortante')
    #python_plot.plot(t, FuerzaZ11, 'b-', label='FuerzaZ')

    python_plot.legend()
    python_plot.xlabel('Tiempo (s)')
    python_plot.ylabel('Fuerza (N)')
    python_plot.title('Fuerza ventosa 5')

    python_plot.grid(True)
    python_plot.show()




    # Plot the data suction pad 6
    python_plot.figure(1)

    python_plot.plot(t, FuerzaZ21, 'b-', label='Fuerza Normal')
    python_plot.plot(t, FuerzaY21, 'r-', label='Fuerza Cortante')
    # python_plot.plot(t, FuerzaZ1, 'b-', label='FuerzaZ')

    python_plot.legend()
    python_plot.xlabel('Tiempo (s)')
    python_plot.ylabel('Fuerza (N)')
    python_plot.title('Fuerza ventosa 6')

    python_plot.grid(True)
    python_plot.show()

    vrep.simxFinish(-1)

    f = open('ventosas.txt', 'w')
    f.write(" ".join(str(x) for x in FuerzaZ1) + '\n')
    f.write(" ".join(str(x) for x in FuerzaY1) + '\n')
    f.write(" ".join(str(x) for x in t) + '\n')
    f.close()

else:
    sys.exit('Error: unable to connect')
    vrep.simxFinish(clientID)
