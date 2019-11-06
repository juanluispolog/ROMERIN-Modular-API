import math
import classJoint as motor
from enum import Enum

import vrep

class Pata:

    #Definicion de constantes
    L1Z = 41
    L1Y = 37
    L2 = 113.1
    L3 = 180.16 + 50.26
    NUMERO_PUNTOS = 10

    class ElbowPos(Enum):
        ElbUp = 1
        ElbDown = 2

    # Funcion que coge el valor de los handle de los motores para cada pata
    def __init__(self, name0, name1, name2, ventosa, clientID):
        self.clientID = clientID

        self.m0 = motor.Joint(0)
        self.m1 = motor.Joint(65)
        self.m2 = motor.Joint(-140)

        self.m0.setJointHandle(name0)
        self.m1.setJointHandle(name1)
        self.m2.setJointHandle(name2)

        self.m0.setClientID(clientID)
        self.m1.setClientID(clientID)
        self.m2.setClientID(clientID)

        self.vectorAngles = []

        self.vectorAngles.append(self.m0.position)
        self.vectorAngles.append(self.m1.position)
        self.vectorAngles.append(self.m2.position)

        self.vectorPosition = []

        self.ventosa = ventosa

        vrep.simxSynchronousTrigger(clientID)

    #Cinematica Directa
    def getFK_pos(self, angles):
        q1 = -math.radians(angles[0])
        q2 = math.radians(angles[1])
        q3 = -math.radians(angles[1] + angles[2])

        d = Pata.L1Y + Pata.L2 * math.cos(q2) + Pata.L3 * math.cos(q3)

        x = d * math.sin(q1)
        y = d * math.cos(q1)
        z = Pata.L2 * math.sin(q2) - Pata.L3 * math.sin(q3) - Pata.L1Z

        self.vectorPosition = [x, y, z]

    #Cinematica Inversa
    def getIK_angles(self, position, ElbPos):
        x = - position[0]
        y = position[1]
        if ElbPos == 1:
            z = position[2] + Pata.L1Z
        if ElbPos == 2:
            z = (position[2] - Pata.L1Z)
        d = math.sqrt(x ** 2 + y ** 2)
        D = d - Pata.L1Y
        L = math.sqrt(D ** 2 + z ** 2)
        B = math.acos((L ** 2 - Pata.L2 ** 2 - Pata.L3 ** 2) / (-2 * Pata.L2 * Pata.L3))

        q1 = math.atan2(x, y)
        if ElbPos == 1:
            q3_aux = B - math.pi
            alpha = math.atan2(Pata.L3 * math.sin(q3_aux), Pata.L3 * math.cos(q3_aux) + Pata.L2)
            beta = math.atan2(z, D)
            q2 = beta - alpha
            q3 = q3_aux
            #print(math.degrees(alpha), math.degrees(beta), math.degrees(B))

        if ElbPos == 2:
            q3_aux = -(B - math.pi)
            alpha = math.atan2(Pata.L3 * math.sin(q3_aux), Pata.L3 * math.cos(q3_aux) + Pata.L2)
            beta = math.atan2(z, -D)
            q2 = (beta - alpha)
            q3 = q3_aux
            #print(math.degrees(alpha), math.degrees(beta), math.degrees(B))

        q1 = math.degrees(q1)
        q2 = math.degrees(q2)
        q3 = math.degrees(q3)

        self.vectorAngles = [q1, q2, q3]


    def setPosition(self, x, y, z, ElbPos, time):
        self.vectorPosition = [x, y, z]

        #angles = self.getAngles()
        self.getIK_angles(self.vectorPosition, ElbPos)
        print(self.vectorAngles)

        #v1 = (self.vectorAngles[0] - angles[0]) *(math.pi/180) / (time/1000)
        #v2 = (self.vectorAngles[1] - angles[1]) *(math.pi/180) / (time /1000)
        #v3 = (self.vectorAngles[2] - angles[2]) *(math.pi/180) / (time/1000)
        #print(v1, v2, v3)

        #self.setVelocity(v1, v2, v3)
        #self.m0.setJointVelocity(v1, 21)
        self.m0.setJointPosition(self.vectorAngles[0])
        #self.m0.setJointVelocity(v2, 22)
        self.m1.setJointPosition(self.vectorAngles[1])
        #self.m0.setJointVelocity(v3, 23)
        self.m2.setJointPosition(self.vectorAngles[2])


    def getPosition(self):
        self.m0.getJointPosition()
        self.m1.getJointPosition()
        self.m2.getJointPosition()

        self.vectorAngles = [self.m0.position, self.m1.position, self.m2.position]
        self.getFK_pos(self.vectorAngles)

        return self.vectorPosition


    def setAngles(self, a0, a1, a2):
        self.vectorAngles = [a0, a1, a2]

        self.m0.setJointPosition(self.vectorAngles[0])
        self.m1.setJointPosition(self.vectorAngles[1])
        self.m2.setJointPosition(self.vectorAngles[2])

    def getAngles(self):

        self.m0.getJointPosition()
        self.m1.getJointPosition()
        self.m2.getJointPosition()

        self.vectorAngles = [self.m0.position, self.m1.position, self.m2.position]

        return self.vectorAngles


    def setVelocity(self, v0, v1, v2):
        if v0 != -1:
            self.m0.setJointVelocity(v0, 21)
        if v1 != -1:
            self.m1.setJointVelocity(v1, 22)
        if v2 != -1:
            self.m2.setJointVelocity(v2, 23)


    def setGripper(self, active):
        vrep.simxSetIntegerSignal(self.clientID, self.ventosa, active,
                                                                vrep.simx_opmode_oneshot)  # Activacion de la ventosa

        #vrep.simxSynchronousTrigger(self.clientID)


    def getGripper(self):
        return
