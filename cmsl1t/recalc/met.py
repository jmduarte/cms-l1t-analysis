import math
import numpy as np


def recalcMET(caloTowers, exclude=None):
    metx = []
    ets = []
    phis = []
    for tower in caloTowers:
        # ieta = tower.ieta
        if exclude is not None:
            if exclude(tower):
                continue
        phi = (math.pi / 36.0) * tower.iphi
        et = 0.5 * tower.iet
        ets.append(et)
        phis.append(phi)
    metx = -sum(ets * np.cos(phis))
    mety = -sum(ets * np.sin(phis))
    return (metx, mety)


def l1Met28Only(caloTowers):
    return recalcMET(caloTowers, exclude=lambda tower: not abs(tower.ieta) == 28)

# TODO: find better name


def l1MetNot28(caloTowers):
    return recalcMET(caloTowers, exclude=lambda tower: abs(tower.ieta) >= 28)


def l1MetNot28HF(caloTowers):
    return recalcMET(caloTowers, exclude=lambda tower: abs(tower.ieta) == 28)
