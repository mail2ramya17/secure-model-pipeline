# Secure Model Pipeline (ModelScan + Trivy + Cosign + OPA)

Shows how an ML model gets from training to the registry **only if it is safe**:

1. **ModelScan** — blocks pickled models with code-execution payloads
2. **Trivy** — scans the serving container
3. **Cosign** — signs the image (keyless, GitHub OIDC)
4. **OPA/Rego** — policy check on the deployment manifest

## Run locally
```bash
pip install -r requirements.txt
python train.py                     # creates model/model.pkl
modelscan -p model/model.pkl        # should be clean
python make_malicious_model.py      # creates a booby-trapped pickle (harmless: echo)
modelscan -p model/evil.pkl         # flagged CRITICAL
```
Then delete `model/evil.pkl` before you push, or the pipeline will (correctly) fail.

Policy test (install `opa` from openpolicyagent.org):
```bash
opa eval -d policy/deploy.rego -i policy/sample_deploy.json "data.deploy.deny"
```
