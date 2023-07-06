document.getElementById("login-form").addEventListener("submit", function(event) {
    event.preventDefault(); // Evita que el formulario se envíe automáticamente

    // Obtiene los valores del formulario
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    // Crea un objeto con los datos del formulario
    var data = {
        username: username,
        password: password
    };

    // Realiza la solicitud al backend utilizando axios (o la biblioteca de tu elección)
    axios.post("/login", data)
        .then(function(response) {
            // Si la solicitud es exitosa, muestra un mensaje de éxito en la consola
            console.log(response.data.message);
        })
        .catch(function(error) {
            // Si la solicitud falla, muestra el mensaje de error en la consola
            console.error(error.response.data.message);
        });
});
