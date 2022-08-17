import toml
from pathlib import Path


def create_dockerfile_with_env_vars(env_file=".secrets_env.toml", dockerfile="Dockerfile", sections=None):
    try:
        env_dict = toml.load(Path(env_file))
    except Exception as IOError:
        raise(IOError)

    if sections is None:
        sections = DOCKERFILE_SECTIONS = [
            "head", "port", "env", "py", "app"]

    # Read in each of the Dockerfile pieces

    if Path(dockerfile).exists():
        Path(dockerfile).unlink()

    for section in sections:
        if section != "env":
            try:
                with open(Path(f"Dockerfile_{section}.txt"), "r") as f:
                    text = f.readlines()
                    with open(Path(dockerfile), "a") as fout:
                        fout.writelines(text)
                        fout.write("\n")
            except Exception as IOError:
                raise(IOError)
        else:
            try:
                env_dict = toml.load(Path(env_file))
            except Exception as IOError:
                raise(IOError)

            with open(Path(dockerfile), "a") as fout:
                for k, v in env_dict.items():
                    fout.writelines(f"ENV {k}={v}\n")
                fout.write("\n")


if __name__ == "__main__":
    create_dockerfile_with_env_vars()
