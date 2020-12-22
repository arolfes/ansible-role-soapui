import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('version_dir_pattern', [
    '5.6.0$'
])
def test_soapui_installed(host, version_dir_pattern):

    soapui_home = host.check_output('find %s | grep --color=never -E %s',
                                    '/opt/soapui/',
                                    version_dir_pattern)

    soapui_sh = host.file(soapui_home + '/bin/soapui.sh')

    assert soapui_sh.exists
    assert soapui_sh.is_file
    assert soapui_sh.user == 'root'
    assert soapui_sh.group == 'root'
    assert oct(soapui_sh.mode) == '0o755'


@pytest.mark.parametrize('version_dir_pattern', [
    '5.6.0$'
])
def test_fix_for_560(host, version_dir_pattern):

    soapui_home = host.check_output('find %s | grep --color=never -E %s',
                                    '/opt/soapui/',
                                    version_dir_pattern)

    xmlbeans_xpath_old = host.file(soapui_home +
                                   '/lib/xmlbeans-xpath-2.6.0.jar.old')
    xmlbeans_xmlpublic_old = host.file(soapui_home +
                                       '/lib/xmlbeans-xmlpublic-2.6.0.jar.old')

    assert xmlbeans_xpath_old.exists
    assert xmlbeans_xmlpublic_old.exists


def test_soapui(host):
    assert host.run('which soapui.sh').rc == 0


def test_soapui_desktop_file(host):
    desk_file = host.file('/usr/share/applications/SoapUI.desktop')

    assert desk_file.exists
    assert desk_file.is_file
    assert desk_file.user == 'root'
    assert desk_file.group == 'root'
    assert oct(desk_file.mode) == '0o644'


@pytest.mark.parametrize('fact_group_name', [
    'soapui'
])
def test_facts_installed(host, fact_group_name):
    fact_file = host.file('/etc/ansible/facts.d/' + fact_group_name + '.fact')

    assert fact_file.exists
    assert fact_file.is_file
    assert fact_file.user == 'root'
    assert fact_file.group == 'root'
    assert oct(fact_file.mode) == '0o644'
