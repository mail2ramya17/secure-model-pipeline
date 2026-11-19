package deploy

deny contains msg if {
  input.spec.containers[_].securityContext.runAsNonRoot != true
  msg := "containers must run as non-root"
}

deny contains msg if {
  not input.metadata.annotations["cosign.sigstore.dev/signed"]
  msg := "image must be signed with cosign"
}
