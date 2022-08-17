import toml
from pathlib import Path

def create_dockerfile_with_env_vars(env_file="../.secrets.toml", dockerfile="../Dockerfile", sections=None):

    env_dict = toml.load(Path(env_file))

    if sections is None:
        sections = DOCKERFILE_SECTIONS = ["header", "port", "env", "python", "app"]

    # Read in each of the pieces

    if Path(dockerfile).exists():
        Path(dockerfile).unlink() 

    for section in sections:
        if section != "env":
            with open(Path(f"../Dockerfile_{section}.txt"), "r") as f:
                text = f.readlines()
                with open(Path(dockerfile), "a") as fout:
                    fout.writelines(text)
                    fout.write("\n")
        else:
            try:
                env_dict = toml.load(Path(env_file))
            except Exception as IOError:
                print(IOError)

            with open(Path(dockerfile), "a") as fout:
                for k, v in env_dict.items():
                    fout.writelines(f"ENV {k}={v}\n")
                fout.write("\n")

if __main__:
  create_dockerfile_with_env_vars()
