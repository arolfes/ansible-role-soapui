Ansible Role: SOAPUI Community Edition
======================================

Role to install the SoapUI CE **without JDK**.

**Important:** This ansible role is based on [GANTSIGN ansible-role-golang](https://github.com/gantsign/ansible-role-golang) 

**Thanks** a lot to John and Gantsign for providing molecule wrapper script and awesome ansible roles which are available over ansible-galaxy.

Requirements
------------

* Ansible >= 2.7

* Linux Distribution

    * Debian Family

        * Ubuntu

            * Bionic (18.04)
            * Focal (20.04)


    * Note: other versions are likely to work but have not been tested.

Role Variables
--------------

The following variables will change the behavior of this role (default values
are shown below):

```yaml
# SOAPUI Version to download and unpack
soapui_version: '5.5.0'

# Download url for SoapUI tarball
soapui_download_url: 'http://dl.eviware.com/soapuios/{{ soapui_version }}'

# Base installation directory
soapui_install_dir: '/opt/soapui/{{ soapui_version }}'

# Directory to store files downloaded for SoapUI installation
soapui_download_dir: "{{ x_ansible_download_dir | default(ansible_env.HOME + '/.ansible/tmp/downloads') }}"
```

### Supported SoapUI Versions

The following versions of SoapUI are supported without any additional configuration

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


Role Facts
----------

This role exports the following Ansible facts for use by other roles:

* `ansible_local.soapui.general.version`

    * e.g. `5.5.0`

* `ansible_local.soapui.general.home`

    * e.g. `/opt/soapui/5.5.0`

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




