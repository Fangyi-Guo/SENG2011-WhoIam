class Blood:

    def __init__(self, bloodId, volume, type, donor, disposedTime, takenTime):
        self._bloodId = bloodId
        self._volume  = volume
        self._type = type
        self._donor  = donor
        self._disposedTime = disposedTime
        self._isTest = False
        self._takenTime = takenTime
    

    @property
    def volumn(self):
        return self._volumn

    @volumn.setter
    def volumn(self, takenVolumn):
        self._volumn -= takenVolumn

    @property
    def type(self):
        return self._type

    @property
    def donor(self):
        return self._donor

    @property
    def disposedTime(self):
        return self._disposedTime

    @property
    def bloodId(self):
        return self._bloodId

    @property
    def takenTime(self):
        return self._takenTime

    @property
    def isTest(self):
        return self._isTest

    @_isTest.setter
    def isTest(self):
        self._isTest = True


