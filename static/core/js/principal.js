document.addEventListener('DOMContentLoaded', () => {
    console.log("Teyvat Archive cargado correctamente.");

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


document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('searchInput');
    const filterBtns = document.querySelectorAll('.filter-btn');
    const cards = document.querySelectorAll('.character-card');

    function filterCharacters() {
        const searchTerm = searchInput.value.toLowerCase();
        const activeElement = document.querySelector('.filter-btn.active').dataset.element;

        cards.forEach(card => {
            const name = card.dataset.name;
            const element = card.dataset.element;
            
            const matchesSearch = name.includes(searchTerm);
            const matchesElement = activeElement === 'all' || element === activeElement;

            if (matchesSearch && matchesElement) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    }

    searchInput.addEventListener('input', filterCharacters);

    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            filterBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            filterCharacters();
        });
    });
});


document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('searchInput');
    const filterBtns = document.querySelectorAll('.weapon-filters .filter-btn');
    const cards = document.querySelectorAll('.character-card');

    if (filterBtns.length > 0) {
        function filterWeapons() {
            const searchTerm = searchInput.value.toLowerCase();
            const activeType = document.querySelector('.weapon-filters .filter-btn.active').dataset.type;

            cards.forEach(card => {
                const name = card.dataset.name;
                const type = card.dataset.type;
                
                const matchesSearch = name.includes(searchTerm);
                const matchesType = activeType === 'all' || type === activeType;

                if (matchesSearch && matchesType) {
                    card.style.display = '';
                } else {
                    card.style.display = 'none';
                }
            });
        }

        searchInput.addEventListener('input', filterWeapons);

        filterBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                filterBtns.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                filterWeapons();
            });
        });
    }
});