# See https://just.systems/

# Local just variables

project_name := "st-data-app-template"
app_py := "src/Main.py"
server_port := "8080"
gcp_region := "australia-southeast1"
docs_url := "https://TO_BE_DEFINED"

# Load variables from .env file

set dotenv-load

# Show available just commands

help:
  @just -l
  
docs:
	open {{docs_url}}

port-process port:
	sudo lsof -i :{{port}}


# Create the local Python venv (.venv_{{project_name}}) and install requirements(.txt)

venv dev_deploy:
	#!/usr/bin/env bash
	pip-compile requirements-{{dev_deploy}}.in
	python3 -m venv .venv_{{dev_deploy}}_{{project_name}}
	. .venv_{{dev_deploy}}_{{project_name}}/bin/activate
	python3 -m pip install --upgrade pip
	pip install -r requirements-{{dev_deploy}}.txt
	python -m ipykernel install --user --name .venv_{{dev_deploy}}_{{project_name}}
	pip install -U prefect
	echo -e '\n' source .venv_{{dev_deploy}}_{{project_name}}/bin/activate '\n'


activate dev_deploy:
	#!/usr/bin/env zsh
	echo -e '\n' source .venv_{{dev_deploy}}_{{project_name}}/bin/activate '\n'


update-reqs dev_deploy:
	pip-compile requirements-{{dev_deploy}}.in
	pip install -r requirements-{{dev_deploy}}.txt --upgrade


rm-venv dev_deploy:
  #!/usr/bin/env bash
	rm -rf .venv_{{dev_deploy}}_{{project_name}}


test:
  pytest


# Run app

app:
  streamlit run {{app_py}} --server.port={{server_port}} --server.address=localhost

dockerfile:
  #!/usr/bin/env bash
  python -m create_dockerfile.py
  

# Build and run app in a (local) Docker container

docker: 
    docker build . -t {{project_name}}
    docker run -p {{server_port}}:{{server_port}} {{project_name}}


# Google Cloud Run setup: work in progress (still not "STP" without user input)

gcr-setup:
    #!/usr/bin/env bash
    gcloud components update
    gcloud projects create {{project_name}}
    gcloud beta billing projects link {{project_name}} --billing-account $BILLING_ACCOUNT_GCP
    gcloud services enable cloudbuild.googleapis.com
    gcloud services enable run.googleapis.com
    gcloud services enable compute.googleapis.com
    gcloud services enable artifactregistry.googleapis.com
    gcloud config set region {{gcp_region}
    gcloud config set project {{project_name}}


# Deploy container to Google Cloud (Cloud Run) and helper commands

gcr-deploy: 
    gcloud run deploy --source . {{project_name}} --region {{gcp_region}}


gcr-list-deployed-url:
    gcloud run services list --platform managed | awk 'NR==2 {print $4}'


gcr-app-disable:   # deleting project does not delete app
    gcloud app versions list


# See: https://stackoverflow.com/questions/59423245/how-to-get-or-generate-deploy-url-for-google-cloud-run-services
    
  

