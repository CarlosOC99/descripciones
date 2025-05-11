from typing import List, Dict

def descripciones() -> None:
    #declarar lista con usuarios y descripciones
    usuarios: List[Dict[str, str]] = [
        {"nombre": "Liliana", "apellido": "zepeda", "descripcion": "Amante de los libros y la escritura creativa.", "fecha_creacion": "2023-01-15"},
        {"nombre": "caleb", "apellido": "montes de oca", "descripcion": "Ingeniero con pasión por la inteligencia artificial.", "fecha_creacion": "2022-05-12"},
        {"nombre": "Sofía", "apellido": "rivas", "descripcion": "Fanática del café.", "fecha_creacion": "2021-09-23"},
        {"nombre": "jonathan", "apellido": "garcia", "descripcion": "Diseñador gráfico freelance especializado en branding y UX/UI.", "fecha_creacion": "2023-03-10"},
        {"nombre": "diana", "apellido": "contreras", "descripcion": "Viajera empedernida que ha recorrido más de 30 países documentando culturas.", "fecha_creacion": "2020-12-01"},
        {"nombre": "melissa", "apellido": "ramos", "descripcion": "Estudiante de biotecnología con interés en la genética.", "fecha_creacion": "2024-02-18"},
        {"nombre": "vanessa", "apellido": "ramos", "descripcion": "Apasionada por la música clásica y el piano.", "fecha_creacion": "2021-06-30"},
        {"nombre": "carlos", "apellido": "ortiz", "descripcion": "Desarrollador web con 5 años de experiencia en frontend y backend.", "fecha_creacion": "2022-11-22"},
        {"nombre": "daniel", "apellido": "ramirez", "descripcion": "Chef profesional con enfoque en gastronomía vegana e internacional.", "fecha_creacion": "2023-08-19"},
        {"nombre": "omar", "apellido": "garcia", "descripcion": "Atleta de alto rendimiento con logros en natación y triatlón.", "fecha_creacion": "2020-04-17"},
        {"nombre": "Valeria", "apellido": "Reyes", "descripcion": "Voluntaria en organizaciones de derechos humanos y justicia social.", "fecha_creacion": "2021-10-10"},
        {"nombre": "gerardo", "apellido": "badillo", "descripcion": "Fotógrafo profesional especializado en naturaleza y vida salvaje.", "fecha_creacion": "2022-01-04"},
    ]
    #validacion de la lista de usuarios, en caso de tener menos de 3 elementos arroja un mensaje de falta de datos 
    if len(usuarios) < 3:
        print("No es posible mostrar contenido: la lista de usuarios contiene menos de 3 elementos.")
        return

    #Ordena por longitud de la descripción de mayor a menor
    usuarios_ordenados = sorted(usuarios, key=lambda u: len(u["descripcion"]), reverse=True)

    top_3 = usuarios_ordenados[:3]

    #imprime los 3 usuarios con las descripciones mas largas
    print("Top 3 usuarios con descripciones más largas:\n")
    for i, usuario in enumerate(top_3, start=1):
        print(f"{i}. {usuario['nombre']} {usuario['apellido']}")
        print(f"   Descripción: {usuario['descripcion']}")
        print(f"   Fecha de creación: {usuario['fecha_creacion']}\n")

# Ejecutar función
if __name__ == "__main__":
    descripciones()
