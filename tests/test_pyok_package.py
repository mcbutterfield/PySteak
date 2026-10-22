"""Package checks that do not require an STK installation or license."""

import importlib
import importlib.metadata
import importlib.resources
import json
import subprocess
import sys

import pytest


@pytest.mark.parametrize(
    "name",
    [
        "br.ok.core",
        "br.ok.core.stkengine",
        "br.ok.core.stkruntime",
        "br.ok.core.stkobjects",
        "br.ok.core.stkobjects.astrogator",
        "br.ok.core.stkobjects.aviator",
        "br.ok.core.utilities.colors",
        "br.ok.core.utilities.grpcutilities",
        "br.ok.extensions.scenario_construction",
    ],
)
def test_installed_modules_use_pyok_namespace(name):
    module = importlib.import_module(name)
    assert module.__name__ == name


def test_distribution_metadata_and_extras():
    from br.ok import __version__

    distribution = importlib.metadata.distribution("br-ok")
    assert distribution.version == __version__
    assert set(distribution.metadata.get_all("Provides-Extra")) == {
        "all", "core", "extensions", "grpc", "jupyter", "migration"
    }
    requirements = distribution.requires or []
    assert any(requirement.startswith("br-ok[") for requirement in requirements)
    assert not any(requirement.startswith("ansys-stk") for requirement in requirements)
    files = [str(path) for path in distribution.files]
    assert any(path.startswith("br/ok/core/") for path in files)
    assert not any(path.startswith("ansys/") for path in files)


def test_bundled_mappings_target_pyok_namespace():
    package = "br.ok.core.tools.api_migration_assistant"
    mappings = importlib.resources.files(package).joinpath("api-mappings")
    files = list(mappings.iterdir())
    assert files
    for path in files:
        data = json.loads(path.read_text(encoding="utf-8"))
        target = data["RootMapping"]["NewRootScope"]
        assert target.startswith("br.ok.core.")
        assert "ansys.stk" not in path.read_text(encoding="utf-8")


def test_migration_entry_point_and_module_cli():
    distribution = importlib.metadata.distribution("br-ok")
    entry = next(
        entry for entry in distribution.entry_points
        if entry.name == "pyok-migration-assistant"
    )
    assert entry.group == "console_scripts"
    assert entry.value.startswith("br.ok.core.tools.api_migration_assistant.")
    assert callable(entry.load())
    result = subprocess.run(
        [sys.executable, "-m", "br.ok.core.tools.api_migration_assistant", "--help"],
        check=True, capture_output=True, text=True,
    )
    assert "API Migration Assistant" in result.stdout


def test_representative_api_types_and_color_behavior():
    from br.ok.core.stkobjects import STKObjectType
    from br.ok.core.utilities.colors import Color

    assert STKObjectType.SATELLITE.value == 18
    assert STKObjectType.__module__ == "br.ok.core.stkobjects"
    assert Color.from_rgb(127, 255, 212).get_rgb() == (127, 255, 212)
