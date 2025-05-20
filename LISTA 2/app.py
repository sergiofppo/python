class Motor:
    def status(self):
        return "Status do Motor: OK"

class Pneu:
    def status(self):
        return "Status do Pneu: OK"

class Veiculo(Motor, Pneu):
    def status(self):
        status_motor = Motor.status(self)
        status_pneu = Pneu.status(self)
        return f"{status_motor} | {status_pneu}"

veiculo = Veiculo()

print(veiculo.status())
