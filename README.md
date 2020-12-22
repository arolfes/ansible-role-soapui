Ansible Role: SOAPUI Community Edition
======================================

[![Build Status](https://github.com/arolfes/ansible-role-soapui/workflows/molecule%20tests/badge.svg?branch=master)](https://github.com/arolfes/ansible-role-soapui/actions?query=branch%3Amaster+workflow%3A%22molecule+tests%22)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-arolfes.soapui-blue.svg)](https://galaxy.ansible.com/arolfes/soapui)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/arolfes/ansible-role-soapui/master/LICENSE)

Role to install the SoapUI CE **without JDK**.

Requirements
------------

* Ansible >= 2.8.0

* Linux Distribution

    * Debian Family

        * Ubuntu

            * Bionic (18.04)
            * Focal (20.04)

        * Debian

            * Stretch (9)
            * Buster (10)

    * RedHat Family

        * CentOS

            * 7
            * 8

        * Fedora

            * 31

    * SUSE Family

        * openSUSE

            * 15.1

    * Note: other versions are likely to work but have not been tested.

Role Variables
--------------

The following variables will change the behavior of this role (default values
are shown below):

```yaml
# SOAPUI Version to download and unpack
soapui_version: '5.6.0'

# Download url for SoapUI tarball
soapui_download_url: 'http://dl.eviware.com/soapuios/{{ soapui_version }}'

# Base installation directory
soapui_install_dir: '/opt/soapui/{{ soapui_version }}'

# Directory to store files downloaded for SoapUI installation
soapui_download_dir: "{{ x_ansible_download_dir | default(ansible_env.HOME + '/.ansible/tmp/downloads') }}"
```

### Supported SoapUI Versions

The following versions of SoapUI are supported without any additional configuration

* 5.6.0
* 5.5.0
* 5.2.1
* 5.2.0
* 5.1.3
* 5.1.2
* 5.0.0
* 4.6.4

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
     - role: arolfes.soapui
```
You can install a specific version of SoapUI by specifying the soapui_version.
```yaml
- hosts: servers
  roles:
     - role: arolfes.soapui
       soapui_version: '4.6.4'
```
Remember: This role doesn't provide a java runtime to execute SoapUI and it hasn't a dependency. 
This example installs a jdk and the latest version from SoapUI.
```yaml
- hosts: servers
  roles:
    - role: gantsign.java
      java_version: '8'
      java_is_default_installation: yes
    - role: arolfes.soapui
```


Role Facts
----------

This role exports the following Ansible facts for use by other roles:

* `ansible_local.soapui.general.version`

    * e.g. `5.6.0`

* `ansible_local.soapui.general.home`

    * e.g. `/opt/soapui/5.6.0`

Development & Testing
---------------------

This project uses [Molecule](http://molecule.readthedocs.io/) to aid in the
development and testing; the role is unit tested using
[Testinfra](http://testinfra.readthedocs.io/) and
[pytest](http://docs.pytest.org/).

To develop or test you'll need to have installed the following:

* Linux (e.g. [Ubuntu](http://www.ubuntu.com/))
* [Docker](https://www.docker.com/)
* [Python](https://www.python.org/) (including python-pip)
* [Ansible](https://www.ansible.com/)
* [Molecule](http://molecule.readthedocs.io/)

Because the above can be tricky to install, this project includes
[Molecule Wrapper](https://github.com/gantsign/molecule-wrapper). Molecule
Wrapper is a shell script that installs Molecule and it's dependencies (apart
from Linux) and then executes Molecule with the command you pass it.

To test this role using Molecule Wrapper run the following command from the
project root:

```bash
./moleculew test
```

Note: some of the dependencies need `sudo` permission to install.

License
-------

MIT

Author Information
------------------

Alexander Rolfes




