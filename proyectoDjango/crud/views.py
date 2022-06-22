from django.shortcuts import render
from .models import Marca, Categoria, Producto, Usuario, tipoUsuario, tipoPago

# Create your views here.

def indexView(request):
    return render(request, 'index.html', {})

def herramientasView(request):
    return render(request, 'herramientas.html', {})

def herrPequeView(request):
    return render(request, 'herrPeque.html', {})

def herrGrandeView(request):
    return render(request, 'herrGrande.html', {})

def herrTijeraView(request):
    return render(request, 'herrTijera.html', {})

def maceterosView(request):
    return render(request, 'maceteros.html', {})

def macRedondoView(request):
    return render(request, 'macRedondo.html', {})

def macModernoView(request):
    return render(request, 'macModerno.html', {})

def macJardineraView(request):
    return render(request, 'macJardinera.html', {})

def plantasView(request):
    return render(request, 'plantas.html', {})

def plaDolarView(request):
    return render(request, 'plaDolar.html', {})

def plaLavandaView(request):
    return render(request, 'plaLavanda.html', {})

def plaLenguaView(request):
    return render(request, 'plaLengua.html', {})

def susView(request):
    return render(request, 'suscripcion.html', {})

def EmpRegisterView(request):
    return render(request, 'EmpRegister.html', {})

def EmpLoginView(request):
    return render(request, 'EmpLogin.html', {})

def EmpResetView(request):
    return render(request, 'EmpReset.html', {})

def EmpForgetView(request):
    return render(request, 'EmpForget.html', {})
    
#marca
def viewMarca(request):
    cntx = {}
    if request.method == 'POST':
        id = int("0" + request.POST["txtId"])
        nombreMarca = request.POST["txtNombre"]
        activoMarca = False
        if 'chkActivo' in request.POST:
            activo = True
        if 'btnCreate' in request.POST:
            if len(nombreMarca) < 5:
                cntx = {'error': 'El nombre del tipo de usuario debe tener como minimo 5 caracteres'}
            elif id < 1:
                Marca.objects.create(nombreMarca = nombreMarca, activoMarca = activo)
                cntx = {'mensaje': 'Los datos fueron guardados correctamente'}
            else:
                fila = Marca.objects.get(pk = id)
                fila.nombreMarca = nombreMarca
                fila.activoMarca = activoMarca
                fila.save()
                cntx = {'mensaje': 'Los datos fueron guardados correctamente'}
        elif 'btnRead' in request.POST:
            listado = Marca.objects.all()
            if len(listado) >= 1:
                cntx = {'listado': listado }
            else:
                cntx = {'error': 'Aun no existen tipos de usuarios para mostrar'}
        elif 'btnDelete' in request.POST:
            try:
                fila = Marca.objects.get(pk = id)
                fila.delete()
                cntx = {'mensaje': 'Los datos fueron eliminados correctamente'}
            except:
                cntx = {'error': 'Debe seleccionar item a eliminar'}
    productCategories = Categoria.objects.all()
    cntx["productCategories"] = productCategories
    return render(request, 'marca.html', cntx)
  
def viewReadMarca(request, id):
    cntx = {}
    try:
        fila = Marca.objects.get(pk = id)
        cntx = {'fila': fila}
    except:
        cntx = {'error': 'Item no encontrado'}
    productCategories = Categoria.objects.all()
    cntx["productCategories"] = productCategories
    return render(request, 'marca.html', cntx)
#fin marca

