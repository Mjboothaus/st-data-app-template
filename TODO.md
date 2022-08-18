This contains the first things that need to be done to use this template.

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

## TODO

- 
- Allow for various data use cases (abstract?) e.g. pd.read_csv / https:// and S3 examples + API
- Get basic sidebars setup - Done - need to do for all pages
- Set up Streamlit debug - Done
- Report deploy time in justfile - DONE - to test - seems OK
- Exclude dirs from tree listing (do only dir & not subdirs)
- Set up pytest-ing and write some (generic tests - of setup?)
- Maybe replace dirtree.py with seedir package - DONE - test & refine
- seedir not been included in requirements-deploy.txt