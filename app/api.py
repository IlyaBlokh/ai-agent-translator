import os
from fastapi import APIRouter, Query, Body
from fastapi.responses import JSONResponse
from .models import TranslateRequest
from .translation import translate_data

router = APIRouter()

@router.post("/translate")
async def translate_json(
    data: TranslateRequest = Body(...),
    mock: bool = Query(False)
):
    expected_token = os.environ.get("TRANSLATION_API_TOKEN")
    if not expected_token or data.token != expected_token:
        return JSONResponse(status_code=401, content={"error": "Invalid or missing token."})
    response = []
    for record in data.records:
        key = record.key
        table = record.table
        english = record.english
        languages = record.languages
        if not key or not english or not languages:
            return JSONResponse(status_code=400, content={"error": "Each record must have 'key', 'english', and non-empty 'languages' list."})
        row = {"English(en)": english}
        translated_rows = translate_data([row], languages, mock=mock)
        translated = {"key": key, "table": table}
        for lang in languages:
            translated[lang] = translated_rows[0].get(lang, "")
        response.append(translated)
    return response