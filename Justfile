create_new_key:
    #!/bin/bash
    poetry run python -m fernet_encrypt create-fernet-key


encrypt_file in_file out_file="":
    #!/bin/bash
    in_file="{{in_file}}"
    out_file="{{out_file}}"

    if [[ ${#out_file} = 0 ]]; then
        poetry run python -m fernet_encrypt encrypt-file $in_file
    else
        poetry run python -m fernet_encrypt encrypt-file $in_file $out_file
    fi


decrypt_file in_file out_file="":
    #!/bin/bash
    in_file="{{in_file}}"
    out_file="{{out_file}}"

    if [[ ${#out_file} = 0 ]]; then
        poetry run python -m fernet_encrypt decrypt-file $in_file
    else
        poetry run python -m fernet_encrypt decrypt-file $in_file $out_file
    fi


test:
    #!/bin/bash
    poetry run pytest


build:
    #!/bin/bash
    poetry build


publish tag:
    #!/bin/bash
    poetry run twine upload dist/fernet_encrypt-{{tag}}.tar.gz
