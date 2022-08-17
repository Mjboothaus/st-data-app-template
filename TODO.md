This contains the first things that need to be done to use this template.

Create python development (dev) virtual environment

`just venv dev`

Activate the environment where here .venv is the name of the venv directory

`source .venv/bin/activate`

Check the version of Streamlit you're using:

`just stv`


Create a `.env` to store any secrets used in the `justfile` (not to be committed to GitHub)

Use of DynaConf

Can be swapped out for another such library.

Create a file `.secrets_env.toml` in the root (top) directory which contains any environment variables that you want to create in the Dockerfile

