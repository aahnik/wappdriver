# Sending files

## Images, Videos and Documents

With `wappdriver` its easy to do all these. Simply pass the path of the image or video or document file to the `send` method.

!!! caution
    - You must use absoulte file paths.
    - File path must not have any space.

!!! note
    - In Windows absolute paths looks like:
        `C:\Users\mathew\img.png`
    - While in Linux or Mac they look like:
        `/home/aahnik/img.png`

You can send any file type that WhatsApp supports.
> WhatsApp does not support files over 16 MB

![sending an image](https://github.com/aahnik/wappdriver/blob/main/docs/images/sending_media.png?raw=true)

## Sending Multiple Files

You can easily pass as many arguments to `send` method of `WhatsApp` class you wish.
**Just remember that the first argument must be the name of the recipient.**

![sending multiple files](https://github.com/aahnik/wappdriver/blob/main/docs/images/sending_multiple_files.png?raw=true)

## Messages with Files

Hmm! `wappdriver` is extremely smart. It can detect whether a string is a message or a file path. So you can do this as shown below. Dont hesitate to use a multiline line string for a long message.

![files and messages](https://github.com/aahnik/wappdriver/blob/main/docs/images/files_and_messages.png?raw=true)

!!! note
    The messages will be send in exactly that order.
