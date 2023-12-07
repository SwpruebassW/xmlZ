import pyodbc

# Configuración de la conexión
server = 'WINSERVER16\\SQLEXPRESS'  # Nombre del servidor SQL Server
database = 'tu_base_de_datos'  # Nombre de tu base de datos
username = 'tu_usuario'  # Tu usuario (si usas la autenticación de Windows, puedes dejar estos campos vacíos)
password = 'tu_contraseña'  # Tu contraseña

# Cadena de conexión
# Si estás usando la autenticación de Windows (integrada), puedes usar Trusted_Connection=yes y omitir UID y PWD
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};Trusted_Connection=yes'

# Intenta conectarte a la base de datos
try:
    with pyodbc.connect(connection_string, timeout=10) as conn:
        print("Conexión exitosa.")
        # Ejecuta una consulta simple (opcional)
        with conn.cursor() as cursor:
            cursor.execute("SELECT @@version;")
            row = cursor.fetchone()
            while row:
                print(row[0])
                row = cursor.fetchone()

except Exception as e:
    print(f"Error al conectar: {e}")
