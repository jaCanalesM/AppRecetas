from django.db import migrations


def create_initial_recetas(apps, schema_editor):
    Categoria = apps.get_model('categorias', 'Categoria')
    Receta = apps.get_model('recetas', 'Receta')

    categorias = {}
    for nombre, slug in [
        ('Postres', 'postres'),
        ('Sopas', 'sopas'),
        ('Ensaladas', 'ensaladas'),
        ('Carnes', 'carnes'),
        ('Bebidas', 'bebidas'),
    ]:
        categoria, _ = Categoria.objects.get_or_create(nombre=nombre, defaults={'slug': slug})
        categorias[nombre] = categoria

    recetas = [
        {
            'categoria': categorias['Postres'],
            'nombre': 'Tarta de Manzana Casera',
            'descripcion': 'Una tarta de manzana suave y perfumada, con masa crujiente y un relleno dulce y especiado.',
            'ingredientes': '4 manzanas, 200 g de harina, 100 g de mantequilla, 80 g de azúcar, 1 huevo, canela, 1 pizca de sal',
            'pasos': '1. Preparar la masa mezclando harina, mantequilla, azúcar y huevo. 2. Pelar y cortar las manzanas. 3. Rellenar la masa con manzanas y canela. 4. Hornear 40 minutos a 180°C.',
            'slug': 'tarta-de-manzana-casera',
            'tiempo': '1 hora',
            'foto': 'plato.png',
        },
        {
            'categoria': categorias['Sopas'],
            'nombre': 'Crema de Zapallo',
            'descripcion': 'Una crema suave y reconfortante de zapallo, ideal para compartir en días fríos.',
            'ingredientes': '1 zapallo, 1 cebolla, 2 dientes de ajo, 500 ml de caldo de verduras, sal, pimienta, aceite de oliva',
            'pasos': '1. Saltear cebolla y ajo. 2. Añadir trozos de zapallo y caldo. 3. Cocinar hasta que esté tierno. 4. Licuar y corregir sazón.',
            'slug': 'crema-de-zapallo',
            'tiempo': '45 minutos',
            'foto': 'plato.png',
        },
        {
            'categoria': categorias['Ensaladas'],
            'nombre': 'Ensalada Mediterránea',
            'descripcion': 'Ensalada fresca con tomates, pepino, aceitunas y queso, aliñada con aceite de oliva y hierbas.',
            'ingredientes': 'lechuga, tomates cherry, pepino, aceitunas negras, queso feta, aceite de oliva, orégano, sal',
            'pasos': '1. Lavar y cortar verduras. 2. Mezclar con aceitunas y queso. 3. Aliñar con aceite de oliva, orégano y sal.',
            'slug': 'ensalada-mediterranea',
            'tiempo': '15 minutos',
            'foto': 'plato.png',
        },
        {
            'categoria': categorias['Carnes'],
            'nombre': 'Pollo al Horno con Hierbas',
            'descripcion': 'Pollo dorado al horno con una mezcla de hierbas y limón, jugoso por dentro y crujiente por fuera.',
            'ingredientes': '1 pollo entero, romero, tomillo, 1 limón, 3 dientes de ajo, aceite de oliva, sal, pimienta',
            'pasos': '1. Marinar el pollo con hierbas, ajo, limón y aceite. 2. Hornear 1 hora a 190°C. 3. Dejar reposar antes de cortar.',
            'slug': 'pollo-al-horno-con-hierbas',
            'tiempo': '1 hora 20 minutos',
            'foto': 'plato.png',
        },
        {
            'categoria': categorias['Bebidas'],
            'nombre': 'Limonada con Menta',
            'descripcion': 'Bebida refrescante de limón con hojas de menta, perfecta para acompañar cualquier comida.',
            'ingredientes': '4 limones, 1 litro de agua, 8 hojas de menta, 60 g de azúcar, hielo',
            'pasos': '1. Exprimir los limones. 2. Mezclar con agua, azúcar y menta. 3. Refrigerar y servir con hielo.',
            'slug': 'limonada-con-menta',
            'tiempo': '10 minutos',
            'foto': 'plato.png',
        },
    ]

    for receta_data in recetas:
        Receta.objects.update_or_create(slug=receta_data['slug'], defaults=receta_data)


def delete_initial_recetas(apps, schema_editor):
    Categoria = apps.get_model('categorias', 'Categoria')
    Receta = apps.get_model('recetas', 'Receta')

    slugs = [
        'tarta-de-manzana-casera',
        'crema-de-zapallo',
        'ensalada-mediterranea',
        'pollo-al-horno-con-hierbas',
        'limonada-con-menta',
    ]
    Receta.objects.filter(slug__in=slugs).delete()
    Categoria.objects.filter(slug__in=['postres', 'sopas', 'ensaladas', 'carnes', 'bebidas']).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0001_initial'),
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_recetas, delete_initial_recetas),
    ]
