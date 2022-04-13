#from traceback import print_tb
from django.shortcuts import render
from django.template import loader
from .models import Curso
from .models import Estudiante
from .models import Entregable
from .form  import CursoForm
from django.http import HttpResponse

# Create your views here.

def listado_alumnos(request):

    template = loader .get_template('listado_alumnos.html')
    alumnos=Curso.objects.all()
    estudiante=Estudiante.objects.all()
    entregable=Entregable.objects.all()
    print(estudiante)
    print(alumnos)
    print(entregable)
    context = {
        'alumnos' : alumnos,
        'estudiante' : estudiante,
        'entregable' : entregable,
    }

    

    return HttpResponse(template.render(context, request))    


def CursoForm(request):

    if request.method == 'POST':

        curso = Curso (request.POST['curso'], request.POST['camada'])

        curso.save()

        return render(request, 'listado_formulario.html')
    
    return render(request, 'listado_formulario.html')


#def CursoForm(request):

#    if request.method == 'POST':
#        miformulario = CursoForm(request.POST)
#        print(miformulario)
#
#        if miformulario.is_valid:
#            informacion = miformulario.cleaned_data
#            curso = Curso (nombre=informacion['curso'], camada=informacion['camada'])
#            curso.save()

#            return render(request, 'listado_alumnos.html')
#    else:
#        miformulario = CursoForm()

#    return render(request, 'listado_formulario.html', {'miformulario':miformulario})









        #curso = Curso (request.POST['curso'], request.POST['camada'])

        #curso.save()

        #return render(request, 'listado_formulario.html')
    
    #return render(request, 'listado_formulario.html')