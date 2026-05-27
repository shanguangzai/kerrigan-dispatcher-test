# Kerrigan Dispatcher Test

Scratch repository for manually testing Kerrigan GitHub dispatcher integration.

Trigger the `Kerrigan Manual Dispatch Test` workflow from GitHub Actions. The
workflow runs on an ephemeral self-hosted runner launched by Kerrigan and
submits `.kerrigan/job.yaml` through `kerrigan-runner-bridge`.