#usuario
def viewUsuario(request):
    cntx = {}
    if request.method == 'POST':
        id = int("0" + request.POST["txtId"])
        rut = request.POST["txtRut"]
        dv = request.POST["txtDV"]
        nombreUsuario = request.POST["txtNombre"]
        apellidosUsuario = request.POST["txtApellido"]
        fechaNac = request.POST["fecNac"]
        clave = request.POST["txtClave"]
        email = request.POST["txtEmail"]
        direccion = request.POST["txtDireccion"]
        telefono = request.POST["txtTel"]
        tipoUsuario = request.POST["cmbTipoUsuario"]
        if 'btnCreate' in request.POST:
            if len(rut)<8:
                cntx = {'error': 'El rut del usuario debe tener como minimo 8 caracteres'}
            elif len(dv)<1:
                cntx = {'error': 'Debe especificar el digito verificador'}
            elif len(nombreUsuario) < 3:
                cntx = {'error': 'El nombre del usuario debe tener como minimo 3 caracteres'}
            elif len(apellidosUsuario) < 3:
                cntx = {'error': 'El apellido del usuario debe tener como minimo 3 caracteres'}
            # elif len(fechaNac) < 3:
            #     cntx = {'error': 'El nombre del usuario debe tener como minimo 3 caracteres'}
            elif len(clave) < 8:
                cntx = {'error': 'La contraseña del usuario debe tener como minimo 8 caracteres'}
            elif len(email) < 8:
                cntx = {'error': 'El correo del usuario debe tener como minimo 8 caracteres'}
            elif len(direccion) < 8:
                cntx = {'error': 'La direccion del usuario debe tener como minimo 8 caracteres'}
            elif len(telefono) < 8:
                cntx = {'error': 'El telefono del usuario debe tener como minimo 8 caracteres'}
            elif tipoUsuario == '0':
                cntx = {'error': 'Debe seleccionar un tipo de usuario'}
            elif id < 1:
                Usuario.objects.create(rut = rut , dv = dv, nombreUsuario = nombreUsuario, apellidosUsuario = apellidosUsuario, fechaNac = fechaNac, clave = clave , email = email, direccion = direccion, telefono = telefono, tipoUsuario = tipoUsuario)
                cntx = {'mensaje': 'Los datos fueron guardados correctamente'}
            else:
                fila = Usuario.objects.get(pk = id)
                fila.rut = rut
                fila.dv = dv
                fila.nombreUsuario = nombreUsuario
                fila.apellidosUsuario = apellidosUsuario
                fila.fechaNac = fechaNac
                fila.clave = clave
                fila.email = email
                fila.direccion = direccion
                fila.telefono = telefono
                fila.tipoUsuario = tipoUsuario
                fila.save()
                cntx = {'mensaje': 'Los datos fueron guardados correctamente'}
        elif 'btnRead' in request.POST:
            listado = Usuario.objects.all()
            if len(listado) >= 1:
                cntx = {'listado': listado }
            else:
                cntx = {'error': 'Aun no existen productos para mostrar'}
        elif 'btnDelete' in request.POST:
            try:
                fila = Usuario.objects.get(pk = id)
                fila.delete()
                cntx = {'mensaje': 'Los datos fueron eliminados correctamente'}
            except:
                cntx = {'error': 'Debe seleccionar item a eliminar'}
    productCategories = Categoria.objects.all()
    cntx["productCategories"] = productCategories
    userCategories = tipoUsuario.objects.all()
    cntx['userCategories'] = userCategories

    return render(request, 'usuario.html', cntx)

def viewReadUsuario(request, id):
    cntx = {}
    try:
        fila = Usuario.objects.get(pk = id)
        cntx = {'fila': fila}
    except:
        cntx = {'error': 'Item no encontrado'}
    productCategories = Categoria.objects.all()
    cntx["productCategories"] = productCategories
    userCategories = tipoUsuario.objects.all()
    cntx['userCategories'] = userCategories
    return render(request, 'usuario.html', cntx)
#fin usuario

#categoria
def viewCategoria(request):
    cntx = {}
    if request.method == 'POST':
        id = int("0" + request.POST["txtId"])
        nombreCategoria = request.POST["txtNombre"]
        activoCategoria = False
        if 'chkActivo' in request.POST:
            activoCategoria = True
        if 'btnCreate' in request.POST:
            if len(nombreCategoria) < 5:
                cntx = {'error': 'El nombre de la categoria debe tener como minimo 5 caracteres'}
            elif id < 1:
                Categoria.objects.create(nombreCategoria = nombreCategoria, activoCategoria = activoCategoria)
                cntx = {'mensaje': 'Los datos fueron guardados correctamente'}
            else:
                fila = Categoria.objects.get(pk = id)
                fila.nombreCategoria = nombreCategoria
                fila.activoCategoria = activoCategoria
                fila.save()
                cntx = {'mensaje': 'Los datos fueron guardados correctamente'}
        elif 'btnRead' in request.POST:
            listado = Categoria.objects.all()
            if len(listado) >= 1:
                cntx = {'listado': listado }
            else:
                cntx = {'error': 'Aun no existen Categorias para mostrar'}
        elif 'btnDelete' in request.POST:
            try:
                fila = Categoria.objects.get(pk = id)
                fila.delete()
                cntx = {'mensaje': 'Los datos fueron eliminados correctamente'}
            except:
                cntx = {'error': 'Debe seleccionar item a eliminar'}
    productCategories = Categoria.objects.all()
    cntx["productCategories"] = productCategories
    return render(request, 'categoria.html', cntx)
  
