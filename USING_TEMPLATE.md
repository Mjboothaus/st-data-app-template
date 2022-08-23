## Using the Template

This contains the first things that need to be done to use this template.

This is tailored to a VS Code setup, although in most cases should translate to other IDEs. It is also configured to enable deployment via Google Cloud Run on Google Cloud Platform (GCP). You need to set up an account on GCP to be able to deploy here - clearly you could use AWS or Azure etc but will need to create your own deployment recipe(s).

### `justfile` and `just`

See manual at [https://just.systems](https://just.systems). This template requires the installation of the `just` tool. Instead of using a `Makefile`
`just` provides a more contempary and powerful approach for creating recipes for assisting in development. To install on e.g. macOS use:
`brew install just`. See the manual for many other platform install instructions.

After installing, create a `.env` file in the top level directory of your project and specify a `PROJECT_NAME` and other defintions e.g.

```
PROJECT_NAME = "your-project-name"
STREAMLIT_RUN_PY = "app/Main.py"   # path to your main app
SERVER_PORT = "8080"
GCP_REGION = "your-gcp-deployment-region"
DOCS_URL = "https://TO_BE_DEFINED"
PYTHON_VERSION = "3.9.13"
```

Both `.env` and `.env_dockerfile.toml` should NOT be committed to your repo. TODO: Say more on this.

### Create the Python development (`dev`) virtual environment

`just venv dev`

this relies on requirements-dev.in (via `pip-compile` - ideally via `pipx install pip-tools`) which you can adjust for the packages you are using - similarly for the `deploy` environment (which typically has fewer packages required e.g. typically no need for `pytest` or `autopep8` in deployments.

Activate the environment where here .venv is the name of the venv directory

`source .venv/bin/activate`

Check the version of Streamlit you're using:

`just stv`


### Initial steps

After creating a new repo from the template - git clone the repo

1. Customise `README.md`
2. Edit `settings.toml` for the name of your app and subtitle if relevant
3. 



Create a `.env` to store any secrets used in the `justfile` (not to be committed to GitHub)

### Check that you can run the skeleton app

`just app`

### Use of DynaConf

Can be swapped out for another such library.

Create a file `.env_dockerfile.toml` in the root (top) directory which contains any environment variables that you want to create in the Dockerfile

### Debugging is Visual Studio Code (VS Code)\

Debug icon (run &  debug) - debug as normal - put in links
