# Ding [![Build Status](https://travis-ci.org/liviu-/ding.svg?branch=develop)](https://travis-ci.org/liviu-/ding)

![usage_gif](usage.gif)

Tired of `$ sleep 4231; beep`? This is a very simple solution to help with short-term time management. The beep sound uses the motherboard audio, so it works even if your speakers are muted, but not if you muted the PC speakers :stuck_out_tongue: . Furthermore, it works wherever there's a Linux terminal, and that includes ssh sessions.

- No dependencies other than Python itself :dizzy:
- Install with `pip` or just copy the binary somewhere in `$PATH` :sparkles:
- Python2 and Python3 compatible :star2:
- Around 100 LOC :boom:
- Runs on Linux, OS X, Windows, and maybe more :tada:

## Installation

```
$ pip install ding-ding
```

(`ding` was taken)

Alternatively, download the [ding.py](https://github.com/liviu-/ding/blob/develop/ding/ding.py) file and run it however you please.

```
$ ./ding.py in 1s
```

## Scenarios

- You want to start work after browsing the news for a bit, but you don't want to get carried away and do no work. Set a timer for 15 minutes:
```
$ ding in 15m
```
- You need to leave at 17:00 and you want to have time to get ready:
```
$ ding at 16:45
```

- [Pomodoro technique](https://en.wikipedia.org/wiki/Pomodoro_Technique)
```
$ alias pomo="ding in 25m"
$ pomo
```


## Example usage:

```
# Relative time
$ ding in 2m
$ ding in 2h 15m
$ ding in 2m 15s

# Absolute time
$ ding at 12
$ ding at 17:30
$ ding at 17:30:21

# Recurrent notification
$ ding every 15m

# Custom command for beeping
$ ding in 1s --command "paplay --volume 15000 beep.wav"

# Hide timer
$ ding in 1s --no-timer
```
For more help, try:

```
$ ding in --help
$ ding at --help
$ ding every --help
```

## FAQ

### How come I don't hear anything?

This happens when the audible bell was muted for your terminal or for your system. Enabling it differs between environments, so I would suggest trying out some Google searches on how to enable it. For a discussion on this, check this [issue](https://github.com/liviu-/ding/issues/5). You can also use your own custom command that actually beeps for you using `$ ding in 1s -c your-command`

### How can I use a custom command all the time?

Try adding to your start-up script:
```bash
function ding() { ding $@ -c custom-command}
```
(inspired from [mikaylathompson](https://github.com/mikaylathompson)'s comment [here](https://github.com/liviu-/ding/pull/9))

### How can I to run it in the background?

```
$ ding in 1s --no-timer&
```

### Can I use desktop notifications?

Unfortunately, desktop notifications typically come with big GUI dependencies and tend to be less portable. However, you can integrate notifications using a custom command like this `$ ding in 1s --command "notify-send 'Sup'"`. This will display the notification 4 times by default, but if you think it would be useful to have an option to specify the number of calls, let me know by opening an [issue](https://github.com/liviu-/ding/issues) or a [PR](https://github.com/liviu-/ding/pulls).
