
from fastapi.testclient import TestClient
from src.proyect.main import app


#Comenzar el test del cliente
client = TestClient(app)

##############################
#Tests realacionados con usuarios
##############################


def test_create_user():
    """
    1.Enviar una solicitud a post /users/create_user con datos de usuario
    2.Asegurarse de que la respuesta tiene los datos correctos
    3.Asegurarse de que la respuesta tiene un id    
    4.Asegurarse de que la respuesta tiene un código de estado 201
    5.Asegurarse de que las marcas del tiempo created_at y updated_at estan correctas

    """

    response = client.post( 
        "/users/create_user",
        json={
            "username": "test_user2",
            "email": "test2@ejemplo.com ",
            "phone": "2"
        }
    )

    assert response.status_code == 201
    #assert response.status_code == 400 !!!
    assert response.json()["username"] == "test_user2"
    assert response.json()["email"] == "test2@ejemplo.com"
    assert response.json()["phone"] == "2"
    assert "id" in response.json()
     
    assert "created_at" in response.json() 
    assert "updated_at" in response.json()

def test_create_user_with_duplicate_username():
    #Asegurarse de que no se crean usuarios con el mismo nombre
    
    #Se crea un primer usuario 
    client.post("/users/create_user",json={
        "username": "prueba_nombre1",
        "email": "prueba_nombre_1@ejemplo.com ",
        "phone": "prueba_nombre1"
    }
    )
    #Se crea un segundo con todos los campos diferentes menos el nombre, el cual es igual  para comprobar que funcione.
    response = client.post("/users/create_user",json={
        "username": "prueba_nombre1",
        "email": "prueba_nombre_2@ejemplo.com ",
        "phone": "prueba_nombre2"
    } 
    )
    assert response.status_code == 400 
    assert response.json()["detail"]== "El nombre de usuario ya existe"
 
    
    
def test_create_user_with_duplicate_email():
    #Asegurarse de que no se crean usuarios con el mismo email
    
    #Se crea un primer usuario 
    client.post("/users/create_user",json={
        "username": "prueba_email1",
        "email": "prueba_email_1@ejemplo.com",
        "phone": "prueba_email1"
    }
)
    #Se crea un segundo con todos los campos diferentes menos el email, el cual es igual  para comprobar que funcione.
    response = client.post("/users/create_user",json={
        "username": "prueba_email2",
        "email": "prueba_email_1@ejemplo.com",
        "phone": "prueba_email2"
    }
)
    assert response.status_code == 400 
    assert response.json()["detail"]== "El email que se quiere crear ya existe."
    

def test_create_user_with_duplicate_phone():
    #Asegurarse de que no se crean usuarios con el mismo numero de telefono
    
    #Se crea un primer usuario 
    client.post("/users/create_user",json={
        "username": "prueba_phone1",
        "email": "prueba_phone_1@ejemplo.com",
        "phone": "prueba_phone1"
    }
)
    #Se crea un segundo con todos los campos diferentes menos el phone, el cual es igual  para comprobar que funcione.
    response = client.post("/users/create_user",json={
        "username": "prueba_phone2",
        "email": "prueba_phone_2@ejemplo.com",
        "phone": "prueba_phone1"
    }
)
    assert response.status_code == 400 
    assert response.json()["detail"]== "El número de teléfono ingresado ya existe para otro usuario."





