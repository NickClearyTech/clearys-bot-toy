# clearys-bot-toy
The Source Code for the Cleary's Bot Toy discord Bot

## Development

- Get a discord bot token [instructions](https://www.writebots.com/discord-bot-token/)
- Create a "test server" and invite your bot to it
- Enable Developer mode in your discord client
- Create a `.env` (named exactly as `.env`, which is gitignored) file, following the format of the `example.env` file
- In this .env file, add your discord token and desired log level
    - Valid log levels are `CRITICAL`, `ERROR`, `WARNING`, `INFO`, and `DEBUG`
- Copy example-config.yaml to config.yaml
- Customize the values for your given test server
- Run `docker compose build`
- Run `docker compose up`

### Formatting Code

Before pushing, make sure you format your code. We use a formatter called black. To install:

```shell
pip3 install black
```

Then, to format from the root of the project, just run:

```shell
black .
```

Those using the GNU Guix package manager can make use of a script to format the program without installing anything to their system. From the project root, run:

```shell
./bin/format
```
