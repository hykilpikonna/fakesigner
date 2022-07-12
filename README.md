# FakeSigner

Automatically fakesign any .ipa file for use with [AppSync Unified](https://cydia.akemi.ai/?page/net.angelxwind.appsyncunified) or similar

## Installation

### 1. Install Dependencies

ldid - Link Identity Editor for Darwin Binaries

- For iOS, it's already installed.
- For MacOS: `brew install ldid` [Homebrew](https://formulae.brew.sh/formula/ldid)
- For ArchLinux: `yay -Sy ldid` [AUR](https://aur.archlinux.org/packages/ldid)

### 2. Install FakeSigner

If you have Python PIP: `pip install fakesigner`

If you don't have PIP, just clone this repo and place the `fakesigner.sh` file in some bin folders in your `PATH`.

## Usage

Run `fakesigner path/to/app.ipa` and the script will automatically create a fakesigned .ipa file called `app.ipa-fakesigned.ipa`
