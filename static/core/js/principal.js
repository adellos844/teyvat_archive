document.addEventListener('DOMContentLoaded', () => {
    console.log("Teyvat Archive cargado correctamente.");

    // Efecto de scroll suave para la navegación
    const cards = document.querySelectorAll('.card');
    
    cards.forEach((card, index) => {
        card.style.opacity = "0";
        card.style.transform = "translateY(20px)";
        
        setTimeout(() => {
            card.style.opacity = "1";
            card.style.transform = "translateY(0)";
        }, 100 * index);
    });
});