# clearys-bot-toy
The Source Code for the Cleary's Bot Toy discord Bot

## Development

- Get a discord bot token [instructions](https://www.writebots.com/discord-bot-token/)
- Create a "test server" and invite your bot to it
- Enable Developer mode in your discord client
- Create a `.env` (named exactly as `.env`, which is gitignored) file, following the format of the `example.env` file
- In this .env file, add your discord token and the ID of your test server
- Run `docker compose build`
- Run `docker compose up`