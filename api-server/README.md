# API server 🔌

This application is written in [Python](https://python.org/) and uses [Quart](https://pgjones.gitlab.io/quart/) as the web framework. For data persistence is uses the document-based [MongoDB](https://www.mongodb.com/try/download/community) database with the [MongoEngine](https://github.com/MongoEngine/mongoengine) object-document mapper (ODM).

## Prerequisites 🚧

As editor we recommend the free [VS Code](https://code.visualstudio.com/). You can develop this application with two different workflows that are described below.

### Development container 🐳

This requires you to install the ["Remote - Containers" VS Code extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) and [Docker](https://docs.docker.com/get-docker/) on your computer. Afterwards, you can open this subfolder in VS code and it will prompt you with a message where you can click **Reopen in Container** in the bottom right of your screen. If this message is not shown, click the blue button in the bottom-left, type **Remote-Containers** and select click **Reopen in Container**.

### With your Python installation 🐍

You might have Python already installed, if not, now is the time to do so. Afterwards you might also want to create a virtual environment to prevent your global Python environment from being bloated or suffering from version conflicts. You can to this with the command `python -m venv .venv`. Once you created the virtual environment, you can activate it with `source ./venv/bin/activate` and deactivate it by running `deactivate`.

No matter, which workflow you chose, you can not install the dependencies with the following command:

```bash
$ pip install -r requirements.txt
```

## Development 🔧

Run `QUART_APP=app:app quart run` and the application will automatically restart on code changes. You can then visit it at [localhost:5000](http://localhost:5000/health).

## Production 🚀

To run the application in production execute `hypercorn -c hypercorn.toml app:app`.