def viewReadCategoria(request, id):
    cntx = {}
    try:
        fila = Categoria.objects.get(pk = id)
        cntx = {'fila': fila}
    except:
        cntx = {'error': 'Item no encontrado'}
    productCategories = Categoria.objects.all()
    cntx["productCategories"] = productCategories
    return render(request, 'categoria.html', cntx)
#fin categoria

#tipopago
def viewTipoPago(request):
    cntx = {}
    if request.method == 'POST':
        id = int("0" + request.POST["txtId"])
        nombreTipoPago = request.POST["txtNombre"]
        activo = False
        if 'chkActivo' in request.POST:
            activo = True
        if 'btnCreate' in request.POST:
            if len(nombreTipoPago) < 5:
                cntx = {'error': 'El nombre del tipo de pago debe tener como minimo 5 caracteres'}
            elif id < 1:
                tipoPago.objects.create(nombreTipoPago = nombreTipoPago, activo = activo)
                cntx = {'mensaje': 'Los datos fueron guardados correctamente'}
            else:
                fila = tipoPago.objects.get(pk = id)
                fila.nombreTipoPago = nombreTipoPago
                fila.activo = activo
                fila.save()
                cntx = {'mensaje': 'Los datos fueron guardados correctamente'}
        elif 'btnRead' in request.POST:
            listado = tipoPago.objects.all()
            if len(listado) >= 1:
                cntx = {'listado': listado }
            else:
                cntx = {'error': 'Aun no existen Tipos de Pagos para mostrar'}
        elif 'btnDelete' in request.POST:
            try:
                fila = tipoPago.objects.get(pk = id)
                fila.delete()
                cntx = {'mensaje': 'Los datos fueron eliminados correctamente'}
            except:
                cntx = {'error': 'Debe seleccionar item a eliminar'}
    productCategories = Categoria.objects.all()
    cntx["productCategories"] = productCategories
    return render(request, 'tipoPago.html', cntx)
    

def viewReadTipoPago(request, id):
    cntx = {}
    try:
        fila = tipoPago.objects.get(pk = id)
        cntx = {'fila': fila}
    except:
        cntx = {'error': 'Item no encontrado'}
    productCategories = Categoria.objects.all()
    cntx["productCategories"] = productCategories
    return render(request, 'tipoPago.html', cntx)
#fin tipopago

#tipousuario
def viewTipoUsuario(request):
    cntx = {}
    if request.method == 'POST':
        id = int("0" + request.POST["txtId"])
        nombreTipoUsuario = request.POST["txtNombre"]
        activo = False
        if 'chkActivo' in request.POST:
            activo = True
        if 'btnCreate' in request.POST:
            if len(nombreTipoUsuario) < 5:
                cntx = {'error': 'El nombre del tipo de usuario debe tener como minimo 5 caracteres'}
            elif id < 1:
                tipoUsuario.objects.create(nombreTipoUsuario = nombreTipoUsuario, activo = activo)
                cntx = {'mensaje': 'Los datos fueron guardados correctamente'}
            else:
                fila = tipoUsuario.objects.get(pk = id)
                fila.nombreTipoUsuario = nombreTipoUsuario
                fila.activo = activo
                fila.save()
                cntx = {'mensaje': 'Los datos fueron guardados correctamente'}
        elif 'btnRead' in request.POST:
            listado = tipoUsuario.objects.all()
            if len(listado) >= 1:
                cntx = {'listado': listado }
            else:
                cntx = {'error': 'Aun no existen tipos de usuarios para mostrar'}
        elif 'btnDelete' in request.POST:
            try:
                fila = tipoUsuario.objects.get(pk = id)
                fila.delete()
                cntx = {'mensaje': 'Los datos fueron eliminados correctamente'}
            except:
                cntx = {'error': 'Debe seleccionar item a eliminar'}
    productCategories = Categoria.objects.all()
    cntx["productCategories"] = productCategories
    return render(request, 'tipoUsuario.html', cntx)
  
def viewReadTipoUsuario(request, id):
    cntx = {}
    try:
        fila = tipoUsuario.objects.get(pk = id)
        cntx = {'fila': fila}
    except:
        cntx = {'error': 'Item no encontrado'}
    productCategories = Categoria.objects.all()
    cntx["productCategories"] = productCategories
    return render(request, 'tipoUsuario.html', cntx)
#fin tipousuario