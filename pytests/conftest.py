import os
from pathlib import Path
from tempfile import NamedTemporaryFile
from unittest import mock

import pytest

import fernet_encrypt

TEST_DATA_PATH = Path(__file__).parent.joinpath("data")
TEST_KEY_PATH = TEST_DATA_PATH.joinpath("keys")


@pytest.fixture()
def cli():
    yield fernet_encrypt.cli


@pytest.fixture()
def cmd_map(cli):
    return {x.name: x.callback for x in cli.registered_commands}


@pytest.fixture()
def mock_open():
    with mock.patch("builtins.open") as mock_open:
        yield mock_open


@pytest.fixture()
def mock_file(mock_open):
    mock_file = mock.MagicMock()
    mock_writer = mock.MagicMock()
    mock_writer.__enter__.return_value = mock_file
    mock_open.return_value = mock_writer
    yield mock_file


@pytest.fixture()
def mock_key_path(monkeypatch):
    monkeypatch.setattr(fernet_encrypt, "KEY_PATH", TEST_KEY_PATH)


@pytest.fixture()
def tmp_file():
    f = NamedTemporaryFile(delete=False)
    yield f
    f.close()
    os.remove(f.name)


@pytest.fixture()
def test_data():
    with open(str(TEST_DATA_PATH.joinpath("data.txt")), "rb") as f:
        return f.read()


@pytest.fixture()
def test_file(tmp_file, test_data):
    tmp_file.write(test_data)
    tmp_file.close()
    yield tmp_file


@pytest.fixture()
def test_encrypted_data():
    with open(str(TEST_DATA_PATH.joinpath("encrypted.out")), "rb") as f:
        return f.read()


@pytest.fixture()
def test_encrypted_file(tmp_file, test_encrypted_data):
    tmp_file.write(test_encrypted_data)
    tmp_file.close()
    yield tmp_file
