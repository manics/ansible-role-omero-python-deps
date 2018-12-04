import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("module", [
    "Cython",
    "numpy",
    "jinja2",
    "matplotlib",
    "numexpr",
    "PIL",
    "tables",
    "yaml",
    "scipy",
])
def test_python_imports(host, module):
    host.check_output('python -c "import %s"' % module)
