from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from models.note import Note
from utils.common import convert_response_to_json
from typing import List
from database.mongodb_helper import Database

router = APIRouter()
db = Database()
notes_collection = 'Notes'


@router.post('/notes', response_description='Create a new note')
async def create_note(note: Note):
    try:
        note = dict(note)
        data = await db.insert_document(notes_collection, note)
        payload = {
            'message': 'Successfully created resource',
            'data': convert_response_to_json(data)
        }
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=payload)
    except Exception as ex:
        payload = {
            'message': 'Failed to create resource',
            'error': convert_response_to_json(ex)
        }
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=payload)


@router.put('/notes/{noteId}', response_description='Update entire note', response_model=Note)
async def update_note(note_id: str):
    pass


@router.patch('/notes/{noteId}', response_description='Update partial note', response_model=Note)
async def update_partial_note(note_id: str):
    pass


@router.delete('/notes/{noteId}', response_description='Delete specific note', response_model=Note)
async def delete_note(note_id: str):
    pass


@router.delete('/notes', response_description='Delete multiple notes', response_model=List[Note])
async def delete_notes():
    pass


@router.get('/notes', response_description='Get all notes', response_model=List[Note])
async def get_all_notes():
    try:
        data = await db.get_all_documents(notes_collection)
        payload = {
            'message': 'Successfully retrieved resource',
            'data': convert_response_to_json(data)
        }
        return JSONResponse(status_code=status.HTTP_200_OK, content=payload)
    except Exception as ex:
        payload = {
            'message': 'Failed to retrieve resource',
            'error': convert_response_to_json(ex)
        }
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=payload)


@router.get('/notes/{noteId}', response_description='Get specific note by id', response_model=Note)
async def get_note_by_id(note_id: str):
    try:
        data = await db.get_document_by_id(notes_collection, note_id)
        payload = {
            'message': 'Successfully retrieved resource',
            'data': convert_response_to_json(data)
        }
        return JSONResponse(status_code=status.HTTP_200_OK, content=payload)
    except Exception as ex:
        payload = {
            'message': 'Failed to retrieve resource',
            'error': convert_response_to_json(ex)
        }
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=payload)


@router.get('/notes/{key}/{value}', response_description='Get specific note by attribute',
            response_model=Note)
async def get_note_by_attribute(key: str, value: str):
    try:
        data = await db.get_document_by_attribute(notes_collection, key, value)
        payload = {
            'message': 'Successfully retrieved resource',
            'data': convert_response_to_json(data)
        }
        return JSONResponse(status_code=status.HTTP_200_OK, content=payload)
    except Exception as ex:
        payload = {
            'message': 'Failed to retrieve resource',
            'error': convert_response_to_json(ex)
        }
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=payload)
