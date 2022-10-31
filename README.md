# Data analysis
- Document here the project: data_pipeline
- Description: Project Description
- Data Source:
- Type of analysis:

Please document the project the better you can.

# Startup the project

The initial setup.

Create virtualenv and install the project:
```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv ~/venv ; source ~/venv/bin/activate ;\
    pip install pip -U; pip install -r requirements.txt
```

Unittest test:
```bash
make clean install test
```

Check for data_pipeline in gitlab.com/{group}.
If your project is not set please add it:

- Create a new project on `gitlab.com/{group}/data_pipeline`
- Then populate it:

```bash
##   e.g. if group is "{group}" and project_name is "data_pipeline"
git remote add origin git@github.com:{group}/data_pipeline.git
git push -u origin master
git push -u origin --tags
```

Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
data_pipeline-run
```

# Install

Go to `https://github.com/{group}/data_pipeline` to see the project, manage issues,
setup you ssh public key, ...

Create a python3 virtualenv and activate it:

```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv -ppython3 ~/venv ; source ~/venv/bin/activate
```

Clone the project and install it:

```bash
git clone git@github.com:{group}/data_pipeline.git
cd data_pipeline
pip install -r requirements.txt
make clean install test                # install and test
```
Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
data_pipeline-run
```
