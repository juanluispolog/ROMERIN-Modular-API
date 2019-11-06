import vrep
import sys
import classModulo
import time


vrep.simxFinish(-1)
clientID = vrep.simxStart('127.0.0.1', 19999, True, True, 5000, 5)
vrep.simxSynchronous(clientID, True)

if clientID != -1:
    print('Conectado con VREP')
    print("")

    modulo = classModulo.Modulo('modulo_joint11', 'modulo_joint12', 'modulo_joint13', 'BaxterVacuumCup1_active',
                                 'modulo_joint21', 'modulo_joint22', 'modulo_joint23', 'BaxterVacuumCup2_active',
                                 clientID)


    TIME = 0.5

    p1 = [0, 70, -150]
    p2 = [0, 35, -60]
    p3 = [40, 330, -160]
    p4 = [-40, 330, -160]



    while True:

        vrep.simxPauseCommunication(clientID, True)
        modulo.setAngles(2, 0, 60, -100)
        vrep.simxPauseCommunication(clientID, False)
        vrep.simxSynchronousTrigger(clientID)
        time.sleep(TIME)

        modulo.Pata2.setGripper(0)
        time.sleep(TIME/2)

        vrep.simxPauseCommunication(clientID, True)
        modulo.setAngles(2, 0, 30, -60)
        vrep.simxPauseCommunication(clientID, False)
        vrep.simxSynchronousTrigger(clientID)
        time.sleep(TIME/2)

        modulo.Pata2.setGripper(1)
        time.sleep(TIME)




else:
    sys.exit('Error: no se puede conectar')
    vrep.simxFinish(clientID)