# AUTOR: Juan Luis Polo Garzon

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

    time.sleep(4)
    # llamada a la funcion de activar ventosas
    res1, retInts1, retFloats1, retStrings1, retBuffer1 = vrep.simxCallScriptFunction(clientID, "modulo_body_visible",
                                                                                      vrep.sim_scripttype_childscript,
                                                                                      "activar", [], [], [],
                                                                                      bytearray(),
                                                                                      vrep.simx_opmode_blocking)

    time.sleep(5)

    # llamada a la funcion de activar ventosas: prueba 1
    res1, retInts1, retFloats1, retStrings1, retBuffer1 = vrep.simxCallScriptFunction(clientID, "modulo_body_visible",
                                                                                      vrep.sim_scripttype_childscript,
                                                                                      "prueba1", [], [], [],
                                                                                      bytearray(),
                                                                                      vrep.simx_opmode_blocking)

    time.sleep(5)

    # llamada a la funcion de activar ventosas: prueba 2
    res1, retInts1, retFloats1, retStrings1, retBuffer1 = vrep.simxCallScriptFunction(clientID, "modulo_body_visible",
                                                                                      vrep.sim_scripttype_childscript,
                                                                                      "prueba2", [], [], [],
                                                                                      bytearray(),
                                                                                      vrep.simx_opmode_blocking)

    time.sleep(5)

    # llamada a la funcion de activar ventosas: prueba 3
    res1, retInts1, retFloats1, retStrings1, retBuffer1 = vrep.simxCallScriptFunction(clientID, "modulo_body_visible",
                                                                                      vrep.sim_scripttype_childscript,
                                                                                      "prueba3", [], [], [],
                                                                                      bytearray(),
                                                                                      vrep.simx_opmode_blocking)

    time.sleep(5)

    # llamada a la funcion de activar ventosas: prueba 3
    res1, retInts1, retFloats1, retStrings1, retBuffer1 = vrep.simxCallScriptFunction(clientID, "modulo_body_visible",
                                                                                      vrep.sim_scripttype_childscript,
                                                                                      "prueba4", [], [], [],
                                                                                      bytearray(),
                                                                                      vrep.simx_opmode_blocking)

else:
    sys.exit('Error: no se puede conectar')
    vrep.simxFinish(clientID)
