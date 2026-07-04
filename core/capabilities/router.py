class CapabilityRouter:

    def __init__(self):
        self.capabilities = {}

    def register(self, name, capability):
        self._capabilities[name] = capability

    def get(self, name):
        return self._capabilities[name]