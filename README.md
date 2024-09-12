# Gaboon Test
Obviously, Gaboon is in super early alpha so I won’t get into things like hardware wallet support, contract verification, and other things that come with more established frameworks.

## Pros

- Feels like the true successor to Brownie, focused on Vyper
    - Fine to leave Solidity alone as Foundry and Hardhat are already leading the charge there
    - Ecosystem was missing a true developer framework for Vyper (Ape doesn’t count)
- Works with my favorite python tools
    - Poetry
    - Pyenv
    - Pytest
- toml file for configuration rocks, never understood Brownie’s yaml file when toml is the goto in modern python land
- `wallet` command is sick, was one of my favorite features from Brownie
    - global keystores make sense, wouldn’t want to commit keystores to source control
- installing from github works for installing and likely will be the most used way to install
- I love that I can have contracts that don’t compile in the repo but can test other contracts that do compile

## Cons

- Found out there's a difference between `gaboon` and `gaboon-cli` packages :)
- Fuzz testing takes a good chunk of time
    - 100 examples takes 56 sec
- Couldn’t easily figure out what to do in the console
- global `gaboon_history` file may make more sense to store in each repo, not checked into version control, as I would want to only see commands related to the project I currently have open.
- installing from pypi doesn’t work with poetry, would love to see poetry support
- Upgrading a package fails with `io.UnsupportedOperation: write`
- May be an issue with vyper, but installing via github did not compile when importing into a contract (see `OwnableCounter.vy`)