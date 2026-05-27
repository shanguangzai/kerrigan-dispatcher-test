# Kerrigan Dispatcher Test

Scratch repository for manually testing Kerrigan GitHub dispatcher integration.

Trigger the `Kerrigan Manual Dispatch Test` workflow from GitHub Actions. The
workflow runs on an ephemeral self-hosted runner launched by Kerrigan and
submits a checked-in manifest through `kerrigan-runner-bridge`.

Available manifests:

- `.kerrigan/vulcan-core-develop-job.yaml`: staging Vulcan retrieval/install smoke for `core@develop:latest`.
- `.kerrigan/ctest-job.yaml`: artifact-backed CTest shards hosted by GitHub Pages.
- `.kerrigan/job.yaml`: bundled pytest shards from this repository.
