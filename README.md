# Discord Bot

Python と `discord.py` で動作するシンプルなDiscord Botです。

## セットアップ（Windows PowerShell）

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
```

作成された `.env` を開き、`DISCORD_TOKEN` にDiscord Botのトークンを設定します。

> `.env` には秘密情報が入るため、Gitへコミットしないでください。

## 起動

```powershell
python bot.py
```

## コマンド

- `!hello` — Botに挨拶
- `!ping` — 応答確認
- `!time` — 現在時刻
- `!dice` — サイコロを振る
- `!helpme` — コマンド一覧

Discord Developer PortalのBot設定で **Message Content Intent** を有効にしてください。
