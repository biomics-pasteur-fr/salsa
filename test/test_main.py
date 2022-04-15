from salsa.scripts.main import main as script
import pytest


from . import test_dir

def test_salsa_app(tmpdir):
    from click.testing import CliRunner
    runner = CliRunner()

    # The samplesheet command
    results = runner.invoke(script, ['--help'])
    assert results.exit_code == 0

