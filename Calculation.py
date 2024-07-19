KWh = 0.05
CP = 32
EE = 20
BTC = 100000
POOL = 0.00000081


C1 = KWh * 24 * CP * EE / BTC / 1000
C2 = CP * 0.0089 / BTC
PR = CP * POOL
RW = PR - C1 - C2

Value = BTC * RW

print(Value)
