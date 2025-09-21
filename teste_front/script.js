document.addEventListener('DOMContentLoaded', function () {
    const botaoMenu = document.getElementById('botao_menu');
    const menuDropdown = document.getElementById('menu_dropdown');

    botaoMenu.addEventListener('click', function () {
        const aberto = !menuDropdown.hasAttribute('hidden');
        if (aberto) {
            menuDropdown.setAttribute('hidden', '');
            botaoMenu.setAttribute('aria-expanded', 'false');
        } else {
            menuDropdown.removeAttribute('hidden');
            botaoMenu.setAttribute('aria-expanded', 'true');
        }
    });

    // Fecha o menu se clicar fora
    document.addEventListener('click', function (e) {
        if (!menuDropdown.contains(e.target) && e.target !== botaoMenu) {
            menuDropdown.setAttribute('hidden', '');
            botaoMenu.setAttribute('aria-expanded', 'false');
        }
    });

    // Fecha o menu com ESC
    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') {
            menuDropdown.setAttribute('hidden', '');
            botaoMenu.setAttribute('aria-expanded', 'false');
            botaoMenu.focus();
        }
    });
});