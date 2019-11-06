import math
try:
    import vrep
except:
    print('--------------------------------------------------------------')


class Joint:

    #Atributos
    handle = 0
    position = 0
    velocity = 0
    clientID = 0

    def __init__(self, position):
        self.position = position

    def setClientID(self, clientID):
        self.clientID = clientID
        vrep.simxSynchronousTrigger(self.clientID)

    def setJointHandle(self, name):
        r, self.handle = vrep.simxGetObjectHandle(self.clientID, name, vrep.simx_opmode_oneshot_wait)
        vrep.simxSynchronousTrigger(self.clientID)

    def setJointPosition(self, pos):
        self.position = pos
        vrep.simxSetJointTargetPosition(self.clientID, self.handle, pos * math.pi/180, vrep.simx_opmode_oneshot)

    # def setJointVelocity(self, vel):
    #     self.velocity = vel
    #     ret = vrep.simxSetObjectFloatParameter(self.clientID, self.handle, vrep.sim_jointfloatparam_upper_limit, self.velocity,
    #                                                                    vrep.simx_opmode_oneshot)

    def setJointVelocity(self, vel, motor):
        res1, retInts1, real, retStrings1, retBuffer1 = vrep.simxCallScriptFunction(self.clientID,
                                                                                    "modulo_body_visible",
                                                                                    vrep.sim_scripttype_childscript,
                                                                                    "velocidad", [motor], [vel], [],
                                                                                    bytearray(),
                                                                                    vrep.simx_opmode_blocking)

    def getJointPosition(self):
        ret, pos = vrep.simxGetJointPosition(self.clientID, self.handle, vrep.simx_opmode_streaming)
        self.position = math.degrees(pos)
        vrep.simxSynchronousTrigger(self.clientID)




