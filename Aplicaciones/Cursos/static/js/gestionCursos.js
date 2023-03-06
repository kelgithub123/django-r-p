var message_ele = document.getElementById("message_container");

(function () {

    const btnEliminacion = document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('¿Seguro de eliminar el curso?');
            if (!confirmacion) {
                e.preventDefault();
            }
        });
    });
    
}
);

setTimeout(function(){ 
   message_ele.style.display = "none"; 
}, 3000);