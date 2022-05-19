class EWheel:
    '''
        An "electric current wheel" based on Ohm's law is implemented in this class.
        Calculations are made in the international system of units..
    '''

    # watts_...
    @staticmethod
    def watts_volts(power: float, voltage: float):
        if power == 0 and voltage != 0:
            return {'U': float(voltage), 'R': (voltage ** 2) * float('inf'), 'I': float(power / voltage),
                    'P': float(power)}
        elif power != 0 and voltage == 0:
            return {'U': float(voltage), 'R': float((voltage ** 2) / power), 'I': power * float('inf'),
                    'P': float(power)}
        elif power == 0 and voltage == 0:
            return {'U': float(voltage), 'R': (voltage ** 2) * float('inf'), 'I': power * float('inf'),
                    'P': float(power)}
        else:
            return {'U': float(voltage), 'R': float((voltage ** 2) / power), 'I': float(power / voltage),
                    'P': float(power)}

    @staticmethod
    def watts_ohms(power: float, resistance: float):
        if (power < 0 or resistance < 0) and (power >= 0 or resistance >= 0):
            return {'U': float('nan'), 'R': float(resistance), 'I': float('nan'),
                    'P': float(power)}
        else:
            if resistance == 0:
                return {'U': float((power * resistance) ** 0.5), 'R': float(resistance), 'I': power * float('inf'),
                        'P': float(power)}
            return {'U': float((power * resistance) ** 0.5), 'R': float(resistance),
                    'I': float((power / resistance) ** 0.5),
                    'P': float(power)}

    @staticmethod
    def watts_amps(power: float, amperage: float):
        if amperage == 0:
            return {'U': power * float('inf'), 'R': power * float('inf'), 'I': float(amperage), 'P': float(power)}
        return {'U': float(power / amperage), 'R': float(power / (amperage ** 2)), 'I': float(amperage),
                'P': float(power)}

    # volts_...
    @staticmethod
    def volts_watts(voltage: float, power: float):
        if power == 0 and voltage != 0:
            return {'U': float(voltage), 'R': (voltage ** 2) * float('inf'), 'I': float(power / voltage),
                    'P': float(power)}
        elif power != 0 and voltage == 0:
            return {'U': float(voltage), 'R': float((voltage ** 2) / power), 'I': power * float('inf'),
                    'P': float(power)}
        elif power == 0 and voltage == 0:
            return {'U': float(voltage), 'R': (voltage ** 2) * float('inf'), 'I': power * float('inf'),
                    'P': float(power)}
        else:
            return {'U': float(voltage), 'R': float((voltage ** 2) / power), 'I': float(power / voltage),
                    'P': float(power)}

    @staticmethod
    def volts_ohms(voltage: float, resistance: float):
        if resistance == 0:
            return {'U': float(voltage), 'R': float(resistance), 'I': voltage * float('inf'),
                    'P': (voltage ** 2) * float('inf')}
        return {'U': float(voltage), 'R': float(resistance), 'I': float(voltage / resistance),
                'P': float((voltage ** 2) / resistance)}

    @staticmethod
    def volts_amps(voltage: float, amperage: float):
        if amperage == 0:
            return {'U': float(voltage), 'R': voltage * float('inf'), 'I': float(amperage),
                    'P': float(voltage * amperage)}
        return {'U': float(voltage), 'R': float(voltage / amperage), 'I': float(amperage),
                'P': float(voltage * amperage)}

    # ohms_...
    @staticmethod
    def ohms_watts(resistance: float, power: float):
        if (power < 0 or resistance < 0) and (power >= 0 or resistance >= 0):
            return {'U': float('nan'), 'R': float(resistance), 'I': float('nan'),
                    'P': float(power)}
        else:
            if resistance == 0:
                return {'U': float((power * resistance) ** 0.5), 'R': float(resistance), 'I': power * float('inf'),
                        'P': float(power)}
            return {'U': float((power * resistance) ** 0.5), 'R': float(resistance),
                    'I': float((power / resistance) ** 0.5),
                    'P': float(power)}

    @staticmethod
    def ohms_volts(resistance: float, voltage: float):
        if resistance == 0:
            return {'U': float(voltage), 'R': float(resistance), 'I': voltage * float('inf'),
                    'P': (voltage ** 2) * float('inf')}
        return {'U': float(voltage), 'R': float(resistance), 'I': float(voltage / resistance),
                'P': float((voltage ** 2) / resistance)}

    @staticmethod
    def ohms_amps(resistance: float, amperage: float):
        return {'U': float(resistance * amperage), 'R': float(resistance), 'I': float(amperage),
                'P': float((amperage ** 2) * resistance)}

    # amps_...
    @staticmethod
    def amps_watts(amperage: float, power: float):
        if amperage == 0:
            return {'U': power * float('inf'), 'R': power * float('inf'), 'I': float(amperage),
                    'P': float(power)}
        return {'U': power / amperage, 'R': power / (amperage ** 2), 'I': float(amperage),
                'P': float(power)}

    @staticmethod
    def amps_volts(amperage: float, voltage: float):
        if amperage == 0:
            return {'U': float(voltage), 'R': voltage * float('inf'), 'I': float(amperage),
                    'P': float(voltage * amperage)}
        return {'U': float(voltage), 'R': float(voltage / amperage), 'I': float(amperage),
                'P': float(voltage * amperage)}

    @staticmethod
    def amps_ohms(amperage: float, resistance: float):
        return {'U': float(resistance * amperage), 'R': float(resistance), 'I': float(amperage),
                'P': float((amperage ** 2) * resistance)}
