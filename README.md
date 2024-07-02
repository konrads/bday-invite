# Creates birthday party invites for my guests

This program creates birthday invites for the people I invite to my birthday party. Each invite will have the guest's name written up the top!

Written by Oskar and Konrad!

## Before you run the program

Load `python` libraries:

```sh
pip install -r requirements.txt
```

Check that [invite template](./invite-template.png) image is up to date.

Add people names to the [guest list](./guest-list.txt). Use spaces to make sure the name is at the center.

If you want, you can change `FONT` in [main.py](./main.py). To find which fonts can be used, run:

```sh
ls /Library/Fonts /System/Library/Fonts ~/Library/Fonts
```

## Create invites!

```sh
python main.py
```

This creates images in the `invites` folder, as per example below. Check these before printing!

![invite-example](doc/invite-example.png?raw=true)
