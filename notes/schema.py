import strawberry
from typing import List, Optional
from .models import Note

#Funcion de la IA
from transformers import pipeline

# Carga el modelo solo una vez
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")


@strawberry.type
class NoteType:
    id: int
    title: str
    content: str
    created_at: str
    updated_at: str

@strawberry.type
class Query:
    @strawberry.field
    def all_notes(self) -> List[NoteType]:
        return [
            NoteType(
                id=note.id,
                title=note.title,
                content=note.content,
                created_at=str(note.created_at),
                updated_at=str(note.updated_at)
            )
            for note in Note.objects.all()
        ]
    
    @strawberry.field
    def summarize_text(self, content: str) -> str:
        # Puedes ajustar `max_length` y `min_length` si lo deseas
        summary = summarizer(content, max_length=60, min_length=20, do_sample=False)
        return summary[0]["summary_text"]

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_note(self, title: str, content: str) -> NoteType:
        note = Note.objects.create(title=title, content=content)
        return NoteType(
            id=note.id, title=note.title, content=note.content,
            created_at=str(note.created_at), updated_at=str(note.updated_at)
        )

    @strawberry.mutation
    def update_note(self, id: int, title: Optional[str] = None, content: Optional[str] = None) -> NoteType:
        note = Note.objects.get(pk=id)
        if title:
            note.title = title
        if content:
            note.content = content
        note.save()
        return NoteType(
            id=note.id, title=note.title, content=note.content,
            created_at=str(note.created_at), updated_at=str(note.updated_at)
        )

    @strawberry.mutation
    def delete_note(self, id: int) -> bool:
        try:
            note = Note.objects.get(pk=id)
            note.delete()
            return True
        except Note.DoesNotExist:
            return False

schema = strawberry.Schema(query=Query, mutation=Mutation)
