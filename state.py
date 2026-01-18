import numpy as np

class CognitiveState:
    def analyze(self, eeg):
        load = float(np.mean(np.abs(eeg)))
        fatigue = float(np.var(eeg))

        cli = 0.6 * load + 0.4 * fatigue

        return {
            "load": load,
            "fatigue": fatigue,
            "cli": cli,
            "state": self.label_state(load, fatigue)
        }

    def label_state(self, load, fatigue):
        if fatigue > 1.2:
            return "overloaded"
        if load < 0.25:
            return "understimulated"
        return "focused"
