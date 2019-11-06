
#AUTOR: Juan Luis Polo Garzón

#En este archivo se implementa la trayectoria en línea recta del robot

#Son una serie de incrementos previamente medidos que se envían al robot de forma escalonada para
#que realice una trayectoria con la que comprobar que la cinemática implementada no tiene fallos.


import vrep
import sys
import classModulo
import time


vrep.simxFinish(-1)
clientID = vrep.simxStart('127.0.0.1', 19999, True, True, 5000, 5)

if clientID != -1:
    print('Conectado con VREP')
    print("")

    modulo1 = classModulo.Modulo('modulo_joint11', 'modulo_joint12', 'modulo_joint13', 'BaxterVacuumCup1_active',
                                 'modulo_joint21', 'modulo_joint22', 'modulo_joint23', 'BaxterVacuumCup2_active',
                                 clientID)

    modulo2 = classModulo.Modulo('modulo_joint11#0', 'modulo_joint12#0', 'modulo_joint13#0',
                                 'BaxterVacuumCup1#0_active',
                                 'modulo_joint21#0', 'modulo_joint22#0', 'modulo_joint23#0',
                                 'BaxterVacuumCup2#0_active', clientID)

    modulo3 = classModulo.Modulo('modulo_joint11#1', 'modulo_joint12#1', 'modulo_joint13#1',
                                 'BaxterVacuumCup1#1_active',
                                 'modulo_joint21#1', 'modulo_joint22#1', 'modulo_joint23#1',
                                 'BaxterVacuumCup2#1_active', clientID)
    vrep.simxSynchronousTrigger(clientID)

    vector11 = modulo1.getPosition(1)
    vrep.simxSynchronousTrigger(clientID)
    vector12 = modulo1.getPosition(2)
    vrep.simxSynchronousTrigger(clientID)
    vector21 = modulo2.getPosition(1)
    vrep.simxSynchronousTrigger(clientID)
    vector22 = modulo2.getPosition(2)
    vrep.simxSynchronousTrigger(clientID)
    vector31 = modulo3.getPosition(1)
    vrep.simxSynchronousTrigger(clientID)
    vector31 = modulo3.getPosition(2)
    vrep.simxSynchronousTrigger(clientID)


    TIME = 0.6

    p2_1 = [-40, 330, -120]
    p2_2 = [40, 330, -120]
    p2_3 = [40, 330, -160]
    p2_4 = [-40, 330, -160]

    p1_1 = [40, -330, -120]
    p1_2 = [-40, -330, -120]
    p1_3 = [-40, -330, -160]
    p1_4 = [40, -330, -160]


    while True:

        # vrep.simxPauseCommunication(clientID, True)
        # modulo1.Pata1.setGripper(1)
        # modulo1.Pata2.setGripper(0)
        # modulo2.Pata1.setGripper(0)
        # modulo2.Pata2.setGripper(1)
        # modulo3.Pata1.setGripper(1)
        # modulo3.Pata2.setGripper(0)
        # vrep.simxPauseCommunication(clientID, False)

        res1, retInts1, info, retStrings1, retBuffer1 = vrep.simxCallScriptFunction(clientID,
                                                                                    "modulo_body_visible",
                                                                                    vrep.sim_scripttype_childscript,
                                                                                    "activar1", [], [], [],
                                                                                    bytearray(),
                                                                                    vrep.simx_opmode_blocking)
        time.sleep(TIME/4)


        vrep.simxPauseCommunication(clientID, True)
        modulo1.setPosition(1, p1_4, 1, 1)
        modulo1.setPosition(2, p2_1, 1, 1)
        modulo2.setPosition(1, p1_2, 1, 1)
        modulo2.setPosition(2, p2_3, 1, 1)
        modulo3.setPosition(1, p1_4, 1, 1)
        modulo3.setPosition(2, p2_1, 1, 1)
        vrep.simxPauseCommunication(clientID, False)
        vrep.simxSynchronousTrigger(clientID)

        time.sleep(TIME)


        vrep.simxPauseCommunication(clientID, True)
        modulo1.setPosition(1, p1_3, 1, 1)
        modulo1.setPosition(2, p2_2, 1, 1)
        modulo2.setPosition(1, p1_1, 1, 1)
        modulo2.setPosition(2, p2_4, 1, 1)
        modulo3.setPosition(1, p1_3, 1, 1)
        modulo3.setPosition(2, p2_2, 1, 1)
        vrep.simxPauseCommunication(clientID, False)
        vrep.simxSynchronousTrigger(clientID)

        time.sleep(TIME)

        # vrep.simxPauseCommunication(clientID, True)
        # modulo1.Pata1.setGripper(0)
        # modulo1.Pata2.setGripper(1)
        # modulo2.Pata1.setGripper(1)
        # modulo2.Pata2.setGripper(0)
        # modulo3.Pata1.setGripper(0)
        # modulo3.Pata2.setGripper(1)
        # vrep.simxPauseCommunication(clientID, False)

        res1, retInts1, info, retStrings1, retBuffer1 = vrep.simxCallScriptFunction(clientID,
                                                                                    "modulo_body_visible",
                                                                                    vrep.sim_scripttype_childscript,
                                                                                    "activar2", [], [], [],
                                                                                    bytearray(),
                                                                                    vrep.simx_opmode_blocking)
        time.sleep(TIME/4)

        vrep.simxPauseCommunication(clientID, True)
        modulo1.setPosition(1, p1_2, 1, 1)
        modulo1.setPosition(2, p2_3 ,1, 1)
        modulo2.setPosition(1, p1_4, 1, 1)
        modulo2.setPosition(2, p2_1, 1, 1)
        modulo3.setPosition(1, p1_2, 1, 1)
        modulo3.setPosition(2, p2_3, 1, 1)
        vrep.simxPauseCommunication(clientID, False)
        vrep.simxSynchronousTrigger(clientID)

        time.sleep(TIME)


        vrep.simxPauseCommunication(clientID, True)
        modulo1.setPosition(1, p1_1, 1, 1)
        modulo1.setPosition(2, p2_4, 1, 1)
        modulo2.setPosition(1, p1_3, 1, 1)
        modulo2.setPosition(2, p2_2, 1, 1)
        modulo3.setPosition(1, p1_1, 1, 1)
        modulo3.setPosition(2, p2_4, 1, 1)
        vrep.simxPauseCommunication(clientID, False)
        vrep.simxSynchronousTrigger(clientID)

        time.sleep(TIME)


else:
        sys.exit('Error: no se puede conectar')
        vrep.simxFinish(clientID)
