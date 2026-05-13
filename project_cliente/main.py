from fastapi import FastAPI
from Modelos.clientes import Cliente, ClienteCrear, ClienteEditar

app = FastAPI()

lista_clientes: list[Cliente] = []


# LISTAR CLIENTES
@app.get("/clientes")
async def listar_clientes():
    return {"clientes": lista_clientes}


# BUSCAR CLIENTE POR ID
@app.get("/clientes/{id}")
async def lista_cliente(id: int):

    for cliente in lista_clientes:

        if cliente.id == id:
            return cliente

    return {"mensaje": "cliente no encontrado"}


# CREAR CLIENTE
@app.post("/clientes", response_model=Cliente)
async def crear_clientes(datos_cliente: ClienteCrear):

    cliente_val = Cliente(
        id=len(lista_clientes) + 1,
        nombre=datos_cliente.nombre,
        edad=datos_cliente.edad,
        descripcion=datos_cliente.descripcion
    )

    lista_clientes.append(cliente_val)

    return cliente_val


# EDITAR CLIENTE
@app.put("/clientes/{id}")
def editar_clientes(id: int, datos_cliente: ClienteEditar):

    for i, obj_cliente in enumerate(lista_clientes):

        if obj_cliente.id == id:

            cliente_val = Cliente(
                id=id,
                nombre=datos_cliente.nombre,
                edad=datos_cliente.edad,
                descripcion=datos_cliente.descripcion
            )

            lista_clientes[i] = cliente_val

            return {
                "mensaje": "se actualizo el cliente satisfactoriamente",
                "cliente": cliente_val
            }

    return {"mensaje": "cliente no encontrado"}


# ELIMINAR CLIENTE
@app.delete("/clientes/{id}")
def eliminar_clientes(id: int):

    for i, cliente in enumerate(lista_clientes):

        if cliente.id == id:

            cliente_eliminado = lista_clientes.pop(i)

            return {
                "mensaje": "cliente eliminado satisfactoriamente",
                "cliente": cliente_eliminado
            }
