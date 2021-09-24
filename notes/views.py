from django.shortcuts import render,redirect

from django.http import HttpResponse

from .models import Note,Tag


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tag_note = request.POST.get('tag')
        tag_list = Tag.objects.filter(name=tag_note)
        if len(tag_list)==0:
            tag=Tag(name=tag_note)
            tag.save()
        else:
            tag=tag_list[0]
        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
        b = Note(title=title, content=content,tag=tag)
        b.save()
        return redirect('index')
    else:
        all_notes = Note.objects.all()
    
        return render(request, 'notes/index.html', {'notes': all_notes})


def edit(request):
    id = request.POST.get('id')
    ID=int(id)
    note= Note.objects.get(id=ID)
    if request.method == 'POST':
        title = request.POST.get('newtitle')
        content = request.POST.get('newdetails')
        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
        note.title = title
        note.content = content
        note.save()
        return redirect('index')
    else:
        return render(request, 'notes/index.html', {'notes': note})


def delete(request):
    id = request.POST.get('id')
    ID=int(id)
    note = Note.objects.get(id=ID)
    p_tag=request.POST.get('tag')
    if p_tag is not None:
        tag = Note.objects.filter(tag=p_tag)
        if len(tag)==0:
            Tag.objects.filter(name=p_tag).delete()
    note.delete()
    return redirect('index')

def list_of_tags(request):

    p_tag=request.POST.get('tag')

    t_tag=Tag.objects.get(id=p_tag)

    filtered_notes=Note.objects.filter(tag=t_tag)

    return render(request, 'notes/tags.html', {'notes': filtered_notes})

def all_tags(request):
    all_tags = Tag.objects.all()
    return render(request,'notes/alltags.html',{'tags': all_tags})

