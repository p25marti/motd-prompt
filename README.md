# motd-prompt
This is a really simple set of scripts that displays a daily design quote in your prompt 
the first time you launch a terminal every day.

## Details
The script is writen in python and leverages a systemd.timer in order to reset every day at 
midnight.

## Installation
Simply move the `daily-design-quotes` directory into your `~/.config` folder, and move both the
`quotes.timer` and `quotes.service` files into your user-specific systemd unit file folder. For 
example mine can be found at `~/.config/systemd/user/`. Now enable the timer and enjoy.

To start the timer use the following:

```
systemctl --user enable quotes.timer
```

To stop the timer use the following:

```
systemctl --user disable quotes.timer
```
