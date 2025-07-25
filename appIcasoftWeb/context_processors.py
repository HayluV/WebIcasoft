from appIcasoftWeb.models import Categoria, SubCategoria

def categorias_con_subcategorias(request):
    data_categoria = Categoria.objects.all().filter(estadoCategoria=True)
    categorias = []
    for categoria in data_categoria:
        subcategorias = []
        data_subcategoria = SubCategoria.objects.filter(idCategoria=categoria.idCategoria, estado = True)
        
        for subcategoria in data_subcategoria:
            subcategorias.append({
                'nombre': subcategoria.nombre,
                'slugSub': subcategoria.slug,
            })     
        categoria_data = {
            'id': categoria.idCategoria,
            'nombre': categoria.nombreCategoria,
            'slugcat': categoria.slug,
            'subcategorias': subcategorias
        }
        categorias.append(categoria_data)

    return {'categorias': categorias}