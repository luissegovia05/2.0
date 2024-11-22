import json
import tkinter as tk
from tkinter import ttk, messagebox

class FormUsuarios(tk.Tk):
    def __init__(self, parent):
        super().__init__()  # Aseguramos que el constructor base se llame.
        self.tipo_action = "Guardar"
        self.tipo_user = ""

        self.frame = ttk.Frame(parent)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        tk.Label(self.frame, text="Registro de usuarios", font=('Times', 16)).place(x=70, y=30)

        labelcedula = tk.Label(self.frame, text="Cedula", font=('Times', 14))
        labelcedula.place(x=70, y=100)
        self.ccedula = tk.Entry(self.frame, width=40)
        self.ccedula.place(x=220, y=100)

        labelnombre = tk.Label(self.frame, text="Nombre", font=('Times', 14))
        labelnombre.place(x=70, y=130)
        self.cnombre = tk.Entry(self.frame, width=40)
        self.cnombre.place(x=220, y=130)

        labelusuario = tk.Label(self.frame, text="Username", font=('Times', 14))
        labelusuario.place(x=70, y=160)
        self.cusuario = tk.Entry(self.frame, width=40)
        self.cusuario.place(x=220, y=160)

        labelcontrasena = tk.Label(self.frame, text="Contraseña", font=('Times', 14))
        labelcontrasena.place(x=500, y=100)
        self.ccontrasena = tk.Entry(self.frame, width=40, show="*")
        self.ccontrasena.place(x=600, y=100)

        labelcorreo = tk.Label(self.frame, text="Correo", font=('Times', 14))
        labelcorreo.place(x=500, y=130)
        self.ccorreo = tk.Entry(self.frame, width=40)
        self.ccorreo.place(x=600, y=130)

        labeltipo = tk.Label(self.frame, text="Rol", font=('Times', 14))
        labeltipo.place(x=500, y=160)
        self.ctipo = ttk.Combobox(self.frame, width=40)
        self.ctipo.place(x=600, y=160)
        self.ctipo["values"] = ("Administrador", "Vendedor")

        btn_guardar = tk.Button(self.frame, text="Guardar", font=('Times', 14), command=self.guardar_usuario)
        btn_guardar.place(x=70, y=190)

        self.listar_usuarios()

    def listar_usuarios(self):
        tk.Label(self.frame, text="LISTADO DE USUARIOS", font=('Times', 16)).place(x=70, y=230)
        self.tablausuarios = ttk.Treeview(self.frame, columns=("Nombre", "Username", "Email", "Rol"))
        self.tablausuarios.heading("#0", text="Cedula")
        self.tablausuarios.heading("Nombre", text="Nombre")
        self.tablausuarios.heading("Username", text="Username")
        self.tablausuarios.heading("Email", text="Email")
        self.tablausuarios.heading("Rol", text="Rol")

        try:
            with open(r"D:\GITHUB\CLASES\Curso-Python\Clase09\LoginAppPart2\db_users.json", "r", encoding="utf-8") as file:
                data = json.load(file)
                for usuario in data["users"]:
                    self.tablausuarios.insert("", "end", text=f'{usuario["id"]}', values=(
                        f'{usuario["name"]}',
                        f'{usuario["username"]}',
                        f'{usuario["email"]}',
                        f'{usuario["role"]}'
                    ))
        except FileNotFoundError:
            with open(r"D:\GITHUB\CLASES\Curso-Python\Clase09\LoginAppPart2\db_users.json", "w") as file:
                json.dump({"users": []}, file)

        self.tablausuarios.place(x=70, y=280)
        tk.Button(self.frame, text="Eliminar", font=('Times', 14), command=self.eliminar_usuarios).place(x=70, y=580)
        tk.Button(self.frame, text="Actualizar", font=('Times', 14), command=self.actualizar_usuarios).place(x=170, y=580)

    def guardar_usuario(self):
        cedula = self.ccedula.get()
        nombre = self.cnombre.get()
        username = self.cusuario.get()
        contrasena = self.ccontrasena.get()
        correo = self.ccorreo.get()
        rol = self.ctipo.get()

        if not all([cedula, nombre, username, contrasena, correo, rol]):
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        nuevo_usuario = {
            "id": cedula,
            "name": nombre,
            "username": username,
            "password": contrasena,
            "email": correo,
            "role": rol
        }

        try:
            with open(r"D:\GITHUB\CLASES\Curso-Python\Clase09\LoginAppPart2\db_users.json", "r+", encoding="utf-8") as file:
                data = json.load(file)
                for usuario in data["users"]:
                    if usuario["id"] == cedula:
                        messagebox.showerror("Error", "El usuario con esta cédula ya existe.")
                        return
                data["users"].append(nuevo_usuario)
                file.seek(0)
                json.dump(data, file, indent=4)
            self.tablausuarios.insert("", "end", text=cedula, values=(nombre, username, correo, rol))
            messagebox.showinfo("Éxito", "Usuario guardado correctamente.")
        except FileNotFoundError:
            messagebox.showerror("Error", "Archivo de usuarios no encontrado.")

    def actualizar_usuarios(self):
        seleccion = self.tablausuarios.selection()
        if not seleccion:
            messagebox.showerror("Error", "Seleccione un usuario para actualizar.")
            return

        cedula = self.tablausuarios.item(seleccion, "text")
        nuevo_nombre = self.cnombre.get()
        nuevo_username = self.cusuario.get()
        nuevo_correo = self.ccorreo.get()
        nuevo_rol = self.ctipo.get()

        try:
            with open(r"D:\GITHUB\CLASES\Curso-Python\Clase09\LoginAppPart2\db_users.json", "r+", encoding="utf-8") as file:
                data = json.load(file)
                for usuario in data["users"]:
                    if usuario["id"] == cedula:
                        usuario["name"] = nuevo_nombre
                        usuario["username"] = nuevo_username
                        usuario["email"] = nuevo_correo
                        usuario["role"] = nuevo_rol
                        break
                file.seek(0)
                json.dump(data, file, indent=4)
            self.listar_usuarios()
            messagebox.showinfo("Éxito", "Usuario actualizado correctamente.")
        except FileNotFoundError:
            messagebox.showerror("Error", "Archivo de usuarios no encontrado.")

    def eliminar_usuarios(self):
        seleccion = self.tablausuarios.selection()
        if not seleccion:
            messagebox.showerror("Error", "Seleccione un usuario para eliminar.")
            return

        cedula = self.tablausuarios.item(seleccion, "text")

        try:
            with open(r"D:\GITHUB\CLASES\Curso-Python\Clase09\LoginAppPart2\db_users.json", "r+", encoding="utf-8") as file:
                data = json.load(file)
                data["users"] = [usuario for usuario in data["users"] if usuario["id"] != cedula]
                file.seek(0)
                file.truncate()
                json.dump(data, file, indent=4)
            self.tablausuarios.delete(seleccion)
            messagebox.showinfo("Éxito", "Usuario eliminado correctamente.")
        except FileNotFoundError:
            messagebox.showerror("Error", "Archivo de usuarios no encontrado.")

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = FormUsuarios(root)
    root.mainloop()
