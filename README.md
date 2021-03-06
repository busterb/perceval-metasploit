# perceval-metasploit [![Build Status](https://travis-ci.org/rapid7/perceval-metasploit.svg?branch=master)](https://travis-ci.org/rapid7/perceval-metasploit)


Bundle of Perceval backends for Metasploit ecosystem.

## Backends

The backends currently managed by this package support the next repositories:

* Metasploit

## Requirements

* Python >= 3.4
* python3-requests >= 2.7
* grimoirelab-toolkit > = 0.1
* perceval >= 0.9.11

## Installation

To install this package you will need to clone the repository first:

```
$ git clone https://github.com/rapid7/perceval-metasploit.git
```

Then you can execute the following commands:
```
$ pip3 install -r requirements.txt
$ pip3 install -e .
```

In case you are a developer, you should execute the following commands to install Perceval in your working directory (option `-e`) and the packages of requirements_tests.txt.
```
$ pip3 install -r requirements.txt
$ pip3 install -r requirements_test.txt
$ pip3 install -e .
```

## Examples

### Metasploit

```
$ perceval metasploit
```

## License

Licensed under GNU General Public License (GPL), version 3 or later.
