# Python 3 REST API 🐍

An example of a REST API with Python 3. It uses [Quart](https://pgjones.gitlab.io/quart/) as the web framework.

[![pipeline status](https://gitlab.com/paperstack-org/application-examples/python3-rest-api/badges/main/pipeline.svg)](https://gitlab.com/paperstack-org/application-examples/python3-rest-api/-/commits/main)

## Development 🔧

Start the development container and run `QUART_APP=app:app quart run`. The application will automatically restart on code changes and you can visit it at [localhost:5000](http://localhost:5000/health).

## Production 🚀

To run the application in production execute `hypercorn -c hypercorn.toml app:app`.

## License 📄

This project is licensed under the terms of the [MIT license](./LICENSE.md).
