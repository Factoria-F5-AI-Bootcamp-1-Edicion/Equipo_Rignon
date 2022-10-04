# Importamos las librerías necesarias para cargar el modelo y el transformer así como la función que creamos anteriormente.
import pickle
from formulario import paciente

# Cargamos la funcion (paciente), donde él mismo va a tener que introducir sus datos para poder hacer la predicción.
Datos_Paciente = paciente()

# Aquí cargamos el tranformer para poder tratar los datos que introduzca el paciente.
transformer = pickle.load(open("/Users/Pablo/Factoria F5/Stroke/Equipo_Rignon/transformer_modelo_final.pkl", 'rb'))    

# Transformamos los datos que el paciente ha introducido en la consola.
Datos_Paciente_Transformados = transformer.transform(Datos_Paciente)

# Cargamos el modelo que utilizaremos para hacer las predicciones.
modelo_final_XGBClassifier = pickle.load(open('/Users/Pablo/Factoria F5/Stroke/Equipo_Rignon/modelo_final_LGBMClassifier_.pkl', 'rb'))

# Hacemos que el modelo prediga el resultado.
Prediccion_Paciente=modelo_final_XGBClassifier.predict(Datos_Paciente_Transformados)

# Según sea el resultado de la predicción arrojará un mensaje sobre si el paciente tiene riesgo o no de sufrir un ictus.
if Prediccion_Paciente == 1:
    print("Usted tiene riesgo de sufrir un ictus, por favor facilítele esta información a su médico.\n")
elif Prediccion_Paciente == 0:
    print("Usted no tiene riesgo de sufrir un ictus.\n")