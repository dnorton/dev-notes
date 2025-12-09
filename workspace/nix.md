# Nix

[Nix](https://nixos.org/nix/) is a package manager that is used in NixOS, a Linux distribution. It is also used in other Linux distributions, such as Ubuntu, to manage packages. Nix is a functional package manager, which means that it treats packages as functions. This allows for easy reproducibility of packages and easy rollback to previous versions of packages.

## Guides

- [Nixing Homebrew](https://dev.to/synecdokey/nix-on-macos-2oj3)
- [zero-to-nix.comd(https://zero-to-nix.com/start/install)

```bash
❯ curl --proto '=https' --tlsv1.2 -sSf -L https://install.determinate.systems/nix | sh -s -- install
info: downloading installer https://install.determinate.systems/nix/tag/v0.22.0/nix-installer-aarch64-darwin
`nix-installer` needs to run as `root`, attempting to escalate now via `sudo`...
Password:
Nix install plan (v0.22.0)
Planner: macos (with default settings)

Planned actions:
* Create an encrypted APFS volume `Nix Store` for Nix on `disk3` and add it to `/etc/fstab` mounting on `/nix`
* Extract the bundled Nix (originally from /nix/store/qzl0cbn134zgq3vqwzdzvs9sx8ncsva9-nix-binary-tarball-2.24.4/nix-2.24.4-aarch64-darwin.tar.xz)
* Create a directory tree in `/nix`
* Move the downloaded Nix into `/nix`
* Create build users (UID 301-332) and group (GID 30000)
* Configure Time Machine exclusions
* Setup the default Nix profile
* Place the Nix configuration in `/etc/nix/nix.conf`
* Configure the shell profiles
* Configuring zsh to support using Nix in non-interactive shells
* Create a `launchctl` plist to put Nix into your PATH
* Configure upstream Nix daemon service
* Remove directory `/nix/temp-install-dir`


Proceed? ([Y]es/[n]o/[e]xplain):
```
