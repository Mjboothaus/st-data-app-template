## Using the Template

This contains the first things that need to be done to use this template.

After creating a new repo from the template - git clone the repo

1. Customise `README.md`
2. Edit `settings.toml` for the name of your app and subtitle if relevant
3. 

Create python development (dev) virtual environment

`just venv dev`

Activate the environment where here .venv is the name of the venv directory

`source .venv/bin/activate`

Check the version of Streamlit you're using:

`just stv`


Create a `.env` to store any secrets used in the `justfile` (not to be committed to GitHub)

### Use of DynaConf

Can be swapped out for another such library.

Create a file `.env_dockerfile.toml` in the root (top) directory which contains any environment variables that you want to create in the Dockerfile

### Debugging is Visual Studio Code (VS Code)\

Debug icon (run &  debug) - debug as normal - put in links
