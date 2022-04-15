from salsa.scripts.compute_ttest import compute_ttest as script
import subprocess
import pytest


from . import test_dir

def test_salsa_app(tmpdir):
    outfile = tmpdir.join("test.csv")
    image = tmpdir.join("test.png")
    from click.testing import CliRunner
    runner = CliRunner()

    # The samplesheet command
    infile= f"{test_dir}/data/test_compute_ttest.csv"
    results = runner.invoke(script, ['--help'])
    assert results.exit_code == 0

    results = runner.invoke(script, ['--infile', infile, "--outfile", outfile, 
    "--name-group1", "GroupA", "--name-group2", "GroupB", "--image", image])
    assert results.exit_code == 0


