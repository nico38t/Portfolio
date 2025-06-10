document.addEventListener("DOMContentLoaded", function () {
    const elements = document.querySelectorAll('.section, .project');

    function animateOnScroll() {
        elements.forEach(el => {
            const rect = el.getBoundingClientRect();
            if (rect.top < window.innerHeight - 100) {
                el.classList.add('visible');
            }
        });
    }

    window.addEventListener('scroll', animateOnScroll);
    animateOnScroll();
});