from unittest import mock

import fernet_encrypt


def test_registered_commands(cli, cmd_map):
    assert len(cli.registered_commands) == 3
    assert cmd_map == {
        "create-fernet-key": fernet_encrypt.create_fernet_key,
        "encrypt-file": fernet_encrypt.encrypt_file,
        "decrypt-file": fernet_encrypt.decrypt_file,
    }


@mock.patch("fernet_encrypt.Fernet")
@mock.patch("fernet_encrypt.time")
def test_create_fernet_key(mock_time, mock_fernet, mock_open, mock_file):
    mock_fernet.generate_key.return_value = b"test"
    mock_time.return_value = 123

    fernet_encrypt.create_fernet_key()

    assert mock_open.call_args_list[0].args == (
        str(fernet_encrypt.KEY_PATH.joinpath("123.key")),
        "wb",
    )
    assert mock_file.write.call_args.args == (b"test",)


def test_encrypt_file():
    pass


def test_decrypt_file():
    pass
