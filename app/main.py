"""Yosee Wizard add-on — lightweight ingress frontend.

This add-on provides an ingress panel that embeds the Yosee Wizard
HA integration UI (served by the custom_component at /api/yosee_wizard/).
All provisioning logic lives in custom_components/yosee_wizard inside HA.
"""
import os

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

_HA_URL = os.environ.get("SUPERVISOR_API", "http://supervisor/core").replace("/core", "") + "/core"
_WIZARD_URL = "/api/yosee_wizard/"

_INDEX = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Yosee Wizard</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0 }}
  html, body, iframe {{ width: 100%; height: 100%; border: none }}
  body {{ background: #111 }}
  .loading {{ display: flex; align-items: center; justify-content: center;
    height: 100vh; flex-direction: column; gap: 12px; color: #888;
    font-family: system-ui, sans-serif; font-size: .9rem }}
</style>
</head>
<body>
  <div id="loading" class="loading">
    <div>Carregando Yosee Wizard…</div>
  </div>
  <iframe id="frame" src="{_WIZARD_URL}" style="display:none"
    onload="document.getElementById('loading').style.display='none';this.style.display='block'">
  </iframe>
</body>
</html>
"""


@app.get("/", response_class=HTMLResponse)
async def index():
    return _INDEX


@app.get("/health")
async def health():
    return {"status": "ok"}
