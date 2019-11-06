import classPata
import numpy as np


class Modulo:
    # Atributos de la clase Modulo
    traslacionY = 138

    def __init__(self, motor10, motor11, motor12, ventosa1, motor20, motor21, motor22, ventosa2, clientID):
        self.Pata1 = classPata.Pata(motor10, motor11, motor12, ventosa1, clientID)
        self.Pata2 = classPata.Pata(motor20, motor21, motor22, ventosa2, clientID)

        # los modulos tienen asociados dos matrices de transformacion homogenea, una por pata.
        self.MTH1 = [[-1, 0, 0, 0], [0, -1, 0, -138], [0, 0, 1, 0], [0, 0, 0, 1]]
        self.MTH2 = [[1, 0, 0, 0], [0, 1, 0, 138], [0, 0, 1, 0], [0, 0, 0, 1]]

    def setPosition(self, pata, position, ElbPos, time):

        posModulo = np.transpose(np.array([position[0], position[1], position[2], 1]))  # funcion para traspuesta de una matriz

        if pata == 1:
            posPata = np.dot(np.linalg.inv(self.MTH1),
                             posModulo)  # funcion de multiplicacion de matrices y de inversion de matrices
            self.Pata1.setPosition(posPata[0], posPata[1], posPata[2], ElbPos, time)

        if pata == 2:
            posPata = np.dot(np.linalg.inv(self.MTH2),
                             posModulo)  # funcion de multiplicacion de matrices y de inversion de matrices
            self.Pata2.setPosition(posPata[0], posPata[1], posPata[2], ElbPos, time)

    def setAngles(self, pata, q1, q2, q3):

        if pata == 1:
            self.Pata1.setAngles(q1, q2, q3)

        if pata == 2:
            self.Pata2.setAngles(q1, q2, q3)

    def getPosition(self, pata):
        vecPos = []

        if pata == 1:
            vecPos = self.Pata1.getPosition()
            vecPos.append(1)
            vecPos = np.dot(self.MTH1, np.transpose(vecPos))

        if pata == 2:
            vecPos = self.Pata2.getPosition()
            vecPos.append(1)
            vecPos = np.dot(self.MTH2, np.transpose(vecPos))

        return vecPos
