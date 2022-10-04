# Importamos la librería "pandas" para poder pasar los datos del paciente a un dataframe y poder tratarlos. 
import pandas as pd

# Creamos la función "paciente", para que el mismo paciente pueda introducir sus datos.
def paciente():

    # Hacemos una presentación para aquella persona que estará dandonos sus datos.
    print("\nLe damos la bienvenida a Hospital F5. \n\nA continuación le realizaremos unas preguntas para poder predecir si tiene riesgo de sufrir un ictus:\n")

    # El paciente deberá decir si es una mujer con un "sí" o "no" obligatoriamente, lo cual luego pasaremos nosotros a "1" si es mujer 
    # o "0" si no lo es.
    # Para hacerlo creamos un bucle "while" y nos aseguramos de que el usuario escriba lo que nosotros queremos.
    while True:
        # Asignamos el "imput" del usuario a una variable y le hacemos la pregunta para que sepa que tiene que introducir en la consola.
        gender = input("¿Es usted una mujer?, por favor responda sí o no.\n")
        # Convertimos la respuesta a minúscula para que el ussuario no tenga que preocuparse si la escribe en mayúscula, y nos aseguramos 
        # que la respuesta sea una de las opciones que nosotras le estamos al paciente y le reiteramos que si no lo es lo vuelva a escribir.
        if gender.lower() not in ('sí', "si", 'no'):
            print("Por favor, responda sí o no.")
        # Si escribe bien la respuesta salimos del bucle y seguimos con la siguiente respuesta.
        else:
            print()
            break
    # Ahora pasamos las posibles respuestas a las variables con las que hemos hecho nuestro transformer, para que así pueda tratar los datos.    
    if gender == "sí":
        gender = 1
    if gender == "si":
        gender = 1
    elif gender == "no":
        gender = 0
    # Y este método se utiliza para las demás variables.

    # El paciente deberá decir su edad con un número entero positivo y menor a 82, porque no podemos predecir edades superiores a esta.
    while True:
        try:
            age = int(input("Por favor escriba su edad en años.\n"))
        except ValueError:
            print("No le hemos entendido.")
            continue
        if age < 0:
            print("Su edad no puede ser negativa.")
            continue
        elif age > 82:
            print("No podemos predecir a alguien de su edad.")
        else:
            print()
            break

    # El paciente deberá decir si sufre de hipertensión con un "sí" o "no" obligatoriamente, lo cual luego pasaremos nosotros a "1" si sufre hipertensión o "0" si no.
    while True:
        hypertension = input("¿Sufre usted de hipertensión?, responda sí o no.\n")
        if hypertension.lower() not in ('sí', 'si', 'no'):
            print("Por favor responda sí o no.")
        else:
            print()
            break
    if hypertension == "sí":
        hypertension = 1
    if hypertension == "si":
        hypertension = 1
    elif hypertension == "no":
        hypertension = 0

    # El paciente deberá decir si padece alguna patología cardiaca con un "sí" o "no" obligatoriamente, lo cual luego pasaremos nosotros a "1" si la sufre o "0" si no.
    while True:
        heart_disease = input("¿Padece alguna patología cardiaca?, responda sí o no.\n")
        if heart_disease.lower() not in ('sí', 'si', 'no'):
            print("Por favor responda sí o no.")
        else:
            print()
            break
    if heart_disease == "sí":
        heart_disease = 1
    if heart_disease == "si":
        heart_disease = 1
    elif heart_disease == "no":
        heart_disease = 0

    # El paciente deberá decir si está o ha estado en una relación con un "sí" o "no" obligatoriamente, lo cual luego pasaremos nosotros a "1" si ha estado o "0" si no.
    while True:
        ever_married = input("¿Está o ha estado en una relación conyugal?, responda sí o no.\n")
        if ever_married.lower() not in ('sí', 'si', 'no'):
            print("Por favor responda sí o no.")
        else:
            print()
            break
    if ever_married == "sí":
        ever_married = 1
    if ever_married == "si":
        ever_married = 1
    elif ever_married == "no":
        ever_married = 0

    # El paciente deberá decir el tipo de trabajo al que se dedica, especificando si es por cuenta porpia, cuenta ajena, para el estado o es estudiante.
    while True:
        work_type = input("Especifique el tipo de trabajo al que se dedica:\n\n -Si trabaja por cuenta ajena responda 'cuenta ajena'. \n -Si trabaja por cuenta propia responda 'cuenta propia'. \n -Si trabaja para el estado responda 'estado'. \n -Si es menor y no trabaja responda 'menor'. \n")
        if work_type.lower() not in ('cuenta ajena', 'cuenta propia', 'estado', 'menor'):
            print("Por favor responda una de las 4 opciones.")
        else:
            print()
            break
    if work_type == "cuenta ajena":
        work_type = "Private"
    elif work_type == "cuenta propia":
        work_type = "Self-employed"
    elif work_type == "estado":
        work_type = "Govt_job"
    elif work_type == "menor":
        work_type = "children"

    # El paciente deberá decir si vive en una zona urbana con un "sí" o "no" obligatoriamente, lo cual luego pasaremos nosotros a "1" si vive en zona urbana o "0" si no.
    while True:
        Residence_type = input("¿Vive usted en una zona urbana?, responda sí o no.\n")
        if Residence_type.lower() not in ('sí', 'si', 'no'):
            print("Por favor responda sí o no.")
        else:
            print()
            break
    if Residence_type == "sí":
        Residence_type = 1
    if Residence_type == "si":
        Residence_type = 1
    elif Residence_type == "no":
        Residence_type = 0

    # El paciente deberá decir su nivel de glucosa en sangre cuando está en ayunas, mediante un número entre 55.12 y 240.86, porque no podemos predecir a gente con niveles de glucosa superiores o menores.
    while True:
        try:
            avg_glucose_level = float(input("¿Cuál es su nivel de glucosa en sangre estando en ayunas?.\n"))
        except ValueError:
            print("No le hemos entendido.")
            continue
        if avg_glucose_level < 55.12:
            print("No podemos predecir a alguien con un nivel de glucosa tan bajo.")
            continue
        elif avg_glucose_level > 240.86:
            print("No podemos predecir a alguien con un nivel de glucosa tan alto.")
        else:
            print()
            break

    # El paciente deberá decir su indice de masa corporal con un número entre 14 y 48.8, porque no podemos predecir indices de masa corporal superiores ni menores.
    while True:
        try:
            bmi = float(input("¿Cuál es su índice de masa corporal?\n"))
        except ValueError:
            print("No le hemos entendido.")
            continue
        if bmi < 14:
            print("No podemos predecir a alguien con un índice de masa corporal tan bajo.")
            continue
        elif bmi > 48.8:
            print("No podemos predecir a alguien con un índice de masa corporal tan alto.")
        else:
            print()
            break

    # El paciente deberá decir si fuma, fumaba o nunca ha fumado.
    while True:
        smoking_status = input("¿Fuma actualmente o fumaba? Por favor responda con: 'fumo', 'fumaba' o bien 'nunca', si usted nunca ha fumado. \n")
        if smoking_status.lower() not in ('fumo', 'fumaba', 'nunca'):
            print("Por favor responda una de las 3 opciones,")
        else:
            print()
            break
    if smoking_status == "fumo":
        smoking_status = "smokes"
    elif smoking_status == "fumaba":
        smoking_status = "formerly smoked"
    elif smoking_status == "nunca":
        smoking_status = "never smoked"

    # Nombramos las variables que el paciente ha dado para poder pasarlas a un DF.
    data = {'female_gender': [gender], 'age':[age],'hypertension':[hypertension], 'heart_disease':[heart_disease], 'ever_married':[ever_married], 'work_type':[work_type],'urban_residence':[Residence_type],'avg_glucose_level':[avg_glucose_level],'bmi':[bmi],'smoking_status':[smoking_status]  }

    # Pasamos los datos a un DF.
    Datos = pd.DataFrame(data)

    # Hacemos que la función devuelva los datos en DF.
    return Datos