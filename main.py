from modelo.estudiante import Estudiante


def main():
    # Punto de inicio del programa
    estudiante = Estudiante("2024001", "Ana Pérez")
    print(estudiante.matricula, estudiante.nombre)


if __name__ == "__main__":
    main()
