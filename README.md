# IRON-BOT

<p align="center"><img src="https://telegra.ph/file/aece629756cbb1899be93.jpg"/></p>

<p align="center">
    <img alt="Ironbot-" src="https://img.shields.io/badge/Ver-1.1.0-brightgreen?style=for-the-badge&logo=appveyor"/>
    <a href="https://github.com/tesbot07/ironbot/network/members"> <img src="https://img.shields.io/github/forks/tesbot07/ironbot?logo=github&style=for-the-badge" /></a>
    <a href="https://github.com/tesbot07/ironbot"> <img src="https://img.shields.io/github/repo-size/tesbot07/ironbot?logo=github&style=for-the-badge" /></a>
    <a href="https://pypi.org/project/Telethon/"> <img src="https://img.shields.io/pypi/v/telethon?label=telethon&logo=pypi&logoColor=white&style=for-the-badge" /></a>
    <a href="https://github.com/tesbot07/ironbot/blob/master/LICENSE"> <img src="https://img.shields.io/github/license/tesbot07/ironbot?style=for-the-badge&logo=appveyor" /></a>
    <img alt="PYTHON" src="https://img.shields.io/badge/PYTHON-v3.8.5-red?style=for-the-badge&logo=appveyor"/>
</p>

## Installing Heroku 
```python3
The Easy Way:
```
[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/tesbot07/ironbot/)

## Generate String Session
```python3
Run on Repl.it:
```
<p><a href="https://generatestring.tesbot07.repl.run"> <img src="https://img.shields.io/badge/run-string__session.py-blue?style=for-the-badge&logo=repl.it" alt="Generate String Session" /></a></p>

### The Normal Way

An example `local_config.py` file could be:

**Not All of the variables are mandatory**

__The Userbot should work by setting only the first two variables__

```python3
from heroku_config import Var

class Development(Var):
  APP_ID = 6
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
```

### UniBorg Configuration



**Heroku Configuration**
Simply just leave the Config as it is.

**Local Configuration**

Fortunately there are no Mandatory vars for the UniBorg Support Config.

## Mandatory Vars

- Only two of the environment variables are mandatory.
- This is because of `telethon.errors.rpc_error_list.ApiIdPublishedFloodError`

    - `APP_ID`:   You can get this value from https://my.telegram.org
    - `API_HASH`:   You can get this value from https://my.telegram.org
- The userbot will not work without setting the mandatory vars.
