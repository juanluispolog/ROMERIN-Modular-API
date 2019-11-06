# AUTOR: Juan Luis Polo Garzon

# En este archivo se implementa la prueba de la cinematica del robot

# Se indica el numero de la pata sobre la que se quiere probar la cinematica y el punto al que se le quiere enviar
# medido desde el centro del modulo
#

import classModulo
import vrep
import sys
import time
#import subprocess



vrep.simxFinish(-1)
clientID = vrep.simxStart('127.0.0.1', 19999, True, True, 5000, 5)
vrep.simxSynchronous(clientID,True)

if clientID != -1:
    print('Conectado con VREP')
    print("")

    modulo1 = classModulo.Modulo('modulo_joint11', 'modulo_joint12', 'modulo_joint13', 'BaxterVacuumCup1_active',
                                 'modulo_joint21', 'modulo_joint22', 'modulo_joint23', 'BaxterVacuumCup2_active', clientID)

    modulo2 = classModulo.Modulo('modulo_joint11#0', 'modulo_joint12#0', 'modulo_joint13#0', 'BaxterVacuumCup1#0_active',
                                 'modulo_joint21#0', 'modulo_joint22#0', 'modulo_joint23#0', 'BaxterVacuumCup2#0_active', clientID)

    modulo3 = classModulo.Modulo('modulo_joint11#1', 'modulo_joint12#1', 'modulo_joint13#1', 'BaxterVacuumCup1#1_active',
                                 'modulo_joint21#1', 'modulo_joint22#1', 'modulo_joint23#1', 'BaxterVacuumCup2#1_active', clientID)

    vrep.simxSynchronousTrigger(clientID)

    # lectura inicial, para inicializar los valores en V-REP
    res = modulo1.getPosition(1)
    vrep.simxSynchronousTrigger(clientID)
    res = modulo1.getPosition(2)
    vrep.simxSynchronousTrigger(clientID)
    res = modulo2.getPosition(1)
    vrep.simxSynchronousTrigger(clientID)
    res = modulo2.getPosition(2)
    vrep.simxSynchronousTrigger(clientID)
    res = modulo3.getPosition(1)
    vrep.simxSynchronousTrigger(clientID)
    res = modulo3.getPosition(2)
    vrep.simxSynchronousTrigger(clientID)

    # desactivar ventosas
    res1, retInts1, retFloats1, retStrings1, retBuffer1 = vrep.simxCallScriptFunction(clientID, "modulo_body_visible",
                                                                                      vrep.sim_scripttype_childscript,
                                                                                      "desactivar", [], [], [],
                                                                                      bytearray(),
                                                                                      vrep.simx_opmode_blocking)

    # se envia la posicion inicial a las patas
    modulo3.setAngles(1, 0, 60, -140)
    modulo2.setAngles(1, 0, 60, -140)
    modulo1.setAngles(1, 0, 60, -140)
    modulo3.setAngles(2, 0, 60, -140)
    modulo2.setAngles(2, 0, 0, 0)
    modulo1.setAngles(2, 0, 60, -140)


    res1, retInts1, info, retStrings1, retBuffer1 = vrep.simxCallScriptFunction(clientID,
                                                                                "modulo_body_visible",
                                                                                vrep.sim_scripttype_childscript,
                                                                                "activar", [], [], [],
                                                                                bytearray(),
                                                                                vrep.simx_opmode_blocking)

    while True:
        #pata = int(input("Pata a mover (1, 2): "))
        x = float(input("Dame x:  "))
        y = float(input("Dame y:  "))
        z = float(input("Dame z:  "))
        #ElbPos = int(input("Dame ElbPos:  "))
        #t = int(input("Dame time (ms):  "))

        modulo2.setPosition(2, [x, y, z], 1, 1)
        time.sleep(1)
        vrep.simxSynchronousTrigger(clientID)


        if int(input("Quieres seguir probando?:  ")) != 1:
                modulo2.setAngles(2, 0, 0, 0)
                break
        print("----------------------------")

    vrep.simxSynchronousTrigger(clientID)
    vrep.simxFinish(-1)




else:
    sys.exit('Error: no se puede conectar')
    vrep.simxFinish(clientID)
